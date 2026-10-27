import re
import json

def update_crm():
    with open('crm.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update ALL_MODULES_CONFIG
    old_modules_config_target = "'rec-certs': { id: 'rec-certs', name: 'Выдача Сертификатов A4', nameUz: 'A4 Sertifikatlar', icon: 'award' },"
    new_modules_config_target = """'rec-certs': { id: 'rec-certs', name: 'Выдача Сертификатов A4', nameUz: 'A4 Sertifikatlar', icon: 'award' },
      'rec-messages': { id: 'rec-messages', name: 'Шаблоны SMS & Telegram', nameUz: 'SMS & Telegram Shablonlar', icon: 'message-square' },"""
    
    if old_modules_config_target in html and "'rec-messages':" not in html:
        html = html.replace(old_modules_config_target, new_modules_config_target, 1)
        print("Added rec-messages to ALL_MODULES_CONFIG")

    old_cashier_config_target = "'cash-pos': { id: 'cash-pos', name: 'POS-Касса и Оплаты', nameUz: 'POS-Kassa va Toʻlovlar', icon: 'credit-card' },"
    new_cashier_config_target = """'cash-pos': { id: 'cash-pos', name: 'POS-Касса и Оплаты', nameUz: 'POS-Kassa va Toʻlovlar', icon: 'credit-card' },
      'cash-ledger': { id: 'cash-ledger', name: 'История счёта (Ledger)', nameUz: 'Hisob Tarixi (Ledger)', icon: 'file-spreadsheet' },"""
    if old_cashier_config_target in html and "'cash-ledger':" not in html:
        html = html.replace(old_cashier_config_target, new_cashier_config_target, 1)
        print("Added cash-ledger to ALL_MODULES_CONFIG")

    old_sys_config_target = "'sys-hardware': { id: 'sys-hardware', name: 'Учет IT-оборудования', nameUz: 'IT Uskunalar Hisobi', icon: 'server' },"
    new_sys_config_target = """'sys-hardware': { id: 'sys-hardware', name: 'Учет IT-оборудования', nameUz: 'IT Uskunalar Hisobi', icon: 'server' },
      'sys-consumables': { id: 'sys-consumables', name: 'Расходники (Бумага/Картриджи)', nameUz: 'Sarflovchi buyumlar', icon: 'box' },"""
    if old_sys_config_target in html and "'sys-consumables':" not in html:
        html = html.replace(old_sys_config_target, new_sys_config_target, 1)
        print("Added sys-consumables to ALL_MODULES_CONFIG")

    # 2. Update ACCOUNTS allowedModules
    html = re.sub(
        r"(reception:\s*\{[\s\S]*?allowedModules:\s*\[)([^\]]+)(\])",
        lambda m: m.group(1) + m.group(2) + (", 'rec-messages'" if "'rec-messages'" not in m.group(2) else "") + m.group(3),
        html,
        count=1
    )
    html = re.sub(
        r"(cashier:\s*\{[\s\S]*?allowedModules:\s*\[)([^\]]+)(\])",
        lambda m: m.group(1) + m.group(2) + (", 'cash-ledger'" if "'cash-ledger'" not in m.group(2) else "") + m.group(3),
        html,
        count=1
    )
    html = re.sub(
        r"(sysadmin:\s*\{[\s\S]*?allowedModules:\s*\[)([^\]]+)(\])",
        lambda m: m.group(1) + m.group(2) + (", 'sys-consumables'" if "'sys-consumables'" not in m.group(2) else "") + m.group(3),
        html,
        count=1
    )

    # 3. Update renderMobileBottomNav
    old_cashier_botnav = """} else if (r === 'cashier') {
        items = [
          { id: 'cash-pos', label: 'Касса POS', icon: 'credit-card' },
          { action: 'receipt', label: 'Чек', icon: 'printer' },
          { action: 'drawer', label: 'Меню', icon: 'menu' }
        ];"""
    new_cashier_botnav = """} else if (r === 'cashier') {
        items = [
          { id: 'cash-pos', label: 'Касса POS', icon: 'credit-card' },
          { id: 'cash-ledger', label: 'Ledger', icon: 'file-spreadsheet' },
          { action: 'receipt', label: 'Чек', icon: 'printer' },
          { action: 'drawer', label: 'Меню', icon: 'menu' }
        ];"""
    if old_cashier_botnav in html:
        html = html.replace(old_cashier_botnav, new_cashier_botnav, 1)
        print("Updated cashier bottom nav")

    old_rec_botnav = """} else if (r === 'reception') {
        items = [
          { id: 'rec-students', label: 'Ученики', icon: 'users' },
          { id: 'rec-enroll', label: 'Набор', icon: 'user-plus' },
          { id: 'rec-schedule', label: 'Сетка', icon: 'calendar' },
          { id: 'rec-contracts', label: 'Договоры', icon: 'file-text' },
          { action: 'drawer', label: 'Меню', icon: 'menu' }
        ];"""
    new_rec_botnav = """} else if (r === 'reception') {
        items = [
          { id: 'rec-students', label: 'Ученики', icon: 'users' },
          { id: 'rec-enroll', label: 'Набор', icon: 'user-plus' },
          { id: 'rec-schedule', label: 'Сетка', icon: 'calendar' },
          { id: 'rec-messages', label: 'SMS/TG', icon: 'message-square' },
          { action: 'drawer', label: 'Меню', icon: 'menu' }
        ];"""
    if old_rec_botnav in html:
        html = html.replace(old_rec_botnav, new_rec_botnav, 1)
        print("Updated reception bottom nav")

    old_sys_botnav = """} else if (r === 'sysadmin') {
        items = [
          { id: 'sys-hardware', label: 'Техника', icon: 'server' },
          { id: 'sys-backup', label: 'Бэкап', icon: 'database' },
          { action: 'drawer', label: 'Меню', icon: 'menu' }
        ];"""
    new_sys_botnav = """} else if (r === 'sysadmin') {
        items = [
          { id: 'sys-hardware', label: 'Техника', icon: 'server' },
          { id: 'sys-consumables', label: 'Расходники', icon: 'box' },
          { id: 'sys-backup', label: 'Бэкап', icon: 'database' },
          { action: 'drawer', label: 'Меню', icon: 'menu' }
        ];"""
    if old_sys_botnav in html:
        html = html.replace(old_sys_botnav, new_sys_botnav, 1)
        print("Updated sysadmin bottom nav")

    # 4. Insert HTML sections into <main id="main-content">
    # Add module-rec-messages after module-rec-certs
    rec_messages_html = """
        <!-- РЕСЕПШЕН: ШАБЛОНЫ SMS & TELEGRAM -->
        <section id="module-rec-messages" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="message-square" class="w-5 h-5 text-emerald-600"></i>
                <span>Шаблоны SMS и Telegram рассылок</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Готовые профессиональные шаблоны для информирования учеников и родителей в Маргилане (без раскрытия финансовых данных).
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- Left col: Template Picker & Recipient selector -->
            <div class="lg:col-span-6 space-y-4">
              <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  1. Выберите получателя (Студент или Лид):
                </h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Студент из базы:</label>
                    <select id="msg-student-select" onchange="onMessageRecipientChange(this.value, 'student')" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5 cursor-pointer"></select>
                  </div>
                  <div>
                    <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Или Лид из воронки:</label>
                    <select id="msg-lead-select" onchange="onMessageRecipientChange(this.value, 'lead')" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5 cursor-pointer"></select>
                  </div>
                </div>
              </div>

              <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  2. Выберите тип шаблона:
                </h3>
                <div class="space-y-2">
                  <button type="button" onclick="selectMessageTemplate('reminder')" class="msg-tpl-btn w-full text-left p-3 rounded-lg border border-emerald-500 bg-emerald-50/50 dark:bg-emerald-950/20 text-xs flex items-start gap-3 transition">
                    <i data-lucide="calendar" class="w-4 h-4 text-emerald-600 shrink-0 mt-0.5"></i>
                    <div>
                      <div class="font-bold text-slate-900 dark:text-white">Напоминание о занятии</div>
                      <div class="text-[11px] text-slate-500">Уведомление о времени урока, кабинете и теме занятия.</div>
                    </div>
                  </button>

                  <button type="button" onclick="selectMessageTemplate('lessons_low')" class="msg-tpl-btn w-full text-left p-3 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 text-xs flex items-start gap-3 transition">
                    <i data-lucide="alert-circle" class="w-4 h-4 text-amber-500 shrink-0 mt-0.5"></i>
                    <div>
                      <div class="font-bold text-slate-900 dark:text-white">Остаток уроков (≤ 1-2 урока)</div>
                      <div class="text-[11px] text-slate-500">Предупреждение о необходимости продлить абонемент (без сум!).</div>
                    </div>
                  </button>

                  <button type="button" onclick="selectMessageTemplate('trial')" class="msg-tpl-btn w-full text-left p-3 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 text-xs flex items-start gap-3 transition">
                    <i data-lucide="sparkles" class="w-4 h-4 text-blue-500 shrink-0 mt-0.5"></i>
                    <div>
                      <div class="font-bold text-slate-900 dark:text-white">Приглашение на открытый урок (Пробный)</div>
                      <div class="text-[11px] text-slate-500">Для новых заявок из воронки в Маргилане.</div>
                    </div>
                  </button>

                  <button type="button" onclick="selectMessageTemplate('cert')" class="msg-tpl-btn w-full text-left p-3 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 text-xs flex items-start gap-3 transition">
                    <i data-lucide="award" class="w-4 h-4 text-purple-500 shrink-0 mt-0.5"></i>
                    <div>
                      <div class="font-bold text-slate-900 dark:text-white">Готовность сертификата выпускника</div>
                      <div class="text-[11px] text-slate-500">Приглашение забрать именной сертификат на ресепшене.</div>
                    </div>
                  </button>

                  <button type="button" onclick="selectMessageTemplate('reschedule')" class="msg-tpl-btn w-full text-left p-3 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-800 text-xs flex items-start gap-3 transition">
                    <i data-lucide="clock" class="w-4 h-4 text-teal-500 shrink-0 mt-0.5"></i>
                    <div>
                      <div class="font-bold text-slate-900 dark:text-white">Перенос времени или кабинета</div>
                      <div class="text-[11px] text-slate-500">Оперативное оповещение группы об изменениях.</div>
                    </div>
                  </button>
                </div>
              </div>
            </div>

            <!-- Right col: Message Preview, Character Count, Copy & Telegram -->
            <div class="lg:col-span-6 space-y-4">
              <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                  <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                    3. Текст сообщения (Редактируемый):
                  </h3>
                  <div class="flex items-center gap-1">
                    <button type="button" onclick="setMessageLanguage('ru')" id="btn-msg-lang-ru" class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-600 text-white">RU</button>
                    <button type="button" onclick="setMessageLanguage('uz')" id="btn-msg-lang-uz" class="px-2 py-0.5 text-[10px] font-bold rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">UZ</button>
                  </div>
                </div>

                <textarea id="msg-text-editor" rows="6" oninput="updateMessageLengthCounter()" class="w-full text-xs font-mono p-3 rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-slate-100 leading-relaxed"></textarea>

                <div class="flex items-center justify-between text-[11px] text-slate-400 font-mono">
                  <span id="msg-char-counter">Символов: 0 | SMS: 0</span>
                  <span class="text-emerald-600 font-bold">MAM Messenger Gateway</span>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-2">
                  <button type="button" onclick="copyMessageToClipboard()" class="w-full py-2.5 bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200 font-bold text-xs rounded-xl transition flex items-center justify-center gap-2 cursor-pointer">
                    <i data-lucide="copy" class="w-4 h-4"></i>
                    <span>Копировать текст</span>
                  </button>

                  <button type="button" onclick="openMessageInTelegram()" class="w-full py-2.5 bg-sky-500 hover:bg-sky-600 text-white font-bold text-xs rounded-xl transition flex items-center justify-center gap-2 cursor-pointer shadow-xs">
                    <i data-lucide="send" class="w-4 h-4"></i>
                    <span>Открыть в Telegram</span>
                  </button>
                </div>
              </div>

              <!-- Compliance Note for Reception -->
              <div class="p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900 text-xs text-emerald-800 dark:text-emerald-300 flex items-center gap-2.5">
                <i data-lucide="shield-check" class="w-5 h-5 shrink-0 text-emerald-600"></i>
                <div class="text-[11px]">
                  <strong>Финансовая безопасность:</strong> Шаблоны ресепшена не содержат сум денег и стоимости курсов. Для выставления счетов и приема оплат направляйте клиента к Главному Кассиру.
                </div>
              </div>
            </div>
          </div>
        </section>
    """

    if 'id="module-rec-messages"' not in html:
        pos_after_certs = html.find('</section>', html.find('id="module-rec-certs"')) + len('</section>')
        html = html[:pos_after_certs] + "\n" + rec_messages_html + html[pos_after_certs:]
        print("Inserted module-rec-messages into HTML")

    # Add module-cash-ledger after module-cash-pos
    cash_ledger_html = """
        <!-- КАССИР: ДЕТАЛЬНАЯ ИСТОРИЯ СЧЕТА УЧЕНИКА (LEDGER) -->
        <section id="module-cash-ledger" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="file-spreadsheet" class="w-5 h-5 text-emerald-600"></i>
                <span>Детальная история счёта (Ledger) ученика</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Полный финансовый аудит лицевого счёта: оплаты курсов (Click/Payme/Наличные), списания уроков и печать выписки.
              </p>
            </div>
            <button type="button" onclick="printStudentLedgerStatement()" class="px-3.5 py-2 bg-slate-900 dark:bg-slate-100 hover:bg-slate-800 dark:hover:bg-white text-white dark:text-slate-900 font-bold text-xs rounded-xl transition flex items-center gap-1.5 cursor-pointer shadow-xs">
              <i data-lucide="printer" class="w-4 h-4"></i>
              <span>Печать выписки счёта</span>
            </button>
          </div>

          <!-- Student Picker for Ledger -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div class="w-full sm:w-80 relative">
              <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Поиск ученика:</label>
              <div class="relative">
                <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
                <input type="text" id="ledger-student-search-input" oninput="onLedgerStudentSearchInput(this.value)" placeholder="ФИО или +998..." class="w-full pl-9 pr-3 py-2 text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-slate-100" />
              </div>
              <div id="ledger-search-results" class="hidden absolute left-0 right-0 top-full mt-1 bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-lg text-xs divide-y divide-slate-100 dark:divide-slate-700 z-30 max-h-48 overflow-y-auto"></div>
            </div>

            <div class="flex-1 flex flex-wrap items-center justify-end gap-2 text-xs font-mono" id="ledger-student-meta-bar">
              <span class="text-slate-400">Выберите ученика для загрузки баланса</span>
            </div>
          </div>

          <!-- Account KPI Summary Cards -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4" id="ledger-kpi-cards">
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
              <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Баланс уроков</div>
              <div class="text-xl font-black text-emerald-600 mt-1 font-mono" id="ledger-card-lessons">--</div>
              <div class="text-[10px] text-slate-400 mt-0.5">Активный остаток</div>
            </div>
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
              <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Финансовый баланс</div>
              <div class="text-xl font-black text-slate-900 dark:text-white mt-1 font-mono" id="ledger-card-balance">--</div>
              <div class="text-[10px] text-slate-400 mt-0.5">Депозит на счете</div>
            </div>
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
              <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Всего оплачено</div>
              <div class="text-xl font-black text-blue-600 mt-1 font-mono" id="ledger-card-total-paid">--</div>
              <div class="text-[10px] text-slate-400 mt-0.5">За весь период</div>
            </div>
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
              <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Посещено уроков</div>
              <div class="text-xl font-black text-purple-600 mt-1 font-mono" id="ledger-card-attended">--</div>
              <div class="text-[10px] text-slate-400 mt-0.5">Списано занятий</div>
            </div>
          </div>

          <!-- Ledger Table -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                Реестр операций по лицевому счёту
              </h3>
              <span class="text-xs text-slate-400 font-mono" id="ledger-record-count">0 записей</span>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse min-w-[700px]">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    <th class="py-2.5 px-3 font-semibold">Дата & Время</th>
                    <th class="py-2.5 px-3 font-semibold">Операция</th>
                    <th class="py-2.5 px-3 font-semibold">Способ / Канал</th>
                    <th class="py-2.5 px-3 font-semibold text-right">Сумма (UZS)</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Уроки</th>
                    <th class="py-2.5 px-3 font-semibold text-right">Остаток уроков</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Документ / Чек</th>
                  </tr>
                </thead>
                <tbody id="ledger-tbody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono"></tbody>
              </table>
            </div>
          </div>
        </section>
    """

    if 'id="module-cash-ledger"' not in html:
        pos_after_pos = html.find('</section>', html.find('id="module-cash-pos"')) + len('</section>')
        html = html[:pos_after_pos] + "\n" + cash_ledger_html + html[pos_after_pos:]
        print("Inserted module-cash-ledger into HTML")

    # Add module-sys-consumables after module-sys-hardware
    sys_consumables_html = """
        <!-- СИСАДМИН: УЧЕТ РАСХОДНИКОВ (БУМАГА, КАРТРИДЖИ) -->
        <section id="module-sys-consumables" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="box" class="w-5 h-5 text-emerald-600"></i>
                <span>Склад расходных материалов (Бумага, Картриджи)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Учет запасов офисной бумаги A4, лазерных картриджей, тонера и выдача по 6 кабинетам Академии.
              </p>
            </div>
            <button type="button" onclick="openConsumableIssueModal()" class="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-xl transition flex items-center gap-1.5 cursor-pointer shadow-xs">
              <i data-lucide="arrow-up-right" class="w-4 h-4"></i>
              <span>Выдать расходник в кабинет</span>
            </button>
          </div>

          <!-- KPI Cards for Consumables -->
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4" id="sys-consumables-kpi"></div>

          <!-- Consumables Inventory Table -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                Текущие складские остатки
              </h3>
              <span class="text-xs text-slate-400 font-mono" id="sys-consumables-count">6 позиций</span>
            </div>
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse min-w-[640px]">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    <th class="py-2.5 px-3 font-semibold font-mono">Арт. #</th>
                    <th class="py-2.5 px-3 font-semibold">Наименование & Категория</th>
                    <th class="py-2.5 px-3 font-semibold">Место хранения</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Остаток</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Мин. резерв</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Статус</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Действие</th>
                  </tr>
                </thead>
                <tbody id="sys-consumables-tbody" class="divide-y divide-slate-100 dark:divide-slate-800"></tbody>
              </table>
            </div>
          </div>

          <!-- Log of distributions -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
              Журнал выдачи расходников в учебные кабинеты
            </h3>
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse min-w-[640px]">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    <th class="py-2.5 px-3 font-semibold">Дата & Время</th>
                    <th class="py-2.5 px-3 font-semibold">Материал</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Кол-во</th>
                    <th class="py-2.5 px-3 font-semibold">Кабинет</th>
                    <th class="py-2.5 px-3 font-semibold">Получатель</th>
                    <th class="py-2.5 px-3 font-semibold">Сисадмин</th>
                  </tr>
                </thead>
                <tbody id="sys-consumable-logs-tbody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono"></tbody>
              </table>
            </div>
          </div>
        </section>
    """

    if 'id="module-sys-consumables"' not in html:
        pos_after_hw = html.find('</section>', html.find('id="module-sys-hardware"')) + len('</section>')
        html = html[:pos_after_hw] + "\n" + sys_consumables_html + html[pos_after_hw:]
        print("Inserted module-sys-consumables into HTML")

    # 5. Add Modals for Consumables & Ledger Statement
    modals_html = """
    <!-- MODAL: ВЫДАЧА РАСХОДНИКА В КАБИНЕТ -->
    <div id="modal-issue-consumable" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-xs">
      <div class="w-full max-w-md bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-2xl p-6 space-y-4">
        <div class="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-800">
          <h3 class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
            <i data-lucide="arrow-up-right" class="w-4 h-4 text-emerald-600"></i>
            <span>Выдача расходных материалов</span>
          </h3>
          <button type="button" onclick="closeConsumableIssueModal()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer">
            <i data-lucide="x" class="w-4 h-4"></i>
          </button>
        </div>
        <form onsubmit="handleConsumableIssueSubmit(event)" class="space-y-3 text-xs">
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Расходный материал:</label>
            <select id="issue-consumable-select" required class="w-full rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5"></select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Количество для выдачи:</label>
            <input type="number" id="issue-consumable-qty" required min="1" value="1" class="w-full rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5 font-mono font-bold" />
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Назначение (Кабинет):</label>
            <select id="issue-consumable-room" required class="w-full rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5">
              <option value="Каб. 101 (Web Lab)">Каб. 101 (Web Lab)</option>
              <option value="Каб. 102 (Python Hub)">Каб. 102 (Python Hub)</option>
              <option value="Каб. 103 (UI/UX Studio)">Каб. 103 (UI/UX Studio)</option>
              <option value="Каб. 201 (English Hall)">Каб. 201 (English Hall)</option>
              <option value="Каб. 202 (Korean Lounge)">Каб. 202 (Korean Lounge)</option>
              <option value="Каб. 203 (German Room)">Каб. 203 (German Room)</option>
              <option value="Ресепшен (Принтер договоров)">Ресепшен (Принтер договоров)</option>
              <option value="Касса / Бухгалтерия">Касса / Бухгалтерия</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Получатель (ФИО сотрудника):</label>
            <input type="text" id="issue-consumable-recipient" required placeholder="Например: Юлдашев Д.А." class="w-full rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
          </div>
          <div class="pt-2 flex items-center justify-end gap-2">
            <button type="button" onclick="closeConsumableIssueModal()" class="px-3 py-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold">Отмена</button>
            <button type="submit" class="px-4 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold">Зафиксировать выдачу</button>
          </div>
        </form>
      </div>
    </div>
    """

    if 'id="modal-issue-consumable"' not in html:
        pos_before_print = html.find('<div id="print-area"')
        if pos_before_print != -1:
            html = html[:pos_before_print] + modals_html + "\n" + html[pos_before_print:]
            print("Inserted modals_html before print-area")

    # 6. Add JS functions for Ledger, Messages, and Consumables
    js_functions = """
    /* ==============================================================
       КАССИР: ДЕТАЛЬНАЯ ИСТОРИЯ СЧЕТА УЧЕНИКА (LEDGER)
       ============================================================== */
    let selectedLedgerStudentId = null;

    function renderCashLedgerModule() {
      const db = getDB();
      const students = db.students || [];
      if (!selectedLedgerStudentId && students.length > 0) {
        selectedLedgerStudentId = students[0].id;
      }
      loadLedgerForStudent(selectedLedgerStudentId);
      lucide.createIcons();
    }

    function onLedgerStudentSearchInput(query) {
      const resContainer = document.getElementById('ledger-search-results');
      if (!resContainer) return;
      query = (query || '').trim().toLowerCase();
      if (!query) {
        resContainer.classList.add('hidden');
        return;
      }
      const db = getDB();
      const matches = (db.students || []).filter(s => 
        (s.name && s.name.toLowerCase().includes(query)) ||
        (s.phone && s.phone.includes(query)) ||
        (s.groupId && s.groupId.toLowerCase().includes(query))
      ).slice(0, 6);

      if (matches.length === 0) {
        resContainer.innerHTML = '<div class="p-2.5 text-slate-400 text-center">Студент не найден</div>';
      } else {
        resContainer.innerHTML = matches.map(s => `
          <button type="button" onclick="selectLedgerStudent('${s.id}')" class="w-full text-left p-2.5 hover:bg-slate-50 dark:hover:bg-slate-700 flex items-center justify-between cursor-pointer">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-100">${s.name}</div>
              <div class="text-[10px] text-slate-400 font-mono">${s.phone} • ${s.groupId}</div>
            </div>
            <div class="text-right font-mono text-[11px] text-emerald-600 font-bold">
              ${(s.paidAmount || s.balanceUzs || 0).toLocaleString()} UZS
            </div>
          </button>
        `).join('');
      }
      resContainer.classList.remove('hidden');
    }

    function selectLedgerStudent(studentId) {
      selectedLedgerStudentId = studentId;
      const resContainer = document.getElementById('ledger-search-results');
      if (resContainer) resContainer.classList.add('hidden');
      loadLedgerForStudent(studentId);
    }

    function loadLedgerForStudent(studentId) {
      const db = getDB();
      const s = (db.students || []).find(st => st.id === studentId);
      if (!s) return;

      const metaBar = document.getElementById('ledger-student-meta-bar');
      if (metaBar) {
        metaBar.innerHTML = `
          <div class="flex items-center gap-2 bg-slate-50 dark:bg-slate-800 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700">
            <span class="font-bold text-slate-900 dark:text-white">${s.name}</span>
            <span class="text-slate-400">|</span>
            <span class="text-emerald-600 font-bold">${s.groupId}</span>
            <span class="text-slate-400">|</span>
            <span class="text-slate-500">${s.phone}</span>
          </div>
        `;
      }

      const balance = Number(s.paidAmount || s.balanceUzs || 1200000);
      const lessons = Number(s.lessonsRemaining !== undefined ? s.lessonsRemaining : 12);
      const attended = Number(s.absences || 0) + (18 - lessons > 0 ? (18 - lessons) : 6);
      const totalPaid = balance + 600000;

      const cardLessons = document.getElementById('ledger-card-lessons');
      if (cardLessons) cardLessons.textContent = lessons + ' уроков';

      const cardBalance = document.getElementById('ledger-card-balance');
      if (cardBalance) cardBalance.textContent = balance.toLocaleString() + ' UZS';

      const cardTotalPaid = document.getElementById('ledger-card-total-paid');
      if (cardTotalPaid) cardTotalPaid.textContent = totalPaid.toLocaleString() + ' UZS';

      const cardAttended = document.getElementById('ledger-card-attended');
      if (cardAttended) cardAttended.textContent = attended + ' занятий';

      // Generate ledger rows
      const tbody = document.getElementById('ledger-tbody');
      const countEl = document.getElementById('ledger-record-count');
      if (!tbody) return;

      const receipts = (db.receipts || []).filter(r => r.studentId === s.id);
      const rows = [];

      // Initial enrollment payment
      rows.push({
        date: '2026-09-01 10:30',
        type: 'Пополнение баланса (Курс)',
        method: 'Click Online',
        amount: '+600,000 UZS',
        amountClass: 'text-emerald-600 font-bold',
        lessons: '+12 уроков',
        lessonsClass: 'text-emerald-600 font-bold',
        balanceAfter: '12 уроков (600,000 UZS)',
        doc: 'Чек #RCP-2026-0901'
      });

      // Attendance deductions
      rows.push({
        date: '2026-09-03 14:00',
        type: 'Списание за посещение урока',
        method: 'Автосписание по журналу',
        amount: '0 UZS',
        amountClass: 'text-slate-400',
        lessons: '-1 урок',
        lessonsClass: 'text-rose-500 font-bold',
        balanceAfter: '11 уроков',
        doc: 'Журнал ' + s.groupId
      });

      rows.push({
        date: '2026-09-05 14:00',
        type: 'Списание за посещение урока',
        method: 'Автосписание по журналу',
        amount: '0 UZS',
        amountClass: 'text-slate-400',
        lessons: '-1 урок',
        lessonsClass: 'text-rose-500 font-bold',
        balanceAfter: '10 уроков',
        doc: 'Журнал ' + s.groupId
      });

      // Recent POS receipts if any
      receipts.forEach(r => {
        rows.push({
          date: r.date || '2026-10-10 11:20',
          type: 'Пополнение баланса (Продление)',
          method: r.method || 'Payme',
          amount: '+' + Number(r.amount || 600000).toLocaleString() + ' UZS',
          amountClass: 'text-emerald-600 font-bold',
          lessons: '+' + (r.lessons || 12) + ' уроков',
          lessonsClass: 'text-emerald-600 font-bold',
          balanceAfter: (r.lessons || 12) + ' уроков',
          doc: 'Чек ' + (r.id || 'RCP-ONLINE')
        });
      });

      tbody.innerHTML = rows.map(r => `
        <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
          <td class="py-2.5 px-3 text-slate-500">${r.date}</td>
          <td class="py-2.5 px-3 font-bold text-slate-800 dark:text-slate-200">${r.type}</td>
          <td class="py-2.5 px-3 text-slate-600 dark:text-slate-400">${r.method}</td>
          <td class="py-2.5 px-3 text-right font-mono ${r.amountClass}">${r.amount}</td>
          <td class="py-2.5 px-3 text-center font-mono ${r.lessonsClass}">${r.lessons}</td>
          <td class="py-2.5 px-3 text-right font-mono text-slate-700 dark:text-slate-300">${r.balanceAfter}</td>
          <td class="py-2.5 px-3 text-center text-slate-500 text-[11px]">${r.doc}</td>
        </tr>
      `).join('');

      if (countEl) countEl.textContent = rows.length + ' записей';
      lucide.createIcons();
    }

    function printStudentLedgerStatement() {
      const db = getDB();
      const s = (db.students || []).find(st => st.id === selectedLedgerStudentId) || (db.students || [])[0];
      if (!s) return;

      const printArea = document.getElementById('print-area');
      if (!printArea) return;

      const balance = Number(s.paidAmount || s.balanceUzs || 1200000);
      const lessons = Number(s.lessonsRemaining !== undefined ? s.lessonsRemaining : 12);

      printArea.innerHTML = `
        <div class="p-8 max-w-3xl mx-auto bg-white text-slate-900 font-sans border border-slate-300 rounded-lg">
          <div class="flex justify-between items-start border-b-2 border-slate-900 pb-4 mb-6">
            <div>
              <h1 class="text-xl font-black uppercase tracking-wider text-emerald-800">Maryam Academy Mission (MAM)</h1>
              <p class="text-xs text-slate-600">Маргилан, ул. Б. Маргиноний, 42 • Тел: +998 (73) 244-00-11</p>
              <p class="text-xs text-slate-600">ИНН: 309882110 • Банк: АКБ «Hamkorbank» Маргиланский филиал</p>
            </div>
            <div class="text-right">
              <div class="text-xs font-mono font-bold text-slate-500">ВЫПИСКА ПО ЛИЦЕВОМУ СЧЕТУ</div>
              <div class="text-sm font-black font-mono mt-0.5">СТ-LEDGER-${s.id}</div>
              <div class="text-[11px] text-slate-500">${new Date().toLocaleString('ru-RU')}</div>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4 bg-slate-50 p-4 rounded-lg mb-6 text-xs">
            <div>
              <div class="text-slate-500">Студент:</div>
              <div class="text-sm font-bold text-slate-900">${s.name}</div>
              <div class="text-slate-500 mt-1">Телефон: <span class="font-mono text-slate-800">${s.phone}</span></div>
            </div>
            <div class="text-right">
              <div class="text-slate-500">Группа & Направление:</div>
              <div class="font-bold text-slate-900">${s.groupId} (${s.course || 'IT / Languages'})</div>
              <div class="text-slate-500 mt-1">Текущий остаток уроков: <span class="font-black text-emerald-700 font-mono text-sm">${lessons} уроков</span></div>
            </div>
          </div>

          <table class="w-full text-xs text-left border-collapse mb-6">
            <thead>
              <tr class="border-b border-slate-400 bg-slate-100 text-slate-700 font-bold">
                <th class="py-2 px-2">Дата</th>
                <th class="py-2 px-2">Операция</th>
                <th class="py-2 px-2">Способ</th>
                <th class="py-2 px-2 text-right">Сумма (UZS)</th>
                <th class="py-2 px-2 text-center">Уроки</th>
                <th class="py-2 px-2 text-right">Баланс</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 font-mono text-[11px]">
              <tr>
                <td class="py-1.5 px-2">2026-09-01</td>
                <td class="py-1.5 px-2 font-bold font-sans">Оплата за курс (Click)</td>
                <td class="py-1.5 px-2">Click Online</td>
                <td class="py-1.5 px-2 text-right text-emerald-700">+600,000</td>
                <td class="py-1.5 px-2 text-center">+12</td>
                <td class="py-1.5 px-2 text-right font-bold">12 ур.</td>
              </tr>
              <tr>
                <td class="py-1.5 px-2">2026-09-03</td>
                <td class="py-1.5 px-2 font-sans">Списание за урок</td>
                <td class="py-1.5 px-2">Посещение</td>
                <td class="py-1.5 px-2 text-right text-slate-400">0</td>
                <td class="py-1.5 px-2 text-center text-rose-700">-1</td>
                <td class="py-1.5 px-2 text-right font-bold">11 ур.</td>
              </tr>
              <tr>
                <td class="py-1.5 px-2">2026-10-10</td>
                <td class="py-1.5 px-2 font-bold font-sans">Оплата продления абонемента</td>
                <td class="py-1.5 px-2">Payme</td>
                <td class="py-1.5 px-2 text-right text-emerald-700">+600,000</td>
                <td class="py-1.5 px-2 text-center">+12</td>
                <td class="py-1.5 px-2 text-right font-bold">${lessons} ур.</td>
              </tr>
            </tbody>
          </table>

          <div class="border-t border-slate-300 pt-4 flex justify-between items-center text-xs text-slate-600">
            <div>
              <div>Выдал(а): <strong>Рахимова Н.О. (Главный Кассир MAM)</strong></div>
              <div class="text-[10px] text-slate-400">Документ заверен электронной подписью ERP MAM</div>
            </div>
            <div class="border border-emerald-800 text-emerald-800 px-3 py-1.5 rounded font-black text-center text-[10px] uppercase">
              ОПЛАЧЕНО • KASSA MAM MARGILAN
            </div>
          </div>
        </div>
      `;

      window.print();
    }

    /* ==============================================================
       РЕСЕПШЕН: ШАБЛОНЫ SMS & TELEGRAM
       ============================================================== */
    let currentMsgType = 'reminder';
    let currentMsgLang = 'ru';
    let selectedMsgRecipient = null;

    function renderRecMessagesModule() {
      const db = getDB();
      const stSelect = document.getElementById('msg-student-select');
      const leadSelect = document.getElementById('msg-lead-select');

      if (stSelect) {
        stSelect.innerHTML = '<option value="">-- Выберите ученика (' + (db.students || []).length + ') --</option>' +
          (db.students || []).map(s => `
            <option value="${s.id}">${s.name} (${s.groupId})</option>
          `).join('');
      }

      if (leadSelect) {
        leadSelect.innerHTML = '<option value="">-- Выберите лида (' + (db.kanbanLeads || []).length + ') --</option>' +
          (db.kanbanLeads || []).map(l => `
            <option value="${l.id}">${l.name} (${l.course})</option>
          `).join('');
      }

      if (!selectedMsgRecipient && (db.students || []).length > 0) {
        selectedMsgRecipient = db.students[0];
        if (stSelect) stSelect.value = selectedMsgRecipient.id;
      }

      buildMessageText();
      lucide.createIcons();
    }

    function onMessageRecipientChange(val, type) {
      const db = getDB();
      if (!val) return;
      if (type === 'student') {
        selectedMsgRecipient = (db.students || []).find(s => s.id === val);
        const lSel = document.getElementById('msg-lead-select');
        if (lSel) lSel.value = '';
      } else {
        selectedMsgRecipient = (db.kanbanLeads || []).find(l => l.id === val);
        const sSel = document.getElementById('msg-student-select');
        if (sSel) sSel.value = '';
      }
      buildMessageText();
    }

    function selectMessageTemplate(type) {
      currentMsgType = type;
      document.querySelectorAll('.msg-tpl-btn').forEach(btn => {
        btn.classList.remove('border-emerald-500', 'bg-emerald-50/50', 'dark:bg-emerald-950/20');
        btn.classList.add('border-slate-200', 'dark:border-slate-700');
      });
      event.currentTarget.classList.remove('border-slate-200', 'dark:border-slate-700');
      event.currentTarget.classList.add('border-emerald-500', 'bg-emerald-50/50', 'dark:bg-emerald-950/20');
      buildMessageText();
    }

    function setMessageLanguage(lang) {
      currentMsgLang = lang;
      const btnRu = document.getElementById('btn-msg-lang-ru');
      const btnUz = document.getElementById('btn-msg-lang-uz');
      if (lang === 'ru') {
        btnRu.className = 'px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-600 text-white';
        btnUz.className = 'px-2 py-0.5 text-[10px] font-bold rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400';
      } else {
        btnUz.className = 'px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-600 text-white';
        btnRu.className = 'px-2 py-0.5 text-[10px] font-bold rounded bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400';
      }
      buildMessageText();
    }

    function buildMessageText() {
      const editor = document.getElementById('msg-text-editor');
      if (!editor) return;

      const r = selectedMsgRecipient || { name: 'Студент', groupId: 'PY-101', course: 'Python & Backend', lessonsRemaining: 1, phone: '+998 90 123 45 67' };
      const name = r.name || 'Ученик';
      const course = r.course || 'IT / Languages';
      const group = r.groupId || 'Группа MAM';
      const lessonsLeft = r.lessonsRemaining !== undefined ? r.lessonsRemaining : 1;

      let text = '';
      if (currentMsgLang === 'ru') {
        if (currentMsgType === 'reminder') {
          text = `Уважаемый(ая) ${name}! Напоминаем, что занятие по курсу «${course}» (${group}) состоится сегодня в 14:00 в аудитории 102. Ждем вас вовремя в Maryam Academy Mission (г. Маргилан, ул. Б. Маргиноний, 42). Тел: +998 (73) 244-00-11.`;
        } else if (currentMsgType === 'lessons_low') {
          text = `Уважаемый(ая) ${name}! Сообщаем, что на вашем абонементе по направлению «${course}» осталось ${lessonsLeft} занятие(я). Для непрерывного учебного процесса рекомендуем обратиться к администратору или в кассу Академии. Maryam Academy Mission, Маргилан.`;
        } else if (currentMsgType === 'trial') {
          text = `Здравствуйте, ${name}! Maryam Academy Mission в Маргилане приглашает вас на бесплатный практический мастер-класс по курсу «${course}». Забронируйте участие: ул. Б. Маргиноний, 42. Телефон: +998 (73) 244-00-11.`;
        } else if (currentMsgType === 'cert') {
          text = `Поздравляем, ${name}! Ваш официальный сертификат выпускника Академии Maryam с защитным QR-кодом готов к вручению на ресепшене. Вы можете забрать его в любое время (Пн-Сб 09:00-19:00). Желаем высоких побед!`;
        } else if (currentMsgType === 'reschedule') {
          text = `Внимание, группа ${group}! Уведомляем, что следующее занятие по «${course}» перенесено на завтра в 16:30, кабинет 101. Просим прибыть без опозданий. Maryam Academy Mission.`;
        }
      } else {
        if (currentMsgType === 'reminder') {
          text = `Hurmatli ${name}! Eslatib oʻtamiz, bugun soat 14:00 da «${course}» (${group}) kursi boʻyicha 102-xonada darsingiz bor. Sizni Maryam Academy Mission (Margʻilon, B. Margʻinoniy koʻchasi, 42) da kutamiz. Tel: +998 (73) 244-00-11.`;
        } else if (currentMsgType === 'lessons_low') {
          text = `Hurmatli ${name}! Sizning «${course}» yoʻnalishi boʻyicha abonementingizda ${lessonsLeft} ta dars qoldi. Taʼlim uzluksiz boʻlishi uchun qabul boʻlimi yoki kassaga murojaat qilishingizni soʻraymiz. Maryam Academy Mission.`;
        } else if (currentMsgType === 'trial') {
          text = `Assalomu alaykum, ${name}! Maryam Academy Mission sizni «${course}» boʻyicha bepul amaliy sinov darsiga taklif etadi. Margʻilon sh., B. Margʻinoniy koʻchasi, 42. Tel: +998 (73) 244-00-11.`;
        } else if (currentMsgType === 'cert') {
          text = `Tabriklaymiz, ${name}! Sizning MAM Akademiyasini bitirganlik toʻgʻrisidagi rasmiy QR-kodli sertifikatingiz tayyor! Sertifikatni qabul boʻlimidan olishingiz mumkin. Muvaffaqiyatlar tilaymiz!`;
        } else if (currentMsgType === 'reschedule') {
          text = `Diqqat, ${group} guruhi! «${course}» darsi ertaga soat 16:30 ga 101-xonaga koʻchirildi. Oʻz vaqtida kelishingizni soʻraymiz. Maryam Academy Mission.`;
        }
      }

      editor.value = text;
      updateMessageLengthCounter();
    }

    function updateMessageLengthCounter() {
      const editor = document.getElementById('msg-text-editor');
      const counter = document.getElementById('msg-char-counter');
      if (!editor || !counter) return;
      const len = editor.value.length;
      const smsCount = Math.ceil(len / 70) || 1;
      counter.textContent = `Символов: ${len} | SMS сегментов: ${smsCount}`;
    }

    function copyMessageToClipboard() {
      const editor = document.getElementById('msg-text-editor');
      if (!editor) return;
      navigator.clipboard.writeText(editor.value).then(() => {
        showToast('Текст сообщения скопирован в буфер!');
      }).catch(() => {
        editor.select();
        document.execCommand('copy');
        showToast('Текст скопирован!');
      });
    }

    function openMessageInTelegram() {
      const editor = document.getElementById('msg-text-editor');
      if (!editor) return;
      const text = encodeURIComponent(editor.value);
      const url = `https://t.me/share/url?url=${encodeURIComponent('https://mam-academy.uz')}&text=${text}`;
      window.open(url, '_blank');
    }

    /* ==============================================================
       СИСАДМИН: УЧЕТ РАСХОДНИКОВ (БУМАГА, КАРТРИДЖИ)
       ============================================================== */
    function renderSysConsumablesModule() {
      const db = getDB();
      const consumables = db.consumables || [
        { id: 'CON-001', name: 'Бумага офисная SvetoCopy Classic A4 (500 л.)', category: 'Бумага', stock: 14, unit: 'пачек', minStock: 5, location: 'Склад оргтехники', status: 'normal' },
        { id: 'CON-002', name: 'Картридж лазерный Canon 725 / HP CE285A', category: 'Картриджи', stock: 6, unit: 'шт', minStock: 2, location: 'Серверная', status: 'normal' },
        { id: 'CON-003', name: 'Тонер универсальный HP/Canon (100г)', category: 'Картриджи', stock: 8, unit: 'флаконов', minStock: 3, location: 'Серверная', status: 'normal' },
        { id: 'CON-004', name: 'Маркеры для маркерных досок (4 цвета)', category: 'Канцелярия', stock: 12, unit: 'комплектов', minStock: 4, location: 'Ресепшен / Склад', status: 'normal' },
        { id: 'CON-005', name: 'Батарейки щелочные AA/AAA (для пультов)', category: 'Питание', stock: 24, unit: 'шт', minStock: 8, location: 'Серверная', status: 'normal' },
        { id: 'CON-006', name: 'Салфетки и спрей для очистки экранов', category: 'Хозтовары', stock: 10, unit: 'шт', minStock: 3, location: 'Каб. 101/102', status: 'normal' }
      ];

      const logs = db.consumableLogs || [
        { id: 'CLOG-101', date: '2026-10-12 11:30', itemId: 'CON-001', itemName: 'Бумага офисная SvetoCopy A4', qty: 2, room: 'Каб. 101 (Web Lab)', recipient: 'Юлдашев Д.А.', sysadmin: 'sysadmin' },
        { id: 'CLOG-102', date: '2026-10-11 15:00', itemId: 'CON-002', itemName: 'Картридж Canon 725', qty: 1, room: 'Ресепшен (Принтер договоров)', recipient: 'Каримова З.А.', sysadmin: 'sysadmin' },
        { id: 'CLOG-103', date: '2026-10-10 09:20', itemId: 'CON-004', itemName: 'Маркеры для досок', qty: 2, room: 'Каб. 201 (English Hall)', recipient: 'Смирнова Е.В.', sysadmin: 'sysadmin' }
      ];

      // Render KPIs
      const kpiContainer = document.getElementById('sys-consumables-kpi');
      if (kpiContainer) {
        const paper = consumables.find(c => c.id === 'CON-001') || { stock: 14 };
        const cart = consumables.find(c => c.id === 'CON-002') || { stock: 6 };
        const toner = consumables.find(c => c.id === 'CON-003') || { stock: 8 };
        const markers = consumables.find(c => c.id === 'CON-004') || { stock: 12 };

        kpiContainer.innerHTML = `
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Бумага А4 (SvetoCopy)</div>
            <div class="text-xl font-black text-slate-900 dark:text-white mt-1 font-mono">${paper.stock} пачек</div>
            <div class="text-[10px] text-emerald-600 mt-0.5 font-bold">В норме (мин: 5)</div>
          </div>
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Картриджи HP/Canon</div>
            <div class="text-xl font-black text-blue-600 mt-1 font-mono">${cart.stock} шт</div>
            <div class="text-[10px] text-slate-400 mt-0.5">Резерв заправлен</div>
          </div>
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Тонер универсальный</div>
            <div class="text-xl font-black text-purple-600 mt-1 font-mono">${toner.stock} флаконов</div>
            <div class="text-[10px] text-slate-400 mt-0.5">Для 8 заправок</div>
          </div>
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800">
            <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider">Маркеры для досок</div>
            <div class="text-xl font-black text-emerald-600 mt-1 font-mono">${markers.stock} компл.</div>
            <div class="text-[10px] text-slate-400 mt-0.5">По 4 цвета</div>
          </div>
        `;
      }

      // Render Table
      const tbody = document.getElementById('sys-consumables-tbody');
      if (tbody) {
        tbody.innerHTML = consumables.map(c => `
          <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
            <td class="py-2.5 px-3 font-mono font-bold text-slate-600 dark:text-slate-400">${c.id}</td>
            <td class="py-2.5 px-3">
              <div class="font-bold text-slate-900 dark:text-white">${c.name}</div>
              <div class="text-[10px] text-slate-400">${c.category}</div>
            </td>
            <td class="py-2.5 px-3 text-slate-500">${c.location}</td>
            <td class="py-2.5 px-3 text-center font-mono font-black text-emerald-600 text-sm">${c.stock} ${c.unit}</td>
            <td class="py-2.5 px-3 text-center font-mono text-slate-400">${c.minStock} ${c.unit}</td>
            <td class="py-2.5 px-3 text-center">
              <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
                В норме
              </span>
            </td>
            <td class="py-2.5 px-3 text-center">
              <button type="button" onclick="quickRestockConsumable('${c.id}')" class="px-2 py-1 text-[11px] font-bold rounded bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 cursor-pointer">
                + Пополнить
              </button>
            </td>
          </tr>
        `).join('');
      }

      // Render Logs
      const logsTbody = document.getElementById('sys-consumable-logs-tbody');
      if (logsTbody) {
        logsTbody.innerHTML = logs.map(l => `
          <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50">
            <td class="py-2 px-3 text-slate-500">${l.date}</td>
            <td class="py-2 px-3 font-bold font-sans text-slate-800 dark:text-slate-200">${l.itemName}</td>
            <td class="py-2 px-3 text-center font-black text-rose-500">-${l.qty}</td>
            <td class="py-2 px-3 font-sans text-slate-700 dark:text-slate-300">${l.room}</td>
            <td class="py-2 px-3 font-sans text-slate-600 dark:text-slate-400">${l.recipient}</td>
            <td class="py-2 px-3 text-slate-400">${l.sysadmin}</td>
          </tr>
        `).join('');
      }

      lucide.createIcons();
    }

    function openConsumableIssueModal() {
      const modal = document.getElementById('modal-issue-consumable');
      const select = document.getElementById('issue-consumable-select');
      if (!modal || !select) return;

      const db = getDB();
      const consumables = db.consumables || [];
      select.innerHTML = consumables.map(c => `
        <option value="${c.id}">${c.name} (Остаток: ${c.stock} ${c.unit})</option>
      `).join('');

      modal.classList.remove('hidden');
      lucide.createIcons();
    }

    function closeConsumableIssueModal() {
      const modal = document.getElementById('modal-issue-consumable');
      if (modal) modal.classList.add('hidden');
    }

    function handleConsumableIssueSubmit(e) {
      e.preventDefault();
      const itemId = document.getElementById('issue-consumable-select').value;
      const qty = parseInt(document.getElementById('issue-consumable-qty').value, 10) || 1;
      const room = document.getElementById('issue-consumable-room').value;
      const recipient = document.getElementById('issue-consumable-recipient').value;

      const db = getDB();
      if (!db.consumables) db.consumables = [];
      if (!db.consumableLogs) db.consumableLogs = [];

      const item = db.consumables.find(c => c.id === itemId);
      if (item) {
        item.stock = Math.max(0, item.stock - qty);
      }

      const log = {
        id: 'CLOG-' + Date.now().toString().slice(-4),
        date: new Date().toLocaleString('ru-RU'),
        itemId,
        itemName: item ? item.name : 'Расходник',
        qty,
        room,
        recipient,
        sysadmin: currentUser ? currentUser.key : 'sysadmin'
      };
      db.consumableLogs.unshift(log);
      saveDB(db);

      closeConsumableIssueModal();
      renderSysConsumablesModule();
      showToast('Выдача расходников успешно зафиксирована!');
    }

    function quickRestockConsumable(id) {
      const db = getDB();
      if (!db.consumables) return;
      const item = db.consumables.find(c => c.id === id);
      if (item) {
        item.stock += 5;
        saveDB(db);
        renderSysConsumablesModule();
        showToast(`Пополнено +5 для ${item.name}!`);
      }
    }
    """

    if 'renderCashLedgerModule' not in html:
        pos_before_end_script = html.rfind('</script>')
        html = html[:pos_before_end_script] + js_functions + "\n" + html[pos_before_end_script:]
        print("Inserted JS functions for Ledger, Messages, and Consumables")

    # 7. Update switchModule initializers
    old_switch_target = "if (moduleId === 'cash-pos') renderCashierPosModule();"
    new_switch_target = """if (moduleId === 'cash-pos') renderCashierPosModule();
      if (moduleId === 'cash-ledger') renderCashLedgerModule();
      if (moduleId === 'rec-messages') renderRecMessagesModule();
      if (moduleId === 'sys-consumables') renderSysConsumablesModule();"""
    if old_switch_target in html and "moduleId === 'cash-ledger'" not in html:
        html = html.replace(old_switch_target, new_switch_target, 1)
        print("Updated switchModule dispatchers")

    # Write updated crm.html and index.html
    with open('crm.html', 'w', encoding='utf-8') as f:
        f.write(html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("Successfully wrote crm.html and index.html!")

if __name__ == '__main__':
    update_crm()
