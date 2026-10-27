import re

with open('crm.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update markTeacherAttendance to fire async /api/attendance
old_att = "saveDB(db);"
# Let's inspect markTeacherAttendance exactly
start = html.find("function markTeacherAttendance")
end = html.find("function addTeacherGrade")
att_block = html[start:end]

if "fetch('/api/attendance'" not in att_block:
    new_att_block = att_block.replace("saveDB(db);", """saveDB(db);
      // Asynchronously sync attendance with Node.js Express server
      const token = localStorage.getItem('mam_token');
      fetch('/api/attendance', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : '',
          'x-mam-user': currentUser ? currentUser.key : ''
        },
        body: JSON.stringify({ studentId, status: type })
      }).catch(() => {});""")
    html = html[:start] + new_att_block + html[end:]
    print("Upgraded markTeacherAttendance with /api/attendance sync")

# 2. Update handlePosPaymentSubmit to sync with /api/payments
start_pos = html.find("function handlePosPaymentSubmit")
end_pos = html.find("function handleReceptionNewStudentSubmit")
if start_pos != -1 and end_pos != -1:
    pos_block = html[start_pos:end_pos]
    if "fetch('/api/payments'" not in pos_block:
        new_pos_block = pos_block.replace("saveDB(db);", """saveDB(db);
      // Asynchronously sync payment with Node.js Express server
      const token = localStorage.getItem('mam_token');
      fetch('/api/payments', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : '',
          'x-mam-user': currentUser ? currentUser.key : ''
        },
        body: JSON.stringify({ studentId, amount, method, lessonsToAdd, comment })
      }).catch(() => {});""")
        html = html[:start_pos] + new_pos_block + html[end_pos:]
        print("Upgraded handlePosPaymentSubmit with /api/payments sync")

# 3. Update handleReceptionNewStudentSubmit to sync with /api/students
start_rec = html.find("function handleReceptionNewStudentSubmit")
end_rec = html.find("function handleStudentGroupTransfer")
if start_rec != -1 and end_rec != -1:
    rec_block = html[start_rec:end_rec]
    if "fetch('/api/students'" not in rec_block:
        new_rec_block = rec_block.replace("saveDB(db);", """saveDB(db);
      // Asynchronously sync new student with Node.js Express server
      const token = localStorage.getItem('mam_token');
      fetch('/api/students', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : '',
          'x-mam-user': currentUser ? currentUser.key : ''
        },
        body: JSON.stringify({ name, parentName, phone, parentPhone, parentPassport, groupId, lessonsBalance: balance })
      }).catch(() => {});""")
        html = html[:start_rec] + new_rec_block + html[end_rec:]
        print("Upgraded handleReceptionNewStudentSubmit with /api/students sync")

# 4. Update handleNewExpenseSubmit to sync with /api/expenses
start_exp = html.find("function handleNewExpenseSubmit")
end_exp = html.find("function printContractFromModal")
if start_exp != -1:
    exp_snippet = html[start_exp:start_exp+1000]
    if "fetch('/api/expenses'" not in exp_snippet:
        sub_end = html.find("renderDirectorExpensesTable();", start_exp)
        if sub_end != -1:
            html = html[:sub_end] + """// Asynchronously sync expense with Node.js Express server
      const token = localStorage.getItem('mam_token');
      fetch('/api/expenses', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': token ? `Bearer ${token}` : '',
          'x-mam-user': currentUser ? currentUser.key : ''
        },
        body: JSON.stringify({ title, category, amount, comment })
      }).catch(() => {});\n      """ + html[sub_end:]
            print("Upgraded handleNewExpenseSubmit with /api/expenses sync")

with open('crm.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Synchronized changes across crm.html and index.html!")
