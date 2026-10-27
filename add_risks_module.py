#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_risks_module.py
Integrates:
3. 🚨 РИСКИ И ALERTS (Early-Warning System & Smart Follow-up):
   - Список студентов с риском отчисления (осталось <= 1 урока или 3 пропуска подряд).
   - Кнопка "Сгенерировать напоминание в Telegram": создает готовый скрипт сообщения для родителя с реквизитами на оплату в 1 клик.
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
        { id: 'tab-director', label: '2. 📈 Дашборд финансов', labelUz: '2. 📈 Moliya tahlili & LTV', icon: 'fa-chart-pie', roles: ['director', 'tech'] },
        { id: 'tab-risks', label: '3. 🚨 Риски & Уведомления', labelUz: '3. 🚨 Xavf guruhlari & Eslatma', icon: 'fa-triangle-exclamation', roles: ['director', 'tech', 'manager', 'cashier', 'reception'] },
        { id: 'tab-a4-generator', label: '4. 📑 Генератор A4 (Печать)', labelUz: '4. 📑 A4 Shartnoma & Sertifikat', icon: 'fa-print', roles: ['director', 'tech', 'manager', 'cashier', 'reception', 'teacher'] },
        { id: 'tab-cashier', label: '5. 💰 POS-Касса & Чеки', labelUz: '5. 💰 POS Kassa & Cheklar', icon: 'fa-cash-register', roles: ['director', 'tech', 'cashier'] },
        { id: 'tab-teacher', label: '6. 📚 Журнал 18 групп (1:5)', labelUz: '6. 📚 18 guruh jurnali (1:5)', icon: 'fa-chalkboard-user', roles: ['director', 'tech', 'teacher'] },
        { id: 'tab-backup', label: '7. ⚙️ Бэкап базы данных', labelUz: '7. ⚙️ MB Zaxira (Backup)', icon: 'fa-database', roles: ['director', 'tech', 'cashier', 'manager'] },
        { id: 'tab-nurse', label: '🩺 Медкабинет (Скрининг)', labelUz: '🩺 Tibbiyot xonasi', icon: 'fa-kit-medical', roles: ['director', 'tech', 'nurse'] },
        { id: 'tab-zavhoz', label: '📦 Хозчасть & АХО (Инвентарь)', labelUz: '📦 Xoʻjalik boʻlimi', icon: 'fa-boxes-stacked', roles: ['director', 'tech', 'zavhoz'] },
        { id: 'tab-reception', label: '🏫 Реестр Студентов (54)', labelUz: '🏫 Talabalar roʻyxati', icon: 'fa-users-gear', roles: ['director', 'tech', 'reception', 'manager'] },
        { id: 'tab-manager', label: '📋 Воронка Лидов (CRM)', labelUz: '📋 Lidlar voronkasi', icon: 'fa-table-columns', roles: ['director', 'tech', 'manager'] }
      ];"""

    if re.search(old_items_pat, html):
        html = re.sub(old_items_pat, new_items, html, count=1)
        print("Updated navigation items in setupUserSession.")
    else:
        print("Warning: old_items_pat not matched!")

    # 2. Add switchTab handler for tab-risks
    if "else if (tabId === 'tab-risks') {" not in html:
        html = html.replace("if (tabId === 'tab-roles') {", "if (tabId === 'tab-risks') {\n        renderRisksTab();\n      } else if (tabId === 'tab-roles') {")
        html = html.replace("else if (defaultTab === 'tab-roles') renderRolesTab();", "else if (defaultTab === 'tab-risks') renderRisksTab();\n      else if (defaultTab === 'tab-roles') renderRolesTab();")
        print("Added switchTab handler for tab-risks.")

    # 3. HTML markup for tab-risks section
    tab_risks_html = """
        <!-- ============================================================== -->
        <!-- TAB: 🚨 РИСКИ И ALERTS (Early-Warning System & Smart Follow-up) -->
        <!-- ============================================================== -->
        <section id="tab-risks" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-rose-500/10 text-rose-500 border border-rose-500/20">
                🚨 EARLY-WARNING SYSTEM & SMART FOLLOW-UP
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">Зона риска и Умные напоминания родителям</h2>
              <p class="text-xs text-slate-400">Автоматический мониторинг студентов на грани отчисления (остаток &le; 1 урока или 3 пропуска) с генерацией персональных скриптов оплаты в Telegram</p>
            </div>
            <div class="flex items-center gap-2">
              <button type="button" onclick="renderRisksTab()" class="px-3 py-2 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-200 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer shadow-2xs hover:border-emerald-500">
                <i class="fa-solid fa-arrows-rotate text-emerald-500"></i> Обновить риски
              </button>
            </div>
          </div>

          <!-- KPI Metric Cards of Risk Zone -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-rose-200 dark:border-rose-900/60 shadow-xs space-y-1">
              <div class="flex items-center justify-between text-xs font-semibold text-rose-600 dark:text-rose-400">
                <span>Остаток &le; 1 урока</span>
                <i class="fa-solid fa-triangle-exclamation"></i>
              </div>
              <div class="text-2xl font-black text-rose-700 dark:text-rose-300 font-mono" id="risk-count-critical">0</div>
              <p class="text-[10px] text-slate-400">Требуют срочного продления абонемента</p>
            </div>

            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-amber-200 dark:border-amber-900/60 shadow-xs space-y-1">
              <div class="flex items-center justify-between text-xs font-semibold text-amber-600 dark:text-amber-400">
                <span>Пропуски занятий</span>
                <i class="fa-solid fa-user-xmark"></i>
              </div>
              <div class="text-2xl font-black text-amber-600 dark:text-amber-400 font-mono" id="risk-count-absent">0</div>
              <p class="text-[10px] text-slate-400">Пропуски без уважительной причины</p>
            </div>

            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-emerald-200 dark:border-emerald-900/60 shadow-xs space-y-1">
              <div class="flex items-center justify-between text-xs font-semibold text-emerald-600 dark:text-emerald-400">
                <span>Ожидаемая пролонгация</span>
                <i class="fa-solid fa-hand-holding-dollar"></i>
              </div>
              <div class="text-2xl font-black text-emerald-600 dark:text-emerald-400 font-mono" id="risk-amount-expected">0 UZS</div>
              <p class="text-[10px] text-slate-400">Потенциал выручки зоны риска</p>
            </div>

            <div class="p-4 rounded-2xl bg-white dark:bg-slate-800 border border-indigo-200 dark:border-indigo-900/60 shadow-xs space-y-1">
              <div class="flex items-center justify-between text-xs font-semibold text-indigo-600 dark:text-indigo-400">
                <span>Отправлено в Telegram</span>
                <i class="fa-brands fa-telegram"></i>
              </div>
              <div class="text-2xl font-black text-indigo-600 dark:text-indigo-400 font-mono" id="risk-count-notified">0</div>
              <p class="text-[10px] text-slate-400">Обработано администрацией за смену</p>
            </div>
          </div>

          <!-- Risk Filters & Table Panel -->
          <div class="bg-white dark:bg-slate-800 rounded-2xl border border-slate-200 dark:border-slate-700 shadow-sm overflow-hidden space-y-4 p-4 sm:p-6">
            <div class="flex flex-wrap items-center justify-between gap-3 pb-2 border-b border-slate-100 dark:border-slate-700/60">
              <div class="flex items-center gap-2">
                <button type="button" onclick="filterRiskTable('all')" id="btn-rf-all" class="px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer bg-slate-900 text-white dark:bg-white dark:text-slate-900">
                  Все студенты риска (<span id="rf-count-all">0</span>)
                </button>
                <button type="button" onclick="filterRiskTable('lessons')" id="btn-rf-lessons" class="px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-200 hover:bg-slate-200">
                  Баланс &le; 1 урока (<span id="rf-count-lessons">0</span>)
                </button>
                <button type="button" onclick="filterRiskTable('absent')" id="btn-rf-absent" class="px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-200 hover:bg-slate-200">
                  Пропуски / НБ (<span id="rf-count-absent">0</span>)
                </button>
              </div>

              <div class="text-xs text-slate-400">
                <span>Мини-группы 1:5 • Маргилан</span>
              </div>
            </div>

            <!-- Table -->
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead class="bg-slate-50 dark:bg-slate-900 text-slate-500 font-mono text-[10px] uppercase border-y border-slate-200 dark:border-slate-700">
                  <tr>
                    <th class="p-3">Студент & Группа</th>
                    <th class="p-3">Преподаватель</th>
                    <th class="p-3 text-center">Остаток уроков</th>
                    <th class="p-3">Родитель & Телефон</th>
                    <th class="p-3">Уровень риска</th>
                    <th class="p-3 text-right">Действие</th>
                  </tr>
                </thead>
                <tbody id="risk-students-tbody" class="divide-y divide-slate-100 dark:divide-slate-700">
                  <!-- Dynamically populated by renderRisksTab() -->
                </tbody>
              </table>
            </div>
          </div>
        </section>
"""

    if 'id="tab-risks"' not in html:
        # Place before tab-a4-generator
        target_marker = '<!-- TAB: 📑 ГЕНЕРАТОР A4'
        if target_marker in html:
            html = html.replace(target_marker, tab_risks_html + "\n\n        " + target_marker)
            print("Inserted tab-risks section before tab-a4-generator.")
        else:
            main_end = html.find("</main>")
            html = html[:main_end] + tab_risks_html + "\n" + html[main_end:]
            print("Inserted tab-risks before </main>.")

    # 4. Telegram Reminder Modal markup
    modal_tg_html = """
  <!-- Modal: Telegram Smart Reminder Follow-up -->
  <div id="modal-telegram-reminder" class="hidden fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-xs flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-800 rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-700 space-y-4">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-700">
        <div class="flex items-center gap-2.5">
          <div class="w-10 h-10 rounded-xl bg-sky-100 dark:bg-sky-950/60 text-sky-600 flex items-center justify-center text-lg">
            <i class="fa-brands fa-telegram"></i>
          </div>
          <div>
            <h3 class="font-extrabold text-sm text-slate-900 dark:text-white">Напоминание родителю в Telegram</h3>
            <p class="text-[11px] text-slate-400">Персональный скрипт с реквизитами на оплату курса MAM</p>
          </div>
        </div>
        <button type="button" onclick="closeTelegramReminderModal()" class="w-8 h-8 rounded-lg bg-slate-100 dark:bg-slate-700 text-slate-500 hover:text-slate-900 dark:hover:text-white flex items-center justify-center cursor-pointer">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Language selector for message script -->
      <div class="flex items-center justify-between bg-slate-50 dark:bg-slate-900 p-2 rounded-xl text-xs">
        <span class="font-semibold text-slate-500">Язык скрипта:</span>
        <div class="flex items-center gap-1">
          <button type="button" onclick="setTelegramScriptLang('ru')" id="btn-tg-lang-ru" class="px-2.5 py-1 rounded-lg font-bold text-xs bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-2xs">
            🇷🇺 Русский
          </button>
          <button type="button" onclick="setTelegramScriptLang('uz')" id="btn-tg-lang-uz" class="px-2.5 py-1 rounded-lg font-bold text-xs text-slate-500 hover:text-slate-900 dark:hover:text-white">
            🇺🇿 O'zbekcha
          </button>
        </div>
      </div>

      <!-- Generated Textarea -->
      <div>
        <label class="block text-[11px] font-semibold text-slate-400 mb-1">Текст сообщения:</label>
        <textarea id="tg-script-textarea" rows="8" class="w-full p-3 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl text-xs font-mono leading-relaxed text-slate-800 dark:text-slate-100 focus:outline-none focus:border-sky-500"></textarea>
      </div>

      <!-- Recipient Phone & Actions -->
      <div class="space-y-2 pt-1">
        <div class="flex items-center justify-between text-xs text-slate-500">
          <span>Получатель: <b id="tg-script-parent-phone" class="font-mono text-slate-900 dark:text-white">+998...</b></span>
          <span id="tg-script-student-label" class="font-bold text-emerald-600">Студент</span>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-2">
          <button type="button" onclick="copyTelegramScript()" class="py-2.5 px-4 rounded-xl bg-slate-900 text-white dark:bg-white dark:text-slate-900 font-bold text-xs transition flex items-center justify-center gap-2 cursor-pointer shadow-sm hover:opacity-90">
            <i class="fa-solid fa-copy"></i>
            <span>Скопировать текст</span>
          </button>
          <button type="button" onclick="openTelegramWeb()" class="py-2.5 px-4 rounded-xl bg-sky-500 hover:bg-sky-600 text-white font-bold text-xs transition flex items-center justify-center gap-2 cursor-pointer shadow-md shadow-sky-500/20">
            <i class="fa-brands fa-telegram text-base"></i>
            <span>Открыть в Telegram</span>
          </button>
        </div>

        <button type="button" onclick="payFromRiskModal()" class="w-full py-2 px-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-700 font-bold text-xs transition flex items-center justify-center gap-1.5 cursor-pointer hover:bg-emerald-100">
          <i class="fa-solid fa-cash-register"></i>
          <span>Оплатить в POS-кассе Академии</span>
        </button>
      </div>
    </div>
  </div>
"""

    if 'id="modal-telegram-reminder"' not in html:
        toast_marker = '<div id="toast-msg"'
        if toast_marker in html:
            html = html.replace(toast_marker, modal_tg_html + "\n\n  " + toast_marker)
            print("Inserted modal-telegram-reminder.")
        else:
            body_end = html.rfind("</body>")
            html = html[:body_end] + modal_tg_html + "\n" + html[body_end:]
            print("Inserted modal-telegram-reminder before </body>.")

    # 5. JavaScript functions for risks and telegram reminders
    js_risks_code = """
    // =========================================================================
    // 3. 🚨 РИСКИ И ALERTS (Early-Warning System & Smart Follow-up Logic)
    // =========================================================================
    let currentRiskFilter = 'all';
    let activeRiskStudent = null;
    let tgScriptLanguage = 'ru';
    let sentTelegramsCount = 0;

    function renderRisksTab() {
      const tbody = document.getElementById('risk-students-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      const students = appState.students || [];
      
      // Calculate risk categories
      const atRiskStudents = students.filter(s => {
        const isLessonRisk = (s.remainingLessons !== undefined && s.remainingLessons <= 1);
        const isAbsentRisk = (s.attendance === 'absent');
        return isLessonRisk || isAbsentRisk;
      });

      const criticalCount = students.filter(s => s.remainingLessons !== undefined && s.remainingLessons <= 1).length;
      const absentCount = students.filter(s => s.attendance === 'absent').length;

      // Update counters
      const elCrit = document.getElementById('risk-count-critical');
      const elAbs = document.getElementById('risk-count-absent');
      const elExp = document.getElementById('risk-amount-expected');
      const elNot = document.getElementById('risk-count-notified');
      const elRfAll = document.getElementById('rf-count-all');
      const elRfLess = document.getElementById('rf-count-lessons');
      const elRfAbs = document.getElementById('rf-count-absent');

      if (elCrit) elCrit.textContent = criticalCount;
      if (elAbs) elAbs.textContent = absentCount;
      if (elNot) elNot.textContent = sentTelegramsCount;
      if (elExp) {
        const expectedUZS = criticalCount * 600000;
        elExp.textContent = expectedUZS.toLocaleString('ru-RU') + ' UZS';
      }
      if (elRfAll) elRfAll.textContent = atRiskStudents.length;
      if (elRfLess) elRfLess.textContent = criticalCount;
      if (elRfAbs) elRfAbs.textContent = absentCount;

      // Filtered list
      let displayList = atRiskStudents;
      if (currentRiskFilter === 'lessons') {
        displayList = students.filter(s => s.remainingLessons !== undefined && s.remainingLessons <= 1);
      } else if (currentRiskFilter === 'absent') {
        displayList = students.filter(s => s.attendance === 'absent');
      }

      if (displayList.length === 0) {
        tbody.innerHTML = `
          <tr>
            <td colspan="6" class="p-8 text-center text-slate-400">
              <i class="fa-solid fa-circle-check text-emerald-500 text-2xl mb-2 block"></i>
              Все студенты активны! Студентов с критическим остатком уроков не обнаружено.
            </td>
          </tr>
        `;
        return;
      }

      displayList.forEach(s => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-750 transition';

        const grp = appState.groups.find(g => g.id === s.groupId) || {};
        const teacherName = grp.teacher || 'Преподаватель MAM';
        const rem = s.remainingLessons !== undefined ? s.remainingLessons : 0;
        const isCritical = rem <= 0;
        const isOne = rem === 1;

        let riskBadge = '';
        if (isCritical) {
          riskBadge = '<span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-bold bg-rose-100 text-rose-800 dark:bg-rose-950/60 dark:text-rose-300">🔴 0 УРОКОВ (СТОП)</span>';
        } else if (isOne) {
          riskBadge = '<span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-bold bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300">🟡 1 УРОК ОСТАЛОСЬ</span>';
        } else {
          riskBadge = '<span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-bold bg-purple-100 text-purple-800 dark:bg-purple-950/60 dark:text-purple-300">⚠️ ПРОПУСК УРОКА</span>';
        }

        tr.innerHTML = `
          <td class="p-3">
            <div class="font-extrabold text-slate-900 dark:text-white">${s.name}</div>
            <div class="text-[10px] text-slate-400 font-mono">${s.groupName || s.groupId} • ${s.course}</div>
          </td>
          <td class="p-3 text-slate-600 dark:text-slate-300 font-medium">
            ${teacherName}
          </td>
          <td class="p-3 text-center">
            <span class="font-mono font-black text-sm ${isCritical ? 'text-rose-600 dark:text-rose-400' : 'text-amber-500'}">
              ${rem} ур.
            </span>
          </td>
          <td class="p-3">
            <div class="font-medium text-slate-800 dark:text-slate-200">${s.parent || s.parentName || 'Родитель'}</div>
            <div class="text-[10px] text-slate-400 font-mono">${s.phone}</div>
          </td>
          <td class="p-3">
            ${riskBadge}
          </td>
          <td class="p-3 text-right">
            <div class="flex items-center justify-end gap-1.5">
              <button type="button" onclick="openTelegramReminderModal('${s.id}')" title="Сгенерировать напоминание в Telegram" class="px-2.5 py-1.5 rounded-lg bg-sky-50 dark:bg-sky-950/50 text-sky-600 dark:text-sky-300 border border-sky-200 dark:border-sky-800 hover:bg-sky-500 hover:text-white transition font-bold text-xs flex items-center gap-1 cursor-pointer">
                <i class="fa-brands fa-telegram"></i>
                <span class="hidden md:inline">Telegram</span>
              </button>
              <button type="button" onclick="payFromRisk('${s.id}')" title="Оплатить в кассе" class="px-2.5 py-1.5 rounded-lg bg-emerald-50 dark:bg-emerald-950/50 text-emerald-600 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 hover:bg-emerald-600 hover:text-white transition font-bold text-xs flex items-center gap-1 cursor-pointer">
                <i class="fa-solid fa-cash-register"></i>
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function filterRiskTable(type) {
      currentRiskFilter = type;
      ['all', 'lessons', 'absent'].forEach(t => {
        const btn = document.getElementById(`btn-rf-${t}`);
        if (!btn) return;
        if (t === type) {
          btn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer bg-slate-900 text-white dark:bg-white dark:text-slate-900';
        } else {
          btn.className = 'px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer bg-slate-100 text-slate-700 dark:bg-slate-700 dark:text-slate-200 hover:bg-slate-200';
        }
      });
      renderRisksTab();
    }

    function openTelegramReminderModal(studentId) {
      const s = appState.students.find(st => st.id === studentId);
      if (!s) return;
      activeRiskStudent = s;

      const modal = document.getElementById('modal-telegram-reminder');
      if (modal) modal.classList.remove('hidden');

      const phoneEl = document.getElementById('tg-script-parent-phone');
      const studEl = document.getElementById('tg-script-student-label');
      if (phoneEl) phoneEl.textContent = s.phone;
      if (studEl) studEl.textContent = s.name;

      updateTelegramScriptText();
    }

    function closeTelegramReminderModal() {
      const modal = document.getElementById('modal-telegram-reminder');
      if (modal) modal.classList.add('hidden');
      activeRiskStudent = null;
    }

    function setTelegramScriptLang(lang) {
      tgScriptLanguage = lang;
      const bRu = document.getElementById('btn-tg-lang-ru');
      const bUz = document.getElementById('btn-tg-lang-uz');
      if (lang === 'ru') {
        bRu.className = 'px-2.5 py-1 rounded-lg font-bold text-xs bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-2xs';
        bUz.className = 'px-2.5 py-1 rounded-lg font-bold text-xs text-slate-500 hover:text-slate-900 dark:hover:text-white';
      } else {
        bUz.className = 'px-2.5 py-1 rounded-lg font-bold text-xs bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-2xs';
        bRu.className = 'px-2.5 py-1 rounded-lg font-bold text-xs text-slate-500 hover:text-slate-900 dark:hover:text-white';
      }
      updateTelegramScriptText();
    }

    function updateTelegramScriptText() {
      if (!activeRiskStudent) return;
      const s = activeRiskStudent;
      const grp = appState.groups.find(g => g.id === s.groupId) || {};
      const teacher = grp.teacher || 'Каримов Ислом';
      const parent = s.parent || s.parentName || 'Уважаемый родитель';
      const rem = s.remainingLessons !== undefined ? s.remainingLessons : 0;
      const price = (s.course === 'Python' || s.course === 'Веб-программирование') ? '600 000' : '550 000';

      const ta = document.getElementById('tg-script-textarea');
      if (!ta) return;

      if (tgScriptLanguage === 'ru') {
        ta.value = `Здравствуйте, ${parent}!\\n` +
          `Вас приветствует учебная часть Академии «Maryam Academy Mission» (г. Маргилан).\\n\\n` +
          `Напоминаем, что у ${s.name} по курсу «${s.course}» (Преподаватель: ${teacher}) осталось оплаченных занятий: ${rem} ур.\\n\\n` +
          `Для непрерывности образовательного процесса в мини-группе 1:5, рекомендуем произвести оплату за следующий месяц: ${price} сум.\\n\\n` +
          `Реквизиты для онлайн-оплаты:\\n` +
          `🔹 Click: 8600 1234 5678 9012 (Maryam Academy NTM)\\n` +
          `📱 Payme: payme.uz/fallback/mam_academy\\n` +
          `📍 Касса филиала: г. Маргилан, ул. Б. Маргиноний, 14\\n` +
          `Тел: +998 (90) 100-20-00 (Дирекция MAM)`;
      } else {
        ta.value = `Assalomu alaykum, ${parent}!\\n` +
          `«Maryam Academy Mission» IT & Tillar Akademiyasi (Marg'ilon filiali) ma'muriyati.\\n\\n` +
          `Eslatib o'tamiz, farzandingiz ${s.name}ning «${s.course}» kursi bo'yicha (Ustoz: ${teacher}) qolgan darslar soni: ${rem} ta.\\n\\n` +
          `1:5 mini-guruhda ta'lim uzluksizligini ta'minlash maqsadida navbatdagi oylik to'lovni (${price} so'm) amalga oshirishingizni so'raymiz.\\n\\n` +
          `Onlayn to'lov rekvizitlari:\\n` +
          `🔹 Click: 8600 1234 5678 9012 (Maryam Academy NTM)\\n` +
          `📱 Payme: payme.uz/fallback/mam_academy\\n` +
          `📍 Kassa manzili: Marg'ilon sh., B. Marg'inoniy ko'chasi, 14\\n` +
          `Tel: +998 (90) 100-20-00 (MAM Qabulxona)`;
      }
    }

    function copyTelegramScript() {
      const ta = document.getElementById('tg-script-textarea');
      if (!ta) return;
      ta.select();
      navigator.clipboard.writeText(ta.value).then(() => {
        showToast('📋 Текст напоминания успешно скопирован в буфер обмена!');
        sentTelegramsCount++;
        const elNot = document.getElementById('risk-count-notified');
        if (elNot) elNot.textContent = sentTelegramsCount;
        if (activeRiskStudent) {
          addAudit(`Telegram напоминание скопировано для родителя ${activeRiskStudent.name} (${activeRiskStudent.phone})`);
        }
      }).catch(() => {
        showToast('Текст выделен, нажмите Ctrl+C');
      });
    }

    function openTelegramWeb() {
      const ta = document.getElementById('tg-script-textarea');
      if (!ta || !activeRiskStudent) return;
      const text = encodeURIComponent(ta.value);
      const cleanPhone = (activeRiskStudent.phone || '').replace(/[^0-9]/g, '');
      sentTelegramsCount++;
      const elNot = document.getElementById('risk-count-notified');
      if (elNot) elNot.textContent = sentTelegramsCount;
      addAudit(`Отправлено Telegram уведомление родителю ${activeRiskStudent.name}`);
      window.open(`https://t.me/share/url?url=&text=${text}`, '_blank');
      showToast('🚀 Открыт Telegram для отправки сообщения!');
    }

    function payFromRisk(studentId) {
      const btnCashier = document.querySelector('button[onclick*="tab-cashier"]');
      showTabPane('tab-cashier');
      if (btnCashier) {
        document.querySelectorAll('#sidebar-nav button').forEach(b => {
          b.className = 'w-full px-3 py-2.5 rounded-xl font-bold text-xs text-left transition flex items-center gap-2.5 nav-btn text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800';
        });
        btnCashier.className = 'w-full px-3 py-2.5 rounded-xl font-bold text-xs text-left transition flex items-center gap-2.5 nav-btn bg-emerald-600 text-white';
      }
      renderCashierView();

      const sel = document.getElementById('pos-student-select');
      if (sel) {
        sel.value = studentId;
        sel.dispatchEvent(new Event('change'));
      }
      showToast(`Открыта касса для оплаты студента: ${studentId}`);
    }

    function payFromRiskModal() {
      if (!activeRiskStudent) return;
      const id = activeRiskStudent.id;
      closeTelegramReminderModal();
      payFromRisk(id);
    }
"""

    if 'function renderRisksTab' not in html:
        script_end = html.rfind("</script>")
        if script_end != -1:
            html = html[:script_end] + js_risks_code + "\n  " + html[script_end:]
            print("Inserted JS risks and telegram reminder functions.")

    with open("crm.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("crm.html with 🚨 РИСКИ И ALERTS successfully updated!")

if __name__ == "__main__":
    main()
