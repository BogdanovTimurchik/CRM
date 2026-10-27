/**
 * MARYAM ACADEMY MISSION (MAM) - Mobile CRM & ERP Engine
 * Role-Based Access Control (RBAC), POS Thermal Print Engine, Gamification & Financials
 */

// ================= 1. STATE & RBAC CREDENTIALS =================
const RBAC_USERS = {
  admin: {
    username: 'admin',
    password: 'admin123',
    name: 'Главный Администратор',
    role: 'SUPER ADMIN',
    badge: '👑 SUPER ADMIN',
    defaultTab: 'dashboard',
    allowedTabs: ['dashboard', 'kanban', 'gamification', 'hardware', 'attendance']
  },
  cashier: {
    username: 'cashier',
    password: 'cashier123',
    name: 'Феруза Каримова (Касса)',
    role: 'CASHIER',
    badge: '💵 CASHIER',
    defaultTab: 'dashboard',
    allowedTabs: ['dashboard', 'kanban', 'attendance']
  },
  teacher: {
    username: 'teacher',
    password: 'teacher123',
    name: 'Рустам Алиев (Senior Python)',
    role: 'TEACHER',
    badge: '👨🏫 TEACHER',
    defaultTab: 'attendance',
    allowedTabs: ['attendance', 'hardware', 'gamification']
  },
  manager: {
    username: 'manager',
    password: 'manager123',
    name: 'Жахонгир Мирзаев (Отдел продаж)',
    role: 'MANAGER',
    badge: '📋 MANAGER',
    defaultTab: 'kanban',
    allowedTabs: ['kanban', 'dashboard']
  },
  student: {
    username: 'student',
    password: 'student123',
    name: 'Амир Темуров (Python Junior)',
    role: 'STUDENT',
    badge: '🎓 STUDENT',
    defaultTab: 'gamification',
    allowedTabs: ['gamification', 'hardware', 'attendance']
  },
  parent: {
    username: 'parent',
    password: 'parent123',
    name: 'Шоира Темурова (Мама Амира)',
    role: 'PARENT',
    badge: '👨👩👦 PARENT',
    defaultTab: 'attendance',
    allowedTabs: ['attendance', 'gamification', 'dashboard']
  },
  tech: {
    username: 'tech',
    password: 'tech123',
    name: 'Тимур Сабиров (Hardware Lead)',
    role: 'SYSADMIN',
    badge: '🛠 SYSADMIN',
    defaultTab: 'hardware',
    allowedTabs: ['hardware', 'dashboard']
  },
  methodist: {
    username: 'methodist',
    password: 'methodist123',
    name: 'Елена Васильева (Методист)',
    role: 'METHODIST',
    badge: '📚 METHODIST',
    defaultTab: 'gamification',
    allowedTabs: ['gamification', 'attendance', 'dashboard']
  }
};

// Initial Demo Data
const INITIAL_DATA = {
  currentLang: 'ru',
  activeUser: null,
  currentTab: 'dashboard',
  userCoins: 480,
  leads: [
    { id: 'lead-1', name: 'Бекзод Ахмедов', phone: '+998 90 321-44-55', course: 'Python Junior', stage: 'new', date: '21.09' },
    { id: 'lead-2', name: 'Камила Назарова', phone: '+998 93 881-22-11', course: 'Frontend Web', stage: 'trial', date: '22.09, 16:30' },
    { id: 'lead-3', name: 'Сарвар Искандаров', phone: '+998 97 450-99-00', course: 'Robotics 1:1', stage: 'done', date: 'Вчера (Оценка: 5/5)' },
    { id: 'lead-4', name: 'Диёра Умарова', phone: '+998 91 700-11-22', course: 'Python Junior', stage: 'paid', date: 'Оплачено (1,450,000)' }
  ],
  students: [
    { id: 'st-1', name: 'Амир Темуров', group: '#104', laptop: 'ASUS TUF SN-8942', attendance: 'present', coins: 480, grade: 'A+' },
    { id: 'st-2', name: 'Малика Саидова', group: '#104', laptop: 'Lenovo Legion SN-4412', attendance: 'present', coins: 390, grade: 'A' },
    { id: 'st-3', name: 'Сардор Каримов', group: '#104', laptop: 'Dell G15 SN-9901', attendance: 'late', coins: 310, grade: 'B+' },
    { id: 'st-4', name: 'Дильноза Юсупова', group: '#104', laptop: 'Acer Nitro SN-3381', attendance: 'absent', coins: 250, grade: 'B' },
    { id: 'st-5', name: 'Жасур Рахимов', group: '#104', laptop: 'HP Victus SN-7720', attendance: 'present', coins: 420, grade: 'A' }
  ],
  hardware: [
    { id: 'lp-1', model: 'ASUS TUF Gaming F15', sn: 'SN-8942', student: 'Амир Темуров', seat: 'Место 1', battery: 98, temp: '41°C', ram: '16GB DDR5', ssd: '100% OK', status: 'active' },
    { id: 'lp-2', model: 'Lenovo Legion 5 Pro', sn: 'SN-4412', student: 'Малика Саидова', seat: 'Место 2', battery: 94, temp: '43°C', ram: '16GB DDR5', ssd: '100% OK', status: 'active' },
    { id: 'lp-3', model: 'Dell G15 Special Ed.', sn: 'SN-9901', student: 'Сардор Каримов', seat: 'Место 3', battery: 89, temp: '46°C', ram: '16GB DDR5', ssd: '99% OK', status: 'active' },
    { id: 'lp-4', model: 'Acer Nitro V15', sn: 'SN-3381', student: 'Дильноза Юсупова', seat: 'Место 4', battery: 92, temp: '39°C', ram: '16GB DDR5', ssd: '100% OK', status: 'active' },
    { id: 'lp-5', model: 'HP Victus 16 Edition', sn: 'SN-7720', student: 'Жасур Рахимов', seat: 'Место 5', battery: 96, temp: '42°C', ram: '16GB DDR5', ssd: '100% OK', status: 'active' }
  ],
  teachers: [
    { name: 'Рустам Алиев (Python Lead)', hours: 48, rate: 120000, students: 25, bonus: 1200000 },
    { name: 'Гульноза Исмаилова (Frontend Lead)', hours: 42, rate: 110000, students: 20, bonus: 950000 },
    { name: 'Даврон Юлдашев (Robotics Lead)', hours: 36, rate: 125000, students: 18, bonus: 800000 }
  ],
  expenses: [
    { title: 'Аренда помещений (Ц-1)', amount: '12,500,000 UZS', cat: 'Аренда', date: '01.09' },
    { title: 'Оптоволоконный интернет 1 Gbps', amount: '1,400,000 UZS', cat: 'Связь', date: '05.09' },
    { title: 'Кофе-брейк и бутилированная вода', amount: '1,200,000 UZS', cat: 'Хозрасходы', date: '12.09' },
    { title: 'Сервисное ТО ноутбуков 1:1', amount: '850,000 UZS', cat: 'Hardware', date: '18.09' }
  ],
  merch: [
    { id: 'm-1', name: 'MAM Cyber Hoodie', cost: 350, icon: 'fa-shirt', color: 'bg-emerald-50 text-emerald-700' },
    { id: 'm-2', name: 'Cyberpunk Sticker Pack', cost: 80, icon: 'fa-note-sticky', color: 'bg-blue-50 text-blue-700' },
    { id: 'm-3', name: 'Hacker Metal Pin Badge', cost: 120, icon: 'fa-shield-halved', color: 'bg-purple-50 text-purple-700' },
    { id: 'm-4', name: 'Mechanical Keycap (MAM)', cost: 200, icon: 'fa-keyboard', color: 'bg-amber-50 text-amber-700' },
    { id: 'm-5', name: 'Smart Thermos Bottle', cost: 280, icon: 'fa-mug-hot', color: 'bg-teal-50 text-teal-700' }
  ],
  auditLog: [
    { time: '10:45:12', user: 'cashier', action: 'Принят платеж 1,450,000 UZS от Амира Темурова (чек #008942)', type: 'payment' },
    { time: '10:15:00', user: 'teacher', action: 'Отметка посещаемости мини-группы #104 (5/5 учеников)', type: 'attendance' },
    { time: '09:40:22', user: 'admin', action: 'Пересчитан фонд заработной платы за сентябрь 2026', type: 'payroll' },
    { time: '09:12:10', user: 'manager', action: 'Лид Диёра Умарова переведен в статус «Оплатил / Ученик»', type: 'lead' }
  ]
};

// Multi-language dictionary
const I18N = {
  ru: {
    appTitle: 'MARYAM ACADEMY MISSION',
    installBanner: 'Установить MAM CRM на главный экран',
    installSub: 'Быстрый доступ, офлайн-режим и мгновенные уведомления',
    dashTab: 'Обзор',
    leadsTab: 'Заявки',
    gameTab: 'LMS & Коины',
    techTab: '1:1 Ноутбуки',
    certTab: 'Журнал & A4',
    revenue: 'Выручка за месяц',
    profit: 'Чистая прибыль',
    students: 'Активные ученики',
    occupancy: 'Заполненность',
    payrollTitle: 'Расчет зарплат преподавателей (Payroll)',
    expensesTitle: 'Операционные расходы (P&L)',
    auditTitle: 'Журнал безопасности и транзакций (Audit Trail)'
  },
  uz: {
    appTitle: 'MARYAM ACADEMY MISSION',
    installBanner: 'MAM CRM-ni asosiy ekranga o‘rnatish',
    installSub: 'Tezkor kirish, oflayn rejim va bildirishnomalar',
    dashTab: 'Moliya',
    leadsTab: 'Arizalar',
    gameTab: 'LMS & Tangalar',
    techTab: 'Noutbuklar',
    certTab: 'Davomat & Sertifikat',
    revenue: 'Oylik tushum',
    profit: 'Sof foyda',
    students: 'Faol o‘quvchilar',
    occupancy: 'Guruh to‘lishi',
    payrollTitle: 'O‘qituvchilar maoshi hisobi (Payroll)',
    expensesTitle: 'Operatsion xarajatlar (P&L)',
    auditTitle: 'Xavfsizlik va tranzaksiyalar jurnali'
  },
  en: {
    appTitle: 'MARYAM ACADEMY MISSION',
    installBanner: 'Install MAM CRM to Home Screen',
    installSub: 'Fast access, offline mode & push notifications',
    dashTab: 'Analytics',
    leadsTab: 'Leads',
    gameTab: 'LMS & Coins',
    techTab: 'Laptops 1:1',
    certTab: 'Attendance & A4',
    revenue: 'Monthly Revenue',
    profit: 'Net Profit',
    students: 'Active Students',
    occupancy: 'Group Occupancy',
    payrollTitle: 'Faculty Payroll & Retention Bonus',
    expensesTitle: 'Operating Expenses (P&L)',
    auditTitle: 'Security & Audit Trail Log'
  }
};

let appState = loadState();

function loadState() {
  const saved = localStorage.getItem('MAM_ERP_STATE');
  if (saved) {
    try {
      return JSON.parse(saved);
    } catch (e) {
      console.warn('Fallback to default state', e);
    }
  }
  return JSON.parse(JSON.stringify(INITIAL_DATA));
}

function saveState() {
  localStorage.setItem('MAM_ERP_STATE', JSON.stringify(appState));
}

function renderApp() {
  if (typeof renderAllModules === 'function') {
    renderAllModules();
  }
}

// ================= 2. INITIALIZATION & PWA =================
window.addEventListener('DOMContentLoaded', () => {
  initPWA();
  renderApp();
  if (appState.activeUser) {
    showAppView();
  } else {
    showLoginView();
  }
});

let deferredInstallPrompt = null;

function initPWA() {
  // Service Worker Registration
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch((err) => {
      console.log('SW registration note:', err);
    });
  }

  // Intercept beforeinstallprompt
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredInstallPrompt = e;
    const banner = document.getElementById('pwa-banner');
    if (banner && !sessionStorage.getItem('mam_pwa_dismissed')) {
      banner.classList.remove('hidden');
    }
  });

  // Check if iOS
  const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  const isStandalone = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone;
  if (isIOS && !isStandalone && !sessionStorage.getItem('mam_pwa_dismissed')) {
    const banner = document.getElementById('pwa-banner');
    if (banner) banner.classList.remove('hidden');
  }
}

function installPWA() {
  if (deferredInstallPrompt) {
    deferredInstallPrompt.prompt();
    deferredInstallPrompt.userChoice.then(() => {
      deferredInstallPrompt = null;
      dismissPWABanner();
    });
  } else {
    // Show iOS Guide
    document.getElementById('modal-ios-install').classList.remove('hidden');
  }
}

function dismissPWABanner() {
  const banner = document.getElementById('pwa-banner');
  if (banner) banner.classList.add('hidden');
  sessionStorage.setItem('mam_pwa_dismissed', 'true');
}

function closeIOSGuide() {
  document.getElementById('modal-ios-install').classList.add('hidden');
}

// ================= 3. AUTHENTICATION & ROLE SWITCHING =================
function fillLogin(username, password) {
  document.getElementById('login-username').value = username;
  document.getElementById('login-password').value = password;
  document.getElementById('login-error').classList.add('hidden');
}

function togglePasswordVisibility() {
  const pwdInput = document.getElementById('login-password');
  const eyeIcon = document.getElementById('password-eye-icon');
  if (pwdInput.type === 'password') {
    pwdInput.type = 'text';
    eyeIcon.classList.replace('fa-eye', 'fa-eye-slash');
  } else {
    pwdInput.type = 'password';
    eyeIcon.classList.replace('fa-eye-slash', 'fa-eye');
  }
}

function handleLogin(event) {
  event.preventDefault();
  const username = document.getElementById('login-username').value.trim().toLowerCase();
  const password = document.getElementById('login-password').value;
  const errBox = document.getElementById('login-error');

  const user = RBAC_USERS[username];
  if (user && user.password === password) {
    appState.activeUser = user;
    appState.currentTab = user.defaultTab;
    saveState();
    showToast(`Вход выполнен: ${user.name}`);
    showAppView();
    addAuditLog(user.username, `Пользователь ${user.name} вошел в систему`);
  } else {
    errBox.classList.remove('hidden');
  }
}

function handleLogout() {
  if (confirm('Вы уверены, что хотите выйти из сессии?')) {
    addAuditLog(appState.activeUser?.username || 'user', 'Выход из сессии');
    appState.activeUser = null;
    saveState();
    showLoginView();
    showToast('Сессия завершена');
  }
}

function showLoginView() {
  document.getElementById('login-view').classList.remove('hidden');
  document.getElementById('app-wrapper').classList.add('hidden');
}

function showAppView() {
  document.getElementById('login-view').classList.add('hidden');
  document.getElementById('app-wrapper').classList.remove('hidden');
  updateUserUI();
  switchTab(appState.currentTab || appState.activeUser.defaultTab);
  renderAllModules();
}

function updateUserUI() {
  const user = appState.activeUser;
  if (!user) return;

  const roleBadge = document.getElementById('role-badge');
  const userDisplay = document.getElementById('user-display-name');

  if (roleBadge) {
    roleBadge.textContent = user.role;
  }
  if (userDisplay) {
    userDisplay.textContent = user.name;
  }

  // Filter bottom nav items based on user allowedTabs
  document.querySelectorAll('.nav-item').forEach((btn) => {
    const tabName = btn.getAttribute('data-tab');
    if (user.allowedTabs.includes(tabName)) {
      btn.classList.remove('hidden');
    } else {
      btn.classList.add('hidden');
    }
  });
}

// ================= 4. TAB NAVIGATION =================
function switchTab(tabId) {
  appState.currentTab = tabId;
  saveState();

  // Hide all tabs
  document.querySelectorAll('.tab-content').forEach((tab) => {
    tab.classList.add('hidden');
  });

  // Show active tab
  const activeTabEl = document.getElementById(`tab-${tabId}`);
  if (activeTabEl) {
    activeTabEl.classList.remove('hidden');
  }

  // Update nav button states
  document.querySelectorAll('.nav-item').forEach((btn) => {
    const isTarget = btn.getAttribute('data-tab') === tabId;
    if (isTarget) {
      btn.classList.remove('text-slate-400');
      btn.classList.add('text-emerald-600', 'font-bold');
    } else {
      btn.classList.remove('text-emerald-600', 'font-bold');
      btn.classList.add('text-slate-400');
    }
  });

  if (tabId === 'gamification') {
    setTimeout(drawSkillRadar, 50);
  }
}

// ================= 5. MODULE RENDERERS =================
function renderAllModules() {
  renderPayroll();
  renderExpenses();
  renderAuditLog();
  renderKanban();
  renderMerchStore();
  renderHomework();
  renderHardwareSeats();
  renderAttendance();
  updateCoinsDisplay();
}

// Module 6: Payroll
function renderPayroll() {
  const container = document.getElementById('payroll-list');
  if (!container) return;

  container.innerHTML = appState.teachers.map((t, idx) => {
    const total = (t.hours * t.rate) + t.bonus;
    return `
      <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
        <div>
          <p class="font-bold text-slate-800">${t.name}</p>
          <p class="text-[10px] text-slate-500">
            ${t.hours} ч. × ${t.rate.toLocaleString()} UZS + Бонус за удержание (${t.students} уч.): +${t.bonus.toLocaleString()} UZS
          </p>
        </div>
        <div class="flex items-center justify-between sm:justify-end gap-3 pt-1 sm:pt-0 border-t sm:border-t-0 border-slate-200">
          <span class="font-mono font-black text-emerald-700 text-xs">${total.toLocaleString()} UZS</span>
          <button onclick="payTeacherSalary('${t.name}', ${total})" class="px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-[10px] shadow-xs transition">
            Выплатить
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function recalculatePayroll() {
  showToast('Табель часов и бонусы пересчитаны!');
  addAuditLog(appState.activeUser.username, 'Ручной пересчет табеля зарплат');
}

function payTeacherSalary(name, total) {
  showToast(`Зарплата ${total.toLocaleString()} UZS выплачена: ${name}`);
  addAuditLog(appState.activeUser.username, `Выплата зарплаты ${total.toLocaleString()} UZS -> ${name}`);
}

// Expenses
function renderExpenses() {
  const container = document.getElementById('expense-list');
  if (!container) return;

  container.innerHTML = appState.expenses.map((exp, idx) => `
    <div class="flex items-center justify-between p-2 rounded-xl bg-slate-50 border border-slate-200">
      <div>
        <p class="font-semibold text-slate-800 leading-tight">${exp.title}</p>
        <span class="text-[10px] text-slate-400 font-mono">${exp.cat} • ${exp.date}</span>
      </div>
      <div class="flex items-center gap-2">
        <span class="font-mono font-bold text-slate-700">${exp.amount}</span>
        <button onclick="deleteExpense(${idx})" class="text-slate-400 hover:text-rose-500 text-xs px-1"><i class="fa-solid fa-trash-can"></i></button>
      </div>
    </div>
  `).join('');
}

function openAddExpenseModal() {
  const title = prompt('Название расхода (напр., Закупка кабелей HDMI):');
  if (!title) return;
  const amount = prompt('Сумма (UZS):', '350,000');
  if (!amount) return;

  appState.expenses.unshift({
    title,
    amount: `${amount} UZS`,
    cat: 'Расход',
    date: 'Сегодня'
  });
  saveState();
  renderExpenses();
  showToast('Расход добавлен в P&L');
  addAuditLog(appState.activeUser.username, `Добавлен расход: ${title} (${amount} UZS)`);
}

function deleteExpense(index) {
  appState.expenses.splice(index, 1);
  saveState();
  renderExpenses();
  showToast('Запись расхода удалена');
}

// Audit Trail
function renderAuditLog() {
  const container = document.getElementById('audit-log-container');
  if (!container) return;

  container.innerHTML = appState.auditLog.map(item => `
    <div class="p-1.5 rounded-lg bg-slate-50 border border-slate-200/80 flex items-center justify-between text-[11px]">
      <div class="flex items-center gap-2 truncate">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-500 flex-shrink-0"></span>
        <span class="font-mono text-[10px] text-slate-400">${item.time}</span>
        <span class="font-bold text-slate-700 truncate">[${item.user}]</span>
        <span class="text-slate-600 truncate">${item.action}</span>
      </div>
    </div>
  `).join('');
}

function addAuditLog(user, action) {
  const now = new Date();
  const time = now.toTimeString().split(' ')[0];
  appState.auditLog.unshift({ time, user, action });
  if (appState.auditLog.length > 30) appState.auditLog.pop();
  saveState();
  renderAuditLog();
}

// Kanban Sales Pipeline
function renderKanban() {
  const cols = {
    new: document.getElementById('kanban-col-new'),
    trial: document.getElementById('kanban-col-trial'),
    done: document.getElementById('kanban-col-done'),
    paid: document.getElementById('kanban-col-paid')
  };

  const counts = { new: 0, trial: 0, done: 0, paid: 0 };
  Object.values(cols).forEach(col => { if (col) col.innerHTML = ''; });

  appState.leads.forEach(lead => {
    counts[lead.stage] = (counts[lead.stage] || 0) + 1;
    const col = cols[lead.stage];
    if (!col) return;

    const card = document.createElement('div');
    card.className = 'bg-white p-2.5 rounded-xl border border-slate-200 shadow-xs space-y-1.5 text-xs';
    card.innerHTML = `
      <div class="flex items-center justify-between">
        <p class="font-bold text-slate-900">${lead.name}</p>
        <span class="text-[9px] text-slate-400 font-mono">${lead.date}</span>
      </div>
      <p class="text-[11px] text-emerald-700 font-medium">${lead.course}</p>
      <p class="text-[10px] text-slate-500 font-mono"><i class="fa-solid fa-phone mr-1"></i>${lead.phone}</p>
      <div class="flex items-center justify-between pt-1 border-t border-slate-100">
        <button onclick="moveLead('${lead.id}', -1)" class="p-1 text-slate-400 hover:text-slate-700 text-[10px]"><i class="fa-solid fa-arrow-left"></i></button>
        ${lead.stage !== 'paid' ? `
          <button onclick="convertLeadToStudent('${lead.id}')" class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold text-[10px] hover:bg-emerald-100">
            В ученика
          </button>
        ` : `
          <button onclick="openReceiptForStudent('${lead.name}')" class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 border border-blue-200 font-bold text-[10px]">
            Чек POS
          </button>
        `}
        <button onclick="moveLead('${lead.id}', 1)" class="p-1 text-slate-400 hover:text-slate-700 text-[10px]"><i class="fa-solid fa-arrow-right"></i></button>
      </div>
    `;
    col.appendChild(card);
  });

  document.getElementById('col-count-new').textContent = counts.new;
  document.getElementById('col-count-trial').textContent = counts.trial;
  document.getElementById('col-count-done').textContent = counts.done;
  document.getElementById('col-count-paid').textContent = counts.paid;
}

const STAGES = ['new', 'trial', 'done', 'paid'];

function moveLead(leadId, dir) {
  const lead = appState.leads.find(l => l.id === leadId);
  if (!lead) return;
  const currentIdx = STAGES.indexOf(lead.stage);
  const nextIdx = currentIdx + dir;
  if (nextIdx >= 0 && nextIdx < STAGES.length) {
    lead.stage = STAGES[nextIdx];
    saveState();
    renderKanban();
    showToast(`Лид переведен в статус: ${lead.stage}`);
    addAuditLog(appState.activeUser.username, `Лид ${lead.name} сменил этап на ${lead.stage}`);
  }
}

function convertLeadToStudent(leadId) {
  const lead = appState.leads.find(l => l.id === leadId);
  if (!lead) return;
  lead.stage = 'paid';

  // Add to students if not already present
  if (!appState.students.some(s => s.name === lead.name)) {
    appState.students.push({
      id: `st-${Date.now()}`,
      name: lead.name,
      group: '#104',
      laptop: 'Резерв ASUS TUF',
      attendance: 'present',
      coins: 100,
      grade: 'A'
    });
  }

  saveState();
  renderKanban();
  renderAttendance();
  openReceiptForStudent(lead.name);
  showToast(`Лид ${lead.name} успешно зачислен в ученики!`);
  addAuditLog(appState.activeUser.username, `Конверсия лида в студента: ${lead.name}`);
}

function openAddLeadModal() {
  document.getElementById('modal-add-lead').classList.remove('hidden');
}

function closeAddLeadModal() {
  document.getElementById('modal-add-lead').classList.add('hidden');
}

function handleCreateLead(e) {
  e.preventDefault();
  const name = document.getElementById('new-lead-name').value.trim();
  const phone = document.getElementById('new-lead-phone').value.trim();
  const course = document.getElementById('new-lead-course').value;

  appState.leads.unshift({
    id: `lead-${Date.now()}`,
    name,
    phone,
    course,
    stage: 'new',
    date: 'Сегодня'
  });

  saveState();
  renderKanban();
  closeAddLeadModal();
  e.target.reset();
  showToast('Новый лид добавлен!');
  addAuditLog(appState.activeUser.username, `Добавлен лид: ${name} (${course})`);
}

// Module 2 & 3: Gamification & Merch Store
function updateCoinsDisplay() {
  const coinEl = document.getElementById('user-coin-balance');
  if (coinEl) {
    coinEl.textContent = appState.userCoins;
  }
}

function renderMerchStore() {
  const container = document.getElementById('merch-items-grid');
  if (!container) return;

  container.innerHTML = appState.merch.map(item => `
    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col justify-between space-y-2">
      <div class="flex items-center justify-between">
        <div class="w-8 h-8 rounded-xl ${item.color} flex items-center justify-center text-sm">
          <i class="fa-solid ${item.icon}"></i>
        </div>
        <span class="text-xs font-black font-mono text-amber-600">${item.cost} 🪙</span>
      </div>
      <div>
        <p class="font-bold text-xs text-slate-800 leading-tight">${item.name}</p>
        <p class="text-[10px] text-slate-400">Фирменный мерч MAM</p>
      </div>
      <button onclick="buyMerchItem('${item.name}', ${item.cost})" class="w-full py-1.5 rounded-xl bg-white border border-slate-200 hover:border-emerald-500 hover:bg-emerald-50 text-slate-700 hover:text-emerald-700 font-bold text-[11px] transition shadow-2xs">
        Обменять
      </button>
    </div>
  `).join('');
}

function buyMerchItem(name, cost) {
  if (appState.userCoins >= cost) {
    appState.userCoins -= cost;
    saveState();
    updateCoinsDisplay();
    showToast(`Успешно приобретено: ${name}!`);
    addAuditLog(appState.activeUser.username, `Обмен ${cost} MAM Coins на ${name}`);
  } else {
    alert(`Недостаточно MAM Coins! Требуется ${cost}, у вас ${appState.userCoins}. Посещайте занятия и делайте ДЗ!`);
  }
}

function openAwardCoinsModal() {
  const student = prompt('Имя ученика для начисления:', 'Амир Темуров');
  if (!student) return;
  const amount = parseInt(prompt('Количество MAM Coins (+10, +25, +50):', '25'), 10);
  if (!amount || isNaN(amount)) return;

  appState.userCoins += amount;
  saveState();
  updateCoinsDisplay();
  showToast(`+${amount} MAM Coins начислено ученику: ${student}`);
  addAuditLog(appState.activeUser.username, `Начисление +${amount} MAM Coins -> ${student}`);
}

function scrollToStore() {
  const store = document.getElementById('merch-store-section');
  if (store) store.scrollIntoView({ behavior: 'smooth' });
}

// Homework LMS
function renderHomework() {
  const container = document.getElementById('homework-list');
  if (!container) return;

  const hws = [
    { student: 'Амир Темуров', task: 'ДЗ #4: Калькулятор с функциями Python', status: 'approved', score: '5/5', time: 'Вчера' },
    { student: 'Малика Саидова', task: 'ДЗ #4: Обработка списков и срезов', status: 'pending', score: 'На проверке', time: 'Сегодня' },
    { student: 'Сардор Каримов', task: 'ДЗ #3: Алгоритмы поиска в строках', status: 'revision', score: 'Доработать', time: '2 дня назад' }
  ];

  container.innerHTML = hws.map(h => {
    let badge = 'bg-emerald-50 text-emerald-700 border-emerald-200';
    if (h.status === 'pending') badge = 'bg-amber-50 text-amber-700 border-amber-200';
    if (h.status === 'revision') badge = 'bg-rose-50 text-rose-700 border-rose-200';

    return `
      <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-between text-xs">
        <div>
          <p class="font-bold text-slate-800">${h.student}</p>
          <p class="text-[11px] text-slate-500">${h.task}</p>
        </div>
        <div class="text-right">
          <span class="px-2 py-0.5 rounded-md border text-[10px] font-bold ${badge}">${h.score}</span>
          <p class="text-[9px] text-slate-400 mt-0.5">${h.time}</p>
        </div>
      </div>
    `;
  }).join('');
}

function openSubmitHomeworkModal() {
  const link = prompt('Вставьте ссылку на GitHub репозиторий или файл проекта:');
  if (link) {
    showToast('Домашнее задание отправлено преподавателю на ревью (+25 Coins после проверки)!');
    addAuditLog(appState.activeUser.username, 'Сдача ДЗ на проверку');
  }
}

// Visual Skill Radar Canvas
function drawSkillRadar() {
  const canvas = document.getElementById('skillRadarCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width;
  const h = canvas.height;
  const centerX = w / 2;
  const centerY = h / 2;
  const radius = Math.min(centerX, centerY) - 30;

  ctx.clearRect(0, 0, w, h);

  const skills = [
    { label: 'Логика', value: 0.92 },
    { label: 'Домашки', value: 0.88 },
    { label: 'Дисциплина', value: 0.95 },
    { label: 'Проекты', value: 0.85 },
    { label: 'Алгоритмы', value: 0.90 }
  ];

  const sides = skills.length;
  const angleStep = (Math.PI * 2) / sides;

  // Background Web concentric polygons
  for (let level = 1; level <= 4; level++) {
    const r = (radius / 4) * level;
    ctx.beginPath();
    for (let i = 0; i < sides; i++) {
      const angle = i * angleStep - Math.PI / 2;
      const x = centerX + r * Math.cos(angle);
      const y = centerY + r * Math.sin(angle);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.closePath();
    ctx.strokeStyle = '#E2E8F0';
    ctx.lineWidth = 1;
    ctx.stroke();
  }

  // Draw axis lines
  for (let i = 0; i < sides; i++) {
    const angle = i * angleStep - Math.PI / 2;
    const x = centerX + radius * Math.cos(angle);
    const y = centerY + radius * Math.sin(angle);
    ctx.beginPath();
    ctx.moveTo(centerX, centerY);
    ctx.lineTo(x, y);
    ctx.strokeStyle = '#E2E8F0';
    ctx.stroke();

    // Labels
    const lx = centerX + (radius + 18) * Math.cos(angle);
    const ly = centerY + (radius + 18) * Math.sin(angle);
    ctx.font = 'bold 10px Plus Jakarta Sans, sans-serif';
    ctx.fillStyle = '#0F172A';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(skills[i].label, lx, ly);
  }

  // Draw Data Polygon
  ctx.beginPath();
  for (let i = 0; i < sides; i++) {
    const r = radius * skills[i].value;
    const angle = i * angleStep - Math.PI / 2;
    const x = centerX + r * Math.cos(angle);
    const y = centerY + r * Math.sin(angle);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.closePath();
  ctx.fillStyle = 'rgba(16, 185, 129, 0.25)';
  ctx.fill();
  ctx.strokeStyle = '#10B981';
  ctx.lineWidth = 2.5;
  ctx.stroke();

  // Points on polygon
  for (let i = 0; i < sides; i++) {
    const r = radius * skills[i].value;
    const angle = i * angleStep - Math.PI / 2;
    const x = centerX + r * Math.cos(angle);
    const y = centerY + r * Math.sin(angle);
    ctx.beginPath();
    ctx.arc(x, y, 4, 0, Math.PI * 2);
    ctx.fillStyle = '#059669';
    ctx.fill();
    ctx.strokeStyle = '#FFFFFF';
    ctx.lineWidth = 1.5;
    ctx.stroke();
  }
}

// Module 3: Mini-Group Schedule & Hardware Tracker 1:1
function renderHardwareSeats() {
  const container = document.getElementById('laptops-seat-grid');
  if (!container) return;

  container.innerHTML = appState.hardware.map(item => `
    <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 text-xs">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-white border border-slate-200 flex flex-col items-center justify-center font-bold text-teal-700 shadow-2xs">
          <i class="fa-solid fa-laptop text-xs"></i>
          <span class="text-[9px] font-mono">${item.seat.split(' ')[1]}</span>
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <p class="font-bold text-slate-900">${item.model}</p>
            <span class="text-[9px] font-mono px-1.5 py-0.2 rounded bg-slate-200 text-slate-700">${item.sn}</span>
          </div>
          <p class="text-[11px] text-emerald-700 font-semibold">Закреплен: ${item.student}</p>
          <div class="flex items-center gap-3 text-[10px] text-slate-500 font-mono mt-0.5">
            <span><i class="fa-solid fa-battery-three-quarters text-emerald-600 mr-1"></i>${item.battery}%</span>
            <span><i class="fa-solid fa-temperature-half text-amber-500 mr-1"></i>${item.temp}</span>
            <span><i class="fa-solid fa-memory text-blue-500 mr-1"></i>${item.ram}</span>
          </div>
        </div>
      </div>
      <div class="flex items-center justify-end gap-2 border-t sm:border-t-0 pt-2 sm:pt-0 border-slate-200">
        <button onclick="toggleLaptopStatus('${item.id}')" class="px-2.5 py-1 rounded-lg ${item.status === 'active' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-rose-50 text-rose-700 border border-rose-200'} font-bold text-[10px]">
          ${item.status === 'active' ? 'В строю' : 'Сервис'}
        </button>
        <button onclick="reassignLaptop('${item.id}')" class="px-2 py-1 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-slate-900 text-[10px] font-medium">
          Сменить
        </button>
      </div>
    </div>
  `).join('');
}

function toggleLaptopStatus(id) {
  const item = appState.hardware.find(h => h.id === id);
  if (!item) return;
  item.status = item.status === 'active' ? 'maintenance' : 'active';
  saveState();
  renderHardwareSeats();
  showToast(`Статус ${item.sn} изменен: ${item.status}`);
  addAuditLog(appState.activeUser.username, `Смена статуса оборудования: ${item.sn} -> ${item.status}`);
}

function reassignLaptop(id) {
  const item = appState.hardware.find(h => h.id === id);
  if (!item) return;
  const newStudent = prompt(`Закрепить ноутбук ${item.sn} за учеником:`, item.student);
  if (newStudent) {
    item.student = newStudent;
    saveState();
    renderHardwareSeats();
    showToast(`Ноутбук ${item.sn} закреплен за ${newStudent}`);
    addAuditLog(appState.activeUser.username, `Переназначение ноутбука ${item.sn} -> ${newStudent}`);
  }
}

function runHardwareDiagnostics() {
  showToast('Диагностика оборудования: Все 5 ноутбуков в норме (100% SSD health, 0 троттлинга)');
  addAuditLog(appState.activeUser.username, 'Запуск аппаратной диагностики ноутбуков 1:1');
}

// Module 5: Attendance Ticker & Certificate Engine
function renderAttendance() {
  const container = document.getElementById('attendance-list-container');
  if (!container) return;

  container.innerHTML = appState.students.map(s => {
    return `
      <div class="p-3 rounded-2xl bg-slate-50 border border-slate-200 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 text-xs">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-full bg-emerald-100 text-emerald-800 font-black flex items-center justify-center text-xs">
            ${s.name.split(' ').map(n => n[0]).join('')}
          </div>
          <div>
            <p class="font-bold text-slate-900">${s.name}</p>
            <p class="text-[10px] text-slate-500">Группа ${s.group} • ${s.laptop}</p>
          </div>
        </div>

        <div class="flex items-center gap-1.5 justify-end">
          <button onclick="setAttendance('${s.id}', 'present')" class="px-2 py-1 rounded-lg text-[10px] font-bold transition ${s.attendance === 'present' ? 'bg-emerald-600 text-white shadow-xs' : 'bg-white border border-slate-200 text-slate-600 hover:bg-emerald-50'}">
            ✅ Присутствовал
          </button>
          <button onclick="setAttendance('${s.id}', 'late')" class="px-2 py-1 rounded-lg text-[10px] font-bold transition ${s.attendance === 'late' ? 'bg-amber-500 text-white shadow-xs' : 'bg-white border border-slate-200 text-slate-600 hover:bg-amber-50'}">
            🟡 Опоздал
          </button>
          <button onclick="setAttendance('${s.id}', 'absent')" class="px-2 py-1 rounded-lg text-[10px] font-bold transition ${s.attendance === 'absent' ? 'bg-rose-500 text-white shadow-xs' : 'bg-white border border-slate-200 text-slate-600 hover:bg-rose-50'}">
            ❌ Отсутствовал
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function setAttendance(studentId, status) {
  const s = appState.students.find(stu => stu.id === studentId);
  if (!s) return;
  s.attendance = status;
  if (status === 'present') {
    appState.userCoins += 10;
    showToast(`Отмечено: ${s.name} (+10 MAM Coins за посещение)!`);
  } else {
    showToast(`Отмечено: ${s.name} (${status})`);
  }
  saveState();
  renderAttendance();
  updateCoinsDisplay();
  addAuditLog(appState.activeUser.username, `Отметка посещаемости: ${s.name} -> ${status}`);
}

// QR Scanner Simulation
function openQRScannerModal() {
  document.getElementById('modal-qr-scanner').classList.remove('hidden');
}

function closeQRScannerModal() {
  document.getElementById('modal-qr-scanner').classList.add('hidden');
}

function simulateQRScanSuccess() {
  closeQRScannerModal();
  setAttendance('st-1', 'present');
  showToast('QR успешно распознан: Амир Темуров (MAM-STU-001) отмечен ✅');
}

// Certificate Modal Preview
function previewCertificateModal(studentName = 'Амир Темуров', courseName = '«Python Professional & Data Engineering»') {
  document.getElementById('cert-student-name').textContent = studentName;
  document.getElementById('cert-course-name').textContent = courseName;
  document.getElementById('modal-certificate').classList.remove('hidden');
}

function closeCertificateModal() {
  document.getElementById('modal-certificate').classList.add('hidden');
}

// Thermal Receipt Modal Preview & Print
function openReceiptModal() {
  openReceiptForStudent('Амир Темуров');
}

function openReceiptForStudent(studentName) {
  document.getElementById('rcpt-student-name').textContent = studentName;
  const now = new Date();
  document.getElementById('receipt-date-time').textContent = now.toLocaleDateString() + ' ' + now.toLocaleTimeString();
  document.getElementById('modal-receipt').classList.remove('hidden');
}

function closeReceiptModal() {
  document.getElementById('modal-receipt').classList.add('hidden');
}

// AI Copilot Task Generator
function openAICopilotModal() {
  document.getElementById('modal-ai-copilot').classList.remove('hidden');
}

function closeAICopilotModal() {
  document.getElementById('modal-ai-copilot').classList.add('hidden');
}

function generateAITask() {
  const topic = document.getElementById('ai-task-topic').value;
  const level = document.querySelector('input[name="ai-level"]:checked').value;
  const outBox = document.getElementById('ai-task-output');
  const titleEl = document.getElementById('ai-task-result-title');
  const descEl = document.getElementById('ai-task-result-desc');
  const codeEl = document.getElementById('ai-task-result-code');

  outBox.classList.remove('hidden');

  if (topic === 'python-loops') {
    titleEl.textContent = `[${level}] Задача: Фильтрация и суммирование четных чисел`;
    descEl.textContent = 'Напишите функцию, которая принимает произвольный список чисел и возвращает сумму квадратов только четных элементов.';
    codeEl.innerHTML = `def sum_even_squares(nums):<br>&nbsp;&nbsp;return sum(x**2 for x in nums if x % 2 == 0)<br><br># Test:<br>assert sum_even_squares([1, 2, 3, 4]) == 20`;
  } else if (topic === 'frontend-flex') {
    titleEl.textContent = `[${level}] Задача: Верстка карточки товара на Flexbox`;
    descEl.textContent = 'Создайте адаптивный контейнер с выравниванием space-between и центрированием по вертикали.';
    codeEl.innerHTML = `.card-container {<br>&nbsp;&nbsp;display: flex;<br>&nbsp;&nbsp;justify-content: space-between;<br>&nbsp;&nbsp;align-items: center;<br>&nbsp;&nbsp;gap: 16px;<br>}`;
  } else {
    titleEl.textContent = `[${level}] Задача: Алгоритмический разбор задачи`;
    descEl.textContent = 'Оптимизируйте сложность вычисления до O(N log N) с обработкой краевых случаев.';
    codeEl.innerHTML = `# Решение протестировано MAM AI Copilot<br>def solve(arr):<br>&nbsp;&nbsp;return sorted(set(arr))`;
  }

  showToast('Задача и тест-кейсы сгенерированы AI!');
  addAuditLog(appState.activeUser.username, `AI генерация задачи (${topic}, ${level})`);
}

function assignTaskToGroup() {
  closeAICopilotModal();
  showToast('Задача отправлена ученикам мини-группы #104 (+25 MAM Coins за решение)');
  addAuditLog(appState.activeUser.username, 'Назначение AI-задачи группе #104');
}

// Multi-language
function toggleLangMenu() {
  const menu = document.getElementById('lang-dropdown');
  menu.classList.toggle('hidden');
}

function setLanguage(lang) {
  appState.currentLang = lang;
  saveState();
  const menu = document.getElementById('lang-dropdown');
  if (menu) menu.classList.add('hidden');

  const label = document.getElementById('current-lang-label');
  if (label) {
    if (lang === 'ru') label.textContent = '🇷🇺 RU';
    if (lang === 'uz') label.textContent = '🇺🇿 UZ';
    if (lang === 'en') label.textContent = '🇬🇧 EN';
  }

  // Update text labels
  const d = I18N[lang] || I18N.ru;
  const setText = (id, text) => {
    const el = document.getElementById(id);
    if (el) el.textContent = text;
  };

  setText('pwa-banner-title', d.installBanner);
  setText('pwa-banner-sub', d.installSub);
  setText('nav-lbl-dash', d.dashTab);
  setText('nav-lbl-leads', d.leadsTab);
  setText('nav-lbl-game', d.gameTab);
  setText('nav-lbl-tech', d.techTab);
  setText('nav-lbl-cert', d.certTab);
  setText('kpi-revenue-title', d.revenue);
  setText('kpi-profit-title', d.profit);
  setText('kpi-students-title', d.students);
  setText('kpi-occupancy-title', d.occupancy);
  setText('payroll-title', d.payrollTitle);
  setText('expenses-title', d.expensesTitle);
  setText('audit-title', d.auditTitle);

  showToast(`Язык переключен: ${lang.toUpperCase()}`);
}

// Toast
function showToast(msg) {
  const toast = document.getElementById('toast-notification');
  const msgEl = document.getElementById('toast-message');
  if (!toast || !msgEl) return;
  msgEl.textContent = msg;
  toast.classList.remove('hidden');
  clearTimeout(window._toastTimeout);
  window._toastTimeout = setTimeout(() => {
    toast.classList.add('hidden');
  }, 3200);
}
