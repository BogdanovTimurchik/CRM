#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_crm_final.py
Injects the 3 dedicated tabs and logic into crm.html:
- tab-roles
- tab-a4-generator
- tab-backup
And updates setupUserSession() and switchTab() to support them seamlessly.
"""

import re

def main():
    print("Reading crm.html...")
    with open("crm.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update items in setupUserSession
    old_items_pat = r"const items = \[\s*\{ id: 'tab-director'[\s\S]*?\];"
    new_items = """const items = [
        { id: 'tab-roles', label: '1. 👤 Переключатель ролей (11)', labelUz: '1. 👤 Rollar (11 profil)', icon: 'fa-users', roles: ['director', 'tech', 'manager', 'cashier', 'teacher', 'nurse', 'zavhoz', 'reception'] },
        { id: 'tab-director', label: '2. 📈 Дашборд финансов', labelUz: '2. 📈 Moliya tahlili & LTV', icon: 'fa-chart-pie', roles: ['director', 'tech'] },
        { id: 'tab-a4-generator', label: '3. 📑 Генератор A4 (Печать)', labelUz: '3. 📑 A4 Shartnoma & Sertifikat', icon: 'fa-print', roles: ['director', 'tech', 'manager', 'cashier', 'reception', 'teacher'] },
        { id: 'tab-cashier', label: '4. 💳 POS-Касса & Чеки', labelUz: '4. 💳 POS Kassa & Cheklar', icon: 'fa-cash-register', roles: ['director', 'tech', 'cashier'] },
        { id: 'tab-teacher', label: '5. 👨‍🏫 Журнал 18 групп (1:5)', labelUz: '5. 👨‍🏫 18 guruh jurnali (1:5)', icon: 'fa-chalkboard-user', roles: ['director', 'tech', 'teacher'] },
        { id: 'tab-backup', label: '6. ⚙️ Бэкап базы данных', labelUz: '6. ⚙️ MB Zaxira (Backup)', icon: 'fa-database', roles: ['director', 'tech', 'cashier', 'manager'] },
        { id: 'tab-nurse', label: '🩺 Медкабинет (Скрининг)', labelUz: '🩺 Tibbiyot xonasi', icon: 'fa-kit-medical', roles: ['director', 'tech', 'nurse'] },
        { id: 'tab-zavhoz', label: '📦 Хозчасть & АХО (Инвентарь)', labelUz: '📦 Xoʻjalik boʻlimi', icon: 'fa-boxes-stacked', roles: ['director', 'tech', 'zavhoz'] },
        { id: 'tab-manager', label: '📋 Воронка Лидов (CRM)', labelUz: '📋 Lidlar voronkasi', icon: 'fa-table-columns', roles: ['director', 'tech', 'manager'] },
        { id: 'tab-reception', label: '🏫 Реестр Студентов (54)', labelUz: '🏫 Talabalar roʻyxati', icon: 'fa-users-gear', roles: ['director', 'tech', 'reception', 'manager'] }
      ];"""

    if re.search(old_items_pat, html):
        html = re.sub(old_items_pat, new_items, html, count=1)
        print("Updated navigation items in setupUserSession successfully.")
    else:
        print("Warning: old_items_pat not matched, searching alternate...")

    # 2. Insert tab panes for tab-roles, tab-a4-generator, tab-backup
    # We will insert them right before </main>
    tab_panes_html = """
        <!-- ============================================================== -->
        <!-- TAB: 👤 ПЕРЕКЛЮЧАТЕЛЬ РОЛЕЙ (11 ПРОФИЛЕЙ) -->
        <!-- ============================================================== -->
        <section id="tab-roles" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-indigo-500/10 text-indigo-500 border border-indigo-500/20">
                👤 ПАНЕЛЬ УПРАВЛЕНИЯ ДОСТУПОМ & РОЛЯМИ
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">11 Учетных записей сотрудников Академии MAM</h2>
              <p class="text-xs text-slate-400">Мгновенное переключение между аккаунтами в 1 клик для проверки прав доступа, изолированных кабинетов и интерфейсов</p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-xs text-slate-500">Текущая сессия:</span>
              <span class="px-3 py-1 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-300 font-bold text-xs border border-emerald-300 dark:border-emerald-700" id="roles-tab-current-badge">
                Богданов Т.Я. (Директор)
              </span>
            </div>
          </div>

          <div id="roles-cards-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <!-- Rendered by renderRolesTab() -->
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB: 📑 ГЕНЕРАТОР A4 (Договоры и Сертификаты с печатью) -->
        <!-- ============================================================== -->
        <section id="tab-a4-generator" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-500 border border-emerald-500/20">
                📑 ОФИЦИАЛЬНЫЙ ГЕНЕРАТОР ДОКУМЕНТОВ A4
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">Печать Договоров (UZ/RU) и Сертификатов с QR-кодом</h2>
              <p class="text-xs text-slate-400">Автоматическая подстановка данных студента, реквизитов Академии MAM в Маргилане, подписи Директора Богданова Т.Я. и печати</p>
            </div>
            <div class="flex items-center gap-3">
              <button type="button" onclick="printTabA4Document()" class="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl font-bold text-xs transition flex items-center gap-2 shadow-lg shadow-emerald-600/25 cursor-pointer">
                <i class="fa-solid fa-print text-sm"></i>
                <span>Распечатать на принтере (A4)</span>
              </button>
            </div>
          </div>

          <!-- Document Controls & Configuration -->
          <div class="p-5 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm space-y-4">
            <div class="flex flex-wrap items-center justify-between gap-4">
              <!-- Doc Type Toggle -->
              <div class="flex items-center bg-slate-100 dark:bg-slate-900 p-1 rounded-xl border border-slate-200 dark:border-slate-700">
                <button type="button" onclick="setTabDocType('contract')" id="tab-btn-doc-contract" class="px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs">
                  <i class="fa-solid fa-file-contract text-emerald-500 mr-1.5"></i> Договор обучения (UZ/RU)
                </button>
                <button type="button" onclick="setTabDocType('certificate')" id="tab-btn-doc-cert" class="px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer text-slate-500 hover:text-slate-900 dark:hover:text-white">
                  <i class="fa-solid fa-award text-amber-500 mr-1.5"></i> Сертификат выпускника (A4)
                </button>
              </div>

              <!-- Student Quick Selector -->
              <div class="flex items-center gap-2 flex-1 min-w-[280px]">
                <label class="text-xs font-semibold text-slate-500 whitespace-nowrap">Ученик:</label>
                <select id="tab-a4-student-select" onchange="onTabA4StudentChange()" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl text-xs font-bold text-slate-800 dark:text-slate-100">
                  <!-- Populated from appState.students -->
                </select>
              </div>
            </div>

            <!-- Parameters Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 pt-2 text-xs">
              <div>
                <label class="block text-[11px] text-slate-400 font-semibold mb-1">ФИО Ученика:</label>
                <input type="text" id="tab-a4-student-name" oninput="updateTabA4Preview()" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl font-bold" />
              </div>
              <div>
                <label class="block text-[11px] text-slate-400 font-semibold mb-1">Курс обучения:</label>
                <input type="text" id="tab-a4-course-name" oninput="updateTabA4Preview()" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl font-bold" />
              </div>
              <div>
                <label class="block text-[11px] text-slate-400 font-semibold mb-1">Стоимость курса (сум):</label>
                <input type="text" id="tab-a4-price" oninput="updateTabA4Preview()" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl font-bold" />
              </div>
              <div>
                <label class="block text-[11px] text-slate-400 font-semibold mb-1">ФИО Родителя:</label>
                <input type="text" id="tab-a4-parent-name" oninput="updateTabA4Preview()" class="w-full p-2 bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded-xl font-bold" />
              </div>
            </div>
          </div>

          <!-- Document Live Paper Canvas -->
          <div class="flex justify-center p-4 md:p-8 bg-slate-200/70 dark:bg-slate-950/70 rounded-3xl border border-slate-300 dark:border-slate-800 overflow-x-auto">
            <!-- Contract Paper Container -->
            <div id="tab-a4-contract-view" class="w-full max-w-[210mm] bg-white text-slate-900 p-8 sm:p-12 rounded-lg shadow-2xl space-y-6 text-xs leading-relaxed print-a4-target font-sans">
              <!-- Contract Header -->
              <div class="flex items-center justify-between border-b-2 border-emerald-600 pb-4">
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 bg-emerald-600 rounded-xl flex items-center justify-center text-white font-extrabold text-xl shadow-md">
                    MAM
                  </div>
                  <div>
                    <h1 class="text-base font-extrabold text-slate-900 tracking-tight">MARYAM ACADEMY MISSION</h1>
                    <p class="text-[10px] text-slate-500 font-medium">IT & Xorijiy Tillar Akademiyasi • Marg'ilon filiali</p>
                  </div>
                </div>
                <div class="text-right text-[10px] text-slate-500 font-mono">
                  <p>Hujjat: <b>SHARTNOMA #MAM-2026/04</b></p>
                  <p>Sana: <b id="tab-contract-date">15.01.2026</b></p>
                  <p>Marg'ilon sh., Farg'ona viloyati</p>
                </div>
              </div>

              <!-- Title -->
              <div class="text-center space-y-1">
                <h2 class="text-sm font-black uppercase tracking-wider text-slate-900">TA'LIM XIZMATLARINI KO'RSATISH SHARTNOMASI</h2>
                <p class="text-[11px] text-slate-600 font-medium">ДОГОВОР НА ОКАЗАНИЕ ОБРАЗОВАТЕЛЬНЫХ УСЛУГ</p>
              </div>

              <!-- Parallel Columns Contract Body -->
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2 text-[11px] text-justify leading-relaxed border-t border-slate-200">
                <div class="space-y-3">
                  <p class="font-bold text-emerald-800">1. SHARTNOMA PREDMETI (O'ZBEKCHA):</p>
                  <p>«Maryam Academy Mission» o'quv markazi (Ijrochi) nomidan Direktor <b>Bogdanov Timur Yaxyoyevich</b> bir tomondan, va fuqaro <b id="tab-contract-parent-uz">Axmedov Jasur</b> (Buyurtmachi) ikkinchi tomondan, tinglovchi <b id="tab-contract-student-uz" class="text-emerald-700">Axmedov Sardor</b>ni tanlangan «<b id="tab-contract-course-uz">Python</b>» kursi bo'yicha professional 1:5 mini-guruhda o'qitish to'g'risida ushbu shartnomani tuzdilar.</p>
                  <p><b>2. TO'LOV VA TARTIB:</b> Kurs narxi oyiga <b id="tab-contract-price-uz">600 000</b> so'mni tashkil etadi. Darslar haftasiga 3 marta zamonaviy jihozlangan xonalarda o'tkaziladi.</p>
                  <p><b>3. TOMONLARNING JAVOBGARLIGI:</b> Ijrochi tinglovchini sifatli metodika va malakali ustozlar bilan ta'minlashni o'z zimmasiga oladi.</p>
                </div>
                <div class="space-y-3 border-l md:border-slate-200 md:pl-6">
                  <p class="font-bold text-slate-800">1. ПРЕДМЕТ ДОГОВОРА (НА РУССКОМ):</p>
                  <p>Учебный центр «Maryam Academy Mission» (Исполнитель) в лице Генерального Директора <b>Богданова Тимура Яхёевича</b> с одной стороны, и <b id="tab-contract-parent-ru">Ахмедов Жасур</b> (Заказчик), заключили настоящий договор об обучении слушателя <b id="tab-contract-student-ru" class="text-emerald-700">Ахмедов Сардор</b> по программе «<b id="tab-contract-course-ru">Python</b>» в мини-группе 1:5.</p>
                  <p><b>2. ОПЛАТА И ПОРЯДОК:</b> Стоимость обучения составляет <b id="tab-contract-price-ru">600 000</b> сум/мес. Занятия проводятся 3 раза в неделю в кондиционированных классах.</p>
                  <p><b>3. ОБЯЗАТЕЛЬСТВА:</b> Академия обеспечивает практическое обучение, доступ к ПК и сертификат по окончании.</p>
                </div>
              </div>

              <!-- Signatures & Stamp Block -->
              <div class="grid grid-cols-2 gap-8 pt-8 border-t border-slate-200">
                <div class="text-[11px] space-y-1">
                  <p class="font-bold text-slate-900">IJROCHI / ИСПОЛНИТЕЛЬ:</p>
                  <p>«Maryam Academy Mission» NTM</p>
                  <p>Marg'ilon sh., B.Marg'inoniy ko'chasi 14</p>
                  <p>Tel: +998 (90) 100-20-00</p>
                  <div class="pt-4 flex items-center gap-3">
                    <div>
                      <p class="font-mono text-[9px] text-slate-400">Direktor imzosi:</p>
                      <p class="font-bold text-xs underline decoration-emerald-500">Богданов Т.Я. ________</p>
                    </div>
                    <!-- Stamp Badge -->
                    <div class="w-16 h-16 rounded-full border-2 border-emerald-600/40 text-emerald-700 flex flex-col items-center justify-center text-[7px] font-bold text-center rotate-[-12deg] p-1">
                      <span>MARYAM ACADEMY</span>
                      <span>* MUHR *</span>
                      <span>MARG'ILON</span>
                    </div>
                  </div>
                </div>
                <div class="text-[11px] space-y-1">
                  <p class="font-bold text-slate-900">BUYURTMACHI / ЗАКАЗЧИК:</p>
                  <p id="tab-contract-parent-sign">Axmedov Jasur (Ota-onasi)</p>
                  <p>Pasport: AA 1234567 • Marg'ilon sh.</p>
                  <p>Tel: +998 (90) 123-45-67</p>
                  <div class="pt-4">
                    <p class="font-mono text-[9px] text-slate-400">Ota-ona imzosi:</p>
                    <p class="font-bold text-xs">_____________________</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Certificate Paper Container -->
            <div id="tab-a4-cert-view" class="hidden w-full max-w-[297mm] bg-white text-slate-900 p-8 sm:p-12 rounded-lg shadow-2xl border-8 border-double border-emerald-700 print-a4-target relative font-serif">
              <!-- Outer decorative border -->
              <div class="border-2 border-emerald-600/40 p-6 md:p-10 rounded text-center space-y-6 relative overflow-hidden bg-gradient-to-b from-emerald-50/20 to-white">
                
                <!-- Certificate Header -->
                <div class="flex items-center justify-between">
                  <div class="text-left font-sans">
                    <span class="text-[10px] font-mono font-bold tracking-widest text-emerald-700 uppercase">MARYAM ACADEMY MISSION</span>
                    <p class="text-[9px] text-slate-400">Marg'ilon IT & Xorijiy Tillar Akademiyasi</p>
                  </div>
                  <!-- Logo Emblem -->
                  <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-emerald-700 to-teal-500 text-white flex items-center justify-center font-black text-2xl shadow-lg shadow-emerald-700/20">
                    MAM
                  </div>
                  <div class="text-right font-mono text-[9px] text-slate-500">
                    <p>Seriya: <b id="tab-cert-serial" class="text-emerald-700">MAM-CERT-2026-7841</b></p>
                    <p>Sana: <b>15.01.2026</b></p>
                  </div>
                </div>

                <!-- Main Certificate Headings -->
                <div class="space-y-2 pt-4">
                  <h1 class="text-3xl sm:text-4xl font-black tracking-widest text-emerald-900 uppercase">SERTIFIKAT</h1>
                  <p class="text-xs font-sans uppercase tracking-widest text-emerald-600 font-bold">СЕРТИФИКАТ ОБ ОКОНЧАНИИ КУРСА</p>
                </div>

                <p class="text-xs italic text-slate-500 font-sans">Ushbu hujjat tasdiqlaydiki, tinglovchi / Настоящий сертификат подтверждает, что</p>

                <!-- Student Name -->
                <div class="py-2 border-b-2 border-emerald-600 inline-block px-12">
                  <h2 id="tab-cert-student-name" class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-wide font-sans">
                    Axmedov Sardor
                  </h2>
                </div>

                <!-- Course details -->
                <p class="text-xs sm:text-sm text-slate-700 max-w-xl mx-auto leading-relaxed font-sans">
                  Maryam Academy Mission akademiyasida «<b id="tab-cert-course-name" class="text-emerald-800 text-base">Python Junior & AI</b>» kursi bo'yicha 1:5 mini-guruh formatidagi to'liq amaliy o'quv dasturini muvaffaqiyatli tamomladi.
                </p>

                <!-- Honors Badge -->
                <div class="py-1">
                  <span class="px-4 py-1.5 rounded-full text-xs font-bold font-sans bg-amber-100 text-amber-900 border border-amber-300">
                    ⭐️ DIPLOM SINOVIDAN A'LO NATIJA BILAN O'TDI (94% SCORE)
                  </span>
                </div>

                <!-- Footer: Signatures, Stamp & QR -->
                <div class="grid grid-cols-3 items-end pt-8 font-sans text-xs">
                  <!-- QR verification -->
                  <div class="text-left flex items-center gap-3">
                    <div class="w-16 h-16 bg-white border-2 border-slate-900 p-1 rounded shadow-xs flex items-center justify-center">
                      <svg viewBox="0 0 100 100" class="w-full h-full text-slate-900 fill-current">
                        <rect x="10" y="10" width="30" height="30" />
                        <rect x="60" y="10" width="30" height="30" />
                        <rect x="10" y="60" width="30" height="30" />
                        <rect x="50" y="50" width="15" height="15" />
                        <rect x="75" y="60" width="15" height="25" />
                        <rect x="60" y="80" width="10" height="10" />
                      </svg>
                    </div>
                    <div class="text-[9px] text-slate-500 font-mono">
                      <p class="font-bold text-slate-900">QR-kod orqali tekshirish</p>
                      <p>mam-academy.uz/verify</p>
                      <p id="tab-cert-qr-id">ID: MAM-7841</p>
                    </div>
                  </div>

                  <!-- Stamp in Center -->
                  <div class="flex justify-center">
                    <div class="w-20 h-20 rounded-full border-2 border-emerald-700 text-emerald-800 flex flex-col items-center justify-center text-[8px] font-bold text-center rotate-[-8deg] p-1 shadow-xs">
                      <span>MARYAM ACADEMY</span>
                      <span>* MARG'ILON *</span>
                      <span class="text-[7px]">NTM MUHRI</span>
                    </div>
                  </div>

                  <!-- Director signature -->
                  <div class="text-right">
                    <p class="text-[10px] text-slate-400 font-mono">Bosh Direktor / Директор:</p>
                    <p class="font-bold text-sm text-slate-900 underline decoration-emerald-600">Богданов Тимур Яхёевич</p>
                    <p class="text-[9px] text-slate-500">MAM Akademiyasi rahbari</p>
                  </div>
                </div>

              </div>
            </div>
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB: ⚙️ БЭКАП И УПРАВЛЕНИЕ БАЗОЙ ДАННЫХ -->
        <!-- ============================================================== -->
        <section id="tab-backup" class="tab-pane hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-200 dark:border-slate-700">
            <div>
              <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-purple-500/10 text-purple-400 border border-purple-500/20">
                ⚙️ СУБД & УПРАВЛЕНИЕ БАЗОЙ ДАННЫХ
              </span>
              <h2 class="text-xl font-extrabold text-slate-900 dark:text-white mt-1">Резервное копирование и Восстановление данных</h2>
              <p class="text-xs text-slate-400">Экспорт базы в JSON, импорт резервной копии и сброс к заводским демо-данным Маргиланского филиала</p>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Card 1: Backup JSON -->
            <div class="p-6 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col justify-between space-y-4">
              <div class="space-y-2">
                <div class="w-12 h-12 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-600 flex items-center justify-center text-xl">
                  <i class="fa-solid fa-file-arrow-down"></i>
                </div>
                <h3 class="text-base font-bold text-slate-900 dark:text-white">Скачать JSON (Backup)</h3>
                <p class="text-xs text-slate-500">Выгрузить полный снимок базы данных: 18 академических групп, 54 студента, историю транзакций кассы, медосмотры и инвентарь.</p>
              </div>
              <button type="button" onclick="backupDatabaseJSON()" class="w-full py-3 px-4 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition flex items-center justify-center gap-2 cursor-pointer shadow-md shadow-emerald-600/20">
                <i class="fa-solid fa-download"></i>
                <span>Скачать резервную копию JSON</span>
              </button>
            </div>

            <!-- Card 2: Restore JSON -->
            <div class="p-6 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col justify-between space-y-4">
              <div class="space-y-2">
                <div class="w-12 h-12 rounded-xl bg-indigo-100 dark:bg-indigo-950/60 text-indigo-600 flex items-center justify-center text-xl">
                  <i class="fa-solid fa-file-arrow-up"></i>
                </div>
                <h3 class="text-base font-bold text-slate-900 dark:text-white">Восстановить JSON (Restore)</h3>
                <p class="text-xs text-slate-500">Загрузите ранее сохраненный файл .json для мгновенного восстановления всех структур данных и истории оплат.</p>
              </div>
              <label class="w-full py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-bold text-xs transition flex items-center justify-center gap-2 cursor-pointer shadow-md shadow-indigo-600/20">
                <i class="fa-solid fa-upload"></i>
                <span>Выбрать файл JSON для восстановления</span>
                <input type="file" accept=".json" onchange="restoreDatabaseFromTabInput(event)" class="hidden" />
              </label>
            </div>

            <!-- Card 3: Factory Reset -->
            <div class="p-6 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm flex flex-col justify-between space-y-4">
              <div class="space-y-2">
                <div class="w-12 h-12 rounded-xl bg-rose-100 dark:bg-rose-950/60 text-rose-600 flex items-center justify-center text-xl">
                  <i class="fa-solid fa-arrows-rotate"></i>
                </div>
                <h3 class="text-base font-bold text-slate-900 dark:text-white">Сброс к демо-данным</h3>
                <p class="text-xs text-slate-500">Возврат к эталонным 18 группам и 54 студентам филиала г. Маргилан. Удалит добавленные вручную записи.</p>
              </div>
              <button type="button" onclick="resetDatabaseToDefaults()" class="w-full py-3 px-4 rounded-xl bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/60 text-rose-700 dark:text-rose-300 border border-rose-300 dark:border-rose-800 font-bold text-xs transition flex items-center justify-center gap-2 cursor-pointer">
                <i class="fa-solid fa-triangle-exclamation"></i>
                <span>Сбросить к заводским демо-данным</span>
              </button>
            </div>
          </div>

          <!-- DB Stats info card -->
          <div class="p-6 rounded-2xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 shadow-sm space-y-4">
            <h3 class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
              <i class="fa-solid fa-hard-drive text-slate-400"></i>
              <span>Состояние базы данных в LocalStorage</span>
            </h3>
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 text-center">
              <div class="p-3 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-700">
                <div class="text-[10px] text-slate-400 font-mono">ГРУППЫ (1:5)</div>
                <div class="text-lg font-bold text-slate-900 dark:text-white" id="stat-groups-count">18</div>
              </div>
              <div class="p-3 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-700">
                <div class="text-[10px] text-slate-400 font-mono">УЧЕНИКИ В БАЗЕ</div>
                <div class="text-lg font-bold text-slate-900 dark:text-white" id="stat-students-count">54</div>
              </div>
              <div class="p-3 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-700">
                <div class="text-[10px] text-slate-400 font-mono">ТРАНЗАКЦИИ КАССЫ</div>
                <div class="text-lg font-bold text-slate-900 dark:text-white" id="stat-tx-count">18</div>
              </div>
              <div class="p-3 bg-slate-50 dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-700">
                <div class="text-[10px] text-slate-400 font-mono">РАЗМЕР ХРАНИЛИЩА</div>
                <div class="text-lg font-bold text-emerald-500 font-mono" id="stat-storage-size">~180 KB</div>
              </div>
            </div>
          </div>
        </section>
"""

    # Check if not already inserted
    if 'id="tab-roles"' not in html:
        # Find </main>
        main_end = html.find("</main>")
        if main_end != -1:
            html = html[:main_end] + tab_panes_html + "\n      " + html[main_end:]
            print("Inserted tab-roles, tab-a4-generator, and tab-backup into <main>.")
        else:
            print("Error: </main> not found!")
    else:
        print("tab-roles already in html.")

    # 3. Add JS helper functions for the new tabs:
    # renderRolesTab(), setTabDocType(), onTabA4StudentChange(), updateTabA4Preview(), printTabA4Document(), restoreDatabaseFromTabInput(), resetDatabaseToDefaults()
    js_helpers = """
    // =========================================================================
    // HELPER FUNCTIONS FOR DEDICATED TABS (ROLES, A4 GENERATOR, BACKUP)
    // =========================================================================

    function renderRolesTab() {
      const container = document.getElementById('roles-cards-grid');
      if (!container) return;
      container.innerHTML = '';

      const badge = document.getElementById('roles-tab-current-badge');
      if (badge && currentUser) {
        badge.textContent = `${currentUser.name} (${currentUser.title})`;
      }

      const roleBadges = {
        'director': { label: '👑 РУКОВОДСТВО', color: 'bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300' },
        'tech': { label: '🛠 СИСТЕМА & IT', color: 'bg-blue-100 text-blue-800 dark:bg-blue-950/60 dark:text-blue-300' },
        'cashier': { label: '💵 ФИНАНСЫ & КАССА', color: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300' },
        'teacher': { label: '👨‍🏫 ПРЕПОДАВАТЕЛЬ (1:5)', color: 'bg-purple-100 text-purple-800 dark:bg-purple-950/60 dark:text-purple-300' },
        'nurse': { label: '🩺 МЕДИЦИНА', color: 'bg-rose-100 text-rose-800 dark:bg-rose-950/60 dark:text-rose-300' },
        'zavhoz': { label: '📦 ХОЗЧАСТЬ & АХО', color: 'bg-orange-100 text-orange-800 dark:bg-orange-950/60 dark:text-orange-300' },
        'manager': { label: '📋 ПРОДАЖИ & ДОГОВОРЫ', color: 'bg-teal-100 text-teal-800 dark:bg-teal-950/60 dark:text-teal-300' },
        'reception': { label: '🏫 АДМИНИСТРАЦИЯ', color: 'bg-sky-100 text-sky-800 dark:bg-sky-950/60 dark:text-sky-300' }
      };

      // 11 distinct authorized accounts
      const accountKeys = [
        'director', 'tech', 'cashier', 
        'py_teacher', 'web_teacher', 'design_teacher', 
        'eng_teacher', 'ger_teacher', 'kor_teacher', 
        'nurse', 'zavhoz'
      ];

      accountKeys.forEach(key => {
        const acc = ACCOUNTS[key];
        if (!acc) return;
        const isCurrent = currentUser && currentUser.name === acc.name;
        const b = roleBadges[acc.role] || { label: 'СОТРУДНИК', color: 'bg-slate-100 text-slate-800' };

        const card = document.createElement('div');
        card.className = `p-4 sm:p-5 rounded-2xl bg-white dark:bg-slate-800 border transition-all ${isCurrent ? 'border-emerald-500 shadow-md ring-2 ring-emerald-500/20' : 'border-slate-200 dark:border-slate-700 hover:border-slate-300 dark:hover:border-slate-600 shadow-xs'} flex flex-col justify-between space-y-4`;
        
        card.innerHTML = `
          <div class="space-y-2.5">
            <div class="flex items-center justify-between gap-2">
              <span class="px-2 py-0.5 rounded-full text-[9px] font-mono font-bold ${b.color}">
                ${b.label}
              </span>
              ${isCurrent ? '<span class="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 flex items-center gap-1 font-mono">● АКТИВЕН</span>' : ''}
            </div>
            <div>
              <h3 class="font-extrabold text-sm text-slate-900 dark:text-white">${acc.name}</h3>
              <p class="text-xs text-slate-500 dark:text-slate-400 font-medium">${acc.title}</p>
            </div>
            <div class="pt-1 text-[11px] text-slate-400 font-mono space-y-0.5 border-t border-slate-100 dark:border-slate-700/60">
              <p>Логин: <b class="text-slate-700 dark:text-slate-200 font-mono">${key}</b></p>
              <p>Пароль: <b class="text-slate-700 dark:text-slate-200 font-mono">${acc.pass}</b></p>
              <p>Тел: <b>${acc.phone || '+998 (90) 000-00-00'}</b></p>
            </div>
          </div>

          <button type="button" onclick="fastSwitchUser('${key}')" 
                  class="w-full py-2.5 px-3 rounded-xl font-bold text-xs transition flex items-center justify-center gap-1.5 cursor-pointer ${isCurrent ? 'bg-emerald-50 text-emerald-700 dark:bg-emerald-950/40 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-700' : 'bg-slate-900 text-white hover:bg-slate-800 dark:bg-slate-700 dark:hover:bg-slate-600 shadow-xs'}">
            <i class="fa-solid fa-arrow-right-to-bracket"></i>
            <span>${isCurrent ? 'Текущая учетная запись' : 'Войти под этой ролью'}</span>
          </button>
        `;
        container.appendChild(card);
      });
    }

    let tabDocType = 'contract'; // 'contract' or 'certificate'

    function setTabDocType(type) {
      tabDocType = type;
      const btnContract = document.getElementById('tab-btn-doc-contract');
      const btnCert = document.getElementById('tab-btn-doc-cert');
      const viewContract = document.getElementById('tab-a4-contract-view');
      const viewCert = document.getElementById('tab-a4-cert-view');

      if (type === 'contract') {
        btnContract.className = 'px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs';
        btnCert.className = 'px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer text-slate-500 hover:text-slate-900 dark:hover:text-white';
        viewContract.classList.remove('hidden');
        viewCert.classList.add('hidden');
      } else {
        btnCert.className = 'px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer bg-white dark:bg-slate-800 text-slate-900 dark:text-white shadow-xs';
        btnContract.className = 'px-4 py-2 rounded-lg text-xs font-bold transition cursor-pointer text-slate-500 hover:text-slate-900 dark:hover:text-white';
        viewCert.classList.remove('hidden');
        viewContract.classList.add('hidden');
      }
      updateTabA4Preview();
    }

    function initA4GeneratorTab() {
      const sel = document.getElementById('tab-a4-student-select');
      if (!sel) return;
      sel.innerHTML = '';
      appState.students.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s.id;
        opt.textContent = `${s.name} — ${s.course} (${s.groupName || s.groupId})`;
        sel.appendChild(opt);
      });

      if (appState.students.length > 0) {
        onTabA4StudentChange();
      }
    }

    function onTabA4StudentChange() {
      const sel = document.getElementById('tab-a4-student-select');
      if (!sel) return;
      const studentId = sel.value;
      const s = appState.students.find(st => st.id === studentId);
      if (!s) return;

      document.getElementById('tab-a4-student-name').value = s.name;
      document.getElementById('tab-a4-course-name').value = s.course;
      document.getElementById('tab-a4-price').value = (s.course === 'Python' || s.course === 'Веб-программирование') ? '600 000' : '550 000';
      document.getElementById('tab-a4-parent-name').value = s.parent || 'Родитель / Vasiy';

      updateTabA4Preview();
    }

    function updateTabA4Preview() {
      const name = document.getElementById('tab-a4-student-name').value || 'Студент';
      const course = document.getElementById('tab-a4-course-name').value || 'Курс';
      const price = document.getElementById('tab-a4-price').value || '600 000';
      const parent = document.getElementById('tab-a4-parent-name').value || 'Родитель';

      // Contract bindings
      const sUz = document.getElementById('tab-contract-student-uz');
      const sRu = document.getElementById('tab-contract-student-ru');
      const cUz = document.getElementById('tab-contract-course-uz');
      const cRu = document.getElementById('tab-contract-course-ru');
      const pUz = document.getElementById('tab-contract-price-uz');
      const pRu = document.getElementById('tab-contract-price-ru');
      const prUz = document.getElementById('tab-contract-parent-uz');
      const prRu = document.getElementById('tab-contract-parent-ru');
      const prSign = document.getElementById('tab-contract-parent-sign');

      if (sUz) sUz.textContent = name;
      if (sRu) sRu.textContent = name;
      if (cUz) cUz.textContent = course;
      if (cRu) cRu.textContent = course;
      if (pUz) pUz.textContent = price;
      if (pRu) pRu.textContent = price;
      if (prUz) prUz.textContent = parent;
      if (prRu) prRu.textContent = parent;
      if (prSign) prSign.textContent = `${parent} (Ota-onasi)`;

      // Certificate bindings
      const certName = document.getElementById('tab-cert-student-name');
      const certCourse = document.getElementById('tab-cert-course-name');
      if (certName) certName.textContent = name;
      if (certCourse) certCourse.textContent = course;
    }

    function printTabA4Document() {
      if (tabDocType === 'contract') {
        const preview = document.getElementById('tab-a4-contract-view');
        printElementClean(preview, 'Shartnoma_MAM');
      } else {
        const preview = document.getElementById('tab-a4-cert-view');
        printElementClean(preview, 'Sertifikat_MAM');
      }
    }

    function printElementClean(el, title) {
      if (!el) return;
      const prevClass = document.body.className;
      // Use iframe or window.print with targeted print style
      const printWin = window.open('', '_blank', 'width=900,height=1100');
      if (!printWin) {
        // Fallback to window.print directly
        document.body.classList.add(tabDocType === 'contract' ? 'print-contract' : 'print-certificate');
        window.print();
        document.body.className = prevClass;
        return;
      }

      printWin.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
          <title>${title}</title>
          <script src="https://cdn.tailwindcss.com"></script>
          <style>
            @page { size: A4 portrait; margin: 0; }
            body { margin: 0; padding: 10mm; background: #fff; color: #000; font-family: sans-serif; }
          </style>
        </head>
        <body onload="window.print(); window.close();">
          ${el.outerHTML}
        </body>
        </html>
      `);
      printWin.document.close();
    }

    function initBackupTab() {
      const grpEl = document.getElementById('stat-groups-count');
      const stEl = document.getElementById('stat-students-count');
      const txEl = document.getElementById('stat-tx-count');
      const sizeEl = document.getElementById('stat-storage-size');

      if (grpEl) grpEl.textContent = appState.groups.length;
      if (stEl) stEl.textContent = appState.students.length;
      if (txEl) txEl.textContent = appState.auditLogs.length;

      try {
        const raw = localStorage.getItem('mam_crm_subd_data_v6') || '';
        const kb = (raw.length / 1024).toFixed(1);
        if (sizeEl) sizeEl.textContent = `~${kb} KB`;
      } catch(e){}
    }

    function restoreDatabaseFromTabInput(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const imported = JSON.parse(e.target.result);
          if (!imported.groups || !imported.students) {
            throw new Error("Неверная структура резервной копии MAM");
          }
          appState = imported;
          saveToStorage();
          setupUserSession();
          initBackupTab();
          showToast('✅ База данных MAM успешно восстановлена из JSON!');
          addAudit('Восстановление базы данных из резервного файла JSON');
        } catch(err) {
          showToast(`❌ Ошибка импорта: ${err.message}`);
        }
      };
      reader.readAsText(file);
    }

    function resetDatabaseToDefaults() {
      if (!confirm("Внимание! Вы уверены, что хотите сбросить базу данных к заводским демо-данным Маргиланского филиала? Все добавленные записи будут возвращены к исходным 18 группам.")) {
        return;
      }
      localStorage.removeItem('mam_crm_subd_data_v6');
      location.reload();
    }
"""

    if 'function renderRolesTab' not in html:
        # Place before </script></body>
        script_end = html.rfind("</script>")
        if script_end != -1:
            html = html[:script_end] + js_helpers + "\n  " + html[script_end:]
            print("Inserted JS helper functions into crm.html.")
        else:
            print("Error: </script> not found!")
    else:
        print("renderRolesTab already in html.")

    # 4. Update switchTab to call renderRolesTab, initA4GeneratorTab, initBackupTab
    switch_tab_pat = r"function switchTab\(tabId, btn\) \{[\s\S]*?if \(tabId === 'tab-director'\) \{"
    replacement_switch = """function switchTab(tabId, btn) {
      document.querySelectorAll('#sidebar-nav button').forEach(b => {
        b.className = 'w-full px-3 py-2.5 rounded-xl font-bold text-xs text-left transition flex items-center gap-2.5 nav-btn text-slate-600 hover:bg-slate-100 hover:text-slate-900';
      });
      btn.className = 'w-full px-3 py-2.5 rounded-xl font-bold text-xs text-left transition flex items-center gap-2.5 nav-btn bg-emerald-600 text-white';
      showTabPane(tabId);

      if (tabId === 'tab-roles') {
        renderRolesTab();
      } else if (tabId === 'tab-a4-generator') {
        initA4GeneratorTab();
      } else if (tabId === 'tab-backup') {
        initBackupTab();
      } else if (tabId === 'tab-director') {"""

    if re.search(switch_tab_pat, html):
        html = re.sub(switch_tab_pat, replacement_switch, html, count=1)
        print("Updated switchTab with tab handlers.")
    else:
        print("Warning: switchTab pattern not matched.")

    # 5. Fix fastSwitchUser container IDs
    fast_pat = r"document\.getElementById\('view-auth'\)\.classList\.add\('hidden'\);\s*document\.getElementById\('view-workspace'\)\.classList\.remove\('hidden'\);"
    fast_repl = """const vL = document.getElementById('view-login') || document.getElementById('view-auth');
      const vD = document.getElementById('view-dashboard') || document.getElementById('view-workspace');
      if (vL) vL.classList.add('hidden');
      if (vD) vD.classList.remove('hidden');
      setupUserSession();"""
    html = re.sub(fast_pat, fast_repl, html)

    # Also replace setupWorkspaceForUser(); with setupUserSession();
    html = html.replace("setupWorkspaceForUser();", "setupUserSession();")

    # Call lucide.createIcons() safely if lucide is available
    if "typeof lucide !== 'undefined' && lucide.createIcons" not in html:
        html = html.replace("setupUserSession() {", "setupUserSession() {\n      try { if (typeof lucide !== 'undefined') lucide.createIcons(); } catch(e){}")

    with open("crm.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("crm.html successfully updated!")

if __name__ == "__main__":
    main()
