#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upgrade_to_13_modules.py
Upgrades crm.html to include all 13 modules requested by the user:
1. 👤 ПАНЕЛЬ РОЛЕЙ И ПРАВ ДОСТУПА (11 Аккаунтов)
2. 📈 ДАШБОРД ФИНАНСОВОЙ АНАЛИТИКИ, P&L И KPI (Expenses, Cohort Retention, CAC, Audit)
3. 🎯 ВОРОНКA ПРОДАЖ И ЛИДЫ (Lead Kanban Board)
4. 💵 РАСЧЁТ ЗАРПЛАТ И КОМИССИОННЫХ УЧИТЕЛЕЙ (Teacher Payroll)
5. 🚨 РИСКИ И ALERTS (Early-Warning System & Telegram Gateway)
6. 🎓 МОДУЛЬ ЭКЗАМЕНОВ, ГРЕЙДОВ И GAMIFICATION (MAM-Coins Leaderboard)
7. 📑 ГЕНЕРАТОР A4-ДОГОВОРОВ И СЕРТИФИКАТОВ (Реестр сертификатов)
8. 💳 POS-КАССА И ДЕПОЗИТНЫЙ КОШЕЛЕК
9. 📚 ЭЛЕКТРОННЫЙ ЖУРНАЛ 18 ГРУПП (1:5)
10. ⏱️ ТАБЕЛЬ РАБОЧЕГО ВРЕМЕНИ И СМЕН (Shift & Attendance Log)
11. 📦 СКЛАД, ИНВЕНТАРИЗАЦИЯ И АРЕНДА ОБОРУДОВАНИЯ (Asset & Rental Log под залог)
12. 🏥 ЖУРНАЛ ЗДОРОВЬЯ (Nurse Log для Медсестры)
13. ⚙️ БЭКАП И НАСТРОЙКИ СИСТЕМЫ
"""

import re

def main():
    print("Reading crm.html...")
    with open("crm.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update items in setupUserSession
    old_items_pat = r"const items = \[\s*\{ id: 'tab-roles'[\s\S]*?\];"
    new_items = """const items = [
        { id: 'tab-roles', label: '1. 👤 Переключатель ролей (11)', labelUz: '1. 👤 Rollar (11 profil)', icon: 'fa-users', roles: ['director', 'tech', 'manager', 'cashier', 'teacher', 'nurse', 'zavhoz', 'reception'] },
        { id: 'tab-director', label: '2. 📈 Дашборд P&L & KPI', labelUz: '2. 📈 Moliya P&L & KPI', icon: 'fa-chart-pie', roles: ['director', 'tech'] },
        { id: 'tab-manager', label: '3. 🎯 Воронка лидов (Kanban)', labelUz: '3. 🎯 Lidlar voronkasi (Kanban)', icon: 'fa-table-columns', roles: ['director', 'tech', 'manager', 'reception'] },
        { id: 'tab-payroll', label: '4. 💵 Зарплаты учителей (Payroll)', labelUz: '4. 💵 Oʻqituvchilar oyligi', icon: 'fa-hand-holding-dollar', roles: ['director', 'tech', 'cashier'] },
        { id: 'tab-risks', label: '5. 🚨 Риски & Telegram Alerts', labelUz: '5. 🚨 Xavf guruhi & Telegram', icon: 'fa-triangle-exclamation', roles: ['director', 'tech', 'manager', 'cashier', 'reception'] },
        { id: 'tab-gamification', label: '6. 🎓 Экзамены & MAM-Coins', labelUz: '6. 🎓 Imtihonlar & MAM-Coins', icon: 'fa-trophy', roles: ['director', 'tech', 'teacher'] },
        { id: 'tab-a4-generator', label: '7. 📑 Генератор A4 & Реестр', labelUz: '7. 📑 A4 Shartnoma & Sertifikat', icon: 'fa-print', roles: ['director', 'tech', 'manager', 'cashier', 'reception', 'teacher'] },
        { id: 'tab-cashier', label: '8. 💳 POS-Касса & Депозит', labelUz: '8. 💳 POS Kassa & Depozit', icon: 'fa-cash-register', roles: ['director', 'tech', 'cashier'] },
        { id: 'tab-teacher', label: '9. 📚 Журнал 18 групп (1:5)', labelUz: '9. 📚 18 guruh jurnali (1:5)', icon: 'fa-chalkboard-user', roles: ['director', 'tech', 'teacher'] },
        { id: 'tab-shifts', label: '10. ⏱️ Табель смен (Check-in)', labelUz: '10. ⏱️ Ish vaqti tabeli', icon: 'fa-clock', roles: ['director', 'tech', 'manager', 'cashier', 'teacher', 'nurse', 'zavhoz', 'reception'] },
        { id: 'tab-zavhoz', label: '11. 📦 Склад & Аренда под залог', labelUz: '11. 📦 Ombor & Garov ijarasi', icon: 'fa-boxes-stacked', roles: ['director', 'tech', 'zavhoz'] },
        { id: 'tab-nurse', label: '12. 🏥 Журнал здоровья (Nurse)', labelUz: '12. 🏥 Hamshira jurnali', icon: 'fa-kit-medical', roles: ['director', 'tech', 'nurse'] },
        { id: 'tab-backup', label: '13. ⚙️ Бэкап & Настройки', labelUz: '13. ⚙️ Zaxira & Sozlamalar', icon: 'fa-database', roles: ['director', 'tech', 'cashier', 'manager'] }
      ];"""

    if re.search(old_items_pat, html):
        html = re.sub(old_items_pat, new_items, html, count=1)
        print("Updated navigation items in setupUserSession to 13 items.")
    else:
        print("Warning: old_items_pat not matched!")

    # 2. Update switchTab handler to cover all tabs
    switch_pat = r"function switchTab\(tabId, btn\) \{[\s\S]*?showTabPane\(tabId\);[\s\S]*?if \(tabId === 'tab-director'\) \{"
    new_switch = """function switchTab(tabId, btn) {
      document.querySelectorAll('#sidebar-nav button').forEach(b => {
        b.className = 'w-full px-3 py-2.5 rounded-xl font-bold text-xs text-left transition flex items-center gap-2.5 nav-btn text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800';
      });
      btn.className = 'w-full px-3 py-2.5 rounded-xl font-bold text-xs text-left transition flex items-center gap-2.5 nav-btn bg-emerald-600 text-white';
      showTabPane(tabId);

      if (tabId === 'tab-roles') renderRolesTab();
      else if (tabId === 'tab-director') updateDirectorKPIs();
      else if (tabId === 'tab-manager') renderKanban();
      else if (tabId === 'tab-payroll') renderPayrollTab();
      else if (tabId === 'tab-risks') renderRisksTab();
      else if (tabId === 'tab-gamification') renderGamificationTab();
      else if (tabId === 'tab-a4-generator') { initA4GeneratorTab(); renderCertRegistry(); }
      else if (tabId === 'tab-cashier') renderCashierView();
      else if (tabId === 'tab-teacher') { populateTeacherGroupSelect(); renderTeacherStudentsList(); }
      else if (tabId === 'tab-shifts') renderShiftsTab();
      else if (tabId === 'tab-zavhoz') renderZavhozView();
      else if (tabId === 'tab-nurse') renderNurseDashboard();
      else if (tabId === 'tab-backup') initBackupTab();"""

    if re.search(switch_pat, html):
        html = re.sub(switch_pat, new_switch, html, count=1)
        print("Updated switchTab logic for all 13 tabs.")
    else:
        print("Warning: switch_pat not matched directly, updating switch calls.")

    # 3. HTML Markup for tab-payroll (Teacher Payroll Module)
    tab_payroll_html = """
        <!-- ============================================================== -->
        <!-- TAB 4: 💵 РАСЧЁТ ЗАРПЛАТ И КОМИССИОННЫХ УЧИТЕЛЕЙ (TEACHER PAYROLL) -->
        <!-- ============================================================== -->
        <section id="tab-payroll" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-500 border border-emerald-500/20">
                💵 АВТОМАТИЧЕСКИЙ РАСЧЕТ ВЫПЛАТ & БОНУСОВ
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">Ведомость зарплат 6 преподавателей MAM</h2>
              <p class="text-xs text-slate-400">Формула: Базовый оклад за уроки + Бонус за удержание мини-групп (Retention > 90%) + Премия за студентов</p>
            </div>
            <div class="flex items-center gap-2">
              <button type="button" onclick="renderPayrollTab()" class="px-3 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer shadow-2xs hover:border-emerald-500">
                <i class="fa-solid fa-arrows-rotate text-emerald-500"></i> Пересчитать
              </button>
            </div>
          </div>

          <!-- Payroll KPI Summary -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Общий зарплатный фонд:</span>
              <div class="text-2xl font-black text-slate-900 dark:text-white font-mono" id="payroll-total-fund">28,500,000 UZS</div>
              <p class="text-[10px] text-emerald-500 font-semibold">6 ключевых преподавателей</p>
            </div>
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Средняя выплата учителю:</span>
              <div class="text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono" id="payroll-avg-salary">4,750,000 UZS</div>
              <p class="text-[10px] text-slate-400">За 24 проведенных занятия</p>
            </div>
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Бонусы за удержание (Retention):</span>
              <div class="text-2xl font-black text-purple-600 dark:text-purple-400 font-mono" id="payroll-bonus-fund">4,500,000 UZS</div>
              <p class="text-[10px] text-slate-400">KPI мини-групп 1:5</p>
            </div>
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Статус выплат:</span>
              <div class="text-xl font-bold text-amber-500 font-mono" id="payroll-status-label">Утверждено Директором</div>
              <p class="text-[10px] text-slate-400">Готово к выдаче через POS-кассу</p>
            </div>
          </div>

          <!-- Teachers Payroll Table -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden p-4 sm:p-6 space-y-4">
            <h3 class="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-file-invoice-dollar text-emerald-500"></i> Детализированная ведомость начислений
            </h3>
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 dark:bg-slate-900 text-slate-500 font-mono text-[10px] uppercase border-y border-slate-200 dark:border-slate-700">
                  <tr>
                    <th class="p-3">Преподаватель</th>
                    <th class="p-3">Курс & Группы</th>
                    <th class="p-3 text-center">Студентов</th>
                    <th class="p-3 text-center">Уроков</th>
                    <th class="p-3">Базовая ставка</th>
                    <th class="p-3">Бонус удержания</th>
                    <th class="p-3 font-bold text-emerald-700 dark:text-emerald-400">Итого к выплате</th>
                    <th class="p-3 text-right">Действие</th>
                  </tr>
                </thead>
                <tbody id="payroll-teachers-tbody" class="divide-y divide-slate-100 dark:divide-slate-700">
                  <!-- Rendered dynamically -->
                </tbody>
              </table>
            </div>
          </div>
        </section>
"""

    # 4. HTML Markup for tab-gamification (Exams, Grades & MAM-Coins Leaderboard)
    tab_gamification_html = """
        <!-- ============================================================== -->
        <!-- TAB 6: 🎓 МОДУЛЬ ЭКЗАМЕНОВ, ГРЕЙДОВ И GAMIFICATION (MAM-COINS) -->
        <!-- ============================================================== -->
        <section id="tab-gamification" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-amber-500/10 text-amber-500 border border-amber-500/20">
                🎓 ЭКЗАМЕНАЦИОННАЯ СИСТЕМА & GAMIFICATION
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">Экзамены, Грейды и Лидерборд MAM-Coins</h2>
              <p class="text-xs text-slate-400">Внесение баллов за тесты (Score &ge; 80% для допуска к диплому) и рейтинг топ-10 студентов за активность и проекты</p>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <!-- Left 2 Cols: Exam Grades Management -->
            <div class="lg:col-span-2 bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm p-4 sm:p-6 space-y-4">
              <div class="flex items-center justify-between">
                <h3 class="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                  <i class="fa-solid fa-graduation-cap text-indigo-500"></i> Экзаменационная ведомость групп
                </h3>
                <span class="text-xs text-slate-400">Порог сертификата: <b>80%</b></span>
              </div>

              <div class="overflow-x-auto">
                <table class="w-full text-left text-xs">
                  <thead class="bg-slate-50 dark:bg-slate-900 text-slate-500 font-mono text-[10px] uppercase border-y border-slate-200 dark:border-slate-700">
                    <tr>
                      <th class="p-3">Студент & Курс</th>
                      <th class="p-3 text-center">Midterm (40%)</th>
                      <th class="p-3 text-center">Final (60%)</th>
                      <th class="p-3 text-center">Итоговый балл</th>
                      <th class="p-3 text-center">Допуск к диплому</th>
                      <th class="p-3 text-right">MAM-Coins</th>
                    </tr>
                  </thead>
                  <tbody id="gamification-grades-tbody" class="divide-y divide-slate-100 dark:divide-slate-700">
                    <!-- Populated dynamically -->
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Right Col: MAM-Coins Leaderboard Top-10 -->
            <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm p-4 sm:p-6 space-y-4">
              <div class="flex items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-700">
                <div class="flex items-center gap-2">
                  <div class="w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center font-bold text-sm">
                    🪙
                  </div>
                  <div>
                    <h3 class="font-bold text-xs text-slate-900 dark:text-white">Лидерборд MAM-Coins</h3>
                    <p class="text-[10px] text-slate-400">Топ-10 учеников академии</p>
                  </div>
                </div>
              </div>

              <div class="space-y-2.5" id="gamification-leaderboard-list">
                <!-- Rendered dynamically -->
              </div>
            </div>
          </div>
        </section>
"""

    # 5. HTML Markup for tab-shifts (Shift & Attendance Log)
    tab_shifts_html = """
        <!-- ============================================================== -->
        <!-- TAB 10: ⏱️ ТАБЕЛЬ РАБОЧЕГО ВРЕМЕНИ И СМЕН (SHIFT & ATTENDANCE LOG) -->
        <!-- ============================================================== -->
        <section id="tab-shifts" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-blue-500/10 text-blue-500 border border-blue-500/20">
                ⏱️ ТАБЕЛЬ УЧЕТА РАБОЧЕГО ВРЕМЕНИ STAFF
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">Электронный табель смен сотрудников MAM</h2>
              <p class="text-xs text-slate-400">Отметка Check-in / Check-out, автоматический подсчет отработанных часов за смену и суммарно за месяц</p>
            </div>
            <!-- Current User Quick Check-in Button -->
            <div class="flex items-center gap-3">
              <button type="button" onclick="toggleStaffShift()" id="btn-shift-toggle" class="px-5 py-2.5 rounded-xl font-bold text-xs transition flex items-center gap-2 cursor-pointer shadow-md bg-emerald-600 hover:bg-emerald-700 text-white shadow-emerald-600/20">
                <i class="fa-solid fa-play text-xs"></i>
                <span id="btn-shift-text">Начать смену (Check-in)</span>
              </button>
            </div>
          </div>

          <!-- Active Shifts Status Overview -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Сотрудников на смене:</span>
              <div class="text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono" id="shift-active-count">7 / 11</div>
              <p class="text-[10px] text-slate-400">Филиал г. Маргилан открыт</p>
            </div>
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Ваша текущая смена:</span>
              <div class="text-xl font-bold text-slate-900 dark:text-white font-mono" id="shift-my-status">🟢 С 08:30 (Отработано 6.2 ч)</div>
              <p class="text-[10px] text-slate-400">Текущий пользователь: <b id="shift-my-name">Богданов Т.Я.</b></p>
            </div>
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-xs space-y-1">
              <span class="text-xs font-semibold text-slate-500">Суммарно часов за месяц:</span>
              <div class="text-2xl font-black text-indigo-600 dark:text-indigo-400 font-mono">152 / 168 ч</div>
              <p class="text-[10px] text-slate-400">Норма выработки выполнена на 90.4%</p>
            </div>
          </div>

          <!-- Staff Attendance Log Table -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm p-4 sm:p-6 space-y-4">
            <h3 class="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-users-viewfinder text-blue-500"></i> Журнал смен сотрудников (11 профилей)
            </h3>
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 dark:bg-slate-900 text-slate-500 font-mono text-[10px] uppercase border-y border-slate-200 dark:border-slate-700">
                  <tr>
                    <th class="p-3">Сотрудник</th>
                    <th class="p-3">Должность / Роль</th>
                    <th class="p-3 text-center">Начало смены</th>
                    <th class="p-3 text-center">Завершение</th>
                    <th class="p-3 text-center">Часов сегодня</th>
                    <th class="p-3 text-center">Часов в месяце</th>
                    <th class="p-3 text-right">Статус</th>
                  </tr>
                </thead>
                <tbody id="shifts-staff-tbody" class="divide-y divide-slate-100 dark:divide-slate-700">
                  <!-- Rendered dynamically -->
                </tbody>
              </table>
            </div>
          </div>
        </section>
"""

    # Insert tab-payroll, tab-gamification, tab-shifts into <main>
    if 'id="tab-payroll"' not in html:
        target_marker = '<!-- TAB: 🚨 РИСКИ'
        if target_marker in html:
            html = html.replace(target_marker, tab_payroll_html + "\n\n        " + target_marker)
            print("Inserted tab-payroll before tab-risks.")

    if 'id="tab-gamification"' not in html:
        target_marker = '<!-- ============================================================== -->\n        <!-- TAB: 📑 ГЕНЕРАТОР A4'
        if target_marker in html:
            html = html.replace(target_marker, tab_gamification_html + "\n\n        " + target_marker)
            print("Inserted tab-gamification before tab-a4-generator.")

    if 'id="tab-shifts"' not in html:
        target_marker = '<!-- ============================================================== -->\n        <!-- TAB: ⚙️ БЭКАП'
        if target_marker in html:
            html = html.replace(target_marker, tab_shifts_html + "\n\n        " + target_marker)
            print("Inserted tab-shifts before tab-backup.")

    # 6. Add Certificate Registry inside tab-a4-generator
    cert_registry_html = """
          <!-- Реестр выданных сертификатов со статусами -->
          <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm space-y-4">
            <div class="flex items-center justify-between pb-2 border-b border-slate-100 dark:border-slate-700">
              <h3 class="text-sm font-extrabold text-slate-900 dark:text-white flex items-center gap-2">
                <i class="fa-solid fa-stamp text-amber-500"></i> Реестр выданных сертификатов MAM (Верификация & Статусы)
              </h3>
              <span class="text-xs text-slate-400">Всего в реестре: <b id="cert-registry-count">6</b></span>
            </div>
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 dark:bg-slate-900 text-slate-500 font-mono text-[10px] uppercase border-y border-slate-200 dark:border-slate-700">
                  <tr>
                    <th class="p-3">Номер диплома</th>
                    <th class="p-3">Выпускник</th>
                    <th class="p-3">Курс обучения</th>
                    <th class="p-3 text-center">Дата выпуска</th>
                    <th class="p-3 text-center">Итоговый балл</th>
                    <th class="p-3 text-center">Статус</th>
                    <th class="p-3 text-right">Действие</th>
                  </tr>
                </thead>
                <tbody id="cert-registry-tbody" class="divide-y divide-slate-100 dark:divide-slate-700">
                  <!-- Populated dynamically -->
                </tbody>
              </table>
            </div>
          </div>
"""
    if 'id="cert-registry-tbody"' not in html:
        html = html.replace('</section>\n\n        <!-- ============================================================== -->\n        <!-- TAB: ⚙️ БЭКАП', cert_registry_html + '\n        </section>\n\n        <!-- ============================================================== -->\n        <!-- TAB: ⚙️ БЭКАП')
        print("Added Certificate Registry to tab-a4-generator.")

    # 7. JavaScript logic for the new modules
    js_code_new = """
    // =========================================================================
    // NEW MODULES: PAYROLL, GAMIFICATION (MAM-COINS), SHIFTS, CERT REGISTRY
    // =========================================================================

    // --- 1. TEACHER PAYROLL LOGIC ---
    function renderPayrollTab() {
      const tbody = document.getElementById('payroll-teachers-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const teachers = [
        { name: 'Каримов Ислом', course: 'Python Junior & AI', groups: '#101, #102, #103', students: 9, lessons: 24, base: 3600000, retentionBonus: 750000, paid: true },
        { name: 'Смирнов Алексей', course: 'Веб-разработка FullStack', groups: '#104, #105, #106', students: 9, lessons: 24, base: 3600000, retentionBonus: 750000, paid: true },
        { name: 'Абдуллаева Лола', course: 'UI/UX & Графический Дизайн', groups: '#107, #108, #109', students: 9, lessons: 24, base: 3600000, retentionBonus: 750000, paid: false },
        { name: 'Роберт Эванс', course: 'Английский язык & IELTS', groups: '#201, #202, #203', students: 9, lessons: 24, base: 3600000, retentionBonus: 750000, paid: false },
        { name: 'Шмидт Ханс', course: 'Немецкий язык Goethe', groups: '#204, #205, #206', students: 9, lessons: 24, base: 3600000, retentionBonus: 750000, paid: false },
        { name: 'Ким Мин Джи', course: 'Корейский язык TOPIK', groups: '#207, #208, #209', students: 9, lessons: 24, base: 3600000, retentionBonus: 750000, paid: false }
      ];

      let totalFund = 0;
      let totalBonus = 0;

      teachers.forEach(t => {
        const total = t.base + t.retentionBonus;
        totalFund += total;
        totalBonus += t.retentionBonus;

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-750 transition';
        tr.innerHTML = `
          <td class="p-3">
            <div class="font-extrabold text-slate-900 dark:text-white">${t.name}</div>
            <div class="text-[10px] text-slate-400 font-mono">1:5 мини-группы</div>
          </td>
          <td class="p-3">
            <div class="font-bold text-slate-800 dark:text-slate-200">${t.course}</div>
            <div class="text-[10px] text-slate-400 font-mono">${t.groups}</div>
          </td>
          <td class="p-3 text-center font-mono font-bold">${t.students} чел.</td>
          <td class="p-3 text-center font-mono font-bold">${t.lessons} ур.</td>
          <td class="p-3 font-mono">${t.base.toLocaleString('ru-RU')} UZS</td>
          <td class="p-3 font-mono text-purple-600 dark:text-purple-400">+${t.retentionBonus.toLocaleString('ru-RU')} UZS</td>
          <td class="p-3 font-mono font-extrabold text-emerald-600 dark:text-emerald-400">${total.toLocaleString('ru-RU')} UZS</td>
          <td class="p-3 text-right">
            ${t.paid ? 
              '<span class="px-2.5 py-1 rounded-full text-[10px] font-bold bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300">✅ Выплачено</span>' : 
              `<button type="button" onclick="payTeacherSalary('${t.name}', ${total})" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition cursor-pointer shadow-xs">Выплатить РКО</button>`
            }
          </td>
        `;
        tbody.appendChild(tr);
      });

      const elFund = document.getElementById('payroll-total-fund');
      const elBonus = document.getElementById('payroll-bonus-fund');
      if (elFund) elFund.textContent = totalFund.toLocaleString('ru-RU') + ' UZS';
      if (elBonus) elBonus.textContent = totalBonus.toLocaleString('ru-RU') + ' UZS';
    }

    function payTeacherSalary(name, amount) {
      if (!confirm(`Утвердить выплату зарплаты через кассу: ${name} — ${amount.toLocaleString('ru-RU')} UZS?`)) return;
      addAudit(`Расходный ордер (РКО): выплата ЗП ${name} — ${amount.toLocaleString('ru-RU')} UZS`);
      showToast(`Выплата ЗП для ${name} успешно проведена через POS-кассу!`);
      renderPayrollTab();
    }

    // --- 2. GAMIFICATION & MAM-COINS LOGIC ---
    function renderGamificationTab() {
      const tbody = document.getElementById('gamification-grades-tbody');
      const lbList = document.getElementById('gamification-leaderboard-list');
      if (!tbody || !lbList) return;

      tbody.innerHTML = '';
      lbList.innerHTML = '';

      const students = appState.students.slice(0, 8);
      students.forEach((s, idx) => {
        const midterm = 80 + (idx * 2) % 19;
        const finalScore = 85 + (idx * 3) % 15;
        const totalScore = Math.round((midterm * 0.4) + (finalScore * 0.6));
        const isQualified = totalScore >= 80;
        const coins = 300 + (totalScore * 2);

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-750 transition';
        tr.innerHTML = `
          <td class="p-3">
            <div class="font-bold text-slate-900 dark:text-white">${s.name}</div>
            <div class="text-[10px] text-slate-400 font-mono">${s.course} (${s.groupName || s.groupId})</div>
          </td>
          <td class="p-3 text-center font-mono font-bold">${midterm}%</td>
          <td class="p-3 text-center font-mono font-bold">${finalScore}%</td>
          <td class="p-3 text-center font-mono font-black ${isQualified ? 'text-emerald-600' : 'text-amber-500'}">${totalScore}%</td>
          <td class="p-3 text-center">
            ${isQualified ? 
              '<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300">🟢 Допущен к диплому</span>' : 
              '<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300">🟡 Пересдача</span>'
            }
          </td>
          <td class="p-3 text-right font-mono font-extrabold text-amber-500">
            🪙 ${coins}
          </td>
        `;
        tbody.appendChild(tr);
      });

      // Top 10 Leaderboard
      const top10 = [
        { name: 'Ахмедов Сардор', course: 'Python Junior', coins: 480, badge: '⚡ Python Ninja' },
        { name: 'Рустамова Диёра', course: 'Web FullStack', coins: 465, badge: '🌐 Code Master' },
        { name: 'Каримов Жасур', course: 'IELTS Academic', coins: 450, badge: '🇬🇧 Fluent Speaker' },
        { name: 'Исмаилов Темур', course: 'UI/UX Design', coins: 430, badge: '🎨 Figma Pro' },
        { name: 'Юлдашева Мадина', course: 'Goethe Deutsch', coins: 415, badge: '🇩🇪 B2 Zertifikat' },
        { name: 'Холматов Азиз', course: 'Korean TOPIK', coins: 405, badge: '🇰🇷 TOPIK II' },
        { name: 'Турсунова Нилуфар', course: 'Python AI', coins: 390, badge: '🤖 Data Pioneer' },
        { name: 'Алиев Сарвар', course: 'Web Frontend', coins: 375, badge: '🚀 React Star' },
        { name: 'Ботиров Отабек', course: 'IELTS 7.0', coins: 360, badge: '📚 Vocab King' },
        { name: 'Умарова Севара', course: 'UI Design', coins: 350, badge: '✨ Pixel Perfect' }
      ];

      top10.forEach((item, i) => {
        const medal = i === 0 ? '🥇' : (i === 1 ? '🥈' : (i === 2 ? '🥉' : `${i + 1}.`));
        const div = document.createElement('div');
        div.className = 'flex items-center justify-between p-2.5 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-700/60 text-xs';
        div.innerHTML = `
          <div class="flex items-center gap-2">
            <span class="font-bold text-sm ${i < 3 ? 'text-amber-500 font-extrabold' : 'text-slate-400'}">${medal}</span>
            <div>
              <div class="font-bold text-slate-900 dark:text-white">${item.name}</div>
              <div class="text-[10px] text-slate-400 font-mono">${item.course} • <span class="text-amber-500 font-semibold">${item.badge}</span></div>
            </div>
          </div>
          <div class="font-mono font-extrabold text-amber-500 whitespace-nowrap">
            🪙 ${item.coins}
          </div>
        `;
        lbList.appendChild(div);
      });
    }

    // --- 3. STAFF SHIFTS & CHECK-IN LOGIC ---
    let myShiftActive = true;

    function renderShiftsTab() {
      const tbody = document.getElementById('shifts-staff-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const staffList = [
        { name: 'Богданов Тимур Яхёевич', role: '👑 Генеральный Директор', inTime: '08:30', outTime: '—', hoursToday: '6.2', hoursMonth: '158', active: true },
        { name: 'Сергеев Дмитрий', role: '🛠 Системный Администратор', inTime: '08:45', outTime: '—', hoursToday: '5.9', hoursMonth: '162', active: true },
        { name: 'Азизова Мадина', role: '💵 Главный Кассир', inTime: '08:20', outTime: '—', hoursToday: '6.4', hoursMonth: '165', active: true },
        { name: 'Усманова Нигора', role: '🏫 Ресепшен Администратор', inTime: '08:00', outTime: '—', hoursToday: '6.7', hoursMonth: '170', active: true },
        { name: 'Каримов Ислом', role: '🐍 Преподаватель Python', inTime: '09:00', outTime: '15:00', hoursToday: '6.0', hoursMonth: '144', active: false },
        { name: 'Смирнов Алексей', role: '🌐 Преподаватель Web', inTime: '09:00', outTime: '—', hoursToday: '5.7', hoursMonth: '142', active: true },
        { name: 'Абдуллаева Лола', role: '🎨 Преподаватель Design', inTime: '09:30', outTime: '—', hoursToday: '5.2', hoursMonth: '138', active: true },
        { name: 'Роберт Эванс', role: '🇬🇧 Преподаватель IELTS', inTime: '10:00', outTime: '—', hoursToday: '4.7', hoursMonth: '140', active: true },
        { name: 'Махмудова Зухра', role: '🩺 Медсестра MAM', inTime: '08:15', outTime: '—', hoursToday: '6.5', hoursMonth: '160', active: true },
        { name: 'Юсупов Баходир', role: '📦 Завхоз АХО', inTime: '08:00', outTime: '14:00', hoursToday: '6.0', hoursMonth: '155', active: false }
      ];

      staffList.forEach(st => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-750 transition';
        tr.innerHTML = `
          <td class="p-3 font-bold text-slate-900 dark:text-white">${st.name}</td>
          <td class="p-3 text-slate-600 dark:text-slate-300 font-medium">${st.role}</td>
          <td class="p-3 text-center font-mono">${st.inTime}</td>
          <td class="p-3 text-center font-mono">${st.outTime}</td>
          <td class="p-3 text-center font-mono font-bold">${st.hoursToday} ч</td>
          <td class="p-3 text-center font-mono font-bold">${st.hoursMonth} ч</td>
          <td class="p-3 text-right">
            ${st.active ? 
              '<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300">🟢 На смене</span>' : 
              '<span class="px-2 py-0.5 rounded-full text-[9px] font-bold bg-slate-100 text-slate-600 dark:bg-slate-700 dark:text-slate-300">⚪ Завершена</span>'
            }
          </td>
        `;
        tbody.appendChild(tr);
      });

      const myStatusEl = document.getElementById('shift-my-status');
      const myNameEl = document.getElementById('shift-my-name');
      if (myNameEl && currentUser) myNameEl.textContent = currentUser.name;
      if (myStatusEl) {
        myStatusEl.textContent = myShiftActive ? '🟢 На смене с 08:30 (Отработано 6.2 ч)' : '⚪ Смена завершена';
      }
    }

    function toggleStaffShift() {
      myShiftActive = !myShiftActive;
      const btn = document.getElementById('btn-shift-toggle');
      const text = document.getElementById('btn-shift-text');

      if (myShiftActive) {
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl font-bold text-xs transition flex items-center gap-2 cursor-pointer shadow-md bg-rose-600 hover:bg-rose-700 text-white shadow-rose-600/20';
        if (text) text.textContent = 'Завершить смену (Check-out)';
        showToast('🟢 Смена успешно открыта! Время зафиксировано в табеле.');
        addAudit(`Check-in: ${currentUser ? currentUser.name : 'Сотрудник'} открыл смену`);
      } else {
        if (btn) btn.className = 'px-5 py-2.5 rounded-xl font-bold text-xs transition flex items-center gap-2 cursor-pointer shadow-md bg-emerald-600 hover:bg-emerald-700 text-white shadow-emerald-600/20';
        if (text) text.textContent = 'Начать смену (Check-in)';
        showToast('🔴 Смена успешно закрыта! Отработанные часы сохранены.');
        addAudit(`Check-out: ${currentUser ? currentUser.name : 'Сотрудник'} завершил смену`);
      }
      renderShiftsTab();
    }

    // --- 4. CERTIFICATE REGISTRY LOGIC ---
    function renderCertRegistry() {
      const tbody = document.getElementById('cert-registry-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const certs = [
        { id: 'MAM-CERT-2026-7841', student: 'Ахмедов Сардор', course: 'Python Junior & AI', date: '15.01.2026', score: '94%', status: 'issued' },
        { id: 'MAM-CERT-2026-7842', student: 'Рустамова Диёра', course: 'Веб-разработка FullStack', date: '18.01.2026', score: '91%', status: 'issued' },
        { id: 'MAM-CERT-2026-7843', student: 'Каримов Жасур', course: 'Английский язык IELTS', date: '20.01.2026', score: '88%', status: 'printing' },
        { id: 'MAM-CERT-2026-7844', student: 'Исмаилов Темур', course: 'UI/UX Дизайн', date: '22.01.2026', score: '95%', status: 'issued' },
        { id: 'MAM-CERT-2026-7845', student: 'Юлдашева Мадина', course: 'Немецкий язык Goethe', date: '25.01.2026', score: '84%', status: 'issued' },
        { id: 'MAM-CERT-2026-7846', student: 'Холматов Азиз', course: 'Корейский язык TOPIK', date: '28.01.2026', score: '82%', status: 'printing' }
      ];

      const countEl = document.getElementById('cert-registry-count');
      if (countEl) countEl.textContent = certs.length;

      certs.forEach(c => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-750 transition';
        const isIssued = c.status === 'issued';

        tr.innerHTML = `
          <td class="p-3 font-mono font-bold text-emerald-600 dark:text-emerald-400">${c.id}</td>
          <td class="p-3 font-bold text-slate-900 dark:text-white">${c.student}</td>
          <td class="p-3 font-medium text-slate-700 dark:text-slate-300">${c.course}</td>
          <td class="p-3 text-center font-mono">${c.date}</td>
          <td class="p-3 text-center font-mono font-bold text-emerald-600">${c.score}</td>
          <td class="p-3 text-center">
            ${isIssued ? 
              '<span class="px-2.5 py-0.5 rounded-full text-[9px] font-bold bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300">Выдан</span>' : 
              '<span class="px-2.5 py-0.5 rounded-full text-[9px] font-bold bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300">На печати</span>'
            }
          </td>
          <td class="p-3 text-right">
            <button type="button" onclick="printTabA4Document()" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-700 dark:hover:bg-slate-600 text-slate-800 dark:text-slate-200 font-bold text-[11px] transition">
              <i class="fa-solid fa-print"></i> Печать
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }
"""

    if 'function renderPayrollTab' not in html:
        script_end = html.rfind("</script>")
        if script_end != -1:
            html = html[:script_end] + js_code_new + "\n  " + html[script_end:]
            print("Inserted new JS functions for Payroll, Gamification, Shifts, and Cert Registry.")

    with open("crm.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("crm.html successfully upgraded to all 13 modules!")

if __name__ == "__main__":
    main()
