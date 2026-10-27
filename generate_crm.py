#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_crm.py
Generates the complete, standalone, production-ready crm.html for Maryam Academy Mission (MAM) in Margilan,
with full Login & Password Authentication, Director Executive Command Center (360° KPI, Classrooms, Expenses P&L,
Marketing CAC, Security Audit Log), and all operational ERP modules.
"""

content = '''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MAM ERP/CRM — Maryam Academy Mission (Маргилан)</title>
  <meta name="description" content="Внутренняя ERP/CRM-система Академии IT и Языков Maryam Academy Mission в Маргилане. Кабинет Директора Богданова Т.Я., P&L, CAC, 9 аккаунтов, 18 групп, POS-касса, генератор договоров и сертификатов." />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#ECFDF5',
              100: '#D1FAE5',
              500: '#10B981',
              600: '#059669',
              700: '#047857',
              800: '#065F46',
              900: '#064E3B'
            }
          },
          fontFamily: {
            sans: ['Inter', 'system-ui', '-apple-system', 'Segoe UI', 'Roboto', 'sans-serif'],
            mono: ['JetBrains Mono', 'Fira Code', 'monospace']
          }
        }
      }
    };
  </script>

  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- Early Theme Init -->
  <script>
    (function() {
      const theme = localStorage.getItem('mam_theme') || 'light';
      if (theme === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    })();
  </script>

  <style>
    :root {
      --bg-surface: #F8FAFC;
      --text-main: #0F172A;
    }
    html.dark {
      --bg-surface: #0B1120;
      --text-main: #F8FAFC;
    }
    body {
      background-color: var(--bg-surface);
      color: var(--text-main);
      font-family: 'Inter', system-ui, sans-serif;
    }
    /* Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 4px; }
    html.dark ::-webkit-scrollbar-thumb { background: #334155; }

    /* Print Styles: strictly print only the targeted document container */
    @media print {
      body * {
        visibility: hidden !important;
      }
      #print-modal-container, #print-modal-container * {
        visibility: visible !important;
      }
      #print-modal-container {
        position: absolute !important;
        left: 0 !important;
        top: 0 !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        background: #ffffff !important;
        color: #000000 !important;
        box-shadow: none !important;
      }
      .no-print {
        display: none !important;
      }
      @page {
        size: A4 portrait;
        margin: 12mm;
      }
    }
  </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 antialiased selection:bg-emerald-500 selection:text-white">

  <!-- ============================================================== -->
  <!-- SCREEN 1: СЛУЖЕБНЫЙ ЭКРАН ВХОДА (LOGIN & PASSWORD AUTH) -->
  <!-- ============================================================== -->
  <section id="view-auth" class="min-h-screen flex items-center justify-center p-4 sm:p-6 bg-slate-100 dark:bg-slate-950">
    <div class="max-w-4xl w-full bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl overflow-hidden grid grid-cols-1 lg:grid-cols-12">
      
      <!-- Left side: Login Form (7 cols) -->
      <div class="lg:col-span-7 p-6 sm:p-10 flex flex-col justify-between space-y-6">
        <div>
          <!-- Academy Brand Header -->
          <div class="flex items-center gap-3 mb-6">
            <div class="w-11 h-11 rounded-2xl bg-emerald-600 text-white font-black flex items-center justify-center text-base shadow-md tracking-wider">
              MAM
            </div>
            <div>
              <h1 class="text-sm font-extrabold text-slate-900 dark:text-white leading-tight">
                MARYAM ACADEMY MISSION
              </h1>
              <p class="text-[11px] text-slate-500 dark:text-slate-400">
                Маргилан • Внутренняя ERP/CRM система
              </p>
            </div>
          </div>

          <div class="space-y-1 mb-6">
            <h2 class="text-xl font-black text-slate-900 dark:text-white" data-i18n="auth_welcome">
              Служебный вход для сотрудников
            </h2>
            <p class="text-xs text-slate-500 dark:text-slate-400" data-i18n="auth_subtitle">
              Введите персональный логин и пароль одного из 9 служебных аккаунтов.
            </p>
          </div>

          <!-- Error Alert Banner -->
          <div id="auth-error-banner" class="hidden p-3 rounded-xl bg-rose-50 dark:bg-rose-950/60 border border-rose-200 dark:border-rose-900/60 text-xs text-rose-700 dark:text-rose-300 font-semibold mb-4 flex items-center gap-2">
            <i data-lucide="alert-circle" class="w-4 h-4 shrink-0 text-rose-500"></i>
            <span id="auth-error-text">Неверный логин или пароль!</span>
          </div>

          <!-- Login Form -->
          <form onsubmit="handleAuthSubmit(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1" data-i18n="auth_login_label">
                Логин аккаунта:
              </label>
              <div class="relative">
                <input type="text" id="auth-login-input" required placeholder="director, cashier, teacher_python..." class="w-full text-xs font-mono font-medium rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2.5 pl-9 pr-3 text-slate-900 dark:text-white outline-none focus:border-emerald-500" />
                <i data-lucide="user" class="w-4 h-4 text-slate-400 absolute left-3 top-3"></i>
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1" data-i18n="auth_pass_label">
                Пароль доступа:
              </label>
              <div class="relative">
                <input type="password" id="auth-pass-input" required placeholder="Введите пароль..." class="w-full text-xs font-mono font-medium rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2.5 pl-9 pr-10 text-slate-900 dark:text-white outline-none focus:border-emerald-500" />
                <i data-lucide="lock" class="w-4 h-4 text-slate-400 absolute left-3 top-3"></i>
                <button type="button" onclick="togglePasswordVisibility()" class="absolute right-3 top-2.5 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer">
                  <i data-lucide="eye" id="auth-eye-icon" class="w-4 h-4"></i>
                </button>
              </div>
            </div>

            <button type="submit" class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs uppercase tracking-wider rounded-xl transition flex items-center justify-center gap-2 shadow-lg shadow-emerald-600/25 cursor-pointer">
              <i data-lucide="log-in" class="w-4 h-4"></i>
              <span data-i18n="auth_btn_submit">Войти в панель CRM</span>
            </button>
          </form>
        </div>

        <div class="flex items-center justify-between pt-4 border-t border-slate-100 dark:border-slate-800 text-[11px] text-slate-400">
          <span>г. Маргилан, ул. Б. Маргиноний, 42</span>
          <div class="flex items-center gap-2">
            <button type="button" onclick="toggleLang()" class="hover:text-slate-600 dark:hover:text-slate-200 font-bold cursor-pointer">UZ / RU</button>
            <span>•</span>
            <button type="button" onclick="toggleTheme()" class="hover:text-slate-600 dark:hover:text-slate-200 font-bold cursor-pointer">Тема</button>
          </div>
        </div>
      </div>

      <!-- Right side: Cheat Sheet of Accounts & Quick Fill (5 cols) -->
      <div class="lg:col-span-5 bg-slate-50 dark:bg-slate-800/60 p-6 sm:p-8 border-t lg:border-t-0 lg:border-l border-slate-200 dark:border-slate-800 flex flex-col justify-between space-y-4">
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-extrabold uppercase tracking-wider text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
              <i data-lucide="key" class="w-3.5 h-3.5 text-amber-500"></i>
              Служебные аккаунты (9)
            </span>
            <span class="text-[10px] text-emerald-600 font-bold bg-emerald-100 dark:bg-emerald-950 px-2 py-0.5 rounded-full">
              Тестовый доступ
            </span>
          </div>
          <p class="text-[11px] text-slate-500 dark:text-slate-400 mb-3">
            Нажмите на любой аккаунт ниже для мгновенной подстановки логина и пароля в 1 клик:
          </p>

          <!-- 9 Accounts Quick Fill List -->
          <div class="space-y-1.5 max-h-96 overflow-y-auto pr-1" id="auth-quick-accounts-list">
            <!-- Populated dynamically by JS -->
          </div>
        </div>

        <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-900/60 text-[10px] text-amber-800 dark:text-amber-300 space-y-1">
          <div class="font-bold flex items-center gap-1">
            <i data-lucide="shield-check" class="w-3 h-3 text-emerald-600"></i>
            Кабинет Директора Богданова Т.Я.:
          </div>
          <div>• Включает расширенный Command Center: Сводка 360°, Загрузка аудиторий, P&L Расходы, Маркетинг CAC и Audit Log безопасности.</div>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SCREEN 2: ОСНОВНАЯ ПАНЕЛЬ CRM/ERP (ПОСЛЕ УСПЕШНОЙ АВТОРИЗАЦИИ) -->
  <!-- ============================================================== -->
  <div id="view-app" class="hidden min-h-screen flex flex-col">
    <!-- TOP APP BAR -->
    <header class="sticky top-0 z-40 bg-white/90 dark:bg-slate-900/90 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 px-4 py-2.5 flex items-center justify-between shadow-xs">
      <div class="flex items-center gap-3">
        <div class="w-9 h-9 rounded-xl bg-emerald-600 text-white font-black flex items-center justify-center text-sm shadow-sm tracking-wider">
          MAM
        </div>
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-sm font-bold text-slate-900 dark:text-white leading-tight">
              MARYAM ACADEMY MISSION
            </h1>
            <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800">
              Маргилан ERP/CRM
            </span>
          </div>
          <p class="text-[11px] text-slate-500 dark:text-slate-400" id="header-branch-text">
            Филиал: ул. Б. Маргиноний, 42 • СУБД v4.6
          </p>
        </div>
      </div>

      <!-- Active User & System Quick Controls -->
      <div class="flex items-center gap-2 sm:gap-3">
        <!-- Active User Badge -->
        <div class="flex items-center gap-2 bg-slate-100 dark:bg-slate-800/80 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700">
          <span class="text-base" id="top-user-avatar">👑</span>
          <div class="text-left leading-tight hidden sm:block">
            <div class="text-xs font-bold text-slate-800 dark:text-slate-200" id="top-user-name">Богданов Т.Я.</div>
            <div class="text-[10px] text-emerald-600 dark:text-emerald-400 font-medium" id="top-user-role">Директор</div>
          </div>
        </div>

        <!-- Language Toggle -->
        <button type="button" onclick="toggleLang()" class="px-2.5 py-1.5 text-xs font-bold rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition flex items-center gap-1 cursor-pointer" title="Сменить язык / Tilni o'zgartirish">
          <i data-lucide="languages" class="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400"></i>
          <span id="lang-indicator">UZ / RU</span>
        </button>

        <!-- Theme Toggle -->
        <button type="button" onclick="toggleTheme()" class="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 transition text-slate-600 dark:text-slate-300 cursor-pointer" title="Тема: Светлая/Тёмная">
          <i data-lucide="moon" class="w-4 h-4 hidden dark:block"></i>
          <i data-lucide="sun" class="w-4 h-4 block dark:hidden"></i>
        </button>

        <!-- Logout Button -->
        <button type="button" onclick="logoutSession()" class="px-3 py-1.5 rounded-lg border border-rose-200 dark:border-rose-900 bg-rose-50 dark:bg-rose-950/40 text-rose-600 dark:text-rose-400 hover:bg-rose-100 dark:hover:bg-rose-900/60 transition text-xs font-bold flex items-center gap-1 cursor-pointer" title="Выйти из системы">
          <i data-lucide="log-out" class="w-3.5 h-3.5"></i>
          <span class="hidden md:inline" data-i18n="top_logout">Выйти</span>
        </button>
      </div>
    </header>

    <!-- MAIN LAYOUT: SIDEBAR + CONTENT AREA -->
    <div class="flex-1 flex overflow-hidden">
      <!-- LEFT SIDEBAR NAVIGATION -->
      <aside class="w-64 shrink-0 bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 flex flex-col justify-between overflow-y-auto">
        <div class="p-3 space-y-5">
          
          <!-- Role Quick Switcher in Sidebar -->
          <div class="space-y-1.5">
            <div class="flex items-center justify-between px-2">
              <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500" data-i18n="nav_roles_section">
                Аккаунт / Роль (9)
              </span>
              <span class="text-[10px] font-mono px-1 rounded bg-slate-100 dark:bg-slate-800 text-slate-500" id="sidebar-role-tag">
                DIRECTOR
              </span>
            </div>
            <select id="sidebar-role-select" onchange="onRoleSelectChange(this.value)" class="w-full text-xs font-medium rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-1.5 px-2.5 text-slate-800 dark:text-slate-100 cursor-pointer">
              <!-- populated by JS -->
            </select>
          </div>

          <!-- Navigation Tabs Menu -->
          <div class="space-y-1">
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 px-2 block" data-i18n="nav_modules_title">
              Модули системы
            </span>
            <nav id="sidebar-nav-list" class="space-y-1">
              <!-- Rendered by JS based on user permissions -->
            </nav>
          </div>

          <!-- Quick Summary Box -->
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/60 text-xs space-y-2">
            <div class="flex items-center justify-between text-slate-500 dark:text-slate-400">
              <span data-i18n="box_students">Студентов в базе:</span>
              <span class="font-bold text-slate-900 dark:text-white font-mono" id="side-stat-students">54</span>
            </div>
            <div class="flex items-center justify-between text-slate-500 dark:text-slate-400">
              <span data-i18n="box_groups">Активных групп:</span>
              <span class="font-bold text-slate-900 dark:text-white font-mono" id="side-stat-groups">18</span>
            </div>
            <div class="flex items-center justify-between text-slate-500 dark:text-slate-400">
              <span data-i18n="box_risks">В зоне риска:</span>
              <span class="font-bold text-rose-600 dark:text-rose-400 font-mono" id="side-stat-risks">0</span>
            </div>
          </div>
        </div>

        <!-- Sidebar Footer -->
        <div class="p-3 border-t border-slate-200 dark:border-slate-800 text-[11px] text-slate-400 space-y-2">
          <button type="button" onclick="logoutSession()" class="w-full py-2 px-3 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-rose-50 dark:hover:bg-rose-950/40 hover:text-rose-600 transition flex items-center justify-center gap-1.5 font-bold text-xs cursor-pointer text-slate-600 dark:text-slate-300">
            <i data-lucide="log-out" class="w-3.5 h-3.5"></i>
            <span data-i18n="btn_logout">Завершить сессию</span>
          </button>
          <div class="flex items-center justify-between pt-1">
            <span>Maryam Academy Mission</span>
            <span class="font-mono text-emerald-600 font-semibold">CRM 2026</span>
          </div>
          <div>Маргилан • Локальная база</div>
        </div>
      </aside>

      <!-- RIGHT CONTENT WORKSPACE -->
      <main class="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8 space-y-6">

        <!-- ============================================================== -->
        <!-- TAB 1: 👤 ПАНЕЛЬ И ВХОД ДЛЯ 9 СЛУЖЕБНЫХ АККАУНТОВ -->
        <!-- ============================================================== -->
        <section id="module-roles" class="module-view space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="users" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="roles_heading">1. Панель и вход для 9 Служебных Аккаунтов</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="roles_subheading">
                Изолированные профили сотрудников Академии MAM. Смена активной роли моментально обновляет доступ к разделам.
              </p>
            </div>
            <div class="flex items-center gap-2 text-xs">
              <span class="text-slate-500" data-i18n="roles_active_label">Текущий профиль:</span>
              <span class="px-2.5 py-1 rounded-lg bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-bold font-mono" id="roles-active-name-badge">
                Богданов Т.Я. (Директор)
              </span>
            </div>
          </div>

          <!-- 9 Accounts Grid -->
          <div id="roles-cards-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            <!-- Populated by renderRolesGrid() -->
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB 2: 👑 КАБИНЕТ ДИРЕКТОРА: EXECUTIVE COMMAND CENTER -->
        <!-- ============================================================== -->
        <section id="module-director" class="module-view hidden space-y-6">
          <!-- Header -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <div class="flex items-center gap-2">
                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 border border-emerald-500/20">
                  EXECUTIVE COMMAND CENTER
                </span>
                <span class="text-xs text-slate-400">Официальный кабинет Богданова Т.Я.</span>
              </div>
              <h2 class="text-xl font-black text-slate-900 dark:text-white mt-1 flex items-center gap-2">
                <i data-lucide="crown" class="w-5 h-5 text-amber-500"></i>
                <span data-i18n="dir_title">Стратегическое управление и аудит Академии MAM</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="dir_subtitle">
                360° P&L, загрузка аудиторий, ФОТ и удержание преподавателей, операционные расходы, CAC каналов и журнал аудита.
              </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-xs px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 font-mono text-slate-600 dark:text-slate-300">
                Маргилан • Октябрь 2026
              </span>
            </div>
          </div>

          <!-- Section 1: 📊 360° ВСЯ АКАДЕМИЯ KPI КАРТОЧКИ -->
          <div class="space-y-3">
            <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
              <i data-lucide="bar-chart-3" class="w-4 h-4 text-emerald-600"></i>
              1. Сводка "360° Вся Академия" (P&L и Секторы)
            </h3>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-3">
              <!-- KPI 1: Выручка -->
              <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-1">
                <span class="text-[10px] font-semibold text-slate-500">Выручка (Gross Revenue)</span>
                <div class="text-lg font-black text-slate-900 dark:text-white font-mono" id="dir-kpi-rev">37 100 000 UZS</div>
                <div class="text-[10px] text-emerald-600 font-medium">↑ +8.4% темп роста</div>
              </div>
              <!-- KPI 2: Чистая прибыль -->
              <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-emerald-300 dark:border-emerald-800 shadow-xs space-y-1">
                <span class="text-[10px] font-semibold text-emerald-700 dark:text-emerald-400">Чистая прибыль (Net)</span>
                <div class="text-lg font-black text-emerald-600 dark:text-emerald-400 font-mono" id="dir-kpi-net">12 800 000 UZS</div>
                <div class="text-[10px] text-slate-400">С учётом всех расходов</div>
              </div>
              <!-- KPI 3: Расходы P&L -->
              <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-1">
                <span class="text-[10px] font-semibold text-rose-600 dark:text-rose-400">Расходы и ФОТ</span>
                <div class="text-lg font-black text-rose-600 dark:text-rose-400 font-mono" id="dir-kpi-exp">24 300 000 UZS</div>
                <div class="text-[10px] text-slate-400">Аренда, ЗП, сервисы</div>
              </div>
              <!-- KPI 4: Маржа % -->
              <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-1">
                <span class="text-[10px] font-semibold text-slate-500">Рентабельность %</span>
                <div class="text-lg font-black text-indigo-600 dark:text-indigo-400 font-mono" id="dir-kpi-margin">34.5%</div>
                <div class="text-[10px] text-slate-400">EBITDA норма</div>
              </div>
              <!-- KPI 5: IT Сектор -->
              <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-1">
                <span class="text-[10px] font-semibold text-slate-500">IT Сектор (Python/Web/DS)</span>
                <div class="text-lg font-black text-blue-600 dark:text-blue-400 font-mono" id="dir-kpi-it">27 учеников</div>
                <div class="text-[10px] text-slate-400">50.0% от базы MAM</div>
              </div>
              <!-- KPI 6: Языковой Сектор -->
              <div class="p-3.5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-1">
                <span class="text-[10px] font-semibold text-slate-500">Языки (Eng/Kor/Ger)</span>
                <div class="text-lg font-black text-purple-600 dark:text-purple-400 font-mono" id="dir-kpi-lang">27 учеников</div>
                <div class="text-[10px] text-slate-400">50.0% от базы MAM</div>
              </div>
            </div>

            <!-- Classrooms & Lead Funnel (Grid 2 cols) -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
              <!-- Classroom Load Audit (7 cols) -->
              <div class="lg:col-span-7 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                  <h4 class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                    <i data-lucide="door-open" class="w-4 h-4 text-emerald-600"></i>
                    Загрузка 6 учебных аудиторий в Маргилане
                  </h4>
                  <span class="text-[10px] text-slate-400">Вместимость: 12-16 мест</span>
                </div>
                <div class="overflow-x-auto">
                  <table class="w-full text-xs text-left border-collapse">
                    <thead>
                      <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                        <th class="py-2 px-2.5 font-semibold">Кабинет</th>
                        <th class="py-2 px-2.5 font-semibold">Направление</th>
                        <th class="py-2 px-2.5 font-semibold text-center">Групп</th>
                        <th class="py-2 px-2.5 font-semibold text-center">Смен / День</th>
                        <th class="py-2 px-2.5 font-semibold text-right">Загрузка</th>
                        <th class="py-2 px-2.5 font-semibold text-center">Статус</th>
                      </tr>
                    </thead>
                    <tbody id="dir-classrooms-tbody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                      <!-- Rendered by JS -->
                    </tbody>
                  </table>
                </div>
              </div>

              <!-- Lead Conversion Funnel (5 cols) -->
              <div class="lg:col-span-5 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
                <div class="flex items-center justify-between">
                  <h4 class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                    <i data-lucide="filter" class="w-4 h-4 text-indigo-600"></i>
                    Конверсия воронки лидов Академии
                  </h4>
                  <span class="text-[10px] text-emerald-600 font-bold">ИТОГО: 34.8% в оплату</span>
                </div>
                <div class="space-y-2 text-xs">
                  <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800 flex items-center justify-between">
                    <div>
                      <div class="font-bold text-slate-800 dark:text-slate-200">1. Входящие заявки (Лиды)</div>
                      <div class="text-[10px] text-slate-400">Instagram, Telegram, Звонки</div>
                    </div>
                    <div class="font-mono font-bold text-slate-900 dark:text-white">155 лидов</div>
                  </div>
                  <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800 flex items-center justify-between">
                    <div>
                      <div class="font-bold text-slate-800 dark:text-slate-200">2. Дошли на пробный урок</div>
                      <div class="text-[10px] text-slate-400">Конверсия первого контакта</div>
                    </div>
                    <div class="font-mono font-bold text-blue-600">92 чел. (59.3%)</div>
                  </div>
                  <div class="p-2.5 rounded-lg bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900/60 flex items-center justify-between">
                    <div>
                      <div class="font-bold text-emerald-800 dark:text-emerald-300">3. Оплатили абонемент (Договор)</div>
                      <div class="text-[10px] text-emerald-600">Поступление в группы MAM</div>
                    </div>
                    <div class="font-mono font-black text-emerald-700 dark:text-emerald-300">54 студ. (34.8%)</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Section 2: 👨🏫 АНАЛИТИКА УЧИТЕЛЕЙ, УДЕРЖАНИЕ И ФОТ -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="award" class="w-4 h-4 text-emerald-600"></i>
                  2. Аналитика KPI 6 преподавателей, Удержание (Retention %) и ФОТ
                </h3>
                <p class="text-[11px] text-slate-500">
                  Метрики качества преподавания: процент оттока (Churn), количество активных учеников и авторасчет зарплат.
                </p>
              </div>
              <button type="button" onclick="payAllSalaries()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition flex items-center gap-1.5 cursor-pointer">
                <i data-lucide="check-check" class="w-3.5 h-3.5"></i>
                <span>Выплатить всем преподавателям</span>
              </button>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                    <th class="py-2.5 px-3 font-semibold">Преподаватель</th>
                    <th class="py-2.5 px-3 font-semibold">Курс</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Активных</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Удержание (Retention)</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Отток (Churn)</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Уроков</th>
                    <th class="py-2.5 px-3 font-semibold text-right">Начислено ЗП</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Статус</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Действие</th>
                  </tr>
                </thead>
                <tbody id="dir-teachers-tbody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Section 3: 💸 УПРАВЛЕНИЕ РАСХОДАМИ И УТВЕРЖДЕНИЕ БЮДЖЕТА P&L -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="receipt" class="w-4 h-4 text-rose-500"></i>
                  3. Управление операционными расходами (P&L Маргилан)
                </h3>
                <p class="text-[11px] text-slate-500">
                  Внесение расходов филиала: аренда, коммуналка, маркетинг, интернет. Автоматически вычитается из Чистой Прибыли.
                </p>
              </div>
              <div class="text-xs font-mono font-bold text-rose-600 dark:text-rose-400" id="dir-total-expenses-badge">
                Итого расходов: 0 UZS
              </div>
            </div>

            <!-- Add Expense Form -->
            <form onsubmit="handleNewExpenseSubmit(event)" class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 items-end">
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Категория:</label>
                <select id="exp-category-input" class="w-full text-xs rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5">
                  <option value="Аренда">Аренда помещения (Маргилан)</option>
                  <option value="Коммуналка">Коммунальные услуги & Э/э</option>
                  <option value="Интернет">Интернет & Связь (Uztelecom)</option>
                  <option value="Маркетинг">Маркетинг & Реклама (SMM)</option>
                  <option value="Хозтовары">Хозтовары & Канцелярия</option>
                  <option value="Оборудование">Оборудование & Ремонт ПК</option>
                  <option value="Налоги">Налоги и Лицензирование</option>
                </select>
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Назначение / Описание:</label>
                <input type="text" id="exp-title-input" required placeholder="Например: Аренда 2 этажа, Октябрь" class="w-full text-xs rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Сумма (UZS):</label>
                <input type="number" id="exp-amount-input" required placeholder="4500000" class="w-full text-xs font-mono font-bold rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Дата расхода:</label>
                <input type="date" id="exp-date-input" class="w-full text-xs rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>
              <div>
                <button type="submit" class="w-full py-2 bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-1.5 cursor-pointer">
                  <i data-lucide="plus" class="w-4 h-4"></i>
                  <span>Утвердить расход</span>
                </button>
              </div>
            </form>

            <!-- Expenses Registry Table -->
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                    <th class="py-2 px-3 font-semibold">Дата</th>
                    <th class="py-2 px-3 font-semibold">Категория</th>
                    <th class="py-2 px-3 font-semibold">Описание платежа</th>
                    <th class="py-2 px-3 font-semibold text-right">Сумма (UZS)</th>
                    <th class="py-2 px-3 font-semibold text-center">Утвердил</th>
                    <th class="py-2 px-3 font-semibold text-center">Действие</th>
                  </tr>
                </thead>
                <tbody id="dir-expenses-tbody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Section 4 & 5: МАРКЕТИНГ CAC & AUDIT LOG БЕЗОПАСНОСТИ (Grid 2 cols) -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
            
            <!-- Marketing CAC Analysis (6 cols) -->
            <div class="lg:col-span-6 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                  <i data-lucide="target" class="w-4 h-4 text-amber-500"></i>
                  4. Маркетинг & Стоимость привлечения (CAC)
                </h4>
                <span class="text-[10px] text-slate-400">Маргиланский филиал</span>
              </div>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse">
                  <thead>
                    <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                      <th class="py-2 px-2.5 font-semibold">Источник</th>
                      <th class="py-2 px-2.5 font-semibold text-center">Лидов</th>
                      <th class="py-2 px-2.5 font-semibold text-center">Оплат</th>
                      <th class="py-2 px-2.5 font-semibold text-right">Бюджет</th>
                      <th class="py-2 px-2.5 font-semibold text-right">CAC / Студ.</th>
                      <th class="py-2 px-2.5 font-semibold text-center">Конверсия</th>
                    </tr>
                  </thead>
                  <tbody id="dir-marketing-tbody" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                    <!-- Rendered by JS -->
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Security Audit Log (6 cols) -->
            <div class="lg:col-span-6 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <h4 class="text-xs font-bold text-slate-800 dark:text-slate-200 flex items-center gap-1.5">
                  <i data-lucide="shield-alert" class="w-4 h-4 text-blue-500"></i>
                  5. Журнал безопасности (Audit Log персонала)
                </h4>
                <span class="text-[10px] text-emerald-600 font-mono font-bold">LIVE МОНИТОРИНГ</span>
              </div>
              <p class="text-[11px] text-slate-400">
                Фиксация действий: оплаты, списания баланса, скидки, изменения групп и вход сотрудников.
              </p>
              <div class="max-h-60 overflow-y-auto space-y-2 pr-1" id="dir-audit-list">
                <!-- Rendered by JS -->
              </div>
            </div>

          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB 3: 🚨 РИСКИ И ALERTS (EARLY-WARNING & SMART FOLLOW-UP) -->
        <!-- ============================================================== -->
        <section id="module-risks" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-rose-600 dark:text-rose-400 flex items-center gap-2">
                <i data-lucide="alert-triangle" class="w-5 h-5 text-rose-600"></i>
                <span data-i18n="risk_heading">3. Риски и Alerts (Early-Warning System & Smart Follow-up)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="risk_subheading">
                Автоматический фильтр студентов с риском отчисления (осталось ≤ 1 урока или 3 пропуска подряд).
              </p>
            </div>
            <button type="button" onclick="renderRisksModule()" class="px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-800 text-xs font-semibold flex items-center gap-1.5 cursor-pointer">
              <i data-lucide="refresh-cw" class="w-3.5 h-3.5 text-emerald-600"></i>
              <span data-i18n="btn_refresh">Обновить список</span>
            </button>
          </div>

          <!-- Metric alert counters -->
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div class="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 flex items-center justify-between">
              <div>
                <div class="text-[11px] font-bold text-rose-700 dark:text-rose-400" data-i18n="risk_low_balance">Остаток уроков ≤ 1</div>
                <div class="text-xl font-black text-rose-700 dark:text-rose-300 font-mono" id="risk-count-balance">0</div>
              </div>
              <i data-lucide="hourglass" class="w-8 h-8 text-rose-400"></i>
            </div>

            <div class="p-3.5 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-900/60 flex items-center justify-between">
              <div>
                <div class="text-[11px] font-bold text-amber-700 dark:text-amber-400" data-i18n="risk_absences">3+ пропуска подряд</div>
                <div class="text-xl font-black text-amber-700 dark:text-amber-300 font-mono" id="risk-count-absent">0</div>
              </div>
              <i data-lucide="user-x" class="w-8 h-8 text-amber-400"></i>
            </div>

            <div class="p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900/60 flex items-center justify-between">
              <div>
                <div class="text-[11px] font-bold text-emerald-700 dark:text-emerald-400" data-i18n="risk_expected_renewal">Ожидаемая пролонгация</div>
                <div class="text-xl font-black text-emerald-700 dark:text-emerald-300 font-mono" id="risk-sum-renewal">0 UZS</div>
              </div>
              <i data-lucide="wallet" class="w-8 h-8 text-emerald-400"></i>
            </div>
          </div>

          <!-- At-Risk Students Table -->
          <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-3">
            <div class="flex items-center justify-between">
              <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="risk_list_title">
                Реестр студентов в группе риска
              </h3>
              <span class="text-[11px] text-slate-400" data-i18n="risk_quick_tip">
                Нажмите кнопку Telegram, чтобы сгенерировать готовое персональное сообщение для родителя
              </span>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                    <th class="py-2.5 px-3 font-semibold" data-i18n="risk_th_student">Студент</th>
                    <th class="py-2.5 px-3 font-semibold" data-i18n="risk_th_group">Группа / Курс</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="risk_th_balance">Остаток уроков</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="risk_th_absences">Пропусков</th>
                    <th class="py-2.5 px-3 font-semibold" data-i18n="risk_th_parent">Родитель / Телефон</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="risk_th_status">Причина риска</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="risk_th_action">Telegram напоминание</th>
                  </tr>
                </thead>
                <tbody id="risks-table-body" class="divide-y divide-slate-100 dark:divide-slate-800">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB 4: 📑 ГЕНЕРАТОР A4-ДОГОВОРОВ И СЕРТИФИКАТОВ (ПЕЧАТЬ В 1 КЛИК) -->
        <!-- ============================================================== -->
        <section id="module-contracts" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="file-text" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="doc_heading">4. Генератор A4-Договоров и Сертификатов (Печать в 1 клик)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="doc_subheading">
                Официальный двуязычный Договор (UZ/RU) и Сертификат выпускника с QR-кодом и подписью Директора Богданова Т.Я.
              </p>
            </div>
            <div class="flex items-center gap-2">
              <button type="button" onclick="printActiveA4Document()" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-2 shadow-sm cursor-pointer">
                <i data-lucide="printer" class="w-4 h-4"></i>
                <span data-i18n="doc_btn_print">Печать на A4 (1 клик)</span>
              </button>
            </div>
          </div>

          <!-- Controls: Select student and document type -->
          <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-4">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Doc Type Toggle -->
              <div>
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="doc_select_type">
                  Тип документа:
                </label>
                <div class="flex rounded-lg bg-slate-100 dark:bg-slate-800 p-1 border border-slate-200 dark:border-slate-700">
                  <button type="button" onclick="setDocType('contract')" id="btn-doc-type-contract" class="flex-1 py-1.5 text-xs font-bold rounded-md bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs transition cursor-pointer">
                    Договор UZ/RU
                  </button>
                  <button type="button" onclick="setDocType('certificate')" id="btn-doc-type-cert" class="flex-1 py-1.5 text-xs font-bold rounded-md text-slate-500 hover:text-slate-900 dark:hover:text-white transition cursor-pointer">
                    Сертификат A4
                  </button>
                </div>
              </div>

              <!-- Student Picker -->
              <div>
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="doc_select_student">
                  Выберите студента:
                </label>
                <select id="doc-student-select" onchange="onDocStudentChange(this.value)" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-3 cursor-pointer">
                  <!-- populated by JS -->
                </select>
              </div>

              <!-- Grade / Completion status for Certificate -->
              <div id="cert-extra-fields" class="hidden">
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="doc_cert_grade">
                  Итоговый балл / Квалификация:
                </label>
                <input type="text" id="cert-grade-input" oninput="updateCertPreview()" value="Отлично / 96 баллов (A+)" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-3" />
              </div>
            </div>
          </div>

          <!-- Document Preview Screen Container -->
          <div class="bg-slate-200 dark:bg-slate-950 p-4 sm:p-8 rounded-xl border border-slate-300 dark:border-slate-800 overflow-x-auto flex justify-center">
            <div id="print-modal-container" class="bg-white text-slate-900 w-[210mm] min-h-[297mm] p-[15mm] shadow-lg border border-slate-200">
              <!-- Rendered by renderDocPreview() -->
            </div>
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB 5: 💰 POS-КАССА И ОПЛАТА УРОКОВ -->
        <!-- ============================================================== -->
        <section id="module-pos" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="credit-card" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="pos_heading">5. POS-Касса и Оплата Уроков</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="pos_subheading">
                Приём оплат: Click, Payme, Наличные, Терминал. Пополнение баланса занятий и печать фискального чека.
              </p>
            </div>
            <div class="flex items-center gap-2 text-xs">
              <span class="text-slate-500" data-i18n="pos_cashier_label">Кассир смены:</span>
              <span class="px-2.5 py-1 rounded-lg bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-bold" id="pos-cashier-badge">
                Рахимова Н.
              </span>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- POS Input Form (7 cols) -->
            <div class="lg:col-span-7 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 space-y-4">
              <h3 class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2" data-i18n="pos_new_payment_title">
                <i data-lucide="plus-circle" class="w-4 h-4 text-emerald-600"></i>
                Проведение новой оплаты
              </h3>

              <!-- Search student by phone or name -->
              <div class="space-y-1">
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300" data-i18n="pos_search_label">
                  Поиск студента (по телефону +998... или ФИО):
                </label>
                <div class="relative">
                  <input type="text" id="pos-search-input" oninput="posSearchStudent(this.value)" placeholder="Начните вводить +99890... или фамилию" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2.5 pl-9 pr-3 text-slate-900 dark:text-white font-medium" />
                  <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-3"></i>
                </div>
                <div id="pos-search-dropdown" class="hidden max-h-48 overflow-y-auto bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-md divide-y divide-slate-100 dark:divide-slate-700 text-xs">
                  <!-- Dropdown items rendered dynamically -->
                </div>
              </div>

              <!-- Selected student preview box -->
              <div id="pos-selected-student-box" class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs space-y-2">
                <div class="flex items-center justify-between">
                  <span class="font-bold text-slate-900 dark:text-white text-sm" id="pos-card-name">Студент не выбран</span>
                  <span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-slate-200 dark:bg-slate-700" id="pos-card-id">ID: ---</span>
                </div>
                <div class="grid grid-cols-2 gap-2 text-slate-600 dark:text-slate-300">
                  <div>Группа: <strong class="text-slate-900 dark:text-white" id="pos-card-group">---</strong></div>
                  <div>Телефон: <strong class="text-slate-900 dark:text-white font-mono" id="pos-card-phone">---</strong></div>
                  <div>Текущий баланс: <strong class="text-emerald-600 dark:text-emerald-400 font-mono text-sm" id="pos-card-balance">0 уроков</strong></div>
                  <div>Курс: <strong class="text-slate-900 dark:text-white" id="pos-card-course">---</strong></div>
                </div>
              </div>

              <!-- Payment Package Selection -->
              <div class="space-y-1">
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300" data-i18n="pos_package_label">
                  Пакет уроков:
                </label>
                <div class="grid grid-cols-3 gap-2">
                  <button type="button" onclick="setPosPackage(12, 600000)" class="pos-pkg-btn p-2 rounded-lg border border-emerald-500 bg-emerald-50 dark:bg-emerald-950/40 text-left cursor-pointer">
                    <div class="font-bold text-xs text-emerald-800 dark:text-emerald-300">1 месяц (12 ур.)</div>
                    <div class="text-[11px] text-slate-500 font-mono">600 000 UZS</div>
                  </button>
                  <button type="button" onclick="setPosPackage(24, 1150000)" class="pos-pkg-btn p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-left hover:border-slate-400 cursor-pointer">
                    <div class="font-bold text-xs text-slate-800 dark:text-slate-200">2 месяца (24 ур.)</div>
                    <div class="text-[11px] text-slate-500 font-mono">1 150 000 UZS</div>
                  </button>
                  <button type="button" onclick="setPosPackage(1, 60000)" class="pos-pkg-btn p-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 text-left hover:border-slate-400 cursor-pointer">
                    <div class="font-bold text-xs text-slate-800 dark:text-slate-200">1 урок (Разовый)</div>
                    <div class="text-[11px] text-slate-500 font-mono">60,000 UZS</div>
                  </button>
                </div>
              </div>

              <!-- Payment Method Selection -->
              <div class="space-y-1">
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300" data-i18n="pos_method_label">
                  Способ оплаты:
                </label>
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
                  <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer has-[:checked]:border-emerald-500 has-[:checked]:bg-emerald-50 dark:has-[:checked]:bg-emerald-950/30">
                    <input type="radio" name="pos_method" value="Click" checked class="text-emerald-600" />
                    <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Click</span>
                  </label>
                  <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer has-[:checked]:border-emerald-500 has-[:checked]:bg-emerald-50 dark:has-[:checked]:bg-emerald-950/30">
                    <input type="radio" name="pos_method" value="Payme" class="text-emerald-600" />
                    <span class="text-xs font-bold text-slate-800 dark:text-slate-200">Payme</span>
                  </label>
                  <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer has-[:checked]:border-emerald-500 has-[:checked]:bg-emerald-50 dark:has-[:checked]:bg-emerald-950/30">
                    <input type="radio" name="pos_method" value="Наличные" class="text-emerald-600" />
                    <span class="text-xs font-bold text-slate-800 dark:text-slate-200" data-i18n="pay_cash">Наличные</span>
                  </label>
                  <label class="flex items-center gap-2 p-2 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer has-[:checked]:border-emerald-500 has-[:checked]:bg-emerald-50 dark:has-[:checked]:bg-emerald-950/30">
                    <input type="radio" name="pos_method" value="Терминал" class="text-emerald-600" />
                    <span class="text-xs font-bold text-slate-800 dark:text-slate-200" data-i18n="pay_terminal">Терминал</span>
                  </label>
                </div>
              </div>

              <!-- Amount & Lessons Count inputs -->
              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="pos_amount_label">
                    Сумма оплаты (UZS):
                  </label>
                  <input type="number" id="pos-amount-input" value="600000" class="w-full text-xs font-mono font-bold rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-3 text-slate-900 dark:text-white" />
                </div>
                <div>
                  <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="pos_lessons_add_label">
                    Добавить уроков к балансу:
                  </label>
                  <input type="number" id="pos-lessons-input" value="12" class="w-full text-xs font-mono font-bold rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-3 text-slate-900 dark:text-white" />
                </div>
              </div>

              <!-- Submit Button -->
              <button type="button" onclick="executePosPayment()" class="w-full py-3 bg-emerald-600 hover:bg-emerald-700 text-white font-black text-sm rounded-xl transition flex items-center justify-center gap-2 shadow-md cursor-pointer">
                <i data-lucide="check-circle" class="w-5 h-5"></i>
                <span data-i18n="pos_submit_btn">Провести оплату и напечатать чек</span>
              </button>
            </div>

            <!-- POS Thermal Receipt Preview (5 cols) -->
            <div class="lg:col-span-5 space-y-4">
              <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-3">
                <div class="flex items-center justify-between">
                  <h3 class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-1.5" data-i18n="receipt_preview_title">
                    <i data-lucide="receipt" class="w-4 h-4 text-emerald-600"></i>
                    Предпросмотр фискального чека
                  </h3>
                  <button type="button" onclick="printPosReceipt()" class="px-3 py-1 bg-slate-800 text-white dark:bg-slate-700 hover:bg-slate-900 rounded-lg text-xs font-bold transition flex items-center gap-1 cursor-pointer">
                    <i data-lucide="printer" class="w-3.5 h-3.5"></i>
                    <span>Печать чека</span>
                  </button>
                </div>

                <!-- Thermal Receipt Mockup -->
                <div id="pos-receipt-box" class="p-4 bg-slate-50 dark:bg-slate-800 rounded-lg border border-slate-200 dark:border-slate-700 font-mono text-[11px] leading-relaxed text-slate-800 dark:text-slate-200">
                  <!-- Rendered by renderPosReceipt() -->
                </div>
              </div>

              <!-- Recent Payments History -->
              <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-3">
                <h3 class="text-sm font-bold text-slate-900 dark:text-white flex items-center justify-between">
                  <span data-i18n="pos_history_title">История последних платежей</span>
                  <span class="text-[10px] text-slate-400" id="pos-history-count">0 операций</span>
                </h3>
                <div class="max-h-56 overflow-y-auto space-y-2" id="pos-history-list">
                  <!-- Populated by JS -->
                </div>
              </div>
            </div>
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB 6: 📚 ЭЛЕКТРОННЫЙ ЖУРНАЛ 18 ГРУПП -->
        <!-- ============================================================== -->
        <section id="module-journal" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="book-open" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="journal_heading">6. Электронный журнал 18 групп</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="journal_subheading">
                18 групп (по 3 группы у каждого из 6 учителей). Отметка посещаемости с автосписанием 1 урока с баланса.
              </p>
            </div>
            <div class="flex items-center gap-2">
              <!-- Date Selector -->
              <div class="flex items-center gap-1.5 text-xs bg-white dark:bg-slate-900 px-3 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700">
                <i data-lucide="calendar" class="w-3.5 h-3.5 text-emerald-600"></i>
                <input type="date" id="journal-date-input" onchange="onJournalDateChange(this.value)" class="bg-transparent font-mono font-bold text-slate-800 dark:text-slate-100 outline-none cursor-pointer" />
              </div>
            </div>
          </div>

          <!-- Filter & Group Selection -->
          <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-3">
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
              <!-- Teacher Filter -->
              <div>
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="journal_filter_teacher">
                  Преподаватель:
                </label>
                <select id="journal-teacher-select" onchange="onJournalTeacherChange(this.value)" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-3 cursor-pointer">
                  <!-- populated by JS -->
                </select>
              </div>

              <!-- Group Select (18 groups) -->
              <div>
                <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300 mb-1" data-i18n="journal_filter_group">
                  Группа (из 18 активных):
                </label>
                <select id="journal-group-select" onchange="onJournalGroupChange(this.value)" class="w-full text-xs font-bold rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-3 text-emerald-700 dark:text-emerald-400 cursor-pointer">
                  <!-- populated by JS -->
                </select>
              </div>

              <!-- Group Details Badge -->
              <div class="flex flex-col justify-center text-xs space-y-0.5 p-2 bg-slate-50 dark:bg-slate-800/60 rounded-lg border border-slate-200 dark:border-slate-700">
                <div>Расписание: <strong class="text-slate-900 dark:text-white" id="journal-group-schedule">Пн-Ср-Пт 14:00</strong></div>
                <div>Кабинет: <strong class="text-slate-900 dark:text-white" id="journal-group-room">Ауд. 204</strong> • Стоимость: <strong class="text-slate-900 dark:text-white font-mono" id="journal-group-fee">600,000 UZS</strong></div>
              </div>
            </div>
          </div>

          <!-- Attendance Roster Table -->
          <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-3">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-sm font-bold text-slate-900 dark:text-white flex items-center gap-2">
                  <span id="journal-roster-title">Список студентов группы</span>
                  <span class="text-xs px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-mono font-bold" id="journal-roster-count">0 студентов</span>
                </h3>
                <p class="text-[11px] text-slate-500" data-i18n="journal_rule_note">
                  Правило: При статусе "Был" или "НБ" автоматически списывается 1 урок с баланса.
                </p>
              </div>
              <div class="flex items-center gap-2">
                <button type="button" onclick="markAllPresent()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition flex items-center gap-1 cursor-pointer">
                  <i data-lucide="check" class="w-3.5 h-3.5"></i>
                  <span data-i18n="journal_mark_all_present">Отметить всех "Был"</span>
                </button>
              </div>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                    <th class="py-2.5 px-3 font-semibold" data-i18n="jrn_th_id">ID</th>
                    <th class="py-2.5 px-3 font-semibold" data-i18n="jrn_th_name">Студент (ФИО)</th>
                    <th class="py-2.5 px-3 font-semibold" data-i18n="jrn_th_phone">Телефон</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="jrn_th_balance">Остаток баланса</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="jrn_th_attendance">Отметка за сегодня</th>
                    <th class="py-2.5 px-3 font-semibold text-center" data-i18n="jrn_th_action">Действие / Списание</th>
                  </tr>
                </thead>
                <tbody id="journal-students-table-body" class="divide-y divide-slate-100 dark:divide-slate-800">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </section>

        <!-- ============================================================== -->
        <!-- TAB 7: ⚙️ БЭКАП И НАСТРОЙКИ DBN -->
        <!-- ============================================================== -->
        <section id="module-backup" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="database" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="backup_heading">7. Бэкап и Настройки Базы Данных (DBN)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="backup_subheading">
                Автономная база данных в LocalStorage с функцией полного резервного копирования (Экспорт / Импорт JSON).
              </p>
            </div>
          </div>

          <!-- Database Storage Stats -->
          <div class="grid grid-cols-1 sm:grid-cols-4 gap-4">
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span class="text-xs text-slate-500" data-i18n="db_stat_students">Записей студентов</span>
              <div class="text-xl font-black font-mono text-slate-900 dark:text-white" id="db-stat-students-count">0</div>
            </div>
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span class="text-xs text-slate-500" data-i18n="db_stat_groups">Записей групп</span>
              <div class="text-xl font-black font-mono text-slate-900 dark:text-white" id="db-stat-groups-count">18</div>
            </div>
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span class="text-xs text-slate-500" data-i18n="db_stat_payments">Транзакций оплаты</span>
              <div class="text-xl font-black font-mono text-slate-900 dark:text-white" id="db-stat-payments-count">0</div>
            </div>
            <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
              <span class="text-xs text-slate-500" data-i18n="db_stat_attendance">Журнальных отметок</span>
              <div class="text-xl font-black font-mono text-slate-900 dark:text-white" id="db-stat-attendance-count">0</div>
            </div>
          </div>

          <!-- Backup & Restore Action Cards -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Export Card -->
            <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-4">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-emerald-100 dark:bg-emerald-950/60 text-emerald-600 flex items-center justify-center">
                  <i data-lucide="download" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="backup_export_title">Экспорт базы данных (JSON)</h3>
                  <p class="text-xs text-slate-500" data-i18n="backup_export_desc">Скачать полный дамп LocalStorage со студентами, группами, платежами, расходами и журналом.</p>
                </div>
              </div>
              <button type="button" onclick="exportDatabaseJSON()" class="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-2 cursor-pointer">
                <i data-lucide="file-json" class="w-4 h-4"></i>
                <span data-i18n="backup_btn_export">Выгрузить файл mam_crm_backup.json</span>
              </button>
            </div>

            <!-- Import Card -->
            <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-4">
              <div class="flex items-center gap-3">
                <div class="w-10 h-10 rounded-xl bg-blue-100 dark:bg-blue-950/60 text-blue-600 flex items-center justify-center">
                  <i data-lucide="upload" class="w-5 h-5"></i>
                </div>
                <div>
                  <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="backup_import_title">Импорт базы данных из JSON</h3>
                  <p class="text-xs text-slate-500" data-i18n="backup_import_desc">Восстановить базу данных из ранее сохранённого файла резервной копии.</p>
                </div>
              </div>
              <div class="flex items-center gap-2">
                <input type="file" id="db-import-file-input" accept=".json" class="hidden" onchange="importDatabaseJSON(event)" />
                <button type="button" onclick="document.getElementById('db-import-file-input').click()" class="w-full py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-2 cursor-pointer">
                  <i data-lucide="folder-up" class="w-4 h-4"></i>
                  <span data-i18n="backup_btn_import">Выбрать JSON-файл и восстановить</span>
                </button>
              </div>
            </div>
          </div>

          <!-- Factory Reset Danger Zone -->
          <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-rose-200 dark:border-rose-950/80 space-y-3">
            <div class="flex items-center justify-between">
              <div>
                <h3 class="text-sm font-bold text-rose-600 dark:text-rose-400" data-i18n="backup_reset_title">Сброс к эталонным демонстрационным данным (18 групп)</h3>
                <p class="text-xs text-slate-500" data-i18n="backup_reset_desc">Очистит пользовательские правки и восстановит 54 студента, 18 групп и 9 аккаунтов MAM Маргилан.</p>
              </div>
              <button type="button" onclick="resetDatabaseToFactory()" class="px-4 py-2 bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs rounded-lg transition flex items-center gap-1.5 cursor-pointer">
                <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                <span data-i18n="backup_btn_reset">Сбросить базу к эталону</span>
              </button>
            </div>
          </div>
        </section>

      </main>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- MODAL: TELEGRAM REMINDER SCRIPT GENERATOR -->
  <!-- ============================================================== -->
  <div id="telegram-modal" class="hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 max-w-lg w-full p-5 space-y-4 shadow-2xl">
      <div class="flex items-center justify-between pb-3 border-b border-slate-200 dark:border-slate-800">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-blue-500 text-white flex items-center justify-center">
            <i data-lucide="send" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-bold text-slate-900 dark:text-white">Скрипт напоминания в Telegram</h3>
            <p class="text-[11px] text-slate-500">Автоматически подставлены реквизиты и баланс</p>
          </div>
        </div>
        <button type="button" onclick="closeTelegramModal()" class="text-slate-400 hover:text-slate-600 text-lg font-bold cursor-pointer">&times;</button>
      </div>

      <div class="space-y-2">
        <label class="block text-xs font-semibold text-slate-600 dark:text-slate-300">
          Текст сообщения для отправки родителю:
        </label>
        <textarea id="telegram-script-text" rows="8" class="w-full text-xs font-mono p-3 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-800 dark:text-slate-200 leading-relaxed outline-none"></textarea>
      </div>

      <div class="flex items-center justify-between gap-3 pt-2">
        <button type="button" onclick="copyTelegramScript()" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
          <i data-lucide="copy" class="w-4 h-4"></i>
          <span id="tg-copy-btn-text">Копировать в буфер</span>
        </button>
        <button type="button" onclick="openDirectTelegram()" class="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
          <i data-lucide="external-link" class="w-4 h-4"></i>
          <span>Открыть Telegram</span>
        </button>
      </div>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- JAVASCRIPT: LOGIC, LOGIN AUTH, EXECUTIVE CENTER & DATABASE ENGINE -->
  <!-- ============================================================== -->
  <script>
    /* ==============================================================
       1. DICTIONARIES & LOCALIZATION (UZ / RU)
       ============================================================== */
    let currentLang = localStorage.getItem('mam_lang') || 'ru';

    const I18N = {
      ru: {
        auth_welcome: 'Служебный вход для сотрудников',
        auth_subtitle: 'Введите персональный логин и пароль одного из 9 служебных аккаунтов.',
        auth_login_label: 'Логин аккаунта:',
        auth_pass_label: 'Пароль доступа:',
        auth_btn_submit: 'Войти в панель CRM',
        nav_roles_section: 'Аккаунт / Роль (9)',
        nav_modules_title: 'Модули системы',
        box_students: 'Студентов в базе:',
        box_groups: 'Активных групп:',
        box_risks: 'В зоне риска:',
        top_logout: 'Выйти',
        btn_logout: 'Завершить сессию',
        dir_title: 'Стратегическое управление и аудит Академии MAM',
        dir_subtitle: '360° P&L, загрузка аудиторий, ФОТ и удержание преподавателей, операционные расходы, CAC каналов и журнал аудита.',
        roles_heading: '1. Панель и вход для 9 Служебных Аккаунтов',
        roles_subheading: 'Изолированные профили сотрудников Академии MAM. Смена активной роли моментально обновляет доступ к разделам.',
        roles_active_label: 'Текущий профиль:',
        risk_heading: '3. Риски и Alerts (Early-Warning System & Smart Follow-up)',
        risk_subheading: 'Автоматический фильтр студентов с риском отчисления (осталось ≤ 1 урока или 3 пропуска подряд).',
        btn_refresh: 'Обновить список',
        risk_low_balance: 'Остаток уроков ≤ 1',
        risk_absences: '3+ пропуска подряд',
        risk_expected_renewal: 'Ожидаемая пролонгация',
        risk_list_title: 'Реестр студентов в группе риска',
        risk_quick_tip: 'Нажмите кнопку Telegram, чтобы сгенерировать готовое персональное сообщение для родителя',
        risk_th_student: 'Студент',
        risk_th_group: 'Группа / Курс',
        risk_th_balance: 'Остаток уроков',
        risk_th_absences: 'Пропусков',
        risk_th_parent: 'Родитель / Телефон',
        risk_th_status: 'Причина риска',
        risk_th_action: 'Telegram напоминание',
        doc_heading: '4. Генератор A4-Договоров и Сертификатов (Печать в 1 клик)',
        doc_subheading: 'Официальный двуязычный Договор (UZ/RU) и Сертификат выпускника с QR-кодом и подписью Директора Богданова Т.Я.',
        doc_btn_print: 'Печать на A4 (1 клик)',
        doc_select_type: 'Тип документа:',
        doc_select_student: 'Выберите студента:',
        doc_cert_grade: 'Итоговый балл / Квалификация:',
        pos_heading: '5. POS-Касса и Оплата Уроков',
        pos_subheading: 'Приём оплат: Click, Payme, Наличные, Терминал. Пополнение баланса занятий и печать фискального чека.',
        pos_cashier_label: 'Кассир смены:',
        pos_new_payment_title: 'Проведение новой оплаты',
        pos_search_label: 'Поиск студента (по телефону +998... или ФИО):',
        pos_package_label: 'Пакет уроков:',
        pos_method_label: 'Способ оплаты:',
        pay_cash: 'Наличные',
        pay_terminal: 'Терминал',
        pos_amount_label: 'Сумма оплаты (UZS):',
        pos_lessons_add_label: 'Добавить уроков к балансу:',
        pos_submit_btn: 'Провести оплату и напечатать чек',
        receipt_preview_title: 'Предпросмотр фискального чека',
        pos_history_title: 'История последних платежей',
        journal_heading: '6. Электронный журнал 18 групп',
        journal_subheading: '18 групп (по 3 группы у каждого из 6 учителей). Отметка посещаемости с автосписанием 1 урока с баланса.',
        journal_filter_teacher: 'Преподаватель:',
        journal_filter_group: 'Группа (из 18 активных):',
        journal_rule_note: 'Правило: При статусе "Был" или "НБ" автоматически списывается 1 урок с баланса.',
        journal_mark_all_present: 'Отметить всех "Был"',
        jrn_th_id: 'ID',
        jrn_th_name: 'Студент (ФИО)',
        jrn_th_phone: 'Телефон',
        jrn_th_balance: 'Остаток баланса',
        jrn_th_attendance: 'Отметка за сегодня',
        jrn_th_action: 'Действие / Списание',
        backup_heading: '7. Бэкап и Настройки Базы Данных (DBN)',
        backup_subheading: 'Автономная база данных в LocalStorage с функцией полного резервного копирования (Экспорт / Импорт JSON).',
        db_stat_students: 'Записей студентов',
        db_stat_groups: 'Записей групп',
        db_stat_payments: 'Транзакций оплаты',
        db_stat_attendance: 'Журнальных отметок',
        backup_export_title: 'Экспорт базы данных (JSON)',
        backup_export_desc: 'Скачать полный дамп LocalStorage со студентами, группами, платежами и журналом.',
        backup_btn_export: 'Выгрузить файл mam_crm_backup.json',
        backup_import_title: 'Импорт базы данных из JSON',
        backup_import_desc: 'Восстановить базу данных из ранее сохранённого файла резервной копии.',
        backup_btn_import: 'Выбрать JSON-файл и восстановить',
        backup_reset_title: 'Сброс к эталонным демонстрационным данным (18 групп)',
        backup_reset_desc: 'Очистит пользовательские правки и восстановит 54 студента, 18 групп и 9 аккаунтов MAM Маргилан.',
        backup_btn_reset: 'Сбросить базу к эталону'
      },
      uz: {
        auth_welcome: 'Xodimlar uchun xizmat kirishi',
        auth_subtitle: '9 ta xizmat hisoblaridan birining shaxsiy login va parolini kiriting.',
        auth_login_label: 'Hisob logini:',
        auth_pass_label: 'Kirish paroli:',
        auth_btn_submit: 'CRM tizimiga kirish',
        nav_roles_section: 'Hisob / Rol (9)',
        nav_modules_title: 'Tizim modullari',
        box_students: 'Talabalar soni:',
        box_groups: 'Faol guruhlar:',
        box_risks: 'Xavf guruhida:',
        top_logout: 'Chiqish',
        btn_logout: 'Sessiyani yakunlash',
        dir_title: 'MAM Akademiyasi Strategik boshqaruvi va Auditi',
        dir_subtitle: '360° P&L, xonalar bandligi, oʻqituvchilar FOT va retention, xarajatlar, CAC va audit jurnali.',
        roles_heading: '1. 9 ta Xizmat hisobi va Kirish paneli',
        roles_subheading: 'MAM Akademiyasi xodimlarining profillari. Rolni oʻzgartirish ruxsat etilgan modullarni darhol yangilaydi.',
        roles_active_label: 'Joriy profil:',
        risk_heading: '3. Xavflar va Alerts (Early-Warning & Smart Follow-up)',
        risk_subheading: 'Oʻqishdan chetlatilish xavfi bor talabalar (balans ≤ 1 dars yoki ketma-ket 3 ta qoldirish).',
        btn_refresh: 'Roʻyxatni yangilash',
        risk_low_balance: 'Darslar qoldigʻi ≤ 1',
        risk_absences: 'Ketma-ket 3+ qoldirish',
        risk_expected_renewal: 'Kutilayotgan toʻlov',
        risk_list_title: 'Xavf guruhidagi talabalar reyestri',
        risk_quick_tip: 'Ota-onaga Telegram orqali shaxsiy xabar yaratish uchun Telegram tugmasini bosing',
        risk_th_student: 'Talaba',
        risk_th_group: 'Guruh / Kurs',
        risk_th_balance: 'Darslar qoldigʻi',
        risk_th_absences: 'Qoldirishlar',
        risk_th_parent: 'Ota-ona / Tel',
        risk_th_status: 'Xavf sababi',
        risk_th_action: 'Telegram eslatma',
        doc_heading: '4. A4-Shartnoma va Sertifikatlar generatori (1-bosishda chop etish)',
        doc_subheading: 'Ikki tilli Shartnoma (UZ/RU) va QR-kodli bitiruvchi Sertifikati hamda Direktor Bogdanov T.Y. imzosi.',
        doc_btn_print: 'A4-da chop etish (1-bosishda)',
        doc_select_type: 'Hujjat turi:',
        doc_select_student: 'Talabani tanlang:',
        doc_cert_grade: 'Yakuniy ball / Malaka:',
        pos_heading: '5. POS Kassa va Darslar Toʻlovi',
        pos_subheading: 'Toʻlov turlari: Click, Payme, Naqd pul, Terminal. Dars balansini toʻldirish va fiskal chek.',
        pos_cashier_label: 'Smena kassiri:',
        pos_new_payment_title: 'Yangi toʻlovni qabul qilish',
        pos_search_label: 'Talabani qidirish (+998... tel yoki FIO boʻyicha):',
        pos_package_label: 'Darslar paketi:',
        pos_method_label: 'Toʻlov usuli:',
        pay_cash: 'Naqd pul',
        pay_terminal: 'Terminal',
        pos_amount_label: 'Toʻlov summasi (UZS):',
        pos_lessons_add_label: 'Balansga dars qoʻshish:',
        pos_submit_btn: 'Toʻlovni oʻtkazish va chek chiqarish',
        receipt_preview_title: 'Fiskal chek koʻrinishi',
        pos_history_title: 'Oxirgi toʻlovlar tarixi',
        journal_heading: '6. 18 guruh elektron jurnali',
        journal_subheading: '18 ta guruh (6 oʻqituvchining har birida 3 tadan). Davomat belgilash va 1 darsni avtomatik yechib olish.',
        journal_filter_teacher: 'Oʻqituvchi:',
        journal_filter_group: 'Guruh (18 ta faol):',
        journal_rule_note: 'Qoida: "Bor" yoki "Yoʻq" holatida avtomatik ravishda balansdan 1 dars yechiladi.',
        journal_mark_all_present: 'Barchasini "Bor" qilish',
        jrn_th_id: 'ID',
        jrn_th_name: 'Talaba (F.I.O)',
        jrn_th_phone: 'Telefon',
        jrn_th_balance: 'Balans qoldigʻi',
        jrn_th_attendance: 'Bugungi davomat',
        jrn_th_action: 'Amal / Yechish',
        backup_heading: '7. MB Zaxira va Sozlamalar (DBN)',
        backup_subheading: 'LocalStorage-da avtonom maʼlumotlar bazasi va toʻliq zaxira nusxalash (Eksport / Import JSON).',
        db_stat_students: 'Talabalar yozuvi',
        db_stat_groups: 'Guruhlar yozuvi',
        db_stat_payments: 'Toʻlov tranzaksiyalari',
        db_stat_attendance: 'Jurnal belgilari',
        backup_export_title: 'Maʼlumotlar bazasini eksport qilish (JSON)',
        backup_export_desc: 'Talabalar, guruhlar, toʻlovlar va jurnalning toʻliq faylini yuklab olish.',
        backup_btn_export: 'mam_crm_backup.json faylini yuklash',
        backup_import_title: 'JSON fayldan bazani tiklash',
        backup_import_desc: 'Avval saqlangan zaxira nusxadan maʼlumotlarni qayta tiklash.',
        backup_btn_import: 'JSON faylni tanlash va tiklash',
        backup_reset_title: 'Dastlabki namunaviy bazaga qaytarish (18 guruh)',
        backup_reset_desc: 'Barcha oʻzgarishlarni tozalab, 54 talaba, 18 guruh va 9 hisobni tiklaydi.',
        backup_btn_reset: 'Bazani tiklash'
      }
    };

    /* ==============================================================
       2. ACCOUNTS & ROLES (9 PROFILES WITH LOGINS & PASSWORDS)
       ============================================================== */
    const ROLES_DATA = {
      director: {
        key: 'director',
        login: 'director',
        pass: 'admin123',
        name: 'Богданов Тимур Яковлевич',
        shortName: 'Богданов Т.Я.',
        roleName: 'Директор',
        roleNameUz: 'Bosh direktor',
        avatar: '👑',
        badgeColor: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300',
        allowedModules: ['director', 'roles', 'risks', 'contracts', 'pos', 'journal', 'backup'],
        desc: 'Полный доступ: Executive Command Center, P&L, CAC, загрузка аудиторий, зарплаты, договоры.'
      },
      sysadmin: {
        key: 'sysadmin',
        login: 'sysadmin',
        pass: 'sys123',
        name: 'Умаров Алишер Рустамович',
        shortName: 'Умаров А.Р.',
        roleName: 'Системный Администратор',
        roleNameUz: 'Tizim administratori',
        avatar: '🛡️',
        badgeColor: 'bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300',
        allowedModules: ['director', 'roles', 'risks', 'contracts', 'pos', 'journal', 'backup'],
        desc: 'Управление безопасностью, структурой БД, бэкапами и техническим аудитом системы.'
      },
      cashier: {
        key: 'cashier',
        login: 'cashier',
        pass: 'cash123',
        name: 'Рахимова Нигора Олимовна',
        shortName: 'Рахимова Н.О.',
        roleName: 'Главный Кассир / Ресепшен',
        roleNameUz: 'Bosh kassir / Resepshn',
        avatar: '💳',
        badgeColor: 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300',
        allowedModules: ['pos', 'risks', 'contracts', 'journal', 'backup'],
        desc: 'Проведение оплат (Click, Payme, Наличные), печать чеков, мониторинг должников и договоров.'
      },
      teacher_python: {
        key: 'teacher_python',
        login: 'teacher_python',
        pass: 'teacher123',
        name: 'Алимов Сардор Бахтиёрович',
        shortName: 'Алимов С.Б.',
        roleName: 'Преподаватель Python',
        roleNameUz: 'Python oʻqituvchisi',
        avatar: '🐍',
        course: 'Python & Backend',
        groups: ['PY-101', 'PY-102', 'PY-103'],
        badgeColor: 'bg-indigo-100 text-indigo-800 dark:bg-indigo-950 dark:text-indigo-300',
        allowedModules: ['journal', 'risks'],
        desc: 'Курирует группы PY-101, PY-102, PY-103. Отметка посещаемости и контроль успеваемости.'
      },
      teacher_web: {
        key: 'teacher_web',
        login: 'teacher_web',
        pass: 'teacher123',
        name: 'Юлдашев Даврон Акмалович',
        shortName: 'Юлдашев Д.А.',
        roleName: 'Преподаватель Web Dev',
        roleNameUz: 'Web dasturlash oʻqituvchisi',
        avatar: '🌐',
        course: 'Frontend & Web Dev',
        groups: ['WEB-201', 'WEB-202', 'WEB-203'],
        badgeColor: 'bg-cyan-100 text-cyan-800 dark:bg-cyan-950 dark:text-cyan-300',
        allowedModules: ['journal', 'risks'],
        desc: 'Курирует группы WEB-201, WEB-202, WEB-203. Ведение журналов и контроль списания уроков.'
      },
      teacher_design: {
        key: 'teacher_design',
        login: 'teacher_design',
        pass: 'teacher123',
        name: 'Каримова Мадина Шухратовна',
        shortName: 'Каримова М.Ш.',
        roleName: 'Преподаватель UI/UX',
        roleNameUz: 'UI/UX Dizayn oʻqituvchisi',
        avatar: '🎨',
        course: 'UI/UX & Graphic Design',
        groups: ['DS-301', 'DS-302', 'DS-303'],
        badgeColor: 'bg-fuchsia-100 text-fuchsia-800 dark:bg-fuchsia-950 dark:text-fuchsia-300',
        allowedModules: ['journal', 'risks'],
        desc: 'Курирует группы DS-301, DS-302, DS-303. Учёт посещаемости и практических проектов.'
      },
      teacher_english: {
        key: 'teacher_english',
        login: 'teacher_english',
        pass: 'teacher123',
        name: 'Смирнова Елена Викторовна',
        shortName: 'Смирнова Е.В.',
        roleName: 'Преподаватель English',
        roleNameUz: 'Ingliz tili / IELTS',
        avatar: '🇬🇧',
        course: 'General & IELTS English',
        groups: ['ENG-401', 'ENG-402', 'ENG-403'],
        badgeColor: 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300',
        allowedModules: ['journal', 'risks'],
        desc: 'Курирует группы ENG-401, ENG-402, ENG-403. Отметка посещаемости и подготовка к IELTS.'
      },
      teacher_korean: {
        key: 'teacher_korean',
        login: 'teacher_korean',
        pass: 'teacher123',
        name: 'Пак Антонина Сергеевна',
        shortName: 'Пак А.С.',
        roleName: 'Преподаватель Korean',
        roleNameUz: 'Koreys tili / TOPIK',
        avatar: '🇰🇷',
        course: 'Korean & TOPIK',
        groups: ['KOR-501', 'KOR-502', 'KOR-503'],
        badgeColor: 'bg-teal-100 text-teal-800 dark:bg-teal-950 dark:text-teal-300',
        allowedModules: ['journal', 'risks'],
        desc: 'Курирует группы KOR-501, KOR-502, KOR-503. Журнал групп корейского языка и TOPIK.'
      },
      teacher_german: {
        key: 'teacher_german',
        login: 'teacher_german',
        pass: 'teacher123',
        name: 'Мюллер Кристина Андреевна',
        shortName: 'Мюллер К.А.',
        roleName: 'Преподаватель German',
        roleNameUz: 'Nemis tili / Goethe',
        avatar: '🇩🇪',
        course: 'Deutsch A1-B2',
        groups: ['GER-601', 'GER-602', 'GER-603'],
        badgeColor: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-950 dark:text-yellow-300',
        allowedModules: ['journal', 'risks'],
        desc: 'Курирует группы GER-601, GER-602, GER-603. Журнал групп немецкого языка и экзамены.'
      }
    };

    let currentUser = null;
    let currentModule = 'director';

    /* ==============================================================
       3. SEED DATABASE (18 GROUPS, 54 STUDENTS, EXPENSES, AUDIT LOG)
       ============================================================== */
    function generateInitialDB() {
      const groups = [
        // Python
        { id: 'PY-101', name: 'Python Basics 101', teacherKey: 'teacher_python', teacherName: 'Алимов С.Б.', course: 'Python & Backend', schedule: 'Пн-Ср-Пт 14:00-16:00', room: 'Ауд. 201', fee: 600000, lessonsPerMonth: 12, conductedLessons: 18 },
        { id: 'PY-102', name: 'Django & API 102', teacherKey: 'teacher_python', teacherName: 'Алимов С.Б.', course: 'Python & Backend', schedule: 'Вт-Чт-Сб 14:00-16:00', room: 'Ауд. 201', fee: 650000, lessonsPerMonth: 12, conductedLessons: 20 },
        { id: 'PY-103', name: 'Telegram Bots & Async 103', teacherKey: 'teacher_python', teacherName: 'Алимов С.Б.', course: 'Python & Backend', schedule: 'Пн-Ср-Пт 16:30-18:30', room: 'Ауд. 201', fee: 650000, lessonsPerMonth: 12, conductedLessons: 19 },
        // Web
        { id: 'WEB-201', name: 'HTML5 & CSS Modern 201', teacherKey: 'teacher_web', teacherName: 'Юлдашев Д.А.', course: 'Frontend & Web Dev', schedule: 'Пн-Ср-Пт 10:00-12:00', room: 'Ауд. 202', fee: 550000, lessonsPerMonth: 12, conductedLessons: 22 },
        { id: 'WEB-202', name: 'JavaScript & React 202', teacherKey: 'teacher_web', teacherName: 'Юлдашев Д.А.', course: 'Frontend & Web Dev', schedule: 'Вт-Чт-Сб 10:00-12:00', room: 'Ауд. 202', fee: 650000, lessonsPerMonth: 12, conductedLessons: 21 },
        { id: 'WEB-203', name: 'Fullstack Next.js 203', teacherKey: 'teacher_web', teacherName: 'Юлдашев Д.А.', course: 'Frontend & Web Dev', schedule: 'Вт-Чт-Сб 16:30-18:30', room: 'Ауд. 202', fee: 700000, lessonsPerMonth: 12, conductedLessons: 20 },
        // Design
        { id: 'DS-301', name: 'Figma UI Foundations 301', teacherKey: 'teacher_design', teacherName: 'Каримова М.Ш.', course: 'UI/UX & Graphic Design', schedule: 'Пн-Ср-Пт 09:00-11:00', room: 'Ауд. 203', fee: 550000, lessonsPerMonth: 12, conductedLessons: 19 },
        { id: 'DS-302', name: 'UX Research & Mobile 302', teacherKey: 'teacher_design', teacherName: 'Каримова М.Ш.', course: 'UI/UX & Graphic Design', schedule: 'Вт-Чт-Сб 09:00-11:00', room: 'Ауд. 203', fee: 600000, lessonsPerMonth: 12, conductedLessons: 21 },
        { id: 'DS-303', name: 'Brand Identity & Visuals 303', teacherKey: 'teacher_design', teacherName: 'Каримова М.Ш.', course: 'UI/UX & Graphic Design', schedule: 'Пн-Ср-Пт 14:00-16:00', room: 'Ауд. 203', fee: 600000, lessonsPerMonth: 12, conductedLessons: 20 },
        // English
        { id: 'ENG-401', name: 'Pre-Intermediate English 401', teacherKey: 'teacher_english', teacherName: 'Смирнова Е.В.', course: 'General & IELTS English', schedule: 'Пн-Ср-Пт 11:30-13:30', room: 'Ауд. 101', fee: 500000, lessonsPerMonth: 12, conductedLessons: 23 },
        { id: 'ENG-402', name: 'Intermediate Fluency 402', teacherKey: 'teacher_english', teacherName: 'Смирнова Е.В.', course: 'General & IELTS English', schedule: 'Вт-Чт-Сб 11:30-13:30', room: 'Ауд. 101', fee: 550000, lessonsPerMonth: 12, conductedLessons: 22 },
        { id: 'ENG-403', name: 'IELTS Intensive 7.5+ 403', teacherKey: 'teacher_english', teacherName: 'Смирнова Е.В.', course: 'General & IELTS English', schedule: 'Пн-Ср-Пт 16:30-18:30', room: 'Ауд. 101', fee: 650000, lessonsPerMonth: 12, conductedLessons: 24 },
        // Korean
        { id: 'KOR-501', name: 'Hangul & Basic Grammar 501', teacherKey: 'teacher_korean', teacherName: 'Пак А.С.', course: 'Korean & TOPIK', schedule: 'Пн-Ср-Пт 10:00-12:00', room: 'Ауд. 102', fee: 550000, lessonsPerMonth: 12, conductedLessons: 18 },
        { id: 'KOR-502', name: 'EPS-TOPIK Level 1 502', teacherKey: 'teacher_korean', teacherName: 'Пак А.С.', course: 'Korean & TOPIK', schedule: 'Вт-Чт-Сб 10:00-12:00', room: 'Ауд. 102', fee: 600000, lessonsPerMonth: 12, conductedLessons: 20 },
        { id: 'KOR-503', name: 'TOPIK II Academic 503', teacherKey: 'teacher_korean', teacherName: 'Пак А.С.', course: 'Korean & TOPIK', schedule: 'Вт-Чт-Сб 14:00-16:00', room: 'Ауд. 102', fee: 650000, lessonsPerMonth: 12, conductedLessons: 21 },
        // German
        { id: 'GER-601', name: 'Start Deutsch A1 601', teacherKey: 'teacher_german', teacherName: 'Мюллер К.А.', course: 'Deutsch A1-B2', schedule: 'Пн-Ср-Пт 14:00-16:00', room: 'Ауд. 103', fee: 550000, lessonsPerMonth: 12, conductedLessons: 19 },
        { id: 'GER-602', name: 'Deutsch A2.2 Aufbaustufe 602', teacherKey: 'teacher_german', teacherName: 'Мюллер К.А.', course: 'Deutsch A1-B2', schedule: 'Вт-Чт-Сб 14:00-16:00', room: 'Ауд. 103', fee: 600000, lessonsPerMonth: 12, conductedLessons: 20 },
        { id: 'GER-603', name: 'Goethe-Zertifikat B1 603', teacherKey: 'teacher_german', teacherName: 'Мюллер К.А.', course: 'Deutsch A1-B2', schedule: 'Пн-Ср-Пт 16:30-18:30', room: 'Ауд. 103', fee: 650000, lessonsPerMonth: 12, conductedLessons: 21 }
      ];

      const rawNames = [
        // PY-101
        { name: 'Рустамов Азизбек Отабекович', parent: 'Рустамов Отабек Шухратович', phone: '+998901234567', pPhone: '+998901234500', group: 'PY-101', bal: 0, abs: 3 },
        { name: 'Хакимов Жасур Маъруфович', parent: 'Хакимов Маъруф Хамидович', phone: '+998912345678', pPhone: '+998912345600', group: 'PY-101', bal: 9, abs: 0 },
        { name: 'Касымова Дилноза Анваровна', parent: 'Касымов Анвар Илхомович', phone: '+998933456789', pPhone: '+998933456700', group: 'PY-101', bal: 7, abs: 1 },
        // PY-102
        { name: 'Усмонов Сардор Равшанович', parent: 'Усмонов Равшан Собирович', phone: '+998944567890', pPhone: '+998944567800', group: 'PY-102', bal: 1, abs: 0 },
        { name: 'Махмудов Бобур Шавкатович', parent: 'Махмудов Шавкат Акрамович', phone: '+998955678901', pPhone: '+998955678900', group: 'PY-102', bal: 11, abs: 0 },
        { name: 'Турсунова Севара Баходировна', parent: 'Турсунов Баходир Олимович', phone: '+998976789012', pPhone: '+998976789000', group: 'PY-102', bal: 8, abs: 0 },
        // PY-103
        { name: 'Юнусов Иброхим Муродович', parent: 'Юнусов Мурод Кобилович', phone: '+998987890123', pPhone: '+998987890100', group: 'PY-103', bal: 6, abs: 0 },
        { name: 'Хусанов Бехруз Зохидович', parent: 'Хусанов Зохид Фарходович', phone: '+998908901234', pPhone: '+998908901200', group: 'PY-103', bal: 0, abs: 2 },
        { name: 'Назарова Шахло Рустамовна', parent: 'Назаров Рустам Валиевич', phone: '+998919012345', pPhone: '+998919012300', group: 'PY-103', bal: 10, abs: 0 },
        // WEB-201
        { name: 'Исмоилов Мирзохид Камолович', parent: 'Исмоилов Камол Шухратович', phone: '+998930123456', pPhone: '+998930123400', group: 'WEB-201', bal: 1, abs: 3 },
        { name: 'Собиров Давлатжон Мансурович', parent: 'Собиров Мансур Азизович', phone: '+998941234567', pPhone: '+998941234500', group: 'WEB-201', bal: 10, abs: 0 },
        { name: 'Абдуллаева Гульноза Носировна', parent: 'Абдуллаев Носир Тохирович', phone: '+998952345678', pPhone: '+998952345600', group: 'WEB-201', bal: 7, abs: 0 },
        // WEB-202
        { name: 'Тохиров Мухаммадсодик Улугбекович', parent: 'Тохиров Улугбек Абдурашидович', phone: '+998973456789', pPhone: '+998973456700', group: 'WEB-202', bal: 8, abs: 0 },
        { name: 'Каримов Шохрух Бахтиёрович', parent: 'Каримов Бахтиёр Саидович', phone: '+998984567890', pPhone: '+998984567800', group: 'WEB-202', bal: 0, abs: 0 },
        { name: 'Ганиева Мохира Рустамовна', parent: 'Ганиев Рустам Баходирович', phone: '+998905678901', pPhone: '+998905678900', group: 'WEB-202', bal: 12, abs: 0 },
        // WEB-203
        { name: 'Салимов Дониёр Фаррухович', parent: 'Салимов Фаррух Бахромович', phone: '+998916789012', pPhone: '+998916789000', group: 'WEB-203', bal: 6, abs: 0 },
        { name: 'Олимов Сухроб Акрамович', parent: 'Олимов Акрам Иброхимович', phone: '+998937890123', pPhone: '+998937890100', group: 'WEB-203', bal: 11, abs: 0 },
        { name: 'Жураева Нилуфар Музаффаровна', parent: 'Жураев Музаффар Нодирович', phone: '+998948901234', pPhone: '+998948901200', group: 'WEB-203', bal: 8, abs: 0 },
        // DS-301
        { name: 'Эргашев Асилбек Шавкатович', parent: 'Эргашев Шавкат Рахимович', phone: '+998959012345', pPhone: '+998959012300', group: 'DS-301', bal: 1, abs: 1 },
        { name: 'Норматова Шахзода Улугбековна', parent: 'Норматов Улугбек Шухратович', phone: '+998970123456', pPhone: '+998970123400', group: 'DS-301', bal: 9, abs: 0 },
        { name: 'Фозилов Билол Мухторович', parent: 'Фозилов Мухтор Хакимович', phone: '+998981234567', pPhone: '+998981234500', group: 'DS-301', bal: 11, abs: 0 },
        // DS-302
        { name: 'Камолов Ойбек Бахтиёрович', parent: 'Камолов Бахтиёр Исомиддинович', phone: '+998902345678', pPhone: '+998902345600', group: 'DS-302', bal: 0, abs: 3 },
        { name: 'Зокирова Мадинахон Равшановна', parent: 'Зокиров Равшан Анварович', phone: '+998913456789', pPhone: '+998913456700', group: 'DS-302', bal: 8, abs: 0 },
        { name: 'Алиева Зебинисо Олимжоновна', parent: 'Алиев Олимжон Каюмович', phone: '+998934567890', pPhone: '+998934567800', group: 'DS-302', bal: 12, abs: 0 },
        // DS-303
        { name: 'Ботиров Дилшод Аскарович', parent: 'Ботиров Аскар Солихович', phone: '+998945678901', pPhone: '+998945678900', group: 'DS-303', bal: 6, abs: 0 },
        { name: 'Акрамова Райхона Фуркатовна', parent: 'Акрамов Фуркат Носирович', phone: '+998956789012', pPhone: '+998956789000', group: 'DS-303', bal: 1, abs: 0 },
        { name: 'Хамдамов Шерзод Мансурович', parent: 'Хамдамов Мансур Расулович', phone: '+998977890123', pPhone: '+998977890100', group: 'DS-303', bal: 10, abs: 0 },
        // ENG-401
        { name: 'Муродов Жавохир Зокирович', parent: 'Муродов Зокир Хамидович', phone: '+998988901234', pPhone: '+998988901200', group: 'ENG-401', bal: 8, abs: 0 },
        { name: 'Азизова Мафтуна Баходировна', parent: 'Азизов Баходир Махмудович', phone: '+998909012345', pPhone: '+998909012300', group: 'ENG-401', bal: 0, abs: 3 },
        { name: 'Султонов Жалолиддин Илхомович', parent: 'Султонов Илхом Кодирович', phone: '+998910123456', pPhone: '+998910123400', group: 'ENG-401', bal: 12, abs: 0 },
        // ENG-402
        { name: 'Валиев Темурбек Солихович', parent: 'Валиев Солих Умарович', phone: '+998931234567', pPhone: '+998931234500', group: 'ENG-402', bal: 1, abs: 0 },
        { name: 'Шарипова Зиёда Рустамовна', parent: 'Шарипов Рустам Фахриддинович', phone: '+998942345678', pPhone: '+998942345600', group: 'ENG-402', bal: 9, abs: 0 },
        { name: 'Косимов Хусанбой Муроджонович', parent: 'Косимов Муроджон Собирович', phone: '+998953456789', pPhone: '+998953456700', group: 'ENG-402', bal: 7, abs: 0 },
        // ENG-403
        { name: 'Ибрагимов Сарвар Анварович', parent: 'Ибрагимов Анвар Рахимович', phone: '+998974567890', pPhone: '+998974567800', group: 'ENG-403', bal: 11, abs: 0 },
        { name: 'Мирзаева Нодира Шухратовна', parent: 'Мирзаев Шухрат Валиевич', phone: '+998985678901', pPhone: '+998985678900', group: 'ENG-403', bal: 0, abs: 0 },
        { name: 'Расулов Фарходбек Акрамович', parent: 'Расулов Акрам Холикович', phone: '+998906789012', pPhone: '+998906789000', group: 'ENG-403', bal: 10, abs: 0 },
        // KOR-501
        { name: 'Хамидов Озодбек Собирович', parent: 'Хамидов Собир Усмонович', phone: '+998917890123', pPhone: '+998917890100', group: 'KOR-501', bal: 1, abs: 3 },
        { name: 'Абдурахимова Камола Носировна', parent: 'Абдурахимов Носир Толибович', phone: '+998938901234', pPhone: '+998938901200', group: 'KOR-501', bal: 8, abs: 0 },
        { name: 'Йулдошев Сардорбек Азизович', parent: 'Йулдошев Азиз Рахимович', phone: '+998949012345', pPhone: '+998949012300', group: 'KOR-501', bal: 10, abs: 0 },
        // KOR-502
        { name: 'Ким Станислав Робертович', parent: 'Ким Роберт Валерьевич', phone: '+998950123456', pPhone: '+998950123400', group: 'KOR-502', bal: 7, abs: 0 },
        { name: 'Цой Виктория Павловна', parent: 'Цой Павел Игоревич', phone: '+998971234567', pPhone: '+998971234500', group: 'KOR-502', bal: 12, abs: 0 },
        { name: 'Содиков Аброр Мансуржонович', parent: 'Содиков Мансуржон Равшанович', phone: '+998982345678', pPhone: '+998982345600', group: 'KOR-502', bal: 0, abs: 0 },
        // KOR-503
        { name: 'Югай Артур Олегович', parent: 'Югай Олег Вячеславович', phone: '+998903456789', pPhone: '+998903456700', group: 'KOR-503', bal: 9, abs: 0 },
        { name: 'Пак Диана Геннадьевна', parent: 'Пак Геннадий Сергеевич', phone: '+998914567890', pPhone: '+998914567800', group: 'KOR-503', bal: 1, abs: 0 },
        { name: 'Хван Денис Владимирович', parent: 'Хван Владимир Андреевич', phone: '+998935678901', pPhone: '+998935678900', group: 'KOR-503', bal: 11, abs: 0 },
        // GER-601
        { name: 'Шукуров Бекзод Шухратович', parent: 'Шукуров Шухрат Анварович', phone: '+998946789012', pPhone: '+998946789000', group: 'GER-601', bal: 8, abs: 0 },
        { name: 'Ортикова Дилрабо Хакимовна', parent: 'Ортиков Хаким Каримович', phone: '+998957890123', pPhone: '+998957890100', group: 'GER-601', bal: 0, abs: 3 },
        { name: 'Мухторов Исломбек Жалолович', parent: 'Мухторов Жалол Олимович', phone: '+998978901234', pPhone: '+998978901200', group: 'GER-601', bal: 10, abs: 0 },
        // GER-602
        { name: 'Нишонов Искандар Маъруфович', parent: 'Нишонов Маъруф Каюмович', phone: '+998989012345', pPhone: '+998989012300', group: 'GER-602', bal: 1, abs: 0 },
        { name: 'Тоштемирова Лайло Собировна', parent: 'Тоштемиров Собир Улугбекович', phone: '+998900123456', pPhone: '+998900123400', group: 'GER-602', bal: 11, abs: 0 },
        { name: 'Фарходов Шохжахон Муроджонович', parent: 'Фарходов Муроджон Анварович', phone: '+998911234567', pPhone: '+998911234500', group: 'GER-602', bal: 7, abs: 0 },
        // GER-603
        { name: 'Хамидуллаев Достонбек Валиевич', parent: 'Хамидуллаев Вали Иброхимович', phone: '+998932345678', pPhone: '+998932345600', group: 'GER-603', bal: 9, abs: 0 },
        { name: 'Каримова Гульбахор Фарруховна', parent: 'Каримов Фаррух Бахромович', phone: '+998943456789', pPhone: '+998943456700', group: 'GER-603', bal: 0, abs: 0 },
        { name: 'Абдулхамидов Азизжон Шухратович', parent: 'Абдулхамидов Шухрат Одилович', phone: '+998954567890', pPhone: '+998954567800', group: 'GER-603', bal: 12, abs: 0 }
      ];

      const students = rawNames.map((item, idx) => {
        const idNum = 1001 + idx;
        return {
          id: `MAM-${idNum}`,
          fullName: item.name,
          parentName: item.parent,
          phone: item.phone,
          parentPhone: item.pPhone,
          groupId: item.group,
          lessonsBalance: item.bal,
          consecutiveAbsences: item.abs,
          passport: `AA ${2000000 + idNum}`,
          address: `г. Маргилан, ул. Навои, д. ${10 + (idx % 40)}`,
          enrolledDate: '2026-09-01',
          contractNo: `MAM-2026/0${idx + 10}`,
          certNo: `CERT-MAM-88${idx + 10}`
        };
      });

      const payments = [
        { id: 'PAY-8841', studentId: 'MAM-1002', studentName: 'Хакимов Жасур М.', amount: 600000, lessonsAdded: 12, method: 'Click', date: '2026-10-10 11:24', cashier: 'Рахимова Н.О.' },
        { id: 'PAY-8842', studentId: 'MAM-1005', studentName: 'Махмудов Бобур Ш.', amount: 650000, lessonsAdded: 12, method: 'Payme', date: '2026-10-10 14:15', cashier: 'Рахимова Н.О.' },
        { id: 'PAY-8843', studentId: 'MAM-1011', studentName: 'Собиров Давлатжон М.', amount: 550000, lessonsAdded: 12, method: 'Наличные', date: '2026-10-11 09:40', cashier: 'Рахимова Н.О.' },
        { id: 'PAY-8844', studentId: 'MAM-1015', studentName: 'Ганиева Мохира Р.', amount: 650000, lessonsAdded: 12, method: 'Терминал', date: '2026-10-11 15:30', cashier: 'Рахимова Н.О.' }
      ];

      const attendance = {};

      // Seed Operational Expenses for Margilan
      const expenses = [
        { id: 'EXP-101', category: 'Аренда', title: 'Аренда здания (ул. Б. Маргиноний, 42)', amount: 6500000, date: '2026-10-02', approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-102', category: 'Коммуналка', title: 'Электроэнергия и отопление кампуса', amount: 1200000, date: '2026-10-05', approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-103', category: 'Интернет', title: 'Оптоволоконный канал 300 Mbps (Uztelecom)', amount: 650000, date: '2026-10-03', approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-104', category: 'Маркетинг', title: 'Таргетинг Instagram & реклама в пабликах Маргилана', amount: 2400000, date: '2026-10-06', approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-105', category: 'Хозтовары', title: 'Канцелярия, бумага A4, вода и кофе', amount: 850000, date: '2026-10-08', approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-106', category: 'Оборудование', title: 'Замена SSD и кулеров в лаборатории № 2', amount: 1600000, date: '2026-10-09', approvedBy: 'Богданов Т.Я.' }
      ];

      // Audit Log entries
      const auditLogs = [
        { id: 'LOG-301', timestamp: '2026-10-11 15:30', user: 'Рахимова Н.О.', action: 'Проведение оплаты', details: 'Студент MAM-1015, сумма 650,000 UZS, терминал', severity: 'info' },
        { id: 'LOG-302', timestamp: '2026-10-11 14:15', user: 'Алимов С.Б.', action: 'Журнал занятий', details: 'Отметка посещаемости в группе PY-101 (3 студента)', severity: 'info' },
        { id: 'LOG-303', timestamp: '2026-10-10 16:45', user: 'Богданов Т.Я.', action: 'Утверждение бюджета', details: 'Утвержден расход EXP-106 (Оборудование: 1,600,000 UZS)', severity: 'warning' },
        { id: 'LOG-304', timestamp: '2026-10-10 11:24', user: 'Рахимова Н.О.', action: 'Проведение оплаты', details: 'Студент MAM-1002, сумма 600,000 UZS, Click', severity: 'info' },
        { id: 'LOG-305', timestamp: '2026-10-09 17:00', user: 'Умаров А.Р.', action: 'Безопасность', details: 'Создание регулярной резервной копии базы данных MAM', severity: 'info' }
      ];

      return {
        groups,
        students,
        payments,
        attendance,
        expenses,
        auditLogs,
        paidSalaries: {
          teacher_python: false,
          teacher_web: false,
          teacher_design: false,
          teacher_english: false,
          teacher_korean: false,
          teacher_german: false
        }
      };
    }

    function getDB() {
      try {
        const raw = localStorage.getItem('mam_crm_db');
        if (raw) return JSON.parse(raw);
      } catch (e) {
        console.error('Failed reading DB:', e);
      }
      const initial = generateInitialDB();
      saveDB(initial);
      return initial;
    }

    function saveDB(data) {
      localStorage.setItem('mam_crm_db', JSON.stringify(data));
      updateGlobalCounters();
    }

    function logAuditAction(action, details, severity = 'info') {
      const db = getDB();
      if (!db.auditLogs) db.auditLogs = [];
      const userName = currentUser ? currentUser.shortName : 'Система';
      const nowStr = new Date().toLocaleString('ru-RU');
      db.auditLogs.unshift({
        id: `LOG-${Math.floor(100 + Math.random() * 900)}`,
        timestamp: nowStr,
        user: userName,
        action: action,
        details: details,
        severity: severity
      });
      saveDB(db);
    }

    /* ==============================================================
       4. AUTHENTICATION CONTROLLER (LOGIN / PASSWORD)
       ============================================================== */
    function checkSavedSession() {
      const savedUserKey = localStorage.getItem('mam_auth_user');
      if (savedUserKey && ROLES_DATA[savedUserKey]) {
        loginSuccess(ROLES_DATA[savedUserKey]);
        return;
      }
      showAuthScreen();
    }

    function showAuthScreen() {
      document.getElementById('view-auth').classList.remove('hidden');
      document.getElementById('view-app').classList.add('hidden');
      renderQuickAccountsCheatSheet();
      lucide.createIcons();
    }

    function renderQuickAccountsCheatSheet() {
      const container = document.getElementById('auth-quick-accounts-list');
      container.innerHTML = '';

      Object.keys(ROLES_DATA).forEach(key => {
        const acc = ROLES_DATA[key];
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.onclick = () => quickFillAuth(acc.login, acc.pass);
        btn.className = 'w-full text-left p-2 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:border-emerald-500 hover:bg-emerald-50/50 dark:hover:bg-emerald-950/30 transition flex items-center justify-between cursor-pointer group';
        btn.innerHTML = `
          <div class="flex items-center gap-2 truncate">
            <span class="text-base">${acc.avatar}</span>
            <div class="truncate">
              <div class="text-xs font-bold text-slate-800 dark:text-slate-200 group-hover:text-emerald-600 transition truncate">${acc.shortName}</div>
              <div class="text-[10px] text-slate-400 truncate">${acc.roleName}</div>
            </div>
          </div>
          <div class="text-right shrink-0">
            <div class="text-[10px] font-mono font-bold text-slate-700 dark:text-slate-300">${acc.login}</div>
            <div class="text-[9px] font-mono text-emerald-600 dark:text-emerald-400 font-bold">${acc.pass}</div>
          </div>
        `;
        container.appendChild(btn);
      });
    }

    function quickFillAuth(login, pass) {
      document.getElementById('auth-login-input').value = login;
      document.getElementById('auth-pass-input').value = pass;
      document.getElementById('auth-error-banner').classList.add('hidden');
      handleAuthSubmit(new Event('submit'));
    }

    function togglePasswordVisibility() {
      const input = document.getElementById('auth-pass-input');
      const icon = document.getElementById('auth-eye-icon');
      if (input.type === 'password') {
        input.type = 'text';
      } else {
        input.type = 'password';
      }
    }

    function handleAuthSubmit(e) {
      if (e && e.preventDefault) e.preventDefault();

      const login = (document.getElementById('auth-login-input').value || '').trim();
      const pass = (document.getElementById('auth-pass-input').value || '').trim();

      let matchedAcc = null;
      Object.keys(ROLES_DATA).forEach(k => {
        const a = ROLES_DATA[k];
        if (a.login.toLowerCase() === login.toLowerCase() && a.pass === pass) {
          matchedAcc = a;
        }
      });

      if (matchedAcc) {
        document.getElementById('auth-error-banner').classList.add('hidden');
        loginSuccess(matchedAcc);
      } else {
        document.getElementById('auth-error-banner').classList.remove('hidden');
        document.getElementById('auth-error-text').textContent = 'Неверный логин или пароль! Выберите аккаунт из списка справа.';
      }
    }

    function loginSuccess(userAccount) {
      currentUser = userAccount;
      localStorage.setItem('mam_auth_user', userAccount.key);

      document.getElementById('view-auth').classList.add('hidden');
      document.getElementById('view-app').classList.remove('hidden');

      applyUserSession(userAccount.key);
      logAuditAction('Вход в систему', `Пользователь ${userAccount.shortName} авторизовался по логину`);
      showToast(`Добро пожаловать, ${userAccount.shortName}!`);
    }

    function logoutSession() {
      if (currentUser) {
        logAuditAction('Выход из системы', `Пользователь ${currentUser.shortName} завершил сеанс`);
      }
      localStorage.removeItem('mam_auth_user');
      currentUser = null;
      document.getElementById('auth-login-input').value = '';
      document.getElementById('auth-pass-input').value = '';
      showAuthScreen();
      showToast('Вы успешно вышли из системы.');
    }

    function onRoleSelectChange(targetRoleKey) {
      if (!ROLES_DATA[targetRoleKey]) return;
      applyUserSession(targetRoleKey);
      showToast(`Переключено на аккаунт: ${ROLES_DATA[targetRoleKey].shortName}`);
    }

    function applyUserSession(roleKey) {
      currentUser = ROLES_DATA[roleKey] || ROLES_DATA.director;
      localStorage.setItem('mam_auth_user', currentUser.key);

      document.getElementById('top-user-avatar').textContent = currentUser.avatar;
      document.getElementById('top-user-name').textContent = currentUser.shortName;
      document.getElementById('top-user-role').textContent = currentLang === 'uz' ? currentUser.roleNameUz : currentUser.roleName;

      document.getElementById('sidebar-role-tag').textContent = currentUser.key.toUpperCase();
      document.getElementById('roles-active-name-badge').textContent = `${currentUser.shortName} (${currentLang === 'uz' ? currentUser.roleNameUz : currentUser.roleName})`;

      populateSidebarRoleSelect();
      setupUserNav();

      if (!currentUser.allowedModules.includes(currentModule)) {
        switchModule(currentUser.allowedModules[0]);
      } else {
        renderCurrentModule();
      }

      renderRolesGrid();
      lucide.createIcons();
    }

    function populateSidebarRoleSelect() {
      const select = document.getElementById('sidebar-role-select');
      select.innerHTML = '';
      Object.keys(ROLES_DATA).forEach(key => {
        const r = ROLES_DATA[key];
        const opt = document.createElement('option');
        opt.value = key;
        opt.textContent = `${r.avatar} ${r.shortName} (${currentLang === 'uz' ? r.roleNameUz : r.roleName})`;
        if (key === currentUser.key) opt.selected = true;
        select.appendChild(opt);
      });
    }

    function setupUserNav() {
      const navList = document.getElementById('sidebar-nav-list');
      navList.innerHTML = '';

      const modulesConfig = [
        { id: 'director', icon: 'crown', labelRu: '👑 Кабинет Директора 360°', labelUz: '👑 Direktor kabineti 360°' },
        { id: 'roles', icon: 'users', labelRu: '1. 👤 Переключатель ролей (9)', labelUz: '1. 👤 Rollar (9 profil)' },
        { id: 'risks', icon: 'alert-triangle', labelRu: '3. 🚨 Риски & Alerts', labelUz: '3. 🚨 Xavflar & Alerts' },
        { id: 'contracts', icon: 'file-text', labelRu: '4. 📑 Генератор A4 документов', labelUz: '4. 📑 A4 Shartnoma & Sertifikat' },
        { id: 'pos', icon: 'credit-card', labelRu: '5. 💰 POS-Касса & Чеки', labelUz: '5. 💰 POS Kassa & Cheklar' },
        { id: 'journal', icon: 'book-open', labelRu: '6. 📚 Журнал 18 групп', labelUz: '6. 📚 18 guruh jurnali' },
        { id: 'backup', icon: 'database', labelRu: '7. ⚙️ Бэкап базы данных', labelUz: '7. ⚙️ MB Zaxira (Backup)' }
      ];

      modulesConfig.forEach(m => {
        if (!currentUser.allowedModules.includes(m.id)) return;

        const btn = document.createElement('button');
        btn.type = 'button';
        btn.onclick = () => switchModule(m.id);
        const isActive = (currentModule === m.id);

        btn.className = `w-full text-left px-3 py-2 rounded-xl text-xs font-semibold transition flex items-center gap-2.5 cursor-pointer ${
          isActive
            ? 'bg-emerald-600 text-white shadow-xs'
            : 'text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 hover:text-slate-900 dark:hover:text-white'
        }`;

        btn.innerHTML = `
          <i data-lucide="${m.icon}" class="w-4 h-4 shrink-0"></i>
          <span class="truncate">${currentLang === 'uz' ? m.labelUz : m.labelRu}</span>
        `;

        navList.appendChild(btn);
      });
    }

    function switchModule(moduleId) {
      if (!currentUser.allowedModules.includes(moduleId)) {
        moduleId = currentUser.allowedModules[0];
      }
      currentModule = moduleId;

      document.querySelectorAll('.module-view').forEach(sec => {
        sec.classList.add('hidden');
      });

      const target = document.getElementById(`module-${moduleId}`);
      if (target) {
        target.classList.remove('hidden');
      }

      setupUserNav();
      renderCurrentModule();
      lucide.createIcons();
    }

    function renderCurrentModule() {
      if (currentModule === 'director') renderDirectorModule();
      else if (currentModule === 'roles') renderRolesGrid();
      else if (currentModule === 'risks') renderRisksModule();
      else if (currentModule === 'contracts') renderContractsModule();
      else if (currentModule === 'pos') renderPosModule();
      else if (currentModule === 'journal') renderJournalModule();
      else if (currentModule === 'backup') renderBackupModule();
    }

    /* ==============================================================
       5. MODULE: 👑 EXECUTIVE COMMAND CENTER ДИРЕКТОРА (БОГДАНОВ Т.Я.)
       ============================================================== */
    function renderDirectorModule() {
      const db = getDB();

      // 1. Calculations: Gross Revenue, Expenses, Net Profit
      const grossRevenue = 37100000;
      
      // Calculate total operational expenses from db.expenses
      const totalOpExpenses = (db.expenses || []).reduce((acc, item) => acc + (parseInt(item.amount, 10) || 0), 0);
      
      // Teacher Salaries total
      const teacherKeys = ['teacher_python', 'teacher_web', 'teacher_design', 'teacher_english', 'teacher_korean', 'teacher_german'];
      let totalSalaries = 0;
      teacherKeys.forEach(tKey => {
        const teacherGroups = db.groups.filter(g => g.teacherKey === tKey);
        const groupIds = teacherGroups.map(g => g.id);
        const countStu = db.students.filter(s => groupIds.includes(s.groupId)).length;
        const totalConducted = teacherGroups.reduce((acc, g) => acc + (g.conductedLessons || 20), 0);
        totalSalaries += (totalConducted * 75000) + (countStu * 25000);
      });

      const totalOverallExpenses = totalOpExpenses + totalSalaries;
      const netProfit = grossRevenue - totalOverallExpenses;
      const marginPct = ((netProfit / grossRevenue) * 100).toFixed(1);

      // Count students in IT sector vs Language sector
      const itGroupPrefixes = ['PY', 'WEB', 'DS'];
      const itStudentsCount = db.students.filter(s => itGroupPrefixes.some(p => s.groupId.startsWith(p))).length;
      const langStudentsCount = db.students.length - itStudentsCount;

      document.getElementById('dir-kpi-rev').textContent = formatMoney(grossRevenue);
      document.getElementById('dir-kpi-net').textContent = formatMoney(netProfit);
      document.getElementById('dir-kpi-exp').textContent = formatMoney(totalOverallExpenses);
      document.getElementById('dir-kpi-margin').textContent = `${marginPct}%`;
      document.getElementById('dir-kpi-it').textContent = `${itStudentsCount} учеников`;
      document.getElementById('dir-kpi-lang').textContent = `${langStudentsCount} учеников`;
      document.getElementById('dir-total-expenses-badge').textContent = `Итого операционных расходов: ${formatMoney(totalOpExpenses)}`;

      // Render Classrooms Audit Table
      renderClassroomsTable();

      // Render Teachers Retention & KPI Table
      renderDirectorTeachersTable();

      // Render Expenses Registry Table
      renderDirectorExpensesTable();

      // Render Marketing CAC Table
      renderDirectorMarketingTable();

      // Render Security Audit Log
      renderDirectorAuditLog();

      lucide.createIcons();
    }

    function renderClassroomsTable() {
      const db = getDB();
      const classrooms = [
        { room: 'Ауд. 201 (Лаб. Python)', sector: 'Python & AI Engineering', groups: 3, shifts: '09:00 - 18:30', load: '92%', status: 'Оптимально' },
        { room: 'Ауд. 202 (Лаб. Web Dev)', sector: 'Frontend & Fullstack JS', groups: 3, shifts: '10:00 - 18:30', load: '95%', status: 'Высокая' },
        { room: 'Ауд. 203 (Дизайн-Студия)', sector: 'UI/UX & Графика', groups: 3, shifts: '09:00 - 16:00', load: '85%', status: 'Штатно' },
        { room: 'Ауд. 101 (English Hall)', sector: 'IELTS & General English', groups: 3, shifts: '11:30 - 18:30', load: '90%', status: 'Оптимально' },
        { room: 'Ауд. 102 (Korean Center)', sector: 'Корейский язык / TOPIK', groups: 3, shifts: '10:00 - 16:00', load: '80%', status: 'Резерв 20%' },
        { room: 'Ауд. 103 (Deutsches Haus)', sector: 'Немецкий язык / Goethe', groups: 3, shifts: '14:00 - 18:30', load: '75%', status: 'Резерв 25%' }
      ];

      const tbody = document.getElementById('dir-classrooms-tbody');
      tbody.innerHTML = '';
      classrooms.forEach(c => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-800/40';
        tr.innerHTML = `
          <td class="py-2 px-2.5 font-bold text-slate-900 dark:text-white">${c.room}</td>
          <td class="py-2 px-2.5 text-slate-600 dark:text-slate-300">${c.sector}</td>
          <td class="py-2 px-2.5 text-center font-bold">${c.groups}</td>
          <td class="py-2 px-2.5 text-center text-[10px] text-slate-500">${c.shifts}</td>
          <td class="py-2 px-2.5 text-right font-bold text-emerald-600">${c.load}</td>
          <td class="py-2 px-2.5 text-center">
            <span class="px-1.5 py-0.5 rounded text-[9px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700">${c.status}</span>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderDirectorTeachersTable() {
      const db = getDB();
      const teacherKeys = ['teacher_python', 'teacher_web', 'teacher_design', 'teacher_english', 'teacher_korean', 'teacher_german'];
      const tbody = document.getElementById('dir-teachers-tbody');
      tbody.innerHTML = '';

      const retentions = {
        teacher_python: { retention: '96.2%', churn: '3.8%' },
        teacher_web: { retention: '95.5%', churn: '4.5%' },
        teacher_design: { retention: '94.0%', churn: '6.0%' },
        teacher_english: { retention: '97.5%', churn: '2.5%' },
        teacher_korean: { retention: '93.0%', churn: '7.0%' },
        teacher_german: { retention: '92.5%', churn: '7.5%' }
      };

      teacherKeys.forEach(tKey => {
        const t = ROLES_DATA[tKey];
        const teacherGroups = db.groups.filter(g => g.teacherKey === tKey);
        const groupIds = teacherGroups.map(g => g.id);
        const teacherStudents = db.students.filter(s => groupIds.includes(s.groupId));

        const totalConducted = teacherGroups.reduce((acc, g) => acc + (g.conductedLessons || 20), 0);
        const baseRate = totalConducted * 75000;
        const studentBonus = teacherStudents.length * 25000;
        const totalSalary = baseRate + studentBonus;

        const isPaid = db.paidSalaries && db.paidSalaries[tKey];
        const ret = retentions[tKey] || { retention: '95.0%', churn: '5.0%' };

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-800/40';
        tr.innerHTML = `
          <td class="py-2.5 px-3 font-semibold text-slate-800 dark:text-slate-200">
            <span class="text-sm mr-1">${t.avatar}</span> ${t.shortName}
          </td>
          <td class="py-2.5 px-3 text-slate-600 dark:text-slate-300 font-sans">${t.course}</td>
          <td class="py-2.5 px-3 text-center font-bold">${teacherStudents.length}</td>
          <td class="py-2.5 px-3 text-center text-emerald-600 font-bold">${ret.retention}</td>
          <td class="py-2.5 px-3 text-center text-rose-500">${ret.churn}</td>
          <td class="py-2.5 px-3 text-center">${totalConducted}</td>
          <td class="py-2.5 px-3 text-right font-black text-emerald-600 dark:text-emerald-400">${formatMoney(totalSalary)}</td>
          <td class="py-2.5 px-3 text-center">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold ${
              isPaid
                ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
                : 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300'
            }">
              ${isPaid ? 'Выплачено' : 'Начислено'}
            </span>
          </td>
          <td class="py-2.5 px-3 text-center">
            ${isPaid ? `
              <span class="text-xs text-slate-400">Закрыто</span>
            ` : `
              <button type="button" onclick="paySingleSalary('${tKey}')" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-[11px] font-bold transition cursor-pointer">
                Выплатить
              </button>
            `}
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderDirectorExpensesTable() {
      const db = getDB();
      const tbody = document.getElementById('dir-expenses-tbody');
      tbody.innerHTML = '';

      (db.expenses || []).forEach((exp, idx) => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-800/40';
        tr.innerHTML = `
          <td class="py-2 px-3 text-slate-500">${exp.date}</td>
          <td class="py-2 px-3 font-semibold text-slate-800 dark:text-slate-200">
            <span class="px-2 py-0.5 rounded text-[10px] bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold">${exp.category}</span>
          </td>
          <td class="py-2 px-3 font-sans text-slate-700 dark:text-slate-300">${exp.title}</td>
          <td class="py-2 px-3 text-right font-bold text-rose-600 dark:text-rose-400">${formatMoney(exp.amount)}</td>
          <td class="py-2 px-3 text-center text-[10px] text-slate-500">${exp.approvedBy || 'Богданов Т.Я.'}</td>
          <td class="py-2 px-3 text-center">
            <button type="button" onclick="deleteExpenseItem(${idx})" class="text-rose-500 hover:text-rose-700 p-1 transition cursor-pointer" title="Удалить расход">
              <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function handleNewExpenseSubmit(e) {
      if (e) e.preventDefault();

      const cat = document.getElementById('exp-category-input').value;
      const title = document.getElementById('exp-title-input').value;
      const amount = parseInt(document.getElementById('exp-amount-input').value, 10) || 0;
      const date = document.getElementById('exp-date-input').value || new Date().toISOString().split('T')[0];

      if (!title || amount <= 0) {
        alert('Заполните корректное описание и сумму расхода!');
        return;
      }

      const db = getDB();
      if (!db.expenses) db.expenses = [];

      db.expenses.unshift({
        id: `EXP-${Math.floor(100 + Math.random() * 900)}`,
        category: cat,
        title: title,
        amount: amount,
        date: date,
        approvedBy: currentUser ? currentUser.shortName : 'Богданов Т.Я.'
      });

      saveDB(db);
      logAuditAction('Утверждение расхода', `Расход "${title}" на сумму ${formatMoney(amount)} утвержден Директором`, 'warning');

      document.getElementById('exp-title-input').value = '';
      document.getElementById('exp-amount-input').value = '';

      renderDirectorModule();
      showToast(`Расход на сумму ${formatMoney(amount)} утвержден и списан из бюджета!`);
    }

    function deleteExpenseItem(index) {
      if (!confirm('Удалить эту статью расхода? Сумма вернется в чистую прибыль.')) return;
      const db = getDB();
      if (db.expenses && db.expenses[index]) {
        const item = db.expenses[index];
        logAuditAction('Отмена расхода', `Расход "${item.title}" (${formatMoney(item.amount)}) удален`, 'warning');
        db.expenses.splice(index, 1);
        saveDB(db);
        renderDirectorModule();
        showToast('Статья расхода удалена.');
      }
    }

    function renderDirectorMarketingTable() {
      const marketingSources = [
        { name: 'Instagram Ads (Маргилан / Фергана)', leads: 68, clients: 24, cost: 1400000, cac: 58333, conv: '35.3%' },
        { name: 'Telegram-каналы Маргилана', leads: 42, clients: 16, cost: 600000, cac: 37500, conv: '38.1%' },
        { name: 'Наружные баннеры (Центр, Б. Маргиноний)', leads: 26, clients: 8, cost: 400000, cac: 50000, conv: '30.8%' },
        { name: 'Сарафанное радио (Рекомендации учеников)', leads: 19, clients: 6, cost: 0, cac: 0, conv: '31.6%' }
      ];

      const tbody = document.getElementById('dir-marketing-tbody');
      tbody.innerHTML = '';
      marketingSources.forEach(m => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-800/40';
        tr.innerHTML = `
          <td class="py-2 px-2.5 font-bold font-sans text-slate-800 dark:text-slate-200">${m.name}</td>
          <td class="py-2 px-2.5 text-center">${m.leads}</td>
          <td class="py-2 px-2.5 text-center font-bold text-emerald-600">${m.clients}</td>
          <td class="py-2 px-2.5 text-right font-mono text-slate-600 dark:text-slate-300">${formatMoney(m.cost)}</td>
          <td class="py-2 px-2.5 text-right font-mono font-bold text-amber-600">${formatMoney(m.cac)}</td>
          <td class="py-2 px-2.5 text-center font-bold text-emerald-600">${m.conv}</td>
        `;
        tbody.appendChild(tr);
      });
    }

    function renderDirectorAuditLog() {
      const db = getDB();
      const list = document.getElementById('dir-audit-list');
      list.innerHTML = '';

      (db.auditLogs || []).slice(0, 15).forEach(log => {
        const item = document.createElement('div');
        item.className = 'p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-100 dark:border-slate-700 text-xs space-y-1';
        item.innerHTML = `
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-1.5 font-bold text-slate-800 dark:text-slate-200">
              <span class="w-1.5 h-1.5 rounded-full ${log.severity === 'warning' ? 'bg-amber-500' : 'bg-emerald-500'}"></span>
              <span>${log.action}</span>
              <span class="text-[10px] text-slate-400 font-normal">• ${log.user}</span>
            </div>
            <span class="text-[10px] font-mono text-slate-400">${log.timestamp}</span>
          </div>
          <p class="text-[11px] text-slate-500 dark:text-slate-400 font-sans pl-3 leading-relaxed">
            ${log.details}
          </p>
        `;
        list.appendChild(item);
      });
    }

    function paySingleSalary(teacherKey) {
      const db = getDB();
      if (!db.paidSalaries) db.paidSalaries = {};
      db.paidSalaries[teacherKey] = true;
      saveDB(db);
      logAuditAction('Выплата зарплаты', `Выплачена зарплата преподавателю ${ROLES_DATA[teacherKey].shortName}`);
      renderDirectorModule();
      showToast('Зарплата успешно выплачена!');
    }

    function payAllSalaries() {
      const db = getDB();
      if (!db.paidSalaries) db.paidSalaries = {};
      ['teacher_python', 'teacher_web', 'teacher_design', 'teacher_english', 'teacher_korean', 'teacher_german'].forEach(k => {
        db.paidSalaries[k] = true;
      });
      saveDB(db);
      logAuditAction('Массовая выплата зарплат', 'Выплачены зарплаты всем 6 преподавателям за месяц');
      renderDirectorModule();
      showToast('Все зарплаты за месяц успешно выплачены!');
    }

    /* ==============================================================
       6. MODULE 1: ROLES & ACCOUNTS
       ============================================================== */
    function renderRolesGrid() {
      const container = document.getElementById('roles-cards-container');
      if (!container) return;
      container.innerHTML = '';

      Object.keys(ROLES_DATA).forEach(key => {
        const item = ROLES_DATA[key];
        const isCurrent = (currentUser && key === currentUser.key);

        const card = document.createElement('div');
        card.className = `p-4 rounded-xl border transition flex flex-col justify-between ${
          isCurrent
            ? 'bg-emerald-50/60 dark:bg-emerald-950/30 border-emerald-500 shadow-xs'
            : 'bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700'
        }`;

        card.innerHTML = `
          <div class="space-y-3">
            <div class="flex items-start justify-between">
              <div class="flex items-center gap-2.5">
                <span class="text-2xl">${item.avatar}</span>
                <div>
                  <h4 class="text-xs font-bold text-slate-900 dark:text-white leading-tight">${item.name}</h4>
                  <span class="inline-block mt-0.5 text-[10px] font-bold px-2 py-0.5 rounded-full ${item.badgeColor}">
                    ${currentLang === 'uz' ? item.roleNameUz : item.roleName}
                  </span>
                </div>
              </div>
              <div class="flex items-center gap-1">
                ${isCurrent ? '<span class="text-[10px] font-bold px-2 py-0.5 bg-emerald-600 text-white rounded-full">АКТИВЕН</span>' : ''}
              </div>
            </div>

            <div class="p-2 rounded-lg bg-slate-100 dark:bg-slate-800/80 font-mono text-[10px] text-slate-600 dark:text-slate-300 flex justify-between">
              <span>Логин: <strong>${item.login}</strong></span>
              <span>Пароль: <strong>${item.pass}</strong></span>
            </div>

            <p class="text-[11px] text-slate-500 dark:text-slate-400 leading-relaxed">
              ${item.desc}
            </p>

            ${item.course ? `
              <div class="p-2 rounded-lg bg-slate-100 dark:bg-slate-800 text-[11px] space-y-1">
                <div>Направление: <strong class="text-slate-800 dark:text-slate-200">${item.course}</strong></div>
                <div>Группы: <strong class="font-mono text-emerald-600">${item.groups.join(', ')}</strong></div>
              </div>
            ` : ''}

            <div class="text-[10px] text-slate-400">
              Доступные модули: <strong class="text-slate-600 dark:text-slate-300">${item.allowedModules.join(', ')}</strong>
            </div>
          </div>

          <div class="pt-4 mt-2 border-t border-slate-100 dark:border-slate-800">
            <button type="button" onclick="applyUserSession('${item.key}')" class="w-full py-2 text-xs font-bold rounded-lg transition flex items-center justify-center gap-1.5 cursor-pointer ${
              isCurrent
                ? 'bg-emerald-600 text-white shadow-xs cursor-default'
                : 'bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-800 dark:text-slate-200'
            }">
              <i data-lucide="${isCurrent ? 'check' : 'user-check'}" class="w-3.5 h-3.5"></i>
              <span>${isCurrent ? 'Текущая активная сессия' : 'Переключиться в этот аккаунт'}</span>
            </button>
          </div>
        `;

        container.appendChild(card);
      });
      lucide.createIcons();
    }

    /* ==============================================================
       7. MODULE 3: RISKS & SMART ALERTS
       ============================================================== */
    function renderRisksModule() {
      const db = getDB();
      const tbody = document.getElementById('risks-table-body');
      tbody.innerHTML = '';

      const atRiskStudents = db.students.filter(s => (s.lessonsBalance <= 1) || (s.consecutiveAbsences >= 3));

      let lowBalanceCount = 0;
      let highAbsentCount = 0;
      let expectedSum = 0;

      atRiskStudents.forEach(stu => {
        if (stu.lessonsBalance <= 1) lowBalanceCount++;
        if (stu.consecutiveAbsences >= 3) highAbsentCount++;

        const group = db.groups.find(g => g.id === stu.groupId);
        const fee = group ? group.fee : 600000;
        expectedSum += fee;

        let riskLabel = '';
        if (stu.lessonsBalance === 0 && stu.consecutiveAbsences >= 3) {
          riskLabel = '<span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 font-bold">0 уроков & 3 пропуска</span>';
        } else if (stu.lessonsBalance <= 1) {
          riskLabel = `<span class="px-2 py-0.5 rounded bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 font-bold">Осталось уроков: ${stu.lessonsBalance}</span>`;
        } else {
          riskLabel = `<span class="px-2 py-0.5 rounded bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 font-bold">Пропусков подряд: ${stu.consecutiveAbsences}</span>`;
        }

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-800/40';
        tr.innerHTML = `
          <td class="py-2.5 px-3">
            <div class="font-bold text-slate-900 dark:text-white">${stu.fullName}</div>
            <div class="text-[10px] text-slate-400 font-mono">${stu.id} • ${stu.phone}</div>
          </td>
          <td class="py-2.5 px-3">
            <div class="font-semibold text-slate-800 dark:text-slate-200">${stu.groupId}</div>
            <div class="text-[10px] text-slate-400">${group ? group.course : ''}</div>
          </td>
          <td class="py-2.5 px-3 text-center font-mono font-bold ${stu.lessonsBalance <= 1 ? 'text-rose-600' : ''}">
            ${stu.lessonsBalance}
          </td>
          <td class="py-2.5 px-3 text-center font-mono font-bold ${stu.consecutiveAbsences >= 3 ? 'text-rose-600' : ''}">
            ${stu.consecutiveAbsences}
          </td>
          <td class="py-2.5 px-3">
            <div class="font-semibold text-slate-800 dark:text-slate-200">${stu.parentName}</div>
            <div class="text-[10px] text-slate-500 font-mono">${stu.parentPhone}</div>
          </td>
          <td class="py-2.5 px-3 text-center">
            ${riskLabel}
          </td>
          <td class="py-2.5 px-3 text-center">
            <button type="button" onclick="generateTelegramScript('${stu.id}')" class="px-2.5 py-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold transition flex items-center justify-center gap-1 mx-auto shadow-xs cursor-pointer">
              <i data-lucide="send" class="w-3.5 h-3.5"></i>
              <span>Telegram скрипт</span>
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById('risk-count-balance').textContent = lowBalanceCount;
      document.getElementById('risk-count-absent').textContent = highAbsentCount;
      document.getElementById('risk-sum-renewal').textContent = formatMoney(expectedSum);

      lucide.createIcons();
    }

    let activeTelegramPhone = '';
    let activeTelegramText = '';

    function generateTelegramScript(studentId) {
      const db = getDB();
      const student = db.students.find(s => s.id === studentId);
      if (!student) return;
      const group = db.groups.find(g => g.id === student.groupId) || {};
      const fee = group.fee ? formatMoney(group.fee) : '600 000 UZS';

      activeTelegramPhone = student.parentPhone.replace(/[^0-9]/g, '');

      let text = '';
      if (currentLang === 'uz') {
        text = `Assalomu alaykum, ${student.parentName}!\n\n` +
          `Sizga "Maryam Academy Mission" (Marg'ilon) o'quv markazi ma'muriyati nomidan murojaat qilmoqdamiz.\n\n` +
          `Farzandingiz ${student.fullName} (${group.course || 'IT / Tillar'}, ${student.groupId} guruhi) bo'yicha ma'lumot:\n` +
          `• Qolgan darslar balansi: ${student.lessonsBalance} ta dars;\n` +
          `• Dars qoldirishlar: ${student.consecutiveAbsences} ta dars;\n` +
          `• Oylik to'lov summasi: ${fee} (12 ta dars uchun).\n\n` +
          `O'qish jarayoni to'xtab qolmasligi uchun Click yoki Payme orqali to'lovni amalga oshirishingizni so'raymiz:\n` +
          `💳 Karta: 8600 1204 8842 4492 (Maryam Academy Mission)\n` +
          `📱 Click ID: 88421 | Payme ID: 99312\n\n` +
          `Aloqa uchun: +998 (73) 254-88-99 / +998 (90) 555-12-34\n` +
          `Hurmat bilan, Bosh direktor Bogdanov T.Y.`;
      } else {
        text = `Здравствуйте, ${student.parentName}!\n\n` +
          `Вас приветствует администрация Академии IT и Языков "Maryam Academy Mission" (Маргилан).\n\n` +
          `Уведомляем о состоянии обучения студента: ${student.fullName}\n` +
          `Курс: ${group.course || 'IT / Языки'}, Группа: ${student.groupId}\n` +
          `• Остаток уроков на балансе: ${student.lessonsBalance} урок(а/ов);\n` +
          `• Пропусков занятий: ${student.consecutiveAbsences};\n` +
          `• Сумма продления абонемента: ${fee} (за 12 уроков).\n\n` +
          `Реквизиты для быстрой онлайн-оплаты:\n` +
          `💳 Карта: 8600 1204 8842 4492 (Maryam Academy Mission)\n` +
          `📱 Click ID: 88421 | Payme ID: 99312\n\n` +
          `Телефон ресепшена в Маргилане: +998 (73) 254-88-99 / +998 (90) 555-12-34\n` +
          `С уважением, Директор Академии Богданов Т.Я.`;
      }

      activeTelegramText = text;
      document.getElementById('telegram-script-text').value = text;
      document.getElementById('telegram-modal').classList.remove('hidden');
      document.getElementById('tg-copy-btn-text').textContent = 'Копировать в буфер';
    }

    function closeTelegramModal() {
      document.getElementById('telegram-modal').classList.add('hidden');
    }

    function copyTelegramScript() {
      const textarea = document.getElementById('telegram-script-text');
      textarea.select();
      navigator.clipboard.writeText(textarea.value).then(() => {
        document.getElementById('tg-copy-btn-text').textContent = 'Скопировано!';
        setTimeout(() => {
          document.getElementById('tg-copy-btn-text').textContent = 'Копировать в буфер';
        }, 2000);
      });
    }

    function openDirectTelegram() {
      const encoded = encodeURIComponent(activeTelegramText);
      window.open(`https://t.me/share/url?url=${encoded}`, '_blank');
    }

    /* ==============================================================
       8. MODULE 4: A4 CONTRACT & CERTIFICATE GENERATOR
       ============================================================== */
    let currentDocType = 'contract';
    let currentDocStudentId = '';

    function renderContractsModule() {
      const db = getDB();
      const select = document.getElementById('doc-student-select');
      select.innerHTML = '';

      db.students.forEach(s => {
        const opt = document.createElement('option');
        opt.value = s.id;
        opt.textContent = `${s.fullName} (${s.groupId} - ${s.phone})`;
        select.appendChild(opt);
      });

      if (!currentDocStudentId && db.students.length > 0) {
        currentDocStudentId = db.students[0].id;
      }
      select.value = currentDocStudentId;

      renderDocPreview();
    }

    function setDocType(type) {
      currentDocType = type;
      if (type === 'contract') {
        document.getElementById('btn-doc-type-contract').className = 'flex-1 py-1.5 text-xs font-bold rounded-md bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs transition cursor-pointer';
        document.getElementById('btn-doc-type-cert').className = 'flex-1 py-1.5 text-xs font-bold rounded-md text-slate-500 hover:text-slate-900 dark:hover:text-white transition cursor-pointer';
        document.getElementById('cert-extra-fields').classList.add('hidden');
      } else {
        document.getElementById('btn-doc-type-cert').className = 'flex-1 py-1.5 text-xs font-bold rounded-md bg-white dark:bg-slate-700 text-slate-900 dark:text-white shadow-xs transition cursor-pointer';
        document.getElementById('btn-doc-type-contract').className = 'flex-1 py-1.5 text-xs font-bold rounded-md text-slate-500 hover:text-slate-900 dark:hover:text-white transition cursor-pointer';
        document.getElementById('cert-extra-fields').classList.remove('hidden');
      }
      renderDocPreview();
    }

    function onDocStudentChange(studentId) {
      currentDocStudentId = studentId;
      renderDocPreview();
    }

    function updateCertPreview() {
      renderDocPreview();
    }

    function renderDocPreview() {
      const container = document.getElementById('print-modal-container');
      const db = getDB();
      const student = db.students.find(s => s.id === currentDocStudentId) || db.students[0];
      if (!student) return;
      const group = db.groups.find(g => g.id === student.groupId) || {};

      if (currentDocType === 'contract') {
        container.innerHTML = `
          <div class="space-y-4 text-[11px] leading-relaxed text-slate-900 font-sans">
            <!-- Header -->
            <div class="border-b-2 border-slate-900 pb-3 flex items-center justify-between">
              <div>
                <h1 class="text-base font-black tracking-wide uppercase">OOO "MARYAM ACADEMY MISSION"</h1>
                <p class="text-[10px] text-slate-600">Академия IT и Языков в г. Маргилан • Лицензия № 42-MAM/2025</p>
                <p class="text-[9px] text-slate-500">Адрес: г. Маргилан, ул. Бурхонуддин Маргиноний, 42 • Тел: +998 (73) 254-88-99</p>
              </div>
              <div class="text-right">
                <span class="text-xs font-bold font-mono px-2 py-0.5 border border-slate-900">№ ${student.contractNo}</span>
                <p class="text-[9px] text-slate-500 mt-1">г. Маргилан, ${new Date().toLocaleDateString('ru-RU')}</p>
              </div>
            </div>

            <!-- Title -->
            <div class="text-center py-2">
              <h2 class="text-xs font-black uppercase">ДОГОВОР НА ОКАЗАНИЕ ОБРАЗОВАТЕЛЬНЫХ УСЛУГ (UZ / RU)</h2>
              <p class="text-[10px] italic">TA'LIM XIZMATLARINI KO'RSATISH SHARTNOMASI</p>
            </div>

            <!-- Intro -->
            <div class="space-y-2 text-justify">
              <p>
                <strong>OOO «Maryam Academy Mission»</strong>, именуемое в дальнейшем «Исполнитель», в лице Директора <strong>Богданова Тимура Яковлевича</strong>, действующего на основании Устава, с одной стороны, и гражданин(ка):
              </p>
              <div class="p-2 bg-slate-50 border border-slate-300 font-mono text-[10px] space-y-1">
                <div>Студент: <strong>${student.fullName}</strong> (Паспорт: ${student.passport})</div>
                <div>Законный представитель (Родитель): <strong>${student.parentName}</strong></div>
                <div>Адрес: <strong>${student.address}</strong> • Телефон: <strong>${student.parentPhone}</strong></div>
                <div>Курс: <strong>${group.course || 'IT Программирование'}</strong> • Группа: <strong>${student.groupId}</strong></div>
              </div>
              <p>
                именуемый(ая) в дальнейшем «Заказчик», с другой стороны, заключили настоящий Договор о нижеследующем:
              </p>
            </div>

            <!-- Terms -->
            <div class="space-y-2">
              <div>
                <strong>1. ПРЕДМЕТ ДОГОВОРА / SHARTNOMA PREDMETI</strong>
                <p>1.1. Исполнитель обязуется предоставить качественные образовательные услуги по программе «${group.course || 'IT'}» в соответствии с авторским стандартом Академии MAM в Маргилане, а Заказчик обязуется своевременно оплачивать обучение.</p>
              </div>
              <div>
                <strong>2. СТОИМОСТЬ И ПОРЯДОК ОПЛАТЫ / TO'LOV TARTIBI</strong>
                <p>2.1. Стоимость абонемента составляет <strong>${formatMoney(group.fee || 600000)}</strong> за 1 учебный месяц (12 занятий). Оплата производится в национальном сумовом эквиваленте наличными, через терминал или платежные системы Click / Payme до 5 числа каждого месяца.</p>
              </div>
              <div>
                <strong>3. ПРАВА И ОБЯЗАННОСТИ СТОРОН / TOMONLARNING HUQUQ VA MAJBURIYATLARI</strong>
                <p>3.1. Заказчик обязуется обеспечить посещаемость занятий, бережно относиться к компьютерному оборудованию лаборатории MAM и соблюдать внутренний распорядок.</p>
                <p>3.2. При успешном завершении полного курса Академия выдает официальный номерной Сертификат с защитным QR-кодом.</p>
              </div>
            </div>

            <!-- Signatures block with Stamp -->
            <div class="pt-8 border-t border-slate-300 grid grid-cols-2 gap-8 text-[10px]">
              <div>
                <p class="font-bold uppercase">ИСПОЛНИТЕЛЬ / BAJARUVCHI:</p>
                <p>OOO "Maryam Academy Mission"</p>
                <p>г. Маргилан, ул. Б. Маргиноний, 42</p>
                <p>р/с: 20208000900123456001 в АКБ "Капиталбанк"</p>
                <p>МФО: 01088, ИНН: 309876543</p>
                <div class="mt-6 flex items-center gap-4">
                  <div>
                    <p>Директор: <strong>Богданов Т.Я.</strong></p>
                    <div class="w-32 border-b border-slate-800 mt-4"></div>
                    <span class="text-[8px] text-slate-500">(подпись / imzo)</span>
                  </div>
                  <div class="w-16 h-16 rounded-full border-2 border-emerald-700 text-emerald-800 flex items-center justify-center text-[8px] font-bold text-center leading-none uppercase p-1">
                    MAM<br>Маргилан<br>М.П. / MUHR
                  </div>
                </div>
              </div>

              <div>
                <p class="font-bold uppercase">ЗАКАЗЧИК / BUYURTMACHI:</p>
                <p>ФИО: <strong>${student.parentName}</strong></p>
                <p>Паспорт: ${student.passport}</p>
                <p>Телефон: ${student.parentPhone}</p>
                <div class="mt-10">
                  <p>Подпись Заказчика:</p>
                  <div class="w-32 border-b border-slate-800 mt-4"></div>
                  <span class="text-[8px] text-slate-500">(подпись / imzo)</span>
                </div>
              </div>
            </div>
          </div>
        `;
      } else {
        const gradeText = document.getElementById('cert-grade-input') ? document.getElementById('cert-grade-input').value : 'Отлично (A+)';

        container.innerHTML = `
          <div class="border-8 border-double border-slate-900 p-8 h-full flex flex-col justify-between text-center bg-radial from-white to-slate-50 text-slate-900 font-sans">
            <div class="space-y-2">
              <div class="flex items-center justify-center gap-3">
                <div class="w-12 h-12 bg-emerald-700 text-white font-black flex items-center justify-center text-lg rounded-xl shadow-xs">
                  MAM
                </div>
              </div>
              <h1 class="text-xs font-bold tracking-widest uppercase text-slate-600">MARYAM ACADEMY MISSION • MARGILAN</h1>
              <h2 class="text-2xl font-black tracking-wider uppercase text-slate-950 mt-2">СЕРТИФИКАТ ОБ ОКОНЧАНИИ</h2>
              <p class="text-xs italic text-slate-500 tracking-widest uppercase">CERTIFICATE OF COMPLETION / BITIRUV SERTIFIKATI</p>
            </div>

            <div class="my-8 space-y-4">
              <p class="text-xs text-slate-500 uppercase tracking-widest">Настоящий официальный сертификат подтверждает, что</p>
              <div class="text-2xl font-extrabold text-slate-950 font-serif border-b-2 border-slate-900 pb-2 inline-block px-8">
                ${student.fullName}
              </div>
              <p class="text-xs text-slate-600 max-w-md mx-auto leading-relaxed">
                успешно освоил(а) углубленную академическую программу по направлению:
              </p>
              <div class="text-lg font-black text-emerald-800 uppercase tracking-wide">
                ${group.course || 'IT & SOFTWARE ENGINEERING'}
              </div>
              <p class="text-xs font-mono font-bold text-slate-700">
                Группа: ${student.groupId} • Квалификационная оценка: ${gradeText}
              </p>
            </div>

            <div class="pt-6 border-t border-slate-300 grid grid-cols-3 items-end text-[10px]">
              <div class="text-left space-y-1">
                <div class="w-16 h-16 bg-slate-900 text-white font-mono text-[7px] p-1 flex items-center justify-center text-center">
                  [QR-CODE]<br>MAM-VERIFIED
                </div>
                <div class="font-mono text-[9px] text-slate-600">Код: ${student.certNo}</div>
                <div class="text-[8px] text-slate-400">Проверка: mam-academy.uz/verify</div>
              </div>

              <div class="flex justify-center">
                <div class="w-20 h-20 rounded-full border-4 border-double border-emerald-800 text-emerald-900 flex flex-col items-center justify-center text-[7px] font-bold text-center uppercase p-1">
                  <span>★ OFFICIAL ★</span>
                  <span class="text-[9px] font-black">MAM</span>
                  <span>MARGILAN</span>
                  <span>2026</span>
                </div>
              </div>

              <div class="text-right space-y-2">
                <div class="font-bold">Директор Академии MAM:</div>
                <div class="font-serif italic font-bold text-xs text-slate-800">Богданов Т.Я.</div>
                <div class="w-32 ml-auto border-b border-slate-900"></div>
                <div class="text-[8px] text-slate-400">Маргилан, ${new Date().toLocaleDateString('ru-RU')}</div>
              </div>
            </div>
          </div>
        `;
      }
    }

    function printActiveA4Document() {
      window.print();
    }

    /* ==============================================================
       9. MODULE 5: POS CASHIER & PAYMENTS
       ============================================================== */
    let posSelectedStudentId = '';

    function renderPosModule() {
      const db = getDB();
      const cashierName = currentUser ? currentUser.shortName : 'Рахимова Н.О.';
      document.getElementById('pos-cashier-badge').textContent = cashierName;

      if (!posSelectedStudentId && db.students.length > 0) {
        selectPosStudent(db.students[0].id);
      }

      renderPosReceipt();
      renderPosHistory();
    }

    function posSearchStudent(query) {
      const db = getDB();
      const dropdown = document.getElementById('pos-search-dropdown');
      if (!query || query.trim().length < 2) {
        dropdown.classList.add('hidden');
        return;
      }

      const q = query.toLowerCase();
      const filtered = db.students.filter(s =>
        s.fullName.toLowerCase().includes(q) ||
        s.phone.includes(q) ||
        s.id.toLowerCase().includes(q)
      );

      dropdown.innerHTML = '';
      if (filtered.length === 0) {
        dropdown.innerHTML = '<div class="p-2 text-slate-400 text-center">Студент не найден</div>';
      } else {
        filtered.forEach(s => {
          const item = document.createElement('div');
          item.className = 'p-2 hover:bg-slate-100 dark:hover:bg-slate-700 cursor-pointer flex items-center justify-between';
          item.innerHTML = `
            <div>
              <strong class="text-slate-800 dark:text-slate-200">${s.fullName}</strong>
              <span class="text-[10px] text-slate-400 font-mono">(${s.phone})</span>
            </div>
            <span class="text-[10px] font-mono font-bold text-emerald-600">${s.groupId} • ${s.lessonsBalance} ур.</span>
          `;
          item.onclick = () => {
            selectPosStudent(s.id);
            dropdown.classList.add('hidden');
            document.getElementById('pos-search-input').value = s.fullName;
          };
          dropdown.appendChild(item);
        });
      }
      dropdown.classList.remove('hidden');
    }

    function selectPosStudent(studentId) {
      const db = getDB();
      const s = db.students.find(st => st.id === studentId);
      if (!s) return;
      posSelectedStudentId = s.id;

      const group = db.groups.find(g => g.id === s.groupId) || {};

      document.getElementById('pos-card-name').textContent = s.fullName;
      document.getElementById('pos-card-id').textContent = `ID: ${s.id}`;
      document.getElementById('pos-card-group').textContent = s.groupId;
      document.getElementById('pos-card-phone').textContent = s.phone;
      document.getElementById('pos-card-balance').textContent = `${s.lessonsBalance} уроков`;
      document.getElementById('pos-card-course').textContent = group.course || 'IT / Языки';

      renderPosReceipt();
    }

    function setPosPackage(lessons, amount) {
      document.getElementById('pos-amount-input').value = amount;
      document.getElementById('pos-lessons-input').value = lessons;
      renderPosReceipt();
    }

    function getSelectedPosMethod() {
      const radios = document.getElementsByName('pos_method');
      for (let r of radios) {
        if (r.checked) return r.value;
      }
      return 'Click';
    }

    function executePosPayment() {
      const db = getDB();
      if (!posSelectedStudentId) {
        alert('Пожалуйста, выберите студента!');
        return;
      }

      const student = db.students.find(s => s.id === posSelectedStudentId);
      if (!student) return;

      const amount = parseInt(document.getElementById('pos-amount-input').value, 10) || 600000;
      const lessonsToAdd = parseInt(document.getElementById('pos-lessons-input').value, 10) || 12;
      const method = getSelectedPosMethod();
      const cashierName = currentUser ? currentUser.shortName : 'Рахимова Н.О.';

      student.lessonsBalance += lessonsToAdd;
      if (student.consecutiveAbsences > 0) student.consecutiveAbsences = 0;

      const payId = `PAY-${Math.floor(1000 + Math.random() * 9000)}`;
      const nowStr = new Date().toLocaleString('ru-RU');

      db.payments.unshift({
        id: payId,
        studentId: student.id,
        studentName: student.fullName,
        amount: amount,
        lessonsAdded: lessonsToAdd,
        method: method,
        date: nowStr,
        cashier: cashierName
      });

      saveDB(db);
      logAuditAction('Проведение оплаты в POS', `Оплата ${formatMoney(amount)} (${method}) зачислена студенту ${student.fullName} (+${lessonsToAdd} ур.)`);

      selectPosStudent(student.id);
      renderPosHistory();
      renderPosReceipt();

      showToast(`Оплата ${formatMoney(amount)} проведена! Баланс пополнен на ${lessonsToAdd} уроков.`);
    }

    function renderPosReceipt() {
      const db = getDB();
      const s = db.students.find(st => st.id === posSelectedStudentId) || db.students[0];
      const amount = parseInt(document.getElementById('pos-amount-input') ? document.getElementById('pos-amount-input').value : 600000, 10) || 600000;
      const lessons = parseInt(document.getElementById('pos-lessons-input') ? document.getElementById('pos-lessons-input').value : 12, 10) || 12;
      const method = getSelectedPosMethod();
      const cashier = currentUser ? currentUser.shortName : 'Рахимова Н.О.';

      const receiptBox = document.getElementById('pos-receipt-box');
      if (!receiptBox) return;

      receiptBox.innerHTML = `
        <div class="text-center pb-2 border-b border-dashed border-slate-300 dark:border-slate-600">
          <div class="font-black text-sm">MARYAM ACADEMY MISSION</div>
          <div class="text-[9px] text-slate-500">г. Маргилан, ул. Б. Маргиноний, 42</div>
          <div class="text-[9px] text-slate-500">ИНН: 309876543 • ФИСКАЛЬНЫЙ ЧЕК</div>
        </div>
        <div class="py-2 space-y-1 border-b border-dashed border-slate-300 dark:border-slate-600 text-[10px]">
          <div class="flex justify-between"><span>Чек №:</span><strong>#${Math.floor(100000 + Math.random() * 899999)}</strong></div>
          <div class="flex justify-between"><span>Дата / Время:</span><span>${new Date().toLocaleString('ru-RU')}</span></div>
          <div class="flex justify-between"><span>Кассир:</span><span>${cashier}</span></div>
          <div class="flex justify-between"><span>Студент:</span><strong>${s ? s.fullName : '---'}</strong></div>
          <div class="flex justify-between"><span>Группа:</span><span>${s ? s.groupId : '---'}</span></div>
        </div>
        <div class="py-2 space-y-1 border-b border-dashed border-slate-300 dark:border-slate-600 text-[10px]">
          <div class="flex justify-between"><span>Услуга:</span><span>Обучение (${lessons} уроков)</span></div>
          <div class="flex justify-between"><span>Способ оплаты:</span><strong>${method}</strong></div>
          <div class="flex justify-between font-bold text-xs pt-1">
            <span>ИТОГО К ОПЛАТЕ:</span>
            <span class="text-emerald-600">${formatMoney(amount)}</span>
          </div>
        </div>
        <div class="text-center pt-2 text-[8px] text-slate-400 space-y-1">
          <div>СПАСИБО ЗА ОБУЧЕНИЕ В MAM!</div>
          <div>QR: https://mam-academy.uz/check/88421</div>
        </div>
      `;
    }

    function renderPosHistory() {
      const db = getDB();
      const list = document.getElementById('pos-history-list');
      if (!list) return;
      list.innerHTML = '';

      document.getElementById('pos-history-count').textContent = `${db.payments.length} операций`;

      db.payments.slice(0, 10).forEach(p => {
        const item = document.createElement('div');
        item.className = 'p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-100 dark:border-slate-700 flex items-center justify-between text-xs';
        item.innerHTML = `
          <div>
            <div class="font-bold text-slate-800 dark:text-slate-200">${p.studentName}</div>
            <div class="text-[10px] text-slate-400">${p.date} • Метод: <strong class="text-slate-600 dark:text-slate-300">${p.method}</strong></div>
          </div>
          <div class="text-right">
            <div class="font-bold font-mono text-emerald-600">${formatMoney(p.amount)}</div>
            <div class="text-[10px] text-slate-400 font-mono">+${p.lessonsAdded} ур.</div>
          </div>
        `;
        list.appendChild(item);
      });
    }

    function printPosReceipt() {
      const receiptContent = document.getElementById('pos-receipt-box').innerHTML;
      const win = window.open('', '_blank', 'width=350,height=500');
      win.document.write(`
        <html>
          <head>
            <title>Кассовый чек MAM</title>
            <style>
              body { font-family: monospace; font-size: 11px; padding: 10px; margin: 0; }
              .text-center { text-align: center; }
              .flex { display: flex; justify-content: space-between; }
              .border-b { border-bottom: 1px dashed #000; padding-bottom: 6px; margin-bottom: 6px; }
              .font-bold { font-weight: bold; }
            </style>
          </head>
          <body>
            ${receiptContent}
            <script>window.print(); setTimeout(() => window.close(), 500);<\/script>
          </body>
        </html>
      `);
      win.document.close();
    }

    /* ==============================================================
       10. MODULE 6: ELECTRONIC JOURNAL (18 GROUPS)
       ============================================================== */
    let currentJournalGroupId = 'PY-101';
    let currentJournalDate = new Date().toISOString().split('T')[0];

    function renderJournalModule() {
      const db = getDB();
      const teacherSelect = document.getElementById('journal-teacher-select');
      const groupSelect = document.getElementById('journal-group-select');

      document.getElementById('journal-date-input').value = currentJournalDate;

      const teacherKeys = ['teacher_python', 'teacher_web', 'teacher_design', 'teacher_english', 'teacher_korean', 'teacher_german'];
      teacherSelect.innerHTML = '<option value="all">Все преподаватели (6)</option>';

      teacherKeys.forEach(tKey => {
        const t = ROLES_DATA[tKey];
        const opt = document.createElement('option');
        opt.value = tKey;
        opt.textContent = `${t.avatar} ${t.shortName} (${t.course})`;
        if (currentUser && currentUser.key === tKey) opt.selected = true;
        teacherSelect.appendChild(opt);
      });

      populateJournalGroups();
    }

    function populateJournalGroups() {
      const db = getDB();
      const teacherFilter = document.getElementById('journal-teacher-select').value;
      const groupSelect = document.getElementById('journal-group-select');
      groupSelect.innerHTML = '';

      let filteredGroups = db.groups;
      if (teacherFilter !== 'all') {
        filteredGroups = db.groups.filter(g => g.teacherKey === teacherFilter);
      }

      filteredGroups.forEach(g => {
        const opt = document.createElement('option');
        opt.value = g.id;
        opt.textContent = `${g.id} — ${g.name} (${g.teacherName})`;
        if (g.id === currentJournalGroupId) opt.selected = true;
        groupSelect.appendChild(opt);
      });

      if (filteredGroups.length > 0 && !filteredGroups.some(g => g.id === currentJournalGroupId)) {
        currentJournalGroupId = filteredGroups[0].id;
        groupSelect.value = currentJournalGroupId;
      }

      onJournalGroupChange(currentJournalGroupId);
    }

    function onJournalTeacherChange(val) {
      populateJournalGroups();
    }

    function onJournalGroupChange(groupId) {
      currentJournalGroupId = groupId;
      const db = getDB();
      const group = db.groups.find(g => g.id === groupId);
      if (!group) return;

      document.getElementById('journal-group-schedule').textContent = group.schedule;
      document.getElementById('journal-group-room').textContent = group.room;
      document.getElementById('journal-group-fee').textContent = formatMoney(group.fee);
      document.getElementById('journal-roster-title').textContent = `Список студентов: ${group.name}`;

      renderJournalRoster();
    }

    function onJournalDateChange(val) {
      currentJournalDate = val;
      renderJournalRoster();
    }

    function renderJournalRoster() {
      const db = getDB();
      const studentsInGroup = db.students.filter(s => s.groupId === currentJournalGroupId);
      const tbody = document.getElementById('journal-students-table-body');
      tbody.innerHTML = '';

      document.getElementById('journal-roster-count').textContent = `${studentsInGroup.length} студентов`;

      if (studentsInGroup.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" class="p-4 text-center text-slate-400">В этой группе пока нет студентов</td></tr>';
        return;
      }

      studentsInGroup.forEach(stu => {
        const dateKey = `${currentJournalDate}_${stu.id}`;
        const currentMark = db.attendance[dateKey] || 'none';

        const tr = document.createElement('tr');
        tr.className = 'hover:bg-slate-50 dark:hover:bg-slate-800/40';
        tr.innerHTML = `
          <td class="py-2.5 px-3 font-mono text-[10px] text-slate-400">${stu.id}</td>
          <td class="py-2.5 px-3 font-bold text-slate-800 dark:text-slate-200">
            ${stu.fullName}
          </td>
          <td class="py-2.5 px-3 font-mono text-slate-500">${stu.phone}</td>
          <td class="py-2.5 px-3 text-center font-mono font-bold ${stu.lessonsBalance <= 1 ? 'text-rose-600' : 'text-emerald-600'}">
            ${stu.lessonsBalance} ур.
          </td>
          <td class="py-2.5 px-3 text-center">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold ${
              currentMark === 'present'
                ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300'
                : currentMark === 'absent'
                ? 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300'
                : currentMark === 'excused'
                ? 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300'
                : 'bg-slate-100 text-slate-500 dark:bg-slate-800 dark:text-slate-400'
            }">
              ${currentMark === 'present' ? 'БЫЛ (BOR)' : currentMark === 'absent' ? 'НБ (YOʻQ)' : currentMark === 'excused' ? 'УВАЖ. (SABABLI)' : 'Не отмечен'}
            </span>
          </td>
          <td class="py-2.5 px-3 text-center">
            <div class="inline-flex rounded-lg border border-slate-200 dark:border-slate-700 p-0.5 gap-1 bg-slate-50 dark:bg-slate-800">
              <button type="button" onclick="setAttendanceMark('${stu.id}', 'present')" class="px-2 py-1 text-[10px] font-bold rounded cursor-pointer transition ${currentMark === 'present' ? 'bg-emerald-600 text-white' : 'hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300'}">
                Был
              </button>
              <button type="button" onclick="setAttendanceMark('${stu.id}', 'absent')" class="px-2 py-1 text-[10px] font-bold rounded cursor-pointer transition ${currentMark === 'absent' ? 'bg-rose-600 text-white' : 'hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300'}">
                НБ
              </button>
              <button type="button" onclick="setAttendanceMark('${stu.id}', 'excused')" class="px-2 py-1 text-[10px] font-bold rounded cursor-pointer transition ${currentMark === 'excused' ? 'bg-amber-500 text-white' : 'hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300'}">
                Уваж.
              </button>
            </div>
          </td>
        `;
        tbody.appendChild(tr);
      });
    }

    function setAttendanceMark(studentId, mark) {
      const db = getDB();
      const student = db.students.find(s => s.id === studentId);
      if (!student) return;

      const dateKey = `${currentJournalDate}_${studentId}`;
      const prevMark = db.attendance[dateKey];

      if (prevMark === 'present' || prevMark === 'absent') {
        student.lessonsBalance += 1;
      }
      if (prevMark === 'absent' && student.consecutiveAbsences > 0) {
        student.consecutiveAbsences -= 1;
      }

      db.attendance[dateKey] = mark;

      if (mark === 'present') {
        student.lessonsBalance = Math.max(0, student.lessonsBalance - 1);
        student.consecutiveAbsences = 0;
      } else if (mark === 'absent') {
        student.lessonsBalance = Math.max(0, student.lessonsBalance - 1);
        student.consecutiveAbsences = (student.consecutiveAbsences || 0) + 1;
      }

      saveDB(db);
      logAuditAction('Отметка посещаемости', `Студент ${student.fullName} (${student.groupId}) отмечен как "${mark.toUpperCase()}" за ${currentJournalDate}`);
      renderJournalRoster();
      showToast(`Отметка "${mark.toUpperCase()}" сохранена для ${student.fullName}`);
    }

    function markAllPresent() {
      const db = getDB();
      const studentsInGroup = db.students.filter(s => s.groupId === currentJournalGroupId);

      studentsInGroup.forEach(stu => {
        const dateKey = `${currentJournalDate}_${stu.id}`;
        const prevMark = db.attendance[dateKey];
        if (prevMark !== 'present') {
          if (prevMark === 'absent' && stu.consecutiveAbsences > 0) stu.consecutiveAbsences -= 1;
          if (!prevMark || prevMark === 'excused') {
            stu.lessonsBalance = Math.max(0, stu.lessonsBalance - 1);
          }
          stu.consecutiveAbsences = 0;
          db.attendance[dateKey] = 'present';
        }
      });

      saveDB(db);
      logAuditAction('Массовая посещаемость', `Все студенты группы ${currentJournalGroupId} отмечены "Был" за ${currentJournalDate}`);
      renderJournalRoster();
      showToast('Все студенты группы отмечены как "Был". Списано по 1 уроку.');
    }

    /* ==============================================================
       11. MODULE 7: BACKUP & DATABASE SETTINGS
       ============================================================== */
    function renderBackupModule() {
      const db = getDB();
      document.getElementById('db-stat-students-count').textContent = db.students.length;
      document.getElementById('db-stat-groups-count').textContent = db.groups.length;
      document.getElementById('db-stat-payments-count').textContent = db.payments.length;
      document.getElementById('db-stat-attendance-count').textContent = Object.keys(db.attendance).length;
    }

    function exportDatabaseJSON() {
      const db = getDB();
      const dataStr = 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(db, null, 2));
      const downloadAnchor = document.createElement('a');
      const dateStr = new Date().toISOString().split('T')[0];
      downloadAnchor.setAttribute('href', dataStr);
      downloadAnchor.setAttribute('download', `mam_crm_backup_${dateStr}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
      logAuditAction('Экспорт БД', 'Выгружена резервная копия mam_crm_backup.json');
      showToast('Резервная копия базы данных успешно скачана!');
    }

    function importDatabaseJSON(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const parsed = JSON.parse(e.target.result);
          if (parsed && Array.isArray(parsed.students) && Array.isArray(parsed.groups)) {
            saveDB(parsed);
            logAuditAction('Импорт БД', 'База данных успешно восстановлена из внешнего JSON-файла', 'warning');
            showToast('База данных успешно восстановлена из файла!');
            setTimeout(() => {
              location.reload();
            }, 600);
          } else {
            alert('Ошибка структуры файла резервной копии. Проверьте JSON!');
          }
        } catch (err) {
          alert('Ошибка при чтении JSON-файла: ' + err.message);
        }
      };
      reader.readAsText(file);
    }

    function resetDatabaseToFactory() {
      if (confirm('Внимание! Все текущие изменения будут сброшены к исходным 54 студентам и 18 группам MAM. Продолжить?')) {
        const fresh = generateInitialDB();
        saveDB(fresh);
        logAuditAction('Сброс БД к эталону', 'База данных сброшена к исходным демонстрационным данным MAM', 'warning');
        showToast('База данных успешно сброшена к эталонному состоянию.');
        setTimeout(() => {
          location.reload();
        }, 500);
      }
    }

    /* ==============================================================
       12. GENERAL HELPERS & LOCALIZATION
       ============================================================== */
    function formatMoney(amount) {
      if (typeof amount !== 'number') amount = parseInt(amount, 10) || 0;
      return amount.toLocaleString('ru-RU') + ' UZS';
    }

    function toggleTheme() {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('mam_theme', isDark ? 'dark' : 'light');
    }

    function toggleLang() {
      currentLang = (currentLang === 'ru') ? 'uz' : 'ru';
      localStorage.setItem('mam_lang', currentLang);
      applyLanguage(currentLang);
      if (currentUser) {
        populateSidebarRoleSelect();
        setupUserNav();
        renderCurrentModule();
      }
    }

    function applyLanguage(lang) {
      const ind = document.getElementById('lang-indicator');
      if (ind) ind.textContent = lang.toUpperCase();
      const dict = I18N[lang] || I18N.ru;
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
          el.textContent = dict[key];
        }
      });
    }

    function updateGlobalCounters() {
      const db = getDB();
      const atRisk = db.students.filter(s => (s.lessonsBalance <= 1) || (s.consecutiveAbsences >= 3));

      const sideStu = document.getElementById('side-stat-students');
      const sideGrp = document.getElementById('side-stat-groups');
      const sideRsk = document.getElementById('side-stat-risks');

      if (sideStu) sideStu.textContent = db.students.length;
      if (sideGrp) sideGrp.textContent = db.groups.length;
      if (sideRsk) sideRsk.textContent = atRisk.length;
    }

    function showToast(message) {
      const existing = document.getElementById('mam-toast');
      if (existing) existing.remove();

      const toast = document.createElement('div');
      toast.id = 'mam-toast';
      toast.className = 'fixed bottom-5 right-5 z-50 bg-slate-900 text-white dark:bg-white dark:text-slate-900 px-4 py-2.5 rounded-xl shadow-xl text-xs font-bold flex items-center gap-2 border border-slate-700 animate-bounce';
      toast.innerHTML = `<span>✓</span> <span>${message}</span>`;
      document.body.appendChild(toast);

      setTimeout(() => {
        toast.remove();
      }, 3000);
    }

    // Startup sequence
    window.addEventListener('DOMContentLoaded', () => {
      applyLanguage(currentLang);
      updateGlobalCounters();
      checkSavedSession();
      lucide.createIcons();
    });
  </script>
</body>
</html>
'''

with open("crm.html", "w", encoding="utf-8") as f:
    f.write(content)

print(f"crm.html generated successfully! Length: {len(content)} characters, {len(content.splitlines())} lines.")
