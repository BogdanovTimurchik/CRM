import express, { Request, Response, NextFunction } from 'express';
import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createServer as createViteServer } from 'vite';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;
const DB_PATH = path.join(__dirname, 'database.json');
const BACKUP_PATH = path.join(__dirname, 'database.backup.json');

// Middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// CORS headers for local network access in Margilan
app.use((req: Request, res: Response, next: NextFunction) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization, x-mam-user');
  if (req.method === 'OPTIONS') {
    return res.sendStatus(200);
  }
  next();
});

// Helper: Read DB
export function getDatabase(): any {
  if (!fs.existsSync(DB_PATH)) {
    console.warn('database.json not found, attempting to read backup...');
    if (fs.existsSync(BACKUP_PATH)) {
      return JSON.parse(fs.readFileSync(BACKUP_PATH, 'utf8'));
    }
    return null;
  }
  try {
    const raw = fs.readFileSync(DB_PATH, 'utf8');
    return JSON.parse(raw);
  } catch (err) {
    console.error('Error reading database.json:', err);
    if (fs.existsSync(BACKUP_PATH)) {
      console.log('Falling back to database.backup.json...');
      return JSON.parse(fs.readFileSync(BACKUP_PATH, 'utf8'));
    }
    return null;
  }
}

// Helper: Save DB and trigger auto-backup
export function saveDatabase(data: any): boolean {
  try {
    const jsonStr = JSON.stringify(data, null, 2);
    fs.writeFileSync(DB_PATH, jsonStr, 'utf8');
    fs.writeFileSync(BACKUP_PATH, jsonStr, 'utf8');
    return true;
  } catch (err) {
    console.error('Error saving database.json:', err);
    return false;
  }
}

// Helper: Format audit log
function addAuditEntry(db: any, action: string, details: string, user = 'СИСТЕМА', status = 'ok') {
  if (!db.auditLogs) db.auditLogs = [];
  const pad = (n: number) => String(n).padStart(2, '0');
  const now = new Date();
  const dateStr = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}`;
  
  db.auditLogs.unshift({
    id: 'LOG-' + Math.floor(1000 + Math.random() * 9000),
    date: dateStr,
    user,
    action,
    details,
    status
  });
  if (db.auditLogs.length > 300) db.auditLogs.pop();
}

// In-memory token session storage (supports 10 system roles)
const activeSessions = new Map<string, string>();

// Auth Middleware: extract user from token or header
function authMiddleware(req: Request & { user?: any }, res: Response, next: NextFunction) {
  const authHeader = req.headers['authorization'];
  const userHeader = req.headers['x-mam-user'] as string | undefined;
  
  let userKey: string | null = null;
  if (authHeader && authHeader.startsWith('Bearer ')) {
    const token = authHeader.substring(7);
    userKey = activeSessions.get(token) || null;
  } else if (userHeader) {
    userKey = userHeader;
  }

  const db = getDatabase();
  if (userKey && db && db.accounts && db.accounts[userKey]) {
    req.user = db.accounts[userKey];
  } else {
    req.user = null;
  }
  next();
}

// STRICT FINANCIAL SECURITY FILTER
// Completely hides all sums, prices, fees, and cashier totals from Reception, Teachers, and SysAdmin!
export function filterDataByRole(db: any, userKey: string) {
  if (!db) return {};
  const user = db.accounts ? db.accounts[userKey] : null;
  const role = user ? user.key : 'guest';

  // Deep clone to prevent accidental mutation of master DB
  const sanitized = JSON.parse(JSON.stringify(db));

  // Director gets full 360° financial transparency
  if (role === 'director') {
    const totalRev = (sanitized.receipts || []).reduce((acc: number, r: any) => acc + (Number(r.amount) || 0), 0);
    const totalExp = (sanitized.expenses || []).reduce((acc: number, e: any) => acc + (Number(e.amount) || 0), 0);
    const teacherSalaries = (sanitized.groups || []).reduce((acc: number, g: any) => acc + ((g.conductedLessons || 20) * 65000), 0);
    sanitized.computedMetrics = {
      totalRevenue: totalRev,
      totalExpenses: totalExp,
      teacherSalaries,
      netProfit: totalRev - totalExp - teacherSalaries
    };
    return sanitized;
  }

  // Cashier gets POS cash desk & student fee amounts for collecting payments
  if (role === 'cashier') {
    sanitized.expenses = [];
    sanitized.timesheetRecords = [];
    delete sanitized.computedMetrics;
    return sanitized;
  }

  // STRICT FINANCIAL PURGE FOR RECEPTION, TEACHERS, SYSADMIN:
  // 1. Purge all expenses
  sanitized.expenses = [];
  // 2. Purge all receipts
  sanitized.receipts = [];
  // 3. Purge cash balance today
  sanitized.cashBalanceToday = null;
  delete sanitized.computedMetrics;

  // 4. In groups: delete monetary fee
  if (Array.isArray(sanitized.groups)) {
    sanitized.groups = sanitized.groups.map((g: any) => {
      const copy = { ...g };
      delete copy.fee;
      return copy;
    });
  }

  // 5. In students: delete monetary monthlyFee, totalPaid, balanceUzs
  // Teachers and reception ONLY see lesson counts (e.g. "Осталось 5 уроков")
  if (Array.isArray(sanitized.students)) {
    sanitized.students = sanitized.students.map((s: any) => {
      const copy = { ...s };
      delete copy.monthlyFee;
      delete copy.totalPaid;
      delete copy.balanceUzs;
      return copy;
    });
  }

  // 6. For teachers: filter groups and students to their own curriculum
  if (role.startsWith('teacher_')) {
    const teacher = user;
    if (teacher && teacher.groups) {
      sanitized.myGroups = sanitized.groups.filter((g: any) => teacher.groups.includes(g.id));
      sanitized.myStudents = sanitized.students.filter((s: any) => teacher.groups.includes(s.groupId));
    }
  }

  return sanitized;
}

// ---------------- REST API ROUTES ----------------

// 1. Health check
app.get('/api/health', (req: Request, res: Response) => {
  res.json({
    status: 'ok',
    system: 'Maryam Academy Mission CRM/ERP',
    location: 'Маргилан, ул. Б. Маргиноний, 42',
    timestamp: new Date().toISOString(),
    port: PORT
  });
});

// 2. Login
app.post('/api/login', (req: Request, res: Response) => {
  const { login, pass } = req.body || {};
  const db = getDatabase();
  if (!db || !db.accounts) {
    return res.status(500).json({ success: false, message: 'Ошибка базы данных' });
  }

  const account = Object.values(db.accounts).find((a: any) => a.login === login && a.pass === pass) as any;
  if (!account) {
    return res.status(401).json({ success: false, message: 'Неверный логин или пароль персонала MAM' });
  }

  // Create session token
  const token = `mam_${account.key}_${Date.now()}_${Math.random().toString(36).substring(2, 8)}`;
  activeSessions.set(token, account.key);

  // Audit log
  addAuditEntry(db, 'LOGIN', `Вход в систему сотрудника: ${account.roleName} (${account.name})`, account.shortName, 'success');
  saveDatabase(db);

  res.json({
    success: true,
    token,
    user: {
      key: account.key,
      login: account.login,
      name: account.name,
      shortName: account.shortName,
      roleName: account.roleName,
      roleNameUz: account.roleNameUz,
      avatar: account.avatar,
      allowedModules: account.allowedModules,
      course: account.course || null,
      groups: account.groups || null,
      desc: account.desc
    }
  });
});

// 3. Current User
app.get('/api/me', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  if (!req.user) {
    return res.status(401).json({ success: false, message: 'Не авторизован' });
  }
  res.json({ success: true, user: req.user });
});

// 4. Data query with STRICT ROLE-BASED FINANCIAL FILTERING
app.get('/api/data', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  const db = getDatabase();
  if (!db) {
    return res.status(500).json({ error: 'База данных недоступна' });
  }

  const userKey = req.user ? req.user.key : ((req.query.role as string) || 'guest');
  const sanitizedData = filterDataByRole(db, userKey);
  res.json(sanitizedData);
});

// 5. Mark Teacher Attendance (deducts 1 lesson from student balance)
app.post('/api/attendance', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  const { studentId, status } = req.body || {};
  const db = getDatabase();
  if (!db || !db.students) {
    return res.status(500).json({ success: false, message: 'Ошибка БД' });
  }

  const student = db.students.find((s: any) => s.id === studentId);
  if (!student) {
    return res.status(404).json({ success: false, message: 'Студент не найден' });
  }

  if (status === 'present') {
    student.lessonsBalance = Math.max(0, (student.lessonsBalance || 0) - 1);
    student.consecutiveAbsences = 0;
  } else if (status === 'absent') {
    student.consecutiveAbsences = (student.consecutiveAbsences || 0) + 1;
  }

  const userShort = req.user ? req.user.shortName : 'Преподаватель';
  addAuditEntry(db, 'ATTENDANCE_CHECK', `Отметка посещаемости: ${student.name} (${student.groupId}) — ${status === 'present' ? 'Присутствовал (-1 ур.)' : 'Отсутствовал'}. Остаток: ${student.lessonsBalance} ур.`, userShort);
  saveDatabase(db);

  res.json({
    success: true,
    lessonsBalance: student.lessonsBalance,
    consecutiveAbsences: student.consecutiveAbsences
  });
});

// 6. Conduct Cashier Payment (Adds lessons, increases balance, issues receipt)
app.post('/api/payments', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  if (req.user && req.user.key !== 'cashier' && req.user.key !== 'director') {
    return res.status(403).json({ success: false, message: 'Доступ запрещен: проведение оплат доступно только Кассиру' });
  }

  const { studentId, amount, method, lessonsToAdd, comment } = req.body || {};
  const numAmount = Number(amount) || 0;
  const numLessons = Number(lessonsToAdd) || 12;

  const db = getDatabase();
  if (!db) return res.status(500).json({ success: false, message: 'Ошибка БД' });

  const student = db.students.find((s: any) => s.id === studentId);
  if (!student) {
    return res.status(404).json({ success: false, message: 'Ученик не найден' });
  }

  student.lessonsBalance = (student.lessonsBalance || 0) + numLessons;
  student.status = 'Оплачен';

  db.cashBalanceToday = (db.cashBalanceToday || 0) + numAmount;

  const pad = (n: number) => String(n).padStart(2, '0');
  const now = new Date();
  const dateStr = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}`;
  const receiptId = 'REC-' + (1000 + (db.receipts ? db.receipts.length + 1 : 1));
  const cashierName = req.user ? req.user.shortName : 'Рахимова Н.О.';

  const receipt = {
    id: receiptId,
    date: dateStr,
    studentId: student.id,
    studentName: student.name,
    phone: student.phone,
    group: student.groupId,
    amount: numAmount,
    method: method || 'Наличные',
    lessonsAdded: numLessons,
    cashier: cashierName,
    comment: comment || ''
  };

  if (!db.receipts) db.receipts = [];
  db.receipts.unshift(receipt);

  addAuditEntry(db, 'PAYMENT_RECEIVED', `Принята оплата: ${numAmount.toLocaleString()} сум (${method}) от ${student.name} за ${numLessons} уроков. Чек #${receiptId}`, cashierName);
  saveDatabase(db);

  res.json({
    success: true,
    receipt,
    student: {
      id: student.id,
      name: student.name,
      lessonsBalance: student.lessonsBalance,
      status: student.status
    }
  });
});

// 7. Register New Student (Reception)
app.post('/api/students', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  const { name, parentName, phone, parentPhone, parentPassport, groupId, lessonsBalance } = req.body || {};
  if (!name || !groupId) {
    return res.status(400).json({ success: false, message: 'Имя и группа обязательны' });
  }

  const db = getDatabase();
  if (!db) return res.status(500).json({ success: false, message: 'Ошибка БД' });

  const grp = (db.groups || []).find((g: any) => g.id === groupId) || { name: groupId, course: 'Курс MAM', teacherName: 'Преподаватель MAM', fee: 600000 };
  const newIdx = (db.students ? db.students.length : 0) + 1;
  const newStudent = {
    id: 'STU-' + (1000 + newIdx),
    name: name.trim(),
    parentName: (parentName || '').trim(),
    phone: (phone || '').trim(),
    parentPhone: (parentPhone || '').trim(),
    parentPassport: (parentPassport || 'AD 2000000').trim(),
    groupId: grp.id,
    groupName: grp.name,
    course: grp.course,
    teacherName: grp.teacherName,
    lessonsBalance: Number(lessonsBalance) || 12,
    consecutiveAbsences: 0,
    contractNumber: 'MAM-2026-' + (4100 + newIdx),
    monthlyFee: grp.fee,
    status: 'Новый'
  };

  if (!db.students) db.students = [];
  db.students.push(newStudent);

  const userShort = req.user ? req.user.shortName : 'Ресепшен';
  addAuditEntry(db, 'STUDENT_ENROLL', `Зарегистрирован новый ученик: ${newStudent.name} в группу ${newStudent.groupId} (${newStudent.course}). Договор: ${newStudent.contractNumber}`, userShort);
  saveDatabase(db);

  res.json({ success: true, student: newStudent });
});

// 8. Add Expense (Director only)
app.post('/api/expenses', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  if (req.user && req.user.key !== 'director') {
    return res.status(403).json({ success: false, message: 'Доступ запрещен: управление расходами доступно только Директору' });
  }

  const { title, category, amount, comment } = req.body || {};
  const db = getDatabase();
  if (!db) return res.status(500).json({ success: false, message: 'Ошибка БД' });

  const pad = (n: number) => String(n).padStart(2, '0');
  const now = new Date();
  const dateStr = `${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}`;

  const newExpense = {
    id: 'EXP-' + (100 + (db.expenses ? db.expenses.length + 1 : 1)),
    date: dateStr,
    title: (title || 'Операционный расход').trim(),
    category: category || 'Прочее',
    amount: Number(amount) || 0,
    approvedBy: req.user ? req.user.shortName : 'Богданов Т.Я.',
    status: 'paid',
    comment: comment || ''
  };

  if (!db.expenses) db.expenses = [];
  db.expenses.unshift(newExpense);

  addAuditEntry(db, 'EXPENSE_ADDED', `Утвержден расход: ${newExpense.title} (${newExpense.category}) на сумму ${newExpense.amount.toLocaleString()} сум`, req.user ? req.user.shortName : 'Директор');
  saveDatabase(db);

  res.json({ success: true, expense: newExpense });
});

// 9. Update Classroom Schedule Slot
app.post('/api/schedule', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  const { groupId, room, schedule } = req.body || {};
  const db = getDatabase();
  if (!db) return res.status(500).json({ success: false, message: 'Ошибка БД' });

  const grp = (db.groups || []).find((g: any) => g.id === groupId);
  if (!grp) {
    return res.status(404).json({ success: false, message: 'Группа не найдена' });
  }

  grp.room = room || grp.room;
  grp.schedule = schedule || grp.schedule;

  const userShort = req.user ? req.user.shortName : 'Администратор';
  addAuditEntry(db, 'SCHEDULE_UPDATE', `Обновлено расписание группы ${grp.id} (${grp.name}): ${grp.room}, ${grp.schedule}`, userShort);
  saveDatabase(db);

  res.json({ success: true, group: grp });
});

// 10. Update IT Equipment Inventory Status (Sysadmin)
app.post('/api/inventory', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  const { id, status, specsNote } = req.body || {};
  const db = getDatabase();
  if (!db) return res.status(500).json({ success: false, message: 'Ошибка БД' });

  const item = (db.equipment || []).find((e: any) => e.id === id);
  if (!item) {
    return res.status(404).json({ success: false, message: 'Оборудование не найдено' });
  }

  if (status) item.status = status;
  if (specsNote) item.specsNote = specsNote;
  item.checked = new Date().toISOString().split('T')[0];

  const userShort = req.user ? req.user.shortName : 'Сисадмин';
  addAuditEntry(db, 'HARDWARE_CHECK', `Проверка оборудования ${item.id} (${item.name}): статус изменен на ${item.status}. Примечание: ${item.specsNote}`, userShort);
  saveDatabase(db);

  res.json({ success: true, item });
});

// 11. Database Backup & Restore
app.get('/api/backup', (req: Request, res: Response) => {
  const db = getDatabase();
  res.setHeader('Content-Disposition', 'attachment; filename="mam_database_backup.json"');
  res.setHeader('Content-Type', 'application/json');
  res.send(JSON.stringify(db, null, 2));
});

app.post('/api/restore', authMiddleware, (req: Request & { user?: any }, res: Response) => {
  if (req.user && req.user.key !== 'sysadmin' && req.user.key !== 'director') {
    return res.status(403).json({ success: false, message: 'Только Сисадмин или Директор могут восстанавливать БД' });
  }

  const backupData = req.body;
  if (!backupData || !backupData.accounts || !backupData.groups) {
    return res.status(400).json({ success: false, message: 'Неверный формат резервной копии' });
  }

  saveDatabase(backupData);
  res.json({ success: true, message: 'База данных успешно восстановлена из резервной копии' });
});

// 12. Start dev or production server
async function startServer() {
  const isDev = process.env.NODE_ENV !== 'production';

  if (isDev) {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: 'spa',
    });
    // Mount Vite middleware after API routes
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(__dirname, 'dist');
    if (fs.existsSync(distPath)) {
      app.use(express.static(distPath));
    }
    app.use(express.static(__dirname));

    app.get('*', (req: Request, res: Response) => {
      if (req.path.startsWith('/api/')) {
        return res.status(404).json({ error: 'Endpoint not found' });
      }
      const indexPath = path.join(__dirname, 'index.html');
      if (fs.existsSync(indexPath)) {
        res.sendFile(indexPath);
      } else {
        res.sendFile(path.join(__dirname, 'crm.html'));
      }
    });
  }

  const server = http.createServer(app);
  server.listen(PORT, '0.0.0.0', () => {
    console.log(`=======================================================`);
    console.log(` Maryam Academy Mission (MAM) CRM/ERP Server Started`);
    console.log(` Local Network URL: http://0.0.0.0:${PORT}`);
    console.log(` Mode: ${isDev ? 'Development (Vite + Express)' : 'Production'}`);
    console.log(` Financial Security: STRICT ROLE-BASED MASKING ENABLED`);
    console.log(` Database: ${DB_PATH}`);
    console.log(`=======================================================`);
  });
}

startServer().catch((err) => {
  console.error('Fatal server startup error:', err);
  process.exit(1);
});

export { app };
export default app;
