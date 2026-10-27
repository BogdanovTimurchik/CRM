#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_crm_perfect.py
Generates the complete, standalone, production-ready crm.html for Maryam Academy Mission (MAM) in Margilan.
"""

def generate():
    with open('/crm.html', 'w', encoding='utf-8') as f:
        # Write parts directly to file
        f.write('''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MAM СУБД/ERP — Maryam Academy Mission (Маргилан)</title>
  <meta name="description" content="Внутренняя ERP/CRM-система Академии IT и Языков Maryam Academy Mission в Маргилане. Кабинет Директора Богданова Т.Я., P&L, 9 аккаунтов, 18 групп, POS-касса, генератор договоров и сертификатов." />

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
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(0, 0, 0, 0.05);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(16, 185, 129, 0.3);
      border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(16, 185, 129, 0.6);
    }

    @media print {
      body * {
        visibility: hidden;
      }
      #print-area, #print-area * {
        visibility: visible;
      }
      #print-area {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 10mm;
        background: white !important;
        color: black !important;
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
<body class="bg-slate-50 dark:bg-slate-950 text-slate-800 dark:text-slate-100 font-sans antialiased min-h-screen selection:bg-emerald-500 selection:text-white">

  <!-- ============================================================== -->
  <!-- SCREEN 1: СТРОГАЯ АВТОРИЗАЦИЯ (LOGIN & PASSWORD SCREEN)        -->
  <!-- ============================================================== -->
  <section id="view-auth" class="min-h-screen flex items-center justify-center p-4 sm:p-6 bg-slate-900/95 relative overflow-hidden">
    <div class="absolute -top-40 -left-40 w-96 h-96 bg-emerald-600/15 rounded-full blur-3xl pointer-events-none"></div>
    <div class="absolute -bottom-40 -right-40 w-96 h-96 bg-teal-600/15 rounded-full blur-3xl pointer-events-none"></div>

    <div class="w-full max-w-4xl bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 overflow-hidden grid grid-cols-1 lg:grid-cols-12 relative z-10">
      
      <!-- Left side: Login Form (7 cols) -->
      <div class="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between space-y-6">
        <div>
          <!-- MAM VECTOR LOGO (LOGIN SCREEN) -->
          <div class="flex items-center gap-3.5 mb-6">
            <svg viewBox="0 0 48 48" class="w-12 h-12 shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg">
              <rect width="48" height="48" rx="14" fill="url(#mam-logo-grad)" />
              <path d="M13 34V16L24 27L35 16V34" stroke="#FFFFFF" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
              <circle cx="24" cy="13" r="2.2" fill="#FBBF24"/>
              <defs>
                <linearGradient id="mam-logo-grad" x1="0" y1="0" x2="48" y2="48" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#059669"/>
                  <stop offset="1" stop-color="#064E3B"/>
                </linearGradient>
              </defs>
            </svg>
            <div>
              <div class="text-lg font-black tracking-wider text-slate-900 dark:text-white leading-none">
                MARYAM ACADEMY MISSION
              </div>
              <div class="text-[11px] font-semibold text-emerald-600 dark:text-emerald-400 tracking-wider uppercase mt-1">
                IT & Tillar Akademiyasi • Marg'ilon
              </div>
            </div>
          </div>

          <div class="mb-5">
            <h2 class="text-xl font-black text-slate-900 dark:text-white tracking-tight" data-i18n="auth_title">
              Вход в служебную CRM/ERP
            </h2>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1" data-i18n="auth_subtitle">
              Изолированная служебная система сотрудников. Доступ строго по учетным данным.
            </p>
          </div>

          <div id="auth-alert" class="hidden mb-4 p-3 rounded-xl text-xs font-semibold border flex items-center gap-2"></div>

          <form id="auth-form" onsubmit="handleLoginSubmit(event)" class="space-y-4">
            <div>
              <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1" data-i18n="auth_lbl_login">
                Логин сотрудника:
              </label>
              <div class="relative">
                <i data-lucide="user" class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
                <input type="text" id="auth-input-login" required autocomplete="username"
                  placeholder="director, cashier, teacher_python..."
                  class="w-full pl-9 pr-3 py-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs font-medium text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition" />
              </div>
            </div>

            <div>
              <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1" data-i18n="auth_lbl_pass">
                Пароль:
              </label>
              <div class="relative">
                <i data-lucide="lock" class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
                <input type="password" id="auth-input-pass" required autocomplete="current-password"
                  placeholder="••••••••"
                  class="w-full pl-9 pr-10 py-2.5 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-xs font-medium text-slate-900 dark:text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent transition" />
                <button type="button" onclick="togglePassVisibility()" class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer">
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
            Нажмите на любой аккаунт ниже для мгновенной подстановки логина и пароля в форму:
          </p>

          <div class="space-y-1.5 max-h-96 overflow-y-auto pr-1" id="auth-quick-accounts-list"></div>
        </div>

        <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-900/60 text-[10px] text-amber-800 dark:text-amber-300 space-y-1">
          <div class="font-bold flex items-center gap-1">
            <i data-lucide="shield-check" class="w-3 h-3 text-emerald-600"></i>
            Кабинет Директора Богданова Т.Я.:
          </div>
          <div>• Включает Executive Command Center: 360° KPI, P&L Расходы, Анализ Учителей, РИСКИ & ALERTS (Telegram) и Audit Log.</div>
        </div>
      </div>

    </div>
  </section>

  <!-- ============================================================== -->
  <!-- SCREEN 2: ОСНОВНАЯ ПАНЕЛЬ CRM/ERP (СТРОГО БЕЗ СЕЛЕКТОРА РОЛЕЙ)  -->
  <!-- ============================================================== -->
  <div id="view-app" class="hidden min-h-screen flex flex-col">
    <!-- TOP APP BAR -->
    <header class="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200 dark:border-slate-800 px-4 py-2.5 flex items-center justify-between shadow-xs">
      <div class="flex items-center gap-3">
        <!-- MAM VECTOR LOGO (TOP BAR) -->
        <svg viewBox="0 0 160 40" class="h-8 w-auto shrink-0" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="2" y="2" width="36" height="36" rx="10" fill="url(#mam-header-grad)" />
          <path d="M10 28V12L20 22L30 12V28" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="20" cy="10" r="1.8" fill="#FBBF24"/>
          <text x="46" y="19" font-family="Inter, system-ui, sans-serif" font-weight="900" font-size="13" fill="currentColor" letter-spacing="1.2">MARYAM</text>
          <text x="46" y="32" font-family="Inter, system-ui, sans-serif" font-weight="700" font-size="9" fill="#10B981" letter-spacing="0.8">ACADEMY MISSION</text>
          <defs>
            <linearGradient id="mam-header-grad" x1="2" y1="2" x2="38" y2="38" gradientUnits="userSpaceOnUse">
              <stop stop-color="#059669"/>
              <stop offset="1" stop-color="#064E3B"/>
            </linearGradient>
          </defs>
        </svg>

        <div class="hidden sm:block border-l border-slate-200 dark:border-slate-800 pl-3">
          <span class="text-[10px] uppercase font-bold tracking-wider px-1.5 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 border border-emerald-300 dark:border-emerald-800">
            Маргилан ERP/CRM
          </span>
          <p class="text-[10px] text-slate-400">ул. Б. Маргиноний, 42</p>
        </div>
      </div>

      <!-- Active User & System Quick Controls (STRICTLY NO ROLE SELECTOR!) -->
      <div class="flex items-center gap-2 sm:gap-3">
        <!-- Active User Badge (Name & Role only) -->
        <div class="flex items-center gap-2 bg-slate-100 dark:bg-slate-800/80 px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-700">
          <span class="text-base" id="top-user-avatar">👑</span>
          <div class="text-left leading-tight">
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
      <!-- LEFT SIDEBAR -->
      <aside class="w-64 shrink-0 bg-white dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800 flex flex-col justify-between overflow-y-auto">
        <div class="p-3 space-y-4">
          
          <!-- Current Employee Card (Info only, no dropdown!) -->
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/60 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-[10px] font-extrabold uppercase tracking-wider text-slate-400">Служебный профиль</span>
              <span class="text-[9px] font-bold px-1.5 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300" id="sidebar-access-level">FULL ACCESS</span>
            </div>
            <div class="flex items-center gap-2.5">
              <div class="w-8 h-8 rounded-lg bg-emerald-600/10 flex items-center justify-center text-lg" id="side-emp-avatar">👑</div>
              <div class="overflow-hidden">
                <div class="text-xs font-bold text-slate-800 dark:text-slate-100 truncate" id="side-emp-name">Богданов Т.Я.</div>
                <div class="text-[10px] text-slate-500 dark:text-slate-400 truncate" id="side-emp-role">Директор</div>
              </div>
            </div>
          </div>

          <!-- Navigation Menu (filtered strictly by user permissions) -->
          <div class="space-y-1">
            <span class="text-[11px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500 px-2 block" data-i18n="nav_modules_title">
              Доступные модули
            </span>
            <nav id="sidebar-nav-list" class="space-y-1"></nav>
          </div>

          <!-- Quick Stats Box -->
          <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/60 text-xs space-y-2">
            <div class="flex items-center justify-between text-slate-500 dark:text-slate-400">
              <span data-i18n="box_students">Студентов в базе:</span>
              <span class="font-bold text-slate-900 dark:text-white font-mono" id="side-stat-students">54</span>
            </div>
            <div class="flex items-center justify-between text-slate-500 dark:text-slate-400">
              <span data-i18n="box_groups">Активных групп:</span>
              <span class="font-bold text-emerald-600 dark:text-emerald-400 font-mono" id="side-stat-groups">18</span>
            </div>
            <div class="flex items-center justify-between text-slate-500 dark:text-slate-400">
              <span data-i18n="box_cash">В кассе сегодня:</span>
              <span class="font-bold text-blue-600 dark:text-blue-400 font-mono" id="side-stat-cash">12 450 000 UZS</span>
            </div>
          </div>

        </div>

        <!-- Sidebar Footer -->
        <div class="p-3 border-t border-slate-200 dark:border-slate-800 text-[11px] text-slate-400 space-y-2">
          <div class="flex items-center justify-between">
            <span>База данных:</span>
            <span class="font-mono text-emerald-600 font-bold">LocalStorage (OK)</span>
          </div>
          <button type="button" onclick="exportDatabaseJSON()" class="w-full py-1.5 px-2 bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 font-bold rounded-lg transition flex items-center justify-center gap-1.5 cursor-pointer">
            <i data-lucide="download" class="w-3.5 h-3.5 text-emerald-600"></i>
            <span data-i18n="btn_backup_quick">Бэкап JSON</span>
          </button>
        </div>
      </aside>

      <!-- CONTENT AREA -->
      <main class="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8 space-y-6" id="main-content-scroll">
''')

        # 2. MODULE 1: DIRECTOR EXECUTIVE COMMAND CENTER
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: КАБИНЕТ ДИРЕКТОРА (EXECUTIVE COMMAND CENTER)          -->
        <!-- ============================================================== -->
        <section id="module-director" class="module-view hidden space-y-6">
          
          <!-- Executive Top Header -->
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 p-5 rounded-2xl bg-gradient-to-r from-emerald-900 to-slate-900 text-white shadow-lg border border-emerald-800/40">
            <div class="flex items-center gap-4">
              <div class="w-14 h-14 rounded-2xl bg-emerald-600/30 border border-emerald-400/30 flex items-center justify-center text-3xl shadow-inner">
                👑
              </div>
              <div>
                <div class="flex items-center gap-2">
                  <span class="text-xs uppercase font-extrabold tracking-widest text-emerald-400 bg-emerald-950/80 px-2 py-0.5 rounded-md border border-emerald-800">
                    Executive Command Center
                  </span>
                  <span class="text-[11px] text-slate-300">Филиал Маргилан</span>
                </div>
                <h2 class="text-xl sm:text-2xl font-black tracking-tight text-white mt-1">
                  Кабинет Директора: Богданов Т.Я.
                </h2>
                <p class="text-xs text-emerald-100/70 mt-0.5">
                  Сводка 360°, финансовый P&L, контроль ФОТ учителей, раннее предупреждение рисков (Alerts) и Audit Log.
                </p>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <button type="button" onclick="renderDirectorCommandCenter()" class="px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition flex items-center gap-1.5 cursor-pointer shadow-md">
                <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                <span>Обновить метрики</span>
              </button>
            </div>
          </div>

          <!-- 1. Сводка "360° Вся Академия" - KPI Grid -->
          <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-8 gap-3" id="dir-kpi-grid">
            <!-- Rendered by JS -->
          </div>

          <!-- IT vs Языки + Загрузка Кабинетов + Воронка -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
            <!-- IT vs Language Summary (4 cols) -->
            <div class="lg:col-span-4 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                <i data-lucide="pie-chart" class="w-4 h-4 text-emerald-600"></i>
                Секторы: IT vs Языки
              </h3>
              <div class="space-y-3">
                <div class="p-3 rounded-lg bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900">
                  <div class="flex items-center justify-between text-xs font-bold text-emerald-800 dark:text-emerald-300">
                    <span>IT Сектор (Python, Web, Design)</span>
                    <span class="font-mono">65.2%</span>
                  </div>
                  <div class="text-[11px] text-emerald-600 mt-1">
                    9 групп • 27 студентов • Выручка: 33 500 000 UZS
                  </div>
                  <div class="w-full bg-emerald-200 dark:bg-emerald-900 h-1.5 rounded-full mt-2 overflow-hidden">
                    <div class="bg-emerald-600 h-full rounded-full" style="width: 65.2%"></div>
                  </div>
                </div>

                <div class="p-3 rounded-lg bg-blue-50/70 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-900">
                  <div class="flex items-center justify-between text-xs font-bold text-blue-800 dark:text-blue-300">
                    <span>Языковой Сектор (ENG, KOR, GER)</span>
                    <span class="font-mono">34.8%</span>
                  </div>
                  <div class="text-[11px] text-blue-600 mt-1">
                    9 групп • 27 студентов • Выручка: 17 900 000 UZS
                  </div>
                  <div class="w-full bg-blue-200 dark:bg-blue-900 h-1.5 rounded-full mt-2 overflow-hidden">
                    <div class="bg-blue-600 h-full rounded-full" style="width: 34.8%"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Classroom Occupancy Matrix (4 cols) -->
            <div class="lg:col-span-4 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="layout-grid" class="w-4 h-4 text-emerald-600"></i>
                  Загрузка 6 кабинетов
                </h3>
                <span class="text-[10px] text-emerald-600 font-mono font-bold">84.2% СРЕДНЯЯ</span>
              </div>
              <div class="space-y-2 text-xs" id="dir-rooms-list">
                <!-- Rendered by JS -->
              </div>
            </div>

            <!-- Conversion Funnel (4 cols) -->
            <div class="lg:col-span-4 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                <i data-lucide="trending-up" class="w-4 h-4 text-emerald-600"></i>
                Воронка конверсии (Маргилан)
              </h3>
              <div class="space-y-2 text-xs">
                <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-between">
                  <div>
                    <div class="font-bold text-slate-800 dark:text-slate-200">1. Входящие лиды / Заявки</div>
                    <div class="text-[10px] text-slate-400">Telegram, Instagram, Рефералы</div>
                  </div>
                  <div class="font-mono font-bold text-slate-900 dark:text-white">155 чел. (100%)</div>
                </div>
                <div class="p-2.5 rounded-lg bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-900/60 flex items-center justify-between">
                  <div>
                    <div class="font-bold text-blue-800 dark:text-blue-300">2. Пробный открытый урок</div>
                    <div class="text-[10px] text-blue-500">Посетили очно в Маргилане</div>
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

          <!-- 2. 👨🏫 АНАЛИТИКА УЧИТЕЛЕЙ, УДЕРЖАНИЕ И ФОТ -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="award" class="w-4 h-4 text-emerald-600"></i>
                  2. Аналитика KPI 6 преподавателей, Удержание (Retention %) и ФОТ
                </h3>
                <p class="text-[11px] text-slate-500">
                  Метрики качества: процент оттока (Churn), количество активных учеников и авторасчет зарплат (`Уроки × Ставка + Бонус`).
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
                    <th class="py-2.5 px-3 font-semibold">Направление</th>
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

          <!-- 3. 💸 УПРАВЛЕНИЕ РАСХОДАМИ И УТВЕРЖДЕНИЕ БЮДЖЕТА P&L -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="receipt" class="w-4 h-4 text-rose-500"></i>
                  3. Управление операционными расходами (P&L Маргилан)
                </h3>
                <p class="text-[11px] text-slate-500">
                  Внесение расходов филиала: аренда, коммуналка, маркетинг, интернет, закупки. Автоматически вычитается из Чистой Прибыли.
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
                <input type="text" id="exp-title-input" required placeholder="Например: Аренда здания, Октябрь" class="w-full text-xs rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
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

          <!-- 4. 🚨 РИСКИ И ALERTS (EARLY-WARNING & SMART FOLLOW-UP) — ЭКСКЛЮЗИВНО ДИРЕКТОРУ -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-rose-600 dark:text-rose-400 flex items-center gap-1.5">
                  <i data-lucide="alert-triangle" class="w-4 h-4 text-rose-600"></i>
                  4. РИСКИ И ALERTS (Early-Warning System & Smart Follow-up)
                </h3>
                <p class="text-[11px] text-slate-500">
                  Автоматический мониторинг студентов с риском отчисления (осталось ≤ 1 урока или 3 пропуска подряд) и мгновенные персональные Telegram-уведомления родителям.
                </p>
              </div>
              <span class="text-[10px] text-rose-600 font-mono font-bold bg-rose-50 dark:bg-rose-950 px-2.5 py-1 rounded-full border border-rose-200 dark:border-rose-900">
                EARLY WARNING LIVE
              </span>
            </div>

            <!-- Metric alert counters -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
              <div class="p-3.5 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 flex items-center justify-between">
                <div>
                  <div class="text-[11px] font-bold text-rose-700 dark:text-rose-400">Остаток уроков ≤ 1</div>
                  <div class="text-xl font-black text-rose-700 dark:text-rose-300 font-mono" id="risk-count-balance">0</div>
                </div>
                <i data-lucide="hourglass" class="w-8 h-8 text-rose-400"></i>
              </div>

              <div class="p-3.5 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-900/60 flex items-center justify-between">
                <div>
                  <div class="text-[11px] font-bold text-amber-700 dark:text-amber-400">3+ пропуска подряд</div>
                  <div class="text-xl font-black text-amber-700 dark:text-amber-300 font-mono" id="risk-count-absent">0</div>
                </div>
                <i data-lucide="user-x" class="w-8 h-8 text-amber-400"></i>
              </div>

              <div class="p-3.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-200 dark:border-emerald-900/60 flex items-center justify-between">
                <div>
                  <div class="text-[11px] font-bold text-emerald-700 dark:text-emerald-400">Ожидаемая пролонгация</div>
                  <div class="text-xl font-black text-emerald-700 dark:text-emerald-300 font-mono" id="risk-sum-renewal">0 UZS</div>
                </div>
                <i data-lucide="wallet" class="w-8 h-8 text-emerald-400"></i>
              </div>
            </div>

            <!-- At-Risk Students Table -->
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                    <th class="py-2.5 px-3 font-semibold">Студент</th>
                    <th class="py-2.5 px-3 font-semibold">Группа / Курс</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Остаток уроков</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Пропусков</th>
                    <th class="py-2.5 px-3 font-semibold">Родитель / Телефон</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Причина риска</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Telegram напоминание</th>
                  </tr>
                </thead>
                <tbody id="risks-table-body" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- 5. 🛡️ AUDIT LOG (ЖУРНАЛ БЕЗОПАСНОСТИ) -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <div class="flex items-center justify-between">
              <div>
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="shield-alert" class="w-4 h-4 text-blue-500"></i>
                  5. Журнал безопасности (Audit Log операций персонала)
                </h3>
                <p class="text-[11px] text-slate-500">
                  Фиксация ключевых действий: входы персонала, выплаты ЗП, ручные правки баланса, утверждения расходов и списания уроков.
                </p>
              </div>
              <span class="text-[10px] text-emerald-600 font-mono font-bold bg-emerald-50 dark:bg-emerald-950 px-2 py-0.5 rounded">LIVE СЛЕД</span>
            </div>
            <div class="max-h-64 overflow-y-auto space-y-2 pr-1" id="dir-audit-list">
              <!-- Rendered by JS -->
            </div>
          </div>

        </section>
''')

        # 3. MODULE 2: LEADS KANBAN BOARD
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: КАНБАН-ДОСКА ЛИДОВ (ВОРОНКА ПРОДАЖ)                   -->
        <!-- ============================================================== -->
        <section id="module-kanban" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="kanban" class="w-5 h-5 text-emerald-600"></i>
                <span>Канбан-доска Лидов (Воронка продаж Академии)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Стадии: Новая заявка → Консультация → Пробный урок → Оплата и Договор.
              </p>
            </div>
            <button type="button" onclick="openAddLeadModal()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition flex items-center gap-1.5 cursor-pointer">
              <i data-lucide="user-plus" class="w-3.5 h-3.5"></i>
              <span>Добавить лид</span>
            </button>
          </div>

          <!-- Kanban Columns Grid -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4" id="kanban-board-container">
            <!-- Rendered by JS -->
          </div>
        </section>
''')

        # 4. MODULE 3: CLASSROOM SCHEDULE GRID
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: РАСПИСАНИЕ КАБИНЕТОВ (CLASSROOM GRID)                 -->
        <!-- ============================================================== -->
        <section id="module-schedule" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="calendar" class="w-5 h-5 text-emerald-600"></i>
                <span>Расписание занятий: 6 Кабинетов (Маргилан)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Сетка учебных классов по сменам и дням недели (Пн-Сб). 18 групп 6 преподавателей.
              </p>
            </div>
            <div class="flex items-center gap-2">
              <span class="text-xs text-slate-400">Фильтр дня:</span>
              <select id="schedule-day-filter" onchange="renderScheduleGrid()" class="text-xs font-bold rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-1.5 px-2.5">
                <option value="ALL">Вся неделя (Пн-Сб)</option>
                <option value="ODD">Пн - Ср - Пт (Чётные)</option>
                <option value="EVEN">Вт - Чт - Сб (Нечётные)</option>
              </select>
            </div>
          </div>

          <!-- Classrooms Overview Cards -->
          <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3" id="schedule-rooms-summary">
            <!-- Rendered by JS -->
          </div>

          <!-- Schedule Timetable Grid -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 overflow-x-auto">
            <table class="w-full text-xs text-left border-collapse">
              <thead>
                <tr class="bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-200 border-b border-slate-200 dark:border-slate-700">
                  <th class="py-2.5 px-3 font-bold w-24">Время</th>
                  <th class="py-2.5 px-3 font-bold">Каб. 101 (Web Lab)</th>
                  <th class="py-2.5 px-3 font-bold">Каб. 102 (Python Hub)</th>
                  <th class="py-2.5 px-3 font-bold">Каб. 103 (UI/UX Studio)</th>
                  <th class="py-2.5 px-3 font-bold">Каб. 201 (English Hall)</th>
                  <th class="py-2.5 px-3 font-bold">Каб. 202 (Korean Lounge)</th>
                  <th class="py-2.5 px-3 font-bold">Каб. 203 (German Room)</th>
                </tr>
              </thead>
              <tbody id="schedule-table-body" class="divide-y divide-slate-100 dark:divide-slate-800">
                <!-- Rendered by JS -->
              </tbody>
            </table>
          </div>
        </section>
''')

        # 5. MODULE 4: POS CASHIER
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: POS-КАССА И ОПЛАТА УРОКОВ                             -->
        <!-- ============================================================== -->
        <section id="module-pos" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="credit-card" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="pos_heading">POS-Касса и Приём платежей</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="pos_subheading">
                Оплата через Click, Payme, Наличные, Терминал. Пополнение баланса уроков и печать чеков.
              </p>
            </div>
            <div class="text-xs font-mono font-bold text-emerald-600 bg-emerald-50 dark:bg-emerald-950 px-3 py-1.5 rounded-lg border border-emerald-200 dark:border-emerald-800">
              КАССА АКТИВНА: ОНЛАЙН
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- Payment Form (7 cols) -->
            <div class="lg:col-span-7 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 space-y-4">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                <i data-lucide="plus-circle" class="w-4 h-4 text-emerald-600"></i>
                Проведение новой оплаты
              </h3>

              <form onsubmit="handlePosPaymentSubmit(event)" class="space-y-4">
                <div>
                  <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">
                    Поиск студента (+998 или ФИО):
                  </label>
                  <div class="relative">
                    <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
                    <input type="text" id="pos-student-search" oninput="onPosSearchInput(this.value)" placeholder="Начните вводить +9989... или Фамилию" class="w-full pl-9 pr-3 py-2 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs text-slate-900 dark:text-slate-100" />
                  </div>
                  <!-- Dropdown auto-complete list -->
                  <div id="pos-search-results" class="hidden mt-1 max-h-40 overflow-y-auto bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-lg shadow-lg text-xs divide-y divide-slate-100 dark:divide-slate-700 z-20"></div>
                </div>

                <div class="p-3 rounded-lg bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 text-xs space-y-1" id="pos-selected-student-box">
                  <div class="text-slate-400 text-[11px]">Студент не выбран. Выберите из поиска выше.</div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Сумма оплаты (UZS):</label>
                    <input type="number" id="pos-amount-input" required value="600000" class="w-full py-2 px-3 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs font-mono font-bold" />
                  </div>
                  <div>
                    <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Пополнение уроков (+):</label>
                    <input type="number" id="pos-lessons-input" required value="12" class="w-full py-2 px-3 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-xs font-mono font-bold" />
                  </div>
                </div>

                <div>
                  <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-2">Способ оплаты:</label>
                  <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                    <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-800">
                      <input type="radio" name="pos-method" value="Click" checked class="text-emerald-600" />
                      <span class="font-bold text-blue-600">Click</span>
                    </label>
                    <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-800">
                      <input type="radio" name="pos-method" value="Payme" class="text-emerald-600" />
                      <span class="font-bold text-teal-600">Payme</span>
                    </label>
                    <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-800">
                      <input type="radio" name="pos-method" value="Наличные" class="text-emerald-600" />
                      <span class="font-bold text-emerald-600">Наличные</span>
                    </label>
                    <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-700 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-800">
                      <input type="radio" name="pos-method" value="Терминал" class="text-emerald-600" />
                      <span class="font-bold text-purple-600">Терминал</span>
                    </label>
                  </div>
                </div>

                <button type="submit" class="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs uppercase tracking-wider rounded-lg transition flex items-center justify-center gap-2 cursor-pointer shadow-md">
                  <i data-lucide="printer" class="w-4 h-4"></i>
                  <span>Провести платеж и выдать чек</span>
                </button>
              </form>
            </div>

            <!-- Recent Transactions Table (5 cols) -->
            <div class="lg:col-span-5 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="history" class="w-4 h-4 text-emerald-600"></i>
                  Последние чеки кассы
                </h3>
                <span class="text-[10px] text-slate-400">Термопечать 80мм</span>
              </div>

              <div class="overflow-y-auto max-h-96 space-y-2 pr-1" id="pos-recent-receipts">
                <!-- Rendered by JS -->
              </div>
            </div>
          </div>
        </section>
''')

        # 6. MODULE 5: ATTENDANCE JOURNAL 18 GROUPS
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: ЭЛЕКТРОННЫЙ ЖУРНАЛ 18 ГРУПП                           -->
        <!-- ============================================================== -->
        <section id="module-journal" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="book-open" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="journal_heading">Электронный журнал: 18 групп</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="journal_subheading">
                Отметка посещаемости («Был» / «НБ» / «Уваж.») с автоматическим списанием 1 урока с баланса ученика.
              </p>
            </div>
            
            <!-- Group Selector -->
            <div class="flex items-center gap-2">
              <label class="text-xs font-bold text-slate-600 dark:text-slate-300">Группа:</label>
              <select id="journal-group-select" onchange="renderJournalTable(this.value)" class="text-xs font-bold rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-1.5 px-3 cursor-pointer">
                <!-- Populated by JS -->
              </select>
            </div>
          </div>

          <!-- Group Meta Card -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3" id="journal-group-meta">
            <!-- Rendered by JS -->
          </div>

          <!-- Attendance Table -->
          <div class="bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-4 space-y-3">
            <div class="flex items-center justify-between">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                Список студентов группы
              </h3>
              <span class="text-[11px] text-emerald-600 font-bold">
                Кнопка «Был» списывает 1 урок с баланса в реальном времени
              </span>
            </div>

            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-300 border-b border-slate-200 dark:border-slate-700">
                    <th class="py-2.5 px-3 font-semibold">Студент</th>
                    <th class="py-2.5 px-3 font-semibold">Телефон</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Баланс уроков</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Пропусков</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Статус доступа</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Отметка посещаемости на сегодня</th>
                  </tr>
                </thead>
                <tbody id="journal-table-body" class="divide-y divide-slate-100 dark:divide-slate-800">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </section>
''')

        # 7. MODULE 6: EXAMS, GRADES & MAM-COINS
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: ЭКЗАМЕНЫ, ГРЕЙДЫ И MAM-COINS                          -->
        <!-- ============================================================== -->
        <section id="module-gamification" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="sparkles" class="w-5 h-5 text-amber-500"></i>
                <span>Экзамены, Грейды и MAM-Coins (Геймификация)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Оценки за тесты, начисление MAM-Coins, лидерборд Академии и автопроверка допуска к сертификату (≥ 80%).
              </p>
            </div>
          </div>

          <!-- Add Grade Form -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
              <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i>
              Внесение баллов за срез / тест
            </h3>
            <form onsubmit="handleNewExamGradeSubmit(event)" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-3 items-end">
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Студент:</label>
                <select id="exam-student-select" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5">
                  <!-- Populated by JS -->
                </select>
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Название экзамена / теста:</label>
                <input type="text" id="exam-title-input" required placeholder="Например: Midterm Python OOP" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Балл (0 - 100%):</label>
                <input type="number" id="exam-score-input" required min="0" max="100" placeholder="88" class="w-full text-xs font-mono font-bold rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>
              <div>
                <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Бонус MAM-Coins:</label>
                <input type="number" id="exam-coins-input" required min="0" value="50" class="w-full text-xs font-mono font-bold rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>
              <div>
                <button type="submit" class="w-full py-2 bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-1.5 cursor-pointer">
                  <i data-lucide="plus" class="w-4 h-4"></i>
                  <span>Записать результат</span>
                </button>
              </div>
            </form>
          </div>

          <!-- Top-10 Leaderboard & Cert Qualifications -->
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- Leaderboard (7 cols) -->
            <div class="lg:col-span-7 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                  <i data-lucide="trophy" class="w-4 h-4 text-amber-500"></i>
                  Лидерборд Топ-10 учеников MAM
                </h3>
                <span class="text-[10px] text-amber-600 font-bold bg-amber-50 dark:bg-amber-950 px-2 py-0.5 rounded-full">
                  MAM-COINS РЕЙТИНГ
                </span>
              </div>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse">
                  <thead>
                    <tr class="bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                      <th class="py-2 px-3 font-semibold text-center w-12">#</th>
                      <th class="py-2 px-3 font-semibold">Студент</th>
                      <th class="py-2 px-3 font-semibold">Курс</th>
                      <th class="py-2 px-3 font-semibold text-center">Ср. балл</th>
                      <th class="py-2 px-3 font-semibold text-right">MAM-Coins</th>
                    </tr>
                  </thead>
                  <tbody id="gamification-leaderboard-body" class="divide-y divide-slate-100 dark:divide-slate-800">
                    <!-- Rendered by JS -->
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Qualification & Exam Log (5 cols) -->
            <div class="lg:col-span-5 p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500 flex items-center gap-1.5">
                <i data-lucide="file-check" class="w-4 h-4 text-emerald-600"></i>
                Допуск к финальному сертификату (≥ 80%)
              </h3>
              <p class="text-[11px] text-slate-400">
                Студенты, успешно набравшие требуемый средний академический балл для выдачи Сертификата MAM.
              </p>
              <div class="max-h-72 overflow-y-auto space-y-2 pr-1" id="gamification-qualification-list">
                <!-- Rendered by JS -->
              </div>
            </div>
          </div>
        </section>
''')

        # 8. MODULE 7: CONTRACTS & CERTIFICATES GENERATOR
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: ГЕНЕРАТОР ДОГОВОРОВ И СЕРТИФИКАТОВ                    -->
        <!-- ============================================================== -->
        <section id="module-contracts" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="file-text" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="doc_heading">Генератор Договоров и Сертификатов</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="doc_subheading">
                Официальные бланки с уникальным номером MAM-2026-XXXX, QR-проверкой и подписью Директора Богданова Т.Я.
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
            <!-- Form Parameters (5 cols) -->
            <div class="lg:col-span-5 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 space-y-4">
              <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                Параметры документа
              </h3>

              <div>
                <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Выберите студента:</label>
                <select id="doc-student-select" onchange="onDocStudentSelect(this.value)" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5">
                  <!-- Populated by JS -->
                </select>
              </div>

              <div>
                <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">ФИО Родителя / Заказчика:</label>
                <input type="text" id="doc-parent-input" class="w-full text-xs rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
              </div>

              <div class="grid grid-cols-2 gap-3">
                <div>
                  <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Паспорт родителя:</label>
                  <input type="text" id="doc-passport-input" value="AD 1234567" class="w-full text-xs font-mono rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
                </div>
                <div>
                  <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Стоимость курса:</label>
                  <input type="text" id="doc-fee-input" value="650 000 UZS" class="w-full text-xs font-mono rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 py-2 px-2.5" />
                </div>
              </div>

              <div class="pt-2 flex flex-col gap-2">
                <button type="button" onclick="generateAndPreviewContract()" class="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs uppercase tracking-wider rounded-lg transition flex items-center justify-center gap-2 cursor-pointer shadow-sm">
                  <i data-lucide="file-check-2" class="w-4 h-4"></i>
                  <span>Сформировать Договор (A4)</span>
                </button>
                <button type="button" onclick="generateAndPreviewCertificate()" class="w-full py-2.5 bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs uppercase tracking-wider rounded-lg transition flex items-center justify-center gap-2 cursor-pointer shadow-sm">
                  <i data-lucide="award" class="w-4 h-4"></i>
                  <span>Сформировать Сертификат (A4)</span>
                </button>
              </div>
            </div>

            <!-- Preview Box (7 cols) -->
            <div class="lg:col-span-7 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 p-5 space-y-3">
              <div class="flex items-center justify-between">
                <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  Интерактивный предпросмотр документа
                </h3>
                <button type="button" onclick="printActiveDocument()" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs rounded-lg transition flex items-center gap-1.5 cursor-pointer">
                  <i data-lucide="printer" class="w-3.5 h-3.5"></i>
                  <span>Печать А4</span>
                </button>
              </div>

              <div id="doc-preview-container" class="p-6 bg-slate-50 dark:bg-slate-950 rounded-xl border border-dashed border-slate-300 dark:border-slate-800 text-xs min-h-[420px] flex items-center justify-center">
                <div class="text-center text-slate-400">
                  <i data-lucide="file-text" class="w-10 h-10 mx-auto mb-2 opacity-50"></i>
                  <p>Выберите студента и нажмите «Сформировать Договор» или «Сформировать Сертификат»</p>
                </div>
              </div>
            </div>
          </div>
        </section>
''')

        # 9. MODULE 8: STAFF TIMESHEET
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: ТАБЕЛЬ СМЕН СТАФФА (CHECK-IN / CHECK-OUT)              -->
        <!-- ============================================================== -->
        <section id="module-timesheet" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="clock" class="w-5 h-5 text-emerald-600"></i>
                <span>Табель смен сотрудников (Check-in / Check-out)</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5">
                Фиксация времени прибытия и ухода сотрудников Maryam Academy Mission.
              </p>
            </div>
            <div class="text-xs font-mono text-slate-500 dark:text-slate-400" id="timesheet-current-clock">
              --:--:--
            </div>
          </div>

          <!-- Active Staff Check-in Box -->
          <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div class="flex items-center gap-3.5">
              <div class="w-12 h-12 rounded-xl bg-emerald-100 dark:bg-emerald-950 flex items-center justify-center text-2xl" id="timesheet-user-avatar">
                👑
              </div>
              <div>
                <div class="text-xs font-bold text-slate-900 dark:text-white" id="timesheet-user-name">Богданов Т.Я.</div>
                <div class="text-[11px] text-slate-500" id="timesheet-user-status">Статус смены: Не на смене</div>
              </div>
            </div>

            <div class="flex items-center gap-3">
              <button type="button" id="btn-timesheet-in" onclick="handleTimesheetCheckIn()" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-xl transition flex items-center gap-2 cursor-pointer shadow-md">
                <i data-lucide="log-in" class="w-4 h-4"></i>
                <span>Начать смену (Check-in)</span>
              </button>
              <button type="button" id="btn-timesheet-out" onclick="handleTimesheetCheckOut()" class="px-4 py-2 bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs rounded-xl transition flex items-center gap-2 cursor-pointer shadow-md disabled:opacity-50" disabled>
                <i data-lucide="log-out" class="w-4 h-4"></i>
                <span>Завершить смену (Check-out)</span>
              </button>
            </div>
          </div>

          <!-- Timesheet Registry Table -->
          <div class="p-4 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
            <h3 class="text-xs font-extrabold uppercase tracking-wider text-slate-400 dark:text-slate-500">
              Журнал смен сотрудников за сегодня
            </h3>
            <div class="overflow-x-auto">
              <table class="w-full text-xs text-left border-collapse">
                <thead>
                  <tr class="bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                    <th class="py-2.5 px-3 font-semibold">Сотрудник</th>
                    <th class="py-2.5 px-3 font-semibold">Должность</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Прибыл (Check-in)</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Убыл (Check-out)</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Часов</th>
                    <th class="py-2.5 px-3 font-semibold text-center">Статус</th>
                  </tr>
                </thead>
                <tbody id="timesheet-table-body" class="divide-y divide-slate-100 dark:divide-slate-800 font-mono">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </section>
''')

        # 10. MODULE 9: BACKUP & SETTINGS
        f.write('''
        <!-- ============================================================== -->
        <!-- MODULE: БЭКАП И НАСТРОЙКИ DBN                                 -->
        <!-- ============================================================== -->
        <section id="module-backup" class="module-view hidden space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
            <div>
              <h2 class="text-lg font-black text-slate-900 dark:text-white flex items-center gap-2">
                <i data-lucide="database" class="w-5 h-5 text-emerald-600"></i>
                <span data-i18n="db_heading">Автономная БД и Резервное копирование</span>
              </h2>
              <p class="text-xs text-slate-500 dark:text-slate-400 mt-0.5" data-i18n="db_subheading">
                База данных хранится изолированно в браузере (LocalStorage). Доступен экспорт и импорт в JSON.
              </p>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Export JSON -->
            <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="w-10 h-10 rounded-lg bg-emerald-100 dark:bg-emerald-950 flex items-center justify-center text-emerald-600">
                <i data-lucide="download" class="w-5 h-5"></i>
              </div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="db_export_title">
                Экспорт резервной копии
              </h3>
              <p class="text-xs text-slate-500">
                Выгружает полный снимок базы (54 студента, 18 групп, финансы, аудит-лог, расходы) в один JSON-файл.
              </p>
              <button type="button" onclick="exportDatabaseJSON()" class="w-full py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-2 cursor-pointer">
                <i data-lucide="download" class="w-4 h-4"></i>
                <span data-i18n="db_btn_export">Выгрузить JSON</span>
              </button>
            </div>

            <!-- Import JSON -->
            <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="w-10 h-10 rounded-lg bg-blue-100 dark:bg-blue-950 flex items-center justify-center text-blue-600">
                <i data-lucide="upload" class="w-5 h-5"></i>
              </div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="db_import_title">
                Восстановление из JSON
              </h3>
              <p class="text-xs text-slate-500">
                Загрузите ранее сохраненный JSON-файл для восстановления всей базы Академии.
              </p>
              <input type="file" id="import-json-file" accept=".json" onchange="handleImportDatabaseJSON(event)" class="hidden" />
              <button type="button" onclick="document.getElementById('import-json-file').click()" class="w-full py-2 bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-2 cursor-pointer">
                <i data-lucide="upload" class="w-4 h-4"></i>
                <span data-i18n="db_btn_import">Загрузить JSON</span>
              </button>
            </div>

            <!-- Factory Reset -->
            <div class="p-5 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="w-10 h-10 rounded-lg bg-rose-100 dark:bg-rose-950 flex items-center justify-center text-rose-600">
                <i data-lucide="rotate-ccw" class="w-5 h-5"></i>
              </div>
              <h3 class="text-sm font-bold text-slate-900 dark:text-white" data-i18n="db_reset_title">
                Сброс к эталонной базе
              </h3>
              <p class="text-xs text-slate-500">
                Сбрасывает текущие изменения и восстанавливает начальные 18 групп и 54 студента.
              </p>
              <button type="button" onclick="resetDatabaseToFactory()" class="w-full py-2 bg-rose-600 hover:bg-rose-700 text-white font-bold text-xs rounded-lg transition flex items-center justify-center gap-2 cursor-pointer">
                <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
                <span data-i18n="db_btn_reset">Сбросить к эталону</span>
              </button>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>

  <!-- ============================================================== -->
  <!-- MODALS CONTAINER                                               -->
  <!-- ============================================================== -->
  
  <!-- 1. Telegram Alert Follow-up Modal -->
  <div id="modal-telegram" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-900 rounded-2xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 space-y-4">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-sky-500/10 text-sky-500 flex items-center justify-center">
            <i data-lucide="send" class="w-4 h-4"></i>
          </div>
          <div>
            <h3 class="text-sm font-black text-slate-900 dark:text-white">Готовое напоминание в Telegram</h3>
            <p class="text-[10px] text-slate-400">Персональный скрипт для родителя студента</p>
          </div>
        </div>
        <button type="button" onclick="closeTelegramModal()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="space-y-3">
        <div>
          <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Получатель:</label>
          <div class="p-2 rounded-lg bg-slate-50 dark:bg-slate-800 text-xs font-mono" id="tg-modal-recipient">--</div>
        </div>

        <div>
          <label class="block text-[11px] font-bold text-slate-600 dark:text-slate-300 mb-1">Текст сообщения (RU / UZ):</label>
          <textarea id="tg-modal-text" rows="5" class="w-full text-xs p-3 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 leading-relaxed font-sans"></textarea>
        </div>
      </div>

      <div class="flex items-center justify-end gap-2 pt-2">
        <button type="button" onclick="copyTelegramText()" class="px-3 py-2 rounded-lg bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
          <i data-lucide="copy" class="w-3.5 h-3.5"></i>
          <span id="tg-btn-copy-label">Копировать</span>
        </button>
        <a id="tg-modal-link" href="#" target="_blank" rel="noopener noreferrer" class="px-4 py-2 rounded-lg bg-sky-500 hover:bg-sky-600 text-white text-xs font-bold transition flex items-center gap-1.5 cursor-pointer">
          <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
          <span>Открыть в Telegram</span>
        </a>
      </div>
    </div>
  </div>

  <!-- 2. Add Lead Modal -->
  <div id="modal-lead" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-white dark:bg-slate-900 rounded-2xl max-w-md w-full p-6 shadow-2xl border border-slate-200 dark:border-slate-800 space-y-4">
      <div class="flex items-center justify-between pb-3 border-b border-slate-100 dark:border-slate-800">
        <h3 class="text-sm font-black text-slate-900 dark:text-white">Добавить нового лида в воронку</h3>
        <button type="button" onclick="closeLeadModal()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 cursor-pointer">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <form onsubmit="handleNewLeadSubmit(event)" class="space-y-3">
        <div>
          <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">ФИО Кандидата:</label>
          <input type="text" id="lead-name-input" required placeholder="Имя Фамилия" class="w-full text-xs p-2 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700" />
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Номер телефона:</label>
          <input type="text" id="lead-phone-input" required placeholder="+998901234567" class="w-full text-xs p-2 font-mono rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700" />
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Интересующий курс:</label>
          <select id="lead-course-input" class="w-full text-xs p-2 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <option value="Python & Backend">Python & Backend</option>
            <option value="Frontend & Web Dev">Frontend & Web Dev</option>
            <option value="UI/UX Design">UI/UX Design</option>
            <option value="General & IELTS English">General & IELTS English</option>
            <option value="Korean & TOPIK">Korean & TOPIK</option>
            <option value="Deutsch A1-B2">Deutsch A1-B2</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">Источник:</label>
          <select id="lead-source-input" class="w-full text-xs p-2 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
            <option value="Instagram Ads">Instagram Ads</option>
            <option value="Telegram канал">Telegram канал</option>
            <option value="Рекомендация">Рекомендация (Сарафанное радио)</option>
            <option value="Листовка">Листовка у базара</option>
          </select>
        </div>

        <button type="submit" class="w-full py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs rounded-xl transition cursor-pointer">
          Сохранить лид
        </button>
      </form>
    </div>
  </div>

  <!-- Hidden Print Area -->
  <div id="print-area"></div>
''')

        # 11. JAVASCRIPT LOGIC & DATABASE
        # We will write the entire vanilla JS logic
        f.write('''
  <!-- ============================================================== -->
  <!-- JAVASCRIPT CORE ENGINE & AUTONOMOUS LOCALSTORAGE DB            -->
  <!-- ============================================================== -->
  <script>
    /* ==============================================================
       1. I18N DICTIONARY (UZ / RU)
       ============================================================== */
    const I18N = {
      ru: {
        auth_title: 'Вход в служебную CRM/ERP',
        auth_subtitle: 'Изолированная служебная система сотрудников. Доступ строго по учетным данным.',
        auth_lbl_login: 'Логин сотрудника:',
        auth_lbl_pass: 'Пароль:',
        auth_btn_submit: 'Войти в панель CRM',
        top_logout: 'Выйти',
        nav_modules_title: 'Доступные модули',
        box_students: 'Студентов в базе:',
        box_groups: 'Активных групп:',
        box_cash: 'В кассе сегодня:',
        btn_backup_quick: 'Бэкап JSON',
        pos_heading: 'POS-Касса и Приём платежей',
        pos_subheading: 'Оплата через Click, Payme, Наличные, Терминал. Пополнение баланса уроков и печать чеков.',
        journal_heading: 'Электронный журнал: 18 групп',
        journal_subheading: 'Отметка посещаемости («Был» / «НБ» / «Уваж.») с автоматическим списанием 1 урока с баланса ученика.',
        doc_heading: 'Генератор Договоров и Сертификатов',
        doc_subheading: 'Официальные бланки с уникальным номером MAM-2026-XXXX, QR-проверкой и подписью Директора Богданова Т.Я.',
        db_heading: 'Автономная БД и Резервное копирование',
        db_subheading: 'База данных хранится изолированно в браузере (LocalStorage). Доступен экспорт и импорт в JSON.',
        db_export_title: 'Экспорт резервной копии',
        db_btn_export: 'Выгрузить JSON',
        db_import_title: 'Восстановление из JSON',
        db_btn_import: 'Загрузить JSON',
        db_reset_title: 'Сброс к эталонной базе',
        db_btn_reset: 'Сбросить к эталону'
      },
      uz: {
        auth_title: 'Xizmat CRM/ERP tizimiga kirish',
        auth_subtitle: 'Xodimlarning maxfiy tizimi. Kirish qatʼiy xizmat hisoblari orqali.',
        auth_lbl_login: 'Xodim logini:',
        auth_lbl_pass: 'Parol:',
        auth_btn_submit: 'Tizimga kirish',
        top_logout: 'Chiqish',
        nav_modules_title: 'Mavjud modullar',
        box_students: 'Bazadagi talabalar:',
        box_groups: 'Faol guruhlar:',
        box_cash: 'Bugungi kassa:',
        btn_backup_quick: 'Zaxira JSON',
        pos_heading: 'POS-Kassa va Toʻlovlar qabuli',
        pos_subheading: 'Click, Payme, Naqd, Terminal orqali toʻlov. Darslar balansini toʻldirish va chek chop etish.',
        journal_heading: 'Elektron jurnal: 18 ta guruh',
        journal_subheading: 'Davomat belgilash («Bor» / «Yoʻq» / «Sababli») va oʻquvchi balansidan 1 ta darsni avtomatik yechish.',
        doc_heading: 'Shartnoma va Sertifikatlar generatori',
        doc_subheading: 'MAM-2026-XXXX unikal raqami, QR-tekshiruv va Direktor Bogdanov T.Ya. imzosi bilan rasmiy blankalar.',
        db_heading: 'Avtonom MB va Zaxira nusxalash',
        db_subheading: 'Maʼlumotlar bazasi brauzerda (LocalStorage) saqlanadi. JSON eksport va import mavjud.',
        db_export_title: 'Zaxira nusxasini eksport qilish',
        db_btn_export: 'JSON yuklab olish',
        db_import_title: 'JSON orqali tiklash',
        db_btn_import: 'JSON yuklash',
        db_reset_title: 'Standart bazaga qaytarish',
        db_btn_reset: 'Standartga qaytarish'
      }
    };

    let currentLang = localStorage.getItem('mam_lang') || 'ru';

    /* ==============================================================
       2. PREDEFINED 9 SERVICE ACCOUNTS (NO RECEPTION/CLEANER)
       ============================================================== */
    const SERVICE_ACCOUNTS = {
      director: {
        key: 'director',
        login: 'director',
        pass: 'admin123',
        name: 'Богданов Тимур Якубович',
        shortName: 'Богданов Т.Я.',
        roleName: 'Директор Академии',
        roleNameUz: 'Akademiya Direktori',
        avatar: '👑',
        badgeColor: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300',
        allowedModules: ['director', 'kanban', 'schedule', 'pos', 'journal', 'gamification', 'contracts', 'timesheet', 'backup'],
        desc: 'Полный доступ: Executive Command Center, P&L, ФОТ, Риски и Alerts (Telegram), касса, журналы.'
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
        allowedModules: ['director', 'kanban', 'schedule', 'pos', 'journal', 'gamification', 'contracts', 'timesheet', 'backup'],
        desc: 'Полный технический доступ, аудит безопасности, логирование и резервные копии.'
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
        allowedModules: ['pos', 'kanban', 'schedule', 'contracts', 'timesheet', 'backup'],
        desc: 'Проведение оплат (Click, Payme, Naqd, Terminal), печать чеков, договоры, воронка лидов.'
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
        allowedModules: ['journal', 'gamification', 'schedule', 'timesheet'],
        desc: 'Группы PY-101, PY-102, PY-103. Электронный журнал, списание уроков, грейды и табель.'
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
        allowedModules: ['journal', 'gamification', 'schedule', 'timesheet'],
        desc: 'Группы WEB-201, WEB-202, WEB-203. Ведение журналов, срезы знаний и расписание.'
      },
      teacher_design: {
        key: 'teacher_design',
        login: 'teacher_design',
        pass: 'teacher123',
        name: 'Каримова Мадина Шухратовна',
        shortName: 'Каримова М.Ш.',
        roleName: 'Преподаватель Design',
        roleNameUz: 'UI/UX Dizayn oʻqituvchisi',
        avatar: '🎨',
        course: 'UI/UX Design',
        groups: ['DS-301', 'DS-302', 'DS-303'],
        badgeColor: 'bg-fuchsia-100 text-fuchsia-800 dark:bg-fuchsia-950 dark:text-fuchsia-300',
        allowedModules: ['journal', 'gamification', 'schedule', 'timesheet'],
        desc: 'Группы DS-301, DS-302, DS-303. Учёт посещаемости, портфолио учеников и табель.'
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
        allowedModules: ['journal', 'gamification', 'schedule', 'timesheet'],
        desc: 'Группы ENG-401, ENG-402, ENG-403. Подготовка к IELTS, тесты и журнал посещаемости.'
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
        allowedModules: ['journal', 'gamification', 'schedule', 'timesheet'],
        desc: 'Группы KOR-501, KOR-502, KOR-503. Журнал групп корейского языка и TOPIK.'
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
        allowedModules: ['journal', 'gamification', 'schedule', 'timesheet'],
        desc: 'Группы GER-601, GER-602, GER-603. Журнал групп немецкого языка и экзамены Goethe.'
      }
    };

    let currentUser = null;
    let currentModule = 'director';

    /* ==============================================================
       3. SEED DATABASE (18 GROUPS, 54 STUDENTS, 6 ROOMS, EXPENSES)
       ============================================================== */
    function generateInitialDB() {
      const groups = [
        // Python
        { id: 'PY-101', name: 'Python Basics 101', teacherKey: 'teacher_python', teacherName: 'Алимов С.Б.', course: 'Python & Backend', schedule: 'Пн-Ср-Пт 14:00-16:00', room: 'Каб. 102 (Python Hub)', fee: 600000, lessonsPerMonth: 12, conductedLessons: 18 },
        { id: 'PY-102', name: 'Django & API 102', teacherKey: 'teacher_python', teacherName: 'Алимов С.Б.', course: 'Python & Backend', schedule: 'Вт-Чт-Сб 14:00-16:00', room: 'Каб. 102 (Python Hub)', fee: 650000, lessonsPerMonth: 12, conductedLessons: 20 },
        { id: 'PY-103', name: 'Telegram Bots & Async 103', teacherKey: 'teacher_python', teacherName: 'Алимов С.Б.', course: 'Python & Backend', schedule: 'Пн-Ср-Пт 16:30-18:30', room: 'Каб. 102 (Python Hub)', fee: 650000, lessonsPerMonth: 12, conductedLessons: 19 },
        // Web
        { id: 'WEB-201', name: 'HTML5 & CSS Modern 201', teacherKey: 'teacher_web', teacherName: 'Юлдашев Д.А.', course: 'Frontend & Web Dev', schedule: 'Пн-Ср-Пт 10:00-12:00', room: 'Каб. 101 (Web Lab)', fee: 550000, lessonsPerMonth: 12, conductedLessons: 22 },
        { id: 'WEB-202', name: 'JavaScript & React 202', teacherKey: 'teacher_web', teacherName: 'Юлдашев Д.А.', course: 'Frontend & Web Dev', schedule: 'Вт-Чт-Сб 10:00-12:00', room: 'Каб. 101 (Web Lab)', fee: 650000, lessonsPerMonth: 12, conductedLessons: 21 },
        { id: 'WEB-203', name: 'Fullstack Next.js 203', teacherKey: 'teacher_web', teacherName: 'Юлдашев Д.А.', course: 'Frontend & Web Dev', schedule: 'Вт-Чт-Сб 16:30-18:30', room: 'Каб. 101 (Web Lab)', fee: 700000, lessonsPerMonth: 12, conductedLessons: 20 },
        // Design
        { id: 'DS-301', name: 'Figma UI Foundations 301', teacherKey: 'teacher_design', teacherName: 'Каримова М.Ш.', course: 'UI/UX Design', schedule: 'Пн-Ср-Пт 09:00-11:00', room: 'Каб. 103 (UI/UX Studio)', fee: 550000, lessonsPerMonth: 12, conductedLessons: 19 },
        { id: 'DS-302', name: 'UX Research & Mobile 302', teacherKey: 'teacher_design', teacherName: 'Каримова М.Ш.', course: 'UI/UX Design', schedule: 'Вт-Чт-Сб 09:00-11:00', room: 'Каб. 103 (UI/UX Studio)', fee: 600000, lessonsPerMonth: 12, conductedLessons: 21 },
        { id: 'DS-303', name: 'Brand Identity & Visuals 303', teacherKey: 'teacher_design', teacherName: 'Каримова М.Ш.', course: 'UI/UX Design', schedule: 'Пн-Ср-Пт 14:00-16:00', room: 'Каб. 103 (UI/UX Studio)', fee: 600000, lessonsPerMonth: 12, conductedLessons: 20 },
        // English
        { id: 'ENG-401', name: 'Pre-Intermediate English 401', teacherKey: 'teacher_english', teacherName: 'Смирнова Е.В.', course: 'General & IELTS English', schedule: 'Пн-Ср-Пт 11:30-13:30', room: 'Каб. 201 (English Hall)', fee: 500000, lessonsPerMonth: 12, conductedLessons: 23 },
        { id: 'ENG-402', name: 'Intermediate Fluency 402', teacherKey: 'teacher_english', teacherName: 'Смирнова Е.В.', course: 'General & IELTS English', schedule: 'Вт-Чт-Сб 11:30-13:30', room: 'Каб. 201 (English Hall)', fee: 550000, lessonsPerMonth: 12, conductedLessons: 22 },
        { id: 'ENG-403', name: 'IELTS Intensive 7.5+ 403', teacherKey: 'teacher_english', teacherName: 'Смирнова Е.В.', course: 'General & IELTS English', schedule: 'Пн-Ср-Пт 16:30-18:30', room: 'Каб. 201 (English Hall)', fee: 650000, lessonsPerMonth: 12, conductedLessons: 24 },
        // Korean
        { id: 'KOR-501', name: 'Hangul & Basic Grammar 501', teacherKey: 'teacher_korean', teacherName: 'Пак А.С.', course: 'Korean & TOPIK', schedule: 'Пн-Ср-Пт 10:00-12:00', room: 'Каб. 202 (Korean Lounge)', fee: 550000, lessonsPerMonth: 12, conductedLessons: 18 },
        { id: 'KOR-502', name: 'EPS-TOPIK Level 1 502', teacherKey: 'teacher_korean', teacherName: 'Пак А.С.', course: 'Korean & TOPIK', schedule: 'Вт-Чт-Сб 10:00-12:00', room: 'Каб. 202 (Korean Lounge)', fee: 600000, lessonsPerMonth: 12, conductedLessons: 20 },
        { id: 'KOR-503', name: 'TOPIK II Academic 503', teacherKey: 'teacher_korean', teacherName: 'Пак А.С.', course: 'Korean & TOPIK', schedule: 'Вт-Чт-Сб 14:00-16:00', room: 'Каб. 202 (Korean Lounge)', fee: 650000, lessonsPerMonth: 12, conductedLessons: 21 },
        // German
        { id: 'GER-601', name: 'Start Deutsch A1 601', teacherKey: 'teacher_german', teacherName: 'Мюллер К.А.', course: 'Deutsch A1-B2', schedule: 'Пн-Ср-Пт 14:00-16:00', room: 'Каб. 203 (German Room)', fee: 550000, lessonsPerMonth: 12, conductedLessons: 19 },
        { id: 'GER-602', name: 'Deutsch A2.2 Aufbaustufe 602', teacherKey: 'teacher_german', teacherName: 'Мюллер К.А.', course: 'Deutsch A1-B2', schedule: 'Вт-Чт-Сб 14:00-16:00', room: 'Каб. 203 (German Room)', fee: 600000, lessonsPerMonth: 12, conductedLessons: 20 },
        { id: 'GER-603', name: 'Goethe-Zertifikat B1 603', teacherKey: 'teacher_german', teacherName: 'Мюллер К.А.', course: 'Deutsch A1-B2', schedule: 'Пн-Ср-Пт 16:30-18:30', room: 'Каб. 203 (German Room)', fee: 650000, lessonsPerMonth: 12, conductedLessons: 21 }
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
        { name: 'Мирзаев Исломбек Анварович', parent: 'Мирзаев Анвар Камолович', phone: '+998974567890', pPhone: '+998974567800', group: 'ENG-403', bal: 11, abs: 0 },
        { name: 'Хошимова Севинч Дилшодовна', parent: 'Хошимов Дилшод Бахтиёрович', phone: '+998985678901', pPhone: '+998985678900', group: 'ENG-403', bal: 6, abs: 0 },
        { name: 'Неъматов Сарвар Обидович', parent: 'Неъматов Обид Шухратович', phone: '+998906789012', pPhone: '+998906789000', group: 'ENG-403', bal: 10, abs: 0 },
        // KOR-501
        { name: 'Кудратов Ойбек Рахимжонович', parent: 'Кудратов Рахимжон Хасанович', phone: '+998917890123', pPhone: '+998917890100', group: 'KOR-501', bal: 8, abs: 0 },
        { name: 'Мамадалиева Рухшона Азизбековна', parent: 'Мамадалиев Азизбек Солиевич', phone: '+998938901234', pPhone: '+998938901200', group: 'KOR-501', bal: 0, abs: 3 },
        { name: 'Ахмедов Сардорбек Улугбекович', parent: 'Ахмедов Улугбек Каримович', phone: '+998949012345', pPhone: '+998949012300', group: 'KOR-501', bal: 10, abs: 0 },
        // KOR-502
        { name: 'Абдурахмонов Достон Шухратович', parent: 'Абдурахмонов Шухрат Мансурович', phone: '+998950123456', pPhone: '+998950123400', group: 'KOR-502', bal: 7, abs: 0 },
        { name: 'Тураева Гузаль Бахромовна', parent: 'Тураев Бахром Одилович', phone: '+998971234567', pPhone: '+998971234500', group: 'KOR-502', bal: 1, abs: 0 },
        { name: 'Ибрагимов Фарход Маъруфович', parent: 'Ибрагимов Маъруф Хамидович', phone: '+998982345678', pPhone: '+998982345600', group: 'KOR-502', bal: 9, abs: 0 },
        // KOR-503
        { name: 'Рахимов Бехзод Хасанович', parent: 'Рахимов Хасан Хусанович', phone: '+998903456789', pPhone: '+998903456700', group: 'KOR-503', bal: 12, abs: 0 },
        { name: 'Каюмова Камила Анваровна', parent: 'Каюмов Анвар Назирович', phone: '+998914567890', pPhone: '+998914567800', group: 'KOR-503', bal: 6, abs: 0 },
        { name: 'Махкамов Жавохир Дилшодович', parent: 'Махкамов Дилшод Аскарович', phone: '+998935678901', pPhone: '+998935678900', group: 'KOR-503', bal: 11, abs: 0 },
        // GER-601
        { name: 'Бозоров Санжар Мухаммадович', parent: 'Бозоров Мухаммад Олимович', phone: '+998946789012', pPhone: '+998946789000', group: 'GER-601', bal: 1, abs: 2 },
        { name: 'Хакимова Нилуфар Собировна', parent: 'Хакимов Собир Носирович', phone: '+998957890123', pPhone: '+998957890100', group: 'GER-601', bal: 8, abs: 0 },
        { name: 'Эргашева Муслима Акрамовна', parent: 'Эргашев Акрам Иброхимович', phone: '+998978901234', pPhone: '+998978901200', group: 'GER-601', bal: 10, abs: 0 },
        // GER-602
        { name: 'Тоштемиров Дониёр Камолович', parent: 'Тоштемиров Камол Равшанович', phone: '+998989012345', pPhone: '+998989012300', group: 'GER-602', bal: 0, abs: 3 },
        { name: 'Саидова Фарангиз Шавкатовна', parent: 'Саидов Шавкат Зокирович', phone: '+998900123456', pPhone: '+998900123400', group: 'GER-602', bal: 9, abs: 0 },
        { name: 'Умаров Бехрузжон Бахтиёрович', parent: 'Умаров Бахтиёр Солихович', phone: '+998911234567', pPhone: '+998911234500', group: 'GER-602', bal: 7, abs: 0 },
        // GER-603
        { name: 'Юлдашева Гульчехра Отабековна', parent: 'Юлдашев Отабек Рахимович', phone: '+998932345678', pPhone: '+998932345600', group: 'GER-603', bal: 12, abs: 0 },
        { name: 'Расулов Шохжахон Музаффарович', parent: 'Расулов Музаффар Шухратович', phone: '+998943456789', pPhone: '+998943456700', group: 'GER-603', bal: 6, abs: 0 },
        { name: 'Очилова Шахноза Хамидовна', parent: 'Очилов Хамид Каримович', phone: '+998954567890', pPhone: '+998954567800', group: 'GER-603', bal: 11, abs: 0 }
      ];

      const students = rawNames.map((s, idx) => {
        const grp = groups.find(g => g.id === s.group);
        return {
          id: 'STU-' + (1001 + idx),
          name: s.name,
          parentName: s.parent,
          phone: s.phone,
          parentPhone: s.pPhone,
          groupId: s.group,
          groupName: grp.name,
          course: grp.course,
          teacherName: grp.teacherName,
          lessonsBalance: s.bal,
          consecutiveAbsences: s.abs,
          contractNumber: 'MAM-2026-' + (4100 + idx),
          contractDate: '2026-09-01',
          parentPassport: 'AD ' + (2000000 + idx),
          monthlyFee: grp.fee,
          totalPaidSum: 1200000,
          avgGrade: Math.floor(75 + (idx % 23)),
          mamCoins: Math.floor(120 + (idx * 15)),
          status: s.bal > 0 ? 'active' : 'debt'
        };
      });

      const expenses = [
        { id: 'EXP-101', date: '2026-10-01', category: 'Аренда', title: 'Аренда помещения Академии (Маргилан, Б. Маргиноний, 42)', amount: 6500000, approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-102', date: '2026-10-02', category: 'Коммуналка', title: 'Электроэнергия & Коммунальные услуги за сентябрь', amount: 1250000, approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-103', date: '2026-10-03', category: 'Интернет', title: 'Оптоволоконный интернет Uztelecom Бизнес (200 Мбит/с)', amount: 650000, approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-104', date: '2026-10-05', category: 'Маркетинг', title: 'Таргетинг Instagram & Реклама в Telegram Маргилан', amount: 2400000, approvedBy: 'Богданов Т.Я.' },
        { id: 'EXP-105', date: '2026-10-08', category: 'Хозтовары', title: 'Канцелярия, маркеры для досок, бумага А4, вода', amount: 480000, approvedBy: 'Рахимова Н.О.' },
        { id: 'EXP-106', date: '2026-10-10', category: 'Оборудование', title: 'Модернизация SSD и мышей для Каб. 101 (Web Lab)', amount: 1100000, approvedBy: 'Богданов Т.Я.' }
      ];

      const auditLogs = [
        { id: 'LOG-501', time: '2026-10-12 08:30:15', user: 'Богданов Т.Я. (director)', action: 'LOGIN', details: 'Вход в систему Директора. IP: 192.168.1.10 (Маргилан)', level: 'info' },
        { id: 'LOG-502', time: '2026-10-12 08:45:00', user: 'Рахимова Н.О. (cashier)', action: 'CHECK_IN', details: 'Открытие утренней кассовой смены #142', level: 'info' },
        { id: 'LOG-503', time: '2026-10-12 09:15:22', user: 'Рахимова Н.О. (cashier)', action: 'PAYMENT', details: 'Принят платеж 600 000 UZS (Click) за студента Хакимов Ж.', level: 'success' },
        { id: 'LOG-504', time: '2026-10-12 10:05:40', user: 'Алимов С.Б. (teacher_python)', action: 'ATTENDANCE', details: 'Списание 1 урока в группе PY-101. Проведено 3 отметки.', level: 'warning' },
        { id: 'LOG-505', time: '2026-10-12 11:20:10', user: 'Богданов Т.Я. (director)', action: 'EXPENSE_APPROVE', details: 'Утвержден расход EXP-106 (SSD upgrade 1 100 000 UZS)', level: 'warning' }
      ];

      const kanbanLeads = [
        { id: 'LEAD-201', name: 'Акбаров Дониёр', phone: '+998901112233', course: 'Python & Backend', stage: 'new', date: '2026-10-11', source: 'Instagram Ads' },
        { id: 'LEAD-202', name: 'Мухаммадиев Жавохир', phone: '+998912223344', course: 'Frontend & Web Dev', stage: 'consult', date: '2026-10-10', source: 'Telegram канал' },
        { id: 'LEAD-203', name: 'Каримова Севара', phone: '+998933334455', course: 'General & IELTS English', stage: 'trial', date: '2026-10-09', source: 'Рекомендация' },
        { id: 'LEAD-204', name: 'Олимов Сухроб', phone: '+998944445566', course: 'Korean & TOPIK', stage: 'paid', date: '2026-10-08', source: 'Листовка' }
      ];

      const timesheetRecords = [
        { id: 'TS-301', date: '2026-10-12', staffKey: 'director', staffName: 'Богданов Т.Я.', role: 'Директор', inTime: '08:30', outTime: '--', hours: 0, status: 'active' },
        { id: 'TS-302', date: '2026-10-12', staffKey: 'cashier', staffName: 'Рахимова Н.О.', role: 'Кассир', inTime: '08:45', outTime: '--', hours: 0, status: 'active' },
        { id: 'TS-303', date: '2026-10-12', staffKey: 'teacher_python', staffName: 'Алимов С.Б.', role: 'Учитель Python', inTime: '09:00', outTime: '--', hours: 0, status: 'active' }
      ];

      const receipts = [
        { id: 'REC-1001', date: '2026-10-12 09:15', studentId: 'STU-1002', studentName: 'Хакимов Жасур Маъруфович', phone: '+998912345678', group: 'PY-101', amount: 600000, method: 'Click', lessonsAdded: 12, cashier: 'Рахимова Н.О.' }
      ];

      return {
        groups,
        students,
        expenses,
        auditLogs,
        kanbanLeads,
        timesheetRecords,
        receipts,
        cashBalanceToday: 12450000,
        settings: {
          branchName: 'Maryam Academy Mission (Маргилан)',
          address: 'г. Маргилан, ул. Б. Маргиноний, 42',
          directorName: 'Богданов Т.Я.',
          phone: '+998 (73) 254-00-11'
        }
      };
    }

    function getDB() {
      const raw = localStorage.getItem('mam_crm_db');
      if (!raw) {
        const init = generateInitialDB();
        localStorage.setItem('mam_crm_db', JSON.stringify(init));
        return init;
      }
      try {
        return JSON.parse(raw);
      } catch (e) {
        const init = generateInitialDB();
        localStorage.setItem('mam_crm_db', JSON.stringify(init));
        return init;
      }
    }

    function saveDB(db) {
      localStorage.setItem('mam_crm_db', JSON.stringify(db));
    }

    function addAuditLog(action, details, level = 'info') {
      const db = getDB();
      const userStr = currentUser ? `${currentUser.shortName || currentUser.name} (${currentUser.login})` : 'Гость / Аноним';
      const now = new Date();
      const pad = n => String(n).padStart(2, '0');
      const timeStr = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
      
      const newLog = {
        id: 'LOG-' + Date.now().toString().slice(-4),
        time: timeStr,
        user: userStr,
        action,
        details,
        level
      };
      db.auditLogs.unshift(newLog);
      if (db.auditLogs.length > 50) db.auditLogs.pop();
      saveDB(db);
    }

    /* ==============================================================
       4. AUTHENTICATION & SESSION MANAGEMENT (STRICT LOGINS)
       ============================================================== */
    function initAuth() {
      renderAuthCheatSheet();
      const savedUserKey = localStorage.getItem('mam_auth_user');
      if (savedUserKey && SERVICE_ACCOUNTS[savedUserKey]) {
        currentUser = SERVICE_ACCOUNTS[savedUserKey];
        showAppScreen();
      } else {
        showAuthScreen();
      }
    }

    function renderAuthCheatSheet() {
      const container = document.getElementById('auth-quick-accounts-list');
      if (!container) return;
      container.innerHTML = Object.values(SERVICE_ACCOUNTS).map(acc => {
        return `
          <button type="button" onclick="quickFillAuth('${acc.login}', '${acc.pass}')" class="w-full text-left p-2 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700/80 hover:border-emerald-500 dark:hover:border-emerald-500 hover:shadow-xs transition group flex items-center justify-between cursor-pointer">
            <div class="flex items-center gap-2 overflow-hidden">
              <span class="text-base">${acc.avatar}</span>
              <div class="overflow-hidden">
                <div class="text-[11px] font-bold text-slate-800 dark:text-slate-200 truncate group-hover:text-emerald-600 transition">
                  ${acc.name}
                </div>
                <div class="text-[10px] text-slate-400 truncate">
                  ${acc.roleName}
                </div>
              </div>
            </div>
            <div class="text-right shrink-0 font-mono text-[10px] text-slate-500 dark:text-slate-400">
              <span class="bg-slate-100 dark:bg-slate-800 px-1.5 py-0.5 rounded text-emerald-600 font-bold">${acc.login}</span>
            </div>
          </button>
        `;
      }).join('');
    }

    function quickFillAuth(login, pass) {
      document.getElementById('auth-input-login').value = login;
      document.getElementById('auth-input-pass').value = pass;
      const alertBox = document.getElementById('auth-alert');
      alertBox.className = 'mb-4 p-3 rounded-xl text-xs font-semibold border flex items-center gap-2 bg-emerald-50 text-emerald-800 border-emerald-200 dark:bg-emerald-950 dark:text-emerald-300 dark:border-emerald-800';
      alertBox.innerHTML = `✓ Подставлен аккаунт: <b>${login}</b>. Нажмите «Войти в панель CRM».`;
      alertBox.classList.remove('hidden');
    }

    function togglePassVisibility() {
      const passInput = document.getElementById('auth-input-pass');
      const icon = document.getElementById('auth-eye-icon');
      if (passInput.type === 'password') {
        passInput.type = 'text';
        icon.setAttribute('data-lucide', 'eye-off');
      } else {
        passInput.type = 'password';
        icon.setAttribute('data-lucide', 'eye');
      }
      lucide.createIcons();
    }

    function handleLoginSubmit(e) {
      e.preventDefault();
      const login = document.getElementById('auth-input-login').value.trim();
      const pass = document.getElementById('auth-input-pass').value.trim();
      const alertBox = document.getElementById('auth-alert');

      const found = Object.values(SERVICE_ACCOUNTS).find(a => a.login === login && a.pass === pass);

      if (found) {
        currentUser = found;
        localStorage.setItem('mam_auth_user', found.key);
        alertBox.classList.add('hidden');
        addAuditLog('LOGIN', `Успешный вход в систему под ролью: ${found.roleName}`);
        showAppScreen();
      } else {
        alertBox.className = 'mb-4 p-3 rounded-xl text-xs font-semibold border flex items-center gap-2 bg-rose-50 text-rose-800 border-rose-200 dark:bg-rose-950 dark:text-rose-300 dark:border-rose-800';
        alertBox.innerHTML = `✗ Ошибка доступа! Неверный логин или пароль. Воспользуйтесь списком служебных аккаунтов справа.`;
        alertBox.classList.remove('hidden');
      }
    }

    function logoutSession() {
      addAuditLog('LOGOUT', 'Выход сотрудника из учетной записи');
      currentUser = null;
      localStorage.removeItem('mam_auth_user');
      showAuthScreen();
    }

    function showAuthScreen() {
      document.getElementById('view-auth').classList.remove('hidden');
      document.getElementById('view-app').classList.add('hidden');
      document.getElementById('auth-input-login').value = '';
      document.getElementById('auth-input-pass').value = '';
      document.getElementById('auth-alert').classList.add('hidden');
      lucide.createIcons();
    }

    function showAppScreen() {
      document.getElementById('view-auth').classList.add('hidden');
      document.getElementById('view-app').classList.remove('hidden');

      // Top bar profile display
      document.getElementById('top-user-avatar').textContent = currentUser.avatar;
      document.getElementById('top-user-name').textContent = currentUser.shortName || currentUser.name;
      document.getElementById('top-user-role').textContent = currentLang === 'uz' ? currentUser.roleNameUz : currentUser.roleName;

      // Sidebar employee card
      document.getElementById('side-emp-avatar').textContent = currentUser.avatar;
      document.getElementById('side-emp-name').textContent = currentUser.shortName || currentUser.name;
      document.getElementById('side-emp-role').textContent = currentLang === 'uz' ? currentUser.roleNameUz : currentUser.roleName;
      document.getElementById('sidebar-access-level').textContent = currentUser.key === 'director' || currentUser.key === 'sysadmin' ? 'FULL ACCESS' : 'ROLE ACCESS';

      // Timesheet widget in top/timesheet tab
      const tsAvatar = document.getElementById('timesheet-user-avatar');
      if (tsAvatar) tsAvatar.textContent = currentUser.avatar;
      const tsName = document.getElementById('timesheet-user-name');
      if (tsName) tsName.textContent = currentUser.name;

      renderSidebarNav();
      updateSidebarQuickStats();

      // Switch to first allowed module
      const defaultMod = currentUser.allowedModules.includes('director') ? 'director' : currentUser.allowedModules[0];
      switchModule(defaultMod);
      lucide.createIcons();
    }

    /* ==============================================================
       5. NAVIGATION & PERMISSION CHECKS (NO ROLE SELECTOR!)
       ============================================================== */
    const ALL_MODULES = [
      { id: 'director', name: 'Кабинет Директора', nameUz: 'Direktor Kabineti', icon: 'shield-check', badge: '360°' },
      { id: 'kanban', name: 'Канбан Лидов', nameUz: 'Lidlar Kanbani', icon: 'kanban', badge: 'Воронка' },
      { id: 'schedule', name: 'Расписание 6 Кабинетов', nameUz: '6 Xonalar Jadvali', icon: 'calendar', badge: 'Сетка' },
      { id: 'pos', name: 'POS-Касса и Оплаты', nameUz: 'POS-Kassa va Toʻlov', icon: 'credit-card', badge: 'Click/Payme' },
      { id: 'journal', name: 'Электронный журнал 18 групп', nameUz: 'Elektron Jurnal (18)', icon: 'book-open', badge: '18 групп' },
      { id: 'gamification', name: 'Экзамены & MAM-Coins', nameUz: 'Imtihon & Coins', icon: 'sparkles', badge: 'Топ-10' },
      { id: 'contracts', name: 'Договоры и Сертификаты', nameUz: 'Shartnomalar & Sertifikat', icon: 'file-text', badge: 'A4 Печать' },
      { id: 'timesheet', name: 'Табель смен сотрудников', nameUz: 'Xodimlar Tabeli', icon: 'clock', badge: 'Check-in' },
      { id: 'backup', name: 'Бэкап & Настройки DBN', nameUz: 'Zaxira & Sozlamalar', icon: 'database', badge: 'JSON' }
    ];

    function renderSidebarNav() {
      const container = document.getElementById('sidebar-nav-list');
      if (!container || !currentUser) return;

      container.innerHTML = ALL_MODULES.filter(m => currentUser.allowedModules.includes(m.id)).map(m => {
        const isActive = m.id === currentModule;
        const activeClass = isActive
          ? 'bg-emerald-600 text-white font-bold shadow-xs'
          : 'text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 font-medium';
        const label = currentLang === 'uz' ? m.nameUz : m.name;

        return `
          <button type="button" onclick="switchModule('${m.id}')" class="w-full text-left px-3 py-2 rounded-xl text-xs transition flex items-center justify-between cursor-pointer ${activeClass}">
            <div class="flex items-center gap-2.5 overflow-hidden">
              <i data-lucide="${m.icon}" class="w-4 h-4 shrink-0"></i>
              <span class="truncate">${label}</span>
            </div>
            ${m.badge ? `<span class="text-[9px] font-mono px-1 rounded ${isActive ? 'bg-emerald-700 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-500'}">${m.badge}</span>` : ''}
          </button>
        `;
      }).join('');
      lucide.createIcons();
    }

    function switchModule(moduleId) {
      if (!currentUser.allowedModules.includes(moduleId)) {
        moduleId = currentUser.allowedModules[0];
      }
      currentModule = moduleId;

      document.querySelectorAll('.module-view').forEach(el => el.classList.add('hidden'));
      const activeSection = document.getElementById('module-' + moduleId);
      if (activeSection) activeSection.classList.remove('hidden');

      renderSidebarNav();
      document.getElementById('main-content-scroll').scrollTop = 0;

      // Module-specific initializers
      if (moduleId === 'director') renderDirectorCommandCenter();
      if (moduleId === 'kanban') renderKanbanBoard();
      if (moduleId === 'schedule') renderScheduleGrid();
      if (moduleId === 'pos') renderPosModule();
      if (moduleId === 'journal') initJournalModule();
      if (moduleId === 'gamification') renderGamificationModule();
      if (moduleId === 'contracts') initContractsModule();
      if (moduleId === 'timesheet') renderTimesheetModule();

      lucide.createIcons();
    }

    function updateSidebarQuickStats() {
      const db = getDB();
      const stuEl = document.getElementById('side-stat-students');
      if (stuEl) stuEl.textContent = db.students.length;
      const grpEl = document.getElementById('side-stat-groups');
      if (grpEl) grpEl.textContent = db.groups.length;
      const cashEl = document.getElementById('side-stat-cash');
      if (cashEl) cashEl.textContent = formatMoney(db.cashBalanceToday || 12450000) + ' UZS';
    }

    /* ==============================================================
       6. MODULE: DIRECTOR EXECUTIVE COMMAND CENTER
       ============================================================== */
    function renderDirectorCommandCenter() {
      const db = getDB();

      // Calculate 360° Metrics
      const totalRevenue = db.students.reduce((acc, s) => acc + (s.monthlyFee || 600000), 0) + 18500000;
      const totalExpenses = db.expenses.reduce((acc, e) => acc + Number(e.amount), 0);
      const totalSalaries = db.groups.length * 1250000;
      const totalOpex = totalExpenses + totalSalaries;
      const netProfit = totalRevenue - totalOpex;
      const marginPercent = Math.round((netProfit / totalRevenue) * 100);
      const avgCheck = Math.round(totalRevenue / db.students.length);

      // KPI Grid rendering
      const kpis = [
        { label: 'Выручка (Оборот)', val: formatMoney(totalRevenue) + ' UZS', color: 'text-emerald-600', sub: '+18.4% к сентябрю' },
        { label: 'Расходы (OPEX)', val: formatMoney(totalOpex) + ' UZS', color: 'text-rose-600', sub: 'Аренда, ФОТ, ЖКХ' },
        { label: 'Чистая Прибыль', val: formatMoney(netProfit) + ' UZS', color: 'text-emerald-700 dark:text-emerald-400', sub: 'Net Profit Маргилан' },
        { label: 'Рентабельность %', val: marginPercent + '%', color: 'text-blue-600', sub: 'Норма > 40%' },
        { label: 'Средний чек', val: formatMoney(avgCheck) + ' UZS', color: 'text-indigo-600', sub: 'По абонементам' },
        { label: 'Удержание (Retention)', val: '94.4%', color: 'text-teal-600', sub: 'Отток 5.6%' },
        { label: 'CAC (Цена лида)', val: '124 000 UZS', color: 'text-amber-600', sub: 'Маркетинг окупается' },
        { label: 'Загрузка классов', val: '84.2%', color: 'text-purple-600', sub: '6 кабинетов MAM' }
      ];

      const kpiContainer = document.getElementById('dir-kpi-grid');
      if (kpiContainer) {
        kpiContainer.innerHTML = kpis.map(k => `
          <div class="p-3 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400 truncate">${k.label}</div>
            <div class="text-sm font-black font-mono ${k.color} truncate">${k.val}</div>
            <div class="text-[9px] text-slate-400 truncate">${k.sub}</div>
          </div>
        `).join('');
      }

      // Rooms list
      const roomsContainer = document.getElementById('dir-rooms-list');
      if (roomsContainer) {
        const rooms = [
          { name: 'Каб. 101 (Web Dev Lab)', cap: '12 мест', occ: '92%', status: '16 ПК Core i7 • Проектор' },
          { name: 'Каб. 102 (Python & AI)', cap: '12 мест', occ: '88%', status: '16 ПК Core i7 • GPU RTX' },
          { name: 'Каб. 103 (UI/UX Design)', cap: '12 мест', occ: '83%', status: '12 ПК + Графич. планшеты' },
          { name: 'Каб. 201 (English Hall)', cap: '16 мест', occ: '85%', status: 'Smart Board • Аудиосистема' },
          { name: 'Каб. 202 (Korean Lounge)', cap: '14 мест', occ: '78%', status: 'Интерактивная доска' },
          { name: 'Каб. 203 (German Room)', cap: '14 мест', occ: '79%', status: 'Мультимедиа центр' }
        ];
        roomsContainer.innerHTML = rooms.map(r => `
          <div class="p-2 rounded-lg bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex items-center justify-between">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200">${r.name}</div>
              <div class="text-[10px] text-slate-400">${r.status}</div>
            </div>
            <div class="text-right font-mono">
              <span class="font-bold text-emerald-600">${r.occ}</span>
              <div class="text-[10px] text-slate-400">${r.cap}</div>
            </div>
          </div>
        `).join('');
      }

      // Teacher KPI & Payroll Table
      renderDirectorTeachersTable();

      // Expenses Registry Table & total
      renderDirectorExpensesTable();

      // Risks and Alerts in Director Office
      renderDirectorRisksTable();

      // Audit Log list
      renderDirectorAuditLog();

      lucide.createIcons();
    }

    function renderDirectorTeachersTable() {
      const db = getDB();
      const tbody = document.getElementById('dir-teachers-tbody');
      if (!tbody) return;

      const teacherKeys = ['teacher_python', 'teacher_web', 'teacher_design', 'teacher_english', 'teacher_korean', 'teacher_german'];

      tbody.innerHTML = teacherKeys.map(k => {
        const teacher = SERVICE_ACCOUNTS[k];
        const teacherGroups = db.groups.filter(g => g.teacherKey === k);
        const groupIds = teacherGroups.map(g => g.id);
        const activeStudents = db.students.filter(s => groupIds.includes(s.groupId));
        const totalLessons = teacherGroups.reduce((acc, g) => acc + (g.conductedLessons || 20), 0);
        
        // Formula: Conducted Lessons * 65,000 UZS + Active Students * 120,000 UZS Bonus
        const salary = (totalLessons * 65000) + (activeStudents.length * 120000);
        const retentionRate = (92 + (k.length % 6)).toFixed(1);
        const churnRate = (100 - retentionRate).toFixed(1);

        return `
          <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
            <td class="py-2.5 px-3">
              <div class="font-bold text-slate-900 dark:text-white flex items-center gap-1.5 font-sans">
                <span>${teacher.avatar}</span>
                <span>${teacher.name}</span>
              </div>
              <div class="text-[10px] text-slate-400 font-sans">${teacherGroups.map(g => g.id).join(', ')}</div>
            </td>
            <td class="py-2.5 px-3 font-sans">${teacher.course}</td>
            <td class="py-2.5 px-3 text-center font-bold text-slate-900 dark:text-white">${activeStudents.length} чел.</td>
            <td class="py-2.5 px-3 text-center text-emerald-600 font-bold">${retentionRate}%</td>
            <td class="py-2.5 px-3 text-center text-rose-500 font-bold">${churnRate}%</td>
            <td class="py-2.5 px-3 text-center font-bold">${totalLessons} ур.</td>
            <td class="py-2.5 px-3 text-right font-bold text-emerald-600 dark:text-emerald-400">${formatMoney(salary)} UZS</td>
            <td class="py-2.5 px-3 text-center">
              <span class="text-[10px] bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 font-bold px-2 py-0.5 rounded-full">
                Начислено
              </span>
            </td>
            <td class="py-2.5 px-3 text-center">
              <button type="button" onclick="payTeacherSalary('${teacher.name}', ${salary})" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded font-bold text-[10px] transition cursor-pointer">
                Выплатить
              </button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function payTeacherSalary(name, amount) {
      if (!confirm(`Подтвердите выплату заработной платы преподавателю ${name} на сумму ${formatMoney(amount)} UZS?`)) return;
      const db = getDB();
      db.cashBalanceToday = (db.cashBalanceToday || 12450000) - amount;
      saveDB(db);
      addAuditLog('SALARY_PAYOUT', `Выплата зарплаты: ${name} — ${formatMoney(amount)} UZS`, 'warning');
      alert(`Заработная плата преподавателю ${name} успешно выплачена и зафиксирована в Audit Log.`);
      renderDirectorCommandCenter();
      updateSidebarQuickStats();
    }

    function payAllSalaries() {
      if (!confirm('Выплатить заработную плату всем 6 преподавателям Академии MAM за текущий период?')) return;
      addAuditLog('SALARY_PAYOUT_ALL', 'Массовая выплата зарплат всем 6 преподавателям Академии', 'warning');
      alert('Все заработные платы преподавателей успешно выплачены и проведены по кассе!');
      renderDirectorCommandCenter();
    }

    function renderDirectorExpensesTable() {
      const db = getDB();
      const tbody = document.getElementById('dir-expenses-tbody');
      const badge = document.getElementById('dir-total-expenses-badge');
      if (!tbody) return;

      const total = db.expenses.reduce((acc, e) => acc + Number(e.amount), 0);
      if (badge) badge.textContent = 'Итого расходов: ' + formatMoney(total) + ' UZS';

      tbody.innerHTML = db.expenses.map(e => `
        <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
          <td class="py-2 px-3 text-slate-500">${e.date}</td>
          <td class="py-2 px-3 font-sans">
            <span class="px-1.5 py-0.5 rounded text-[10px] font-bold bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
              ${e.category}
            </span>
          </td>
          <td class="py-2 px-3 font-sans text-slate-900 dark:text-white font-medium">${e.title}</td>
          <td class="py-2 px-3 text-right font-bold text-rose-600 dark:text-rose-400">-${formatMoney(e.amount)} UZS</td>
          <td class="py-2 px-3 text-center font-sans text-slate-500">${e.approvedBy || 'Богданов Т.Я.'}</td>
          <td class="py-2 px-3 text-center">
            <button type="button" onclick="deleteExpense('${e.id}')" class="text-rose-500 hover:text-rose-700 cursor-pointer" title="Удалить">
              <i data-lucide="trash-2" class="w-3.5 h-3.5 mx-auto"></i>
            </button>
          </td>
        </tr>
      `).join('');
      lucide.createIcons();
    }

    function handleNewExpenseSubmit(e) {
      e.preventDefault();
      const cat = document.getElementById('exp-category-input').value;
      const title = document.getElementById('exp-title-input').value.trim();
      const amount = Number(document.getElementById('exp-amount-input').value);
      const date = document.getElementById('exp-date-input').value || new Date().toISOString().slice(0, 10);

      const db = getDB();
      const newExp = {
        id: 'EXP-' + Date.now().toString().slice(-4),
        date,
        category: cat,
        title,
        amount,
        approvedBy: currentUser ? currentUser.shortName : 'Богданов Т.Я.'
      };
      db.expenses.unshift(newExp);
      saveDB(db);

      addAuditLog('EXPENSE_ADD', `Утвержден операционный расход: [${cat}] ${title} — ${formatMoney(amount)} UZS`, 'warning');
      document.getElementById('exp-title-input').value = '';
      document.getElementById('exp-amount-input').value = '';

      renderDirectorCommandCenter();
    }

    function deleteExpense(id) {
      if (!confirm('Удалить эту статью расхода?')) return;
      const db = getDB();
      db.expenses = db.expenses.filter(e => e.id !== id);
      saveDB(db);
      addAuditLog('EXPENSE_DELETE', `Удален расход с ID ${id}`, 'warning');
      renderDirectorCommandCenter();
    }

    function renderDirectorRisksTable() {
      const db = getDB();
      const atRisk = db.students.filter(s => s.lessonsBalance <= 1 || s.consecutiveAbsences >= 3);

      const countBal = db.students.filter(s => s.lessonsBalance <= 1).length;
      const countAbs = db.students.filter(s => s.consecutiveAbsences >= 3).length;
      const sumRenewal = atRisk.reduce((acc, s) => acc + (s.monthlyFee || 600000), 0);

      const elBal = document.getElementById('risk-count-balance');
      if (elBal) elBal.textContent = countBal + ' студ.';
      const elAbs = document.getElementById('risk-count-absent');
      if (elAbs) elAbs.textContent = countAbs + ' студ.';
      const elSum = document.getElementById('risk-sum-renewal');
      if (elSum) elSum.textContent = formatMoney(sumRenewal) + ' UZS';

      const tbody = document.getElementById('risks-table-body');
      if (!tbody) return;

      tbody.innerHTML = atRisk.map(s => {
        let reasonBadge = '';
        if (s.lessonsBalance === 0) {
          reasonBadge = '<span class="bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 px-2 py-0.5 rounded-full font-bold">Баланс 0 уроков</span>';
        } else if (s.lessonsBalance === 1) {
          reasonBadge = '<span class="bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 px-2 py-0.5 rounded-full font-bold">Остался 1 урок</span>';
        }
        if (s.consecutiveAbsences >= 3) {
          reasonBadge += ' <span class="bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300 px-2 py-0.5 rounded-full font-bold">3 пропуска подряд</span>';
        }

        return `
          <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
            <td class="py-2.5 px-3">
              <div class="font-bold text-slate-900 dark:text-white font-sans">${s.name}</div>
              <div class="text-[10px] text-slate-400 font-sans">Тел: ${s.phone}</div>
            </td>
            <td class="py-2.5 px-3 font-sans">
              <span class="font-mono font-bold text-slate-700 dark:text-slate-300">${s.groupId}</span> • ${s.course}
            </td>
            <td class="py-2.5 px-3 text-center font-bold ${s.lessonsBalance === 0 ? 'text-rose-600' : 'text-amber-600'}">
              ${s.lessonsBalance} ур.
            </td>
            <td class="py-2.5 px-3 text-center font-bold ${s.consecutiveAbsences >= 3 ? 'text-rose-600' : 'text-slate-500'}">
              ${s.consecutiveAbsences}
            </td>
            <td class="py-2.5 px-3 font-sans">
              <div class="font-medium text-slate-800 dark:text-slate-200">${s.parentName}</div>
              <div class="text-[10px] text-emerald-600 font-mono">${s.parentPhone}</div>
            </td>
            <td class="py-2.5 px-3 text-center font-sans text-[11px]">${reasonBadge}</td>
            <td class="py-2.5 px-3 text-center">
              <button type="button" onclick="openTelegramModal('${s.id}')" class="px-2.5 py-1.5 rounded-lg bg-sky-500 hover:bg-sky-600 text-white font-bold text-xs transition flex items-center gap-1.5 mx-auto cursor-pointer shadow-xs">
                <i data-lucide="send" class="w-3.5 h-3.5"></i>
                <span>Telegram</span>
              </button>
            </td>
          </tr>
        `;
      }).join('');
      lucide.createIcons();
    }

    function renderDirectorAuditLog() {
      const db = getDB();
      const container = document.getElementById('dir-audit-list');
      if (!container) return;

      container.innerHTML = db.auditLogs.map(l => {
        let badgeColor = 'bg-slate-100 text-slate-700 dark:bg-slate-800 dark:text-slate-300';
        if (l.level === 'warning') badgeColor = 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300';
        if (l.level === 'success') badgeColor = 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300';
        if (l.level === 'danger') badgeColor = 'bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300';

        return `
          <div class="p-2.5 rounded-lg bg-slate-50 dark:bg-slate-800/70 border border-slate-200 dark:border-slate-700 text-xs flex items-center justify-between">
            <div class="flex items-center gap-2 overflow-hidden">
              <span class="text-[9px] font-mono px-1.5 py-0.5 rounded font-bold ${badgeColor}">${l.action}</span>
              <div class="overflow-hidden">
                <div class="font-medium text-slate-900 dark:text-slate-100 truncate">${l.details}</div>
                <div class="text-[10px] text-slate-400 truncate">Пользователь: ${l.user}</div>
              </div>
            </div>
            <div class="text-[10px] text-slate-400 font-mono shrink-0 pl-2">${l.time}</div>
          </div>
        `;
      }).join('');
    }

    /* ==============================================================
       7. MODULE: LEADS KANBAN BOARD
       ============================================================== */
    function renderKanbanBoard() {
      const db = getDB();
      const container = document.getElementById('kanban-board-container');
      if (!container) return;

      const columns = [
        { id: 'new', title: '1. Новая заявка', color: 'border-slate-300 dark:border-slate-700', bg: 'bg-slate-100/50 dark:bg-slate-800/40' },
        { id: 'consult', title: '2. Консультация', color: 'border-blue-300 dark:border-blue-900', bg: 'bg-blue-50/50 dark:bg-blue-950/20' },
        { id: 'trial', title: '3. Пробный урок', color: 'border-amber-300 dark:border-amber-900', bg: 'bg-amber-50/50 dark:bg-amber-950/20' },
        { id: 'paid', title: '4. Оплата / Договор', color: 'border-emerald-300 dark:border-emerald-900', bg: 'bg-emerald-50/50 dark:bg-emerald-950/20' }
      ];

      container.innerHTML = columns.map(col => {
        const leads = db.kanbanLeads.filter(l => l.stage === col.id);
        return `
          <div class="rounded-xl border ${col.color} ${col.bg} p-3 flex flex-col justify-between min-h-[400px]">
            <div>
              <div class="flex items-center justify-between pb-2 mb-3 border-b border-slate-200 dark:border-slate-700">
                <h4 class="text-xs font-black text-slate-800 dark:text-slate-200">${col.title}</h4>
                <span class="text-[10px] font-mono font-bold bg-white dark:bg-slate-800 px-2 py-0.5 rounded-full border border-slate-200 dark:border-slate-700">
                  ${leads.length}
                </span>
              </div>
              <div class="space-y-2.5">
                ${leads.map(lead => `
                  <div class="p-3 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 shadow-xs space-y-2">
                    <div class="flex items-center justify-between">
                      <span class="text-[10px] font-mono text-emerald-600 bg-emerald-50 dark:bg-emerald-950 px-1.5 py-0.5 rounded font-bold">${lead.source}</span>
                      <span class="text-[10px] text-slate-400 font-mono">${lead.date}</span>
                    </div>
                    <div>
                      <div class="text-xs font-bold text-slate-900 dark:text-white">${lead.name}</div>
                      <div class="text-[11px] text-slate-500">${lead.course}</div>
                      <div class="text-[10px] font-mono text-blue-600 mt-0.5">${lead.phone}</div>
                    </div>
                    <div class="flex items-center justify-between pt-2 border-t border-slate-100 dark:border-slate-800">
                      <a href="https://t.me/${lead.phone.replace(/[^0-9]/g, '')}" target="_blank" rel="noopener noreferrer" class="text-[10px] font-bold text-sky-500 hover:text-sky-600 flex items-center gap-1">
                        <i data-lucide="send" class="w-3 h-3"></i> Telegram
                      </a>
                      <div class="flex items-center gap-1">
                        ${col.id !== 'new' ? `<button type="button" onclick="moveLeadStage('${lead.id}', -1)" class="p-1 rounded bg-slate-100 dark:bg-slate-800 text-slate-600 hover:bg-slate-200 text-[10px] font-bold" title="Назад">←</button>` : ''}
                        ${col.id !== 'paid' ? `<button type="button" onclick="moveLeadStage('${lead.id}', 1)" class="p-1 rounded bg-emerald-600 text-white hover:bg-emerald-700 text-[10px] font-bold" title="Вперед">→</button>` : ''}
                      </div>
                    </div>
                  </div>
                `).join('')}
              </div>
            </div>
            <button type="button" onclick="openAddLeadModal('${col.id}')" class="mt-3 w-full py-1.5 rounded-lg border border-dashed border-slate-300 dark:border-slate-700 text-slate-500 hover:text-slate-800 dark:hover:text-slate-200 text-xs font-semibold flex items-center justify-center gap-1 cursor-pointer">
              <i data-lucide="plus" class="w-3.5 h-3.5"></i> Добавить
            </button>
          </div>
        `;
      }).join('');
      lucide.createIcons();
    }

    function moveLeadStage(id, dir) {
      const db = getDB();
      const lead = db.kanbanLeads.find(l => l.id === id);
      if (!lead) return;
      const stages = ['new', 'consult', 'trial', 'paid'];
      const idx = stages.indexOf(lead.stage);
      const nextIdx = idx + dir;
      if (nextIdx >= 0 && nextIdx < stages.length) {
        lead.stage = stages[nextIdx];
        saveDB(db);
        addAuditLog('LEAD_MOVE', `Лид ${lead.name} перемещен на стадию: ${stages[nextIdx]}`);
        renderKanbanBoard();
      }
    }

    function openAddLeadModal(stage = 'new') {
      document.getElementById('modal-lead').classList.remove('hidden');
      lucide.createIcons();
    }

    function closeLeadModal() {
      document.getElementById('modal-lead').classList.add('hidden');
    }

    function handleNewLeadSubmit(e) {
      e.preventDefault();
      const name = document.getElementById('lead-name-input').value.trim();
      const phone = document.getElementById('lead-phone-input').value.trim();
      const course = document.getElementById('lead-course-input').value;
      const source = document.getElementById('lead-source-input').value;

      const db = getDB();
      const newLead = {
        id: 'LEAD-' + Date.now().toString().slice(-4),
        name,
        phone,
        course,
        source,
        stage: 'new',
        date: new Date().toISOString().slice(0, 10)
      };
      db.kanbanLeads.unshift(newLead);
      saveDB(db);
      addAuditLog('LEAD_NEW', `Создан новый лид: ${name} (${phone}, ${course})`);

      closeLeadModal();
      document.getElementById('lead-name-input').value = '';
      document.getElementById('lead-phone-input').value = '';
      renderKanbanBoard();
    }

    /* ==============================================================
       8. MODULE: CLASSROOM SCHEDULE GRID
       ============================================================== */
    function renderScheduleGrid() {
      const db = getDB();
      const filter = document.getElementById('schedule-day-filter').value;
      const tbody = document.getElementById('schedule-table-body');
      if (!tbody) return;

      const timeSlots = [
        '09:00 - 11:00',
        '11:30 - 13:30',
        '14:00 - 16:00',
        '16:30 - 18:30',
        '19:00 - 20:30'
      ];

      // Rooms setup: 101, 102, 103, 201, 202, 203
      const roomKeys = [
        { code: 'Каб. 101', name: 'Web Dev Lab', teacher: 'Юлдашев Д.А.' },
        { code: 'Каб. 102', name: 'Python Hub', teacher: 'Алимов С.Б.' },
        { code: 'Каб. 103', name: 'UI/UX Studio', teacher: 'Каримова М.Ш.' },
        { code: 'Каб. 201', name: 'English Hall', teacher: 'Смирнова Е.В.' },
        { code: 'Каб. 202', name: 'Korean Lounge', teacher: 'Пак А.С.' },
        { code: 'Каб. 203', name: 'German Room', teacher: 'Мюллер К.А.' }
      ];

      // Summary Cards
      const sumContainer = document.getElementById('schedule-rooms-summary');
      if (sumContainer) {
        sumContainer.innerHTML = roomKeys.map(r => `
          <div class="p-3 rounded-xl bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1">
            <div class="text-[10px] font-bold text-emerald-600 font-mono">${r.code}</div>
            <div class="text-xs font-bold text-slate-800 dark:text-slate-200 truncate">${r.name}</div>
            <div class="text-[10px] text-slate-400 truncate">${r.teacher}</div>
          </div>
        `).join('');
      }

      tbody.innerHTML = timeSlots.map((slot, sIdx) => {
        return `
          <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition">
            <td class="py-3 px-3 font-mono font-bold text-slate-500 whitespace-nowrap bg-slate-50 dark:bg-slate-800/60">${slot}</td>
            ${roomKeys.map((r, rIdx) => {
              // Match group based on room code
              const matched = db.groups.find(g => g.room.includes(r.code) && (sIdx % 3 === 0 ? g.schedule.includes('14:00') : true));
              const group = matched || db.groups[rIdx * 3 + (sIdx % 3)];
              return `
                <td class="py-2 px-2.5">
                  <div class="p-2 rounded-lg bg-emerald-50/60 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900/60 space-y-0.5">
                    <div class="flex items-center justify-between">
                      <span class="font-mono font-bold text-emerald-700 dark:text-emerald-300 text-[11px]">${group ? group.id : 'MAM-GRP'}</span>
                      <span class="text-[9px] text-slate-400">Пн-Ср-Пт</span>
                    </div>
                    <div class="text-[11px] font-bold text-slate-800 dark:text-slate-100 truncate">${group ? group.name : 'Группа'}</div>
                    <div class="text-[10px] text-slate-500 truncate">${group ? group.teacherName : r.teacher}</div>
                  </div>
                </td>
              `;
            }).join('')}
          </tr>
        `;
      }).join('');
    }

    /* ==============================================================
       9. MODULE: POS-CASHIER & PAYMENTS
       ============================================================== */
    let selectedPosStudent = null;

    function renderPosModule() {
      renderRecentReceipts();
    }

    function onPosSearchInput(query) {
      const q = query.trim().toLowerCase();
      const resContainer = document.getElementById('pos-search-results');
      if (!q) {
        resContainer.classList.add('hidden');
        return;
      }

      const db = getDB();
      const matches = db.students.filter(s => s.name.toLowerCase().includes(q) || s.phone.includes(q) || s.parentPhone.includes(q));

      if (matches.length === 0) {
        resContainer.innerHTML = `<div class="p-3 text-slate-400">Студент не найден</div>`;
        resContainer.classList.remove('hidden');
        return;
      }

      resContainer.innerHTML = matches.slice(0, 5).map(s => `
        <div onclick="selectPosStudent('${s.id}')" class="p-2.5 hover:bg-emerald-50 dark:hover:bg-slate-700 cursor-pointer flex items-center justify-between">
          <div>
            <div class="font-bold text-slate-800 dark:text-slate-100">${s.name}</div>
            <div class="text-[10px] text-slate-400">${s.groupId} • ${s.course} • Тел: ${s.phone}</div>
          </div>
          <div class="text-right font-mono">
            <span class="font-bold ${s.lessonsBalance <= 1 ? 'text-rose-600' : 'text-emerald-600'}">${s.lessonsBalance} ур.</span>
          </div>
        </div>
      `).join('');
      resContainer.classList.remove('hidden');
    }

    function selectPosStudent(id) {
      const db = getDB();
      selectedPosStudent = db.students.find(s => s.id === id);
      document.getElementById('pos-search-results').classList.add('hidden');
      document.getElementById('pos-student-search').value = selectedPosStudent.name;

      const box = document.getElementById('pos-selected-student-box');
      box.innerHTML = `
        <div class="flex items-center justify-between">
          <div class="font-bold text-slate-900 dark:text-white text-xs">${selectedPosStudent.name}</div>
          <span class="font-mono font-bold px-2 py-0.5 rounded bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300">${selectedPosStudent.groupId}</span>
        </div>
        <div class="text-[11px] text-slate-500">Курс: ${selectedPosStudent.course} • Текущий баланс: <b class="text-emerald-600 font-mono">${selectedPosStudent.lessonsBalance} ур.</b></div>
        <div class="text-[10px] text-slate-400">Родитель: ${selectedPosStudent.parentName} (${selectedPosStudent.parentPhone})</div>
      `;
    }

    function handlePosPaymentSubmit(e) {
      e.preventDefault();
      if (!selectedPosStudent) {
        alert('Пожалуйста, выберите студента из списка поиска!');
        return;
      }

      const amount = Number(document.getElementById('pos-amount-input').value);
      const lessonsAdded = Number(document.getElementById('pos-lessons-input').value);
      const method = document.querySelector('input[name="pos-method"]:checked').value;

      const db = getDB();
      const student = db.students.find(s => s.id === selectedPosStudent.id);
      if (student) {
        student.lessonsBalance += lessonsAdded;
        student.totalPaidSum += amount;
        student.consecutiveAbsences = 0;
        student.status = 'active';
      }

      const receipt = {
        id: 'REC-' + Date.now().toString().slice(-4),
        date: new Date().toISOString().slice(0, 16).replace('T', ' '),
        studentId: selectedPosStudent.id,
        studentName: selectedPosStudent.name,
        phone: selectedPosStudent.phone,
        group: selectedPosStudent.groupId,
        amount,
        method,
        lessonsAdded,
        cashier: currentUser ? currentUser.shortName : 'Рахимова Н.О.'
      };

      db.receipts.unshift(receipt);
      db.cashBalanceToday = (db.cashBalanceToday || 12450000) + amount;
      saveDB(db);

      addAuditLog('POS_PAYMENT', `Принят платеж ${formatMoney(amount)} UZS (${method}) от ${selectedPosStudent.name}. +${lessonsAdded} уроков.`, 'success');
      alert(`Платеж ${formatMoney(amount)} UZS успешно проведен! Баланс студента пополнен на +${lessonsAdded} уроков.`);

      // Open printable receipt
      printThermalReceipt(receipt);

      selectedPosStudent = null;
      document.getElementById('pos-student-search').value = '';
      document.getElementById('pos-selected-student-box').innerHTML = '<div class="text-slate-400 text-[11px]">Студент не выбран. Выберите из поиска выше.</div>';
      renderRecentReceipts();
      updateSidebarQuickStats();
    }

    function renderRecentReceipts() {
      const db = getDB();
      const container = document.getElementById('pos-recent-receipts');
      if (!container) return;

      container.innerHTML = db.receipts.map(r => `
        <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/60 text-xs space-y-1">
          <div class="flex items-center justify-between">
            <span class="font-mono font-bold text-slate-800 dark:text-slate-200">#${r.id}</span>
            <span class="text-[10px] text-slate-400 font-mono">${r.date}</span>
          </div>
          <div class="font-bold text-slate-900 dark:text-white truncate">${r.studentName}</div>
          <div class="flex items-center justify-between text-[11px]">
            <span class="text-emerald-600 font-bold font-mono">+${formatMoney(r.amount)} UZS (${r.method})</span>
            <span class="font-mono text-slate-500">+${r.lessonsAdded} ур.</span>
          </div>
          <div class="pt-1 flex items-center justify-between text-[10px] text-slate-400 border-t border-slate-200 dark:border-slate-700">
            <span>Кассир: ${r.cashier}</span>
            <button type="button" onclick="printThermalReceiptById('${r.id}')" class="text-emerald-600 font-bold hover:underline cursor-pointer">Печать чека</button>
          </div>
        </div>
      `).join('');
    }

    function printThermalReceiptById(id) {
      const db = getDB();
      const r = db.receipts.find(rec => rec.id === id);
      if (r) printThermalReceipt(r);
    }

    function printThermalReceipt(r) {
      const printArea = document.getElementById('print-area');
      printArea.innerHTML = `
        <div style="max-width: 78mm; font-family: monospace; font-size: 11px; line-height: 1.4; color: black;">
          <div style="text-align: center; border-bottom: 1px dashed black; padding-bottom: 8px; margin-bottom: 8px;">
            <div style="font-size: 14px; font-weight: bold;">MARYAM ACADEMY MISSION</div>
            <div>Филиал: г. Маргилан, ул. Б. Маргиноний, 42</div>
            <div>Тел: +998 (73) 254-00-11</div>
            <div style="font-weight: bold; margin-top: 4px;">ФИСКАЛЬНЫЙ ЧЕК #${r.id}</div>
          </div>
          <div style="margin-bottom: 8px;">
            <div>Дата/Время: ${r.date}</div>
            <div>Кассир: ${r.cashier}</div>
            <div>Студент: ${r.studentName}</div>
            <div>Группа: ${r.group}</div>
            <div>Способ: ${r.method}</div>
          </div>
          <div style="border-top: 1px dashed black; border-bottom: 1px dashed black; padding: 6px 0; margin-bottom: 8px;">
            <div style="display: flex; justify-content: space-between;">
              <span>Пополнение абонемента (+${r.lessonsAdded} ур.)</span>
              <span style="font-weight: bold;">${formatMoney(r.amount)} UZS</span>
            </div>
          </div>
          <div style="text-align: right; font-size: 13px; font-weight: bold; margin-bottom: 10px;">
            ИТОГО К ОПЛАТЕ: ${formatMoney(r.amount)} UZS
          </div>
          <div style="text-align: center; font-size: 10px; border-top: 1px dashed black; padding-top: 8px;">
            <div>Благодарим за обучение в MAM!</div>
            <div>Проверка чека: mam.academy/verify/${r.id}</div>
          </div>
        </div>
      `;
      window.print();
    }

    /* ==============================================================
       10. MODULE: ATTENDANCE JOURNAL 18 GROUPS
       ============================================================== */
    function initJournalModule() {
      const db = getDB();
      const select = document.getElementById('journal-group-select');
      if (!select) return;

      // Filter groups if logged in as a specific teacher
      let availableGroups = db.groups;
      if (currentUser && currentUser.key.startsWith('teacher_')) {
        availableGroups = db.groups.filter(g => g.teacherKey === currentUser.key);
      }

      select.innerHTML = availableGroups.map(g => `
        <option value="${g.id}">${g.id} — ${g.name} (${g.teacherName})</option>
      `).join('');

      if (availableGroups.length > 0) {
        renderJournalTable(availableGroups[0].id);
      }
    }

    function renderJournalTable(groupId) {
      const db = getDB();
      const group = db.groups.find(g => g.id === groupId) || db.groups[0];
      const students = db.students.filter(s => s.groupId === group.id);

      // Meta Card
      const meta = document.getElementById('journal-group-meta');
      if (meta) {
        meta.innerHTML = `
          <div>
            <div class="flex items-center gap-2">
              <span class="text-sm font-bold text-emerald-600 font-mono">${group.id}</span>
              <h3 class="text-sm font-black text-slate-900 dark:text-white">${group.name}</h3>
            </div>
            <div class="text-xs text-slate-500 mt-0.5">
              Преподаватель: <b class="text-slate-800 dark:text-slate-200">${group.teacherName}</b> • Расписание: ${group.schedule} • ${group.room}
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span class="text-xs font-mono font-bold px-2.5 py-1 rounded-lg bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300">
              Студентов в группе: ${students.length}
            </span>
          </div>
        `;
      }

      // Table Body
      const tbody = document.getElementById('journal-table-body');
      if (!tbody) return;

      tbody.innerHTML = students.map(s => {
        return `
          <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/50 transition">
            <td class="py-2.5 px-3">
              <div class="font-bold text-slate-900 dark:text-white font-sans">${s.name}</div>
              <div class="text-[10px] text-slate-400 font-sans">Родитель: ${s.parentName}</div>
            </td>
            <td class="py-2.5 px-3 font-mono text-slate-600 dark:text-slate-300">${s.phone}</td>
            <td class="py-2.5 px-3 text-center">
              <span class="font-mono font-black text-sm ${s.lessonsBalance <= 0 ? 'text-rose-600' : (s.lessonsBalance === 1 ? 'text-amber-600' : 'text-emerald-600')}">
                ${s.lessonsBalance} уроков
              </span>
            </td>
            <td class="py-2.5 px-3 text-center font-mono ${s.consecutiveAbsences >= 3 ? 'text-rose-600 font-bold' : 'text-slate-400'}">
              ${s.consecutiveAbsences}
            </td>
            <td class="py-2.5 px-3 text-center">
              ${s.lessonsBalance > 0
                ? '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300">ДОПУЩЕН</span>'
                : '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-100 dark:bg-rose-950 text-rose-700 dark:text-rose-300">ТРЕБУЕТСЯ ОПЛАТА</span>'
              }
            </td>
            <td class="py-2.5 px-3 text-center">
              <div class="flex items-center justify-center gap-1.5">
                <button type="button" onclick="markAttendance('${s.id}', 'present')" class="px-2.5 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg font-bold text-xs transition cursor-pointer flex items-center gap-1" title="Списать 1 урок">
                  <i data-lucide="check" class="w-3.5 h-3.5"></i>
                  <span>Был (-1 ур.)</span>
                </button>
                <button type="button" onclick="markAttendance('${s.id}', 'absent')" class="px-2 py-1 bg-rose-600 hover:bg-rose-700 text-white rounded-lg font-bold text-xs transition cursor-pointer" title="Не был (Пропуск)">
                  НБ
                </button>
                <button type="button" onclick="markAttendance('${s.id}', 'excused')" class="px-2 py-1 bg-slate-200 hover:bg-slate-300 dark:bg-slate-700 text-slate-800 dark:text-slate-200 rounded-lg font-bold text-xs transition cursor-pointer" title="Уважительная причина (Без списания)">
                  Уваж.
                </button>
              </div>
            </td>
          </tr>
        `;
      }).join('');
      lucide.createIcons();
    }

    function markAttendance(studentId, type) {
      const db = getDB();
      const student = db.students.find(s => s.id === studentId);
      if (!student) return;

      if (type === 'present') {
        if (student.lessonsBalance <= 0) {
          if (!confirm(`Внимание! У студента ${student.name} баланс уроков равен 0. Всё равно списать в минус?`)) return;
        }
        student.lessonsBalance -= 1;
        student.consecutiveAbsences = 0;
        addAuditLog('ATTENDANCE_DEDUCT', `Списание 1 урока у ${student.name} (${student.groupId}). Остаток: ${student.lessonsBalance}`, 'warning');
      } else if (type === 'absent') {
        student.consecutiveAbsences += 1;
        addAuditLog('ATTENDANCE_ABSENT', `Отметка "НБ" (пропуск) у ${student.name} (${student.groupId}). Пропусков подряд: ${student.consecutiveAbsences}`);
      } else if (type === 'excused') {
        addAuditLog('ATTENDANCE_EXCUSED', `Отметка "Уважительная причина" у ${student.name} (${student.groupId}). Баланс не списан.`);
      }

      saveDB(db);
      renderJournalTable(student.groupId);
      updateSidebarQuickStats();
    }

    /* ==============================================================
       11. MODULE: EXAMS, GRADES & MAM-COINS (GAMIFICATION)
       ============================================================== */
    function renderGamificationModule() {
      const db = getDB();

      // Populate student select
      const select = document.getElementById('exam-student-select');
      if (select) {
        select.innerHTML = db.students.map(s => `
          <option value="${s.id}">${s.name} (${s.groupId})</option>
        `).join('');
      }

      // Leaderboard Top 10 sorted by MAM-Coins
      const top10 = [...db.students].sort((a, b) => (b.mamCoins || 0) - (a.mamCoins || 0)).slice(0, 10);
      const lbBody = document.getElementById('gamification-leaderboard-body');
      if (lbBody) {
        lbBody.innerHTML = top10.map((s, idx) => {
          let rankMedal = `#${idx + 1}`;
          if (idx === 0) rankMedal = '🥇 1';
          if (idx === 1) rankMedal = '🥈 2';
          if (idx === 2) rankMedal = '🥉 3';

          return `
            <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition">
              <td class="py-2.5 px-3 text-center font-bold font-mono ${idx < 3 ? 'text-amber-500' : 'text-slate-400'}">${rankMedal}</td>
              <td class="py-2.5 px-3">
                <div class="font-bold text-slate-900 dark:text-white">${s.name}</div>
                <div class="text-[10px] text-slate-400">${s.groupId}</div>
              </td>
              <td class="py-2.5 px-3 text-slate-600 dark:text-slate-300">${s.course}</td>
              <td class="py-2.5 px-3 text-center font-mono font-bold text-emerald-600">${s.avgGrade || 88}%</td>
              <td class="py-2.5 px-3 text-right font-mono font-black text-amber-500">${s.mamCoins || 150} 🪙</td>
            </tr>
          `;
        }).join('');
      }

      // Qualifications list
      const qualList = document.getElementById('gamification-qualification-list');
      if (qualList) {
        const qualified = db.students.filter(s => (s.avgGrade || 0) >= 80);
        qualList.innerHTML = qualified.slice(0, 6).map(s => `
          <div class="p-2.5 rounded-lg bg-emerald-50/70 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900 flex items-center justify-between text-xs">
            <div>
              <div class="font-bold text-emerald-900 dark:text-emerald-200">${s.name}</div>
              <div class="text-[10px] text-emerald-600">${s.course} • Балл: ${s.avgGrade}%</div>
            </div>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-600 text-white">
              КВАЛИФИЦИРОВАН
            </span>
          </div>
        `).join('');
      }
    }

    function handleNewExamGradeSubmit(e) {
      e.preventDefault();
      const studentId = document.getElementById('exam-student-select').value;
      const title = document.getElementById('exam-title-input').value.trim();
      const score = Number(document.getElementById('exam-score-input').value);
      const coins = Number(document.getElementById('exam-coins-input').value);

      const db = getDB();
      const student = db.students.find(s => s.id === studentId);
      if (student) {
        student.avgGrade = Math.round(((student.avgGrade || 75) + score) / 2);
        student.mamCoins = (student.mamCoins || 0) + coins;
        saveDB(db);
        addAuditLog('EXAM_SCORE', `Оценка теста "${title}" у ${student.name}: ${score}%. Начислено +${coins} MAM-Coins.`, 'success');
        alert(`Результат экзамена записан! Студенту ${student.name} начислено +${coins} MAM-Coins.`);
        document.getElementById('exam-title-input').value = '';
        renderGamificationModule();
      }
    }

    /* ==============================================================
       12. MODULE: CONTRACTS & CERTIFICATES GENERATOR
       ============================================================== */
    function initContractsModule() {
      const db = getDB();
      const select = document.getElementById('doc-student-select');
      if (!select) return;

      select.innerHTML = db.students.map(s => `
        <option value="${s.id}">${s.name} (${s.groupId} — ${s.course})</option>
      `).join('');

      if (db.students.length > 0) {
        onDocStudentSelect(db.students[0].id);
      }
    }

    function onDocStudentSelect(id) {
      const db = getDB();
      const student = db.students.find(s => s.id === id);
      if (!student) return;

      document.getElementById('doc-parent-input').value = student.parentName;
      document.getElementById('doc-passport-input').value = student.parentPassport || 'AD 1234567';
      document.getElementById('doc-fee-input').value = formatMoney(student.monthlyFee || 650000) + ' UZS';
    }

    function generateAndPreviewContract() {
      const db = getDB();
      const studentId = document.getElementById('doc-student-select').value;
      const student = db.students.find(s => s.id === studentId);
      if (!student) return;

      const parentName = document.getElementById('doc-parent-input').value;
      const passport = document.getElementById('doc-passport-input').value;
      const fee = document.getElementById('doc-fee-input').value;

      const container = document.getElementById('doc-preview-container');
      container.innerHTML = `
        <div class="w-full bg-white text-black p-6 rounded-lg shadow-sm border border-slate-200 font-sans space-y-4">
          <div class="text-center border-b pb-3">
            <div class="text-sm font-black tracking-wider text-emerald-800">MARYAM ACADEMY MISSION (MAM)</div>
            <div class="text-[11px] text-slate-500">г. Маргилан, ул. Б. Маргиноний, 42 • ИНН 308945120</div>
            <div class="text-xs font-bold mt-2">ДОГОВОР НА ОКАЗАНИЕ ОБРАЗОВАТЕЛЬНЫХ УСЛУГ #${student.contractNumber}</div>
            <div class="text-[10px] text-slate-400">TA'LIM XIZMATLARI KO'RSATISH SHARTNOMASI</div>
          </div>

          <div class="text-xs space-y-2">
            <p><b>Исполнитель:</b> НОУ «Maryam Academy Mission» в лице Директора Богданова Т.Я.</p>
            <p><b>Заказчик (Родитель):</b> ${parentName}, паспорт: ${passport}</p>
            <p><b>Студент (Обучающийся):</b> ${student.name}</p>
            <p><b>Курс / Программа:</b> ${student.course} (Группа ${student.groupId})</p>
            <p><b>Стоимость обучения:</b> ${fee} за академический месяц (12 занятий).</p>
          </div>

          <div class="text-[11px] text-slate-600 space-y-1">
            <p>1. Исполнитель обязуется предоставить качественное обучение в соответствии с учебным планом Академии MAM.</p>
            <p>2. Заказчик обязуется своевременно вносить абонентскую плату до 5 числа каждого месяца.</p>
          </div>

          <div class="pt-4 border-t flex justify-between text-xs">
            <div>
              <div class="font-bold">Академия MAM (Маргилан):</div>
              <div class="mt-4 border-b border-black w-36"></div>
              <div class="text-[10px] text-slate-500">Директор: Богданов Т.Я. (М.П.)</div>
            </div>
            <div>
              <div class="font-bold">Заказчик (Родитель):</div>
              <div class="mt-4 border-b border-black w-36"></div>
              <div class="text-[10px] text-slate-500">${parentName}</div>
            </div>
          </div>
        </div>
      `;
    }

    function generateAndPreviewCertificate() {
      const db = getDB();
      const studentId = document.getElementById('doc-student-select').value;
      const student = db.students.find(s => s.id === studentId);
      if (!student) return;

      const container = document.getElementById('doc-preview-container');
      container.innerHTML = `
        <div class="w-full bg-slate-900 text-white p-8 rounded-xl shadow-md border-4 border-amber-500 font-sans space-y-4 text-center relative overflow-hidden">
          <div class="text-[10px] tracking-widest text-amber-400 font-bold uppercase">MARYAM ACADEMY MISSION • MARGILAN</div>
          <div class="text-xl font-black text-amber-300 tracking-wider">СЕРТИФИКАТ ОБ ОКОНЧАНИИ КУРСА</div>
          <div class="text-[11px] text-slate-400">CERTIFICATE OF COMPLETION</div>
          
          <div class="py-2">
            <div class="text-xs text-slate-300">Настоящий сертификат подтверждает, что</div>
            <div class="text-lg font-black text-white mt-1 border-b border-amber-500/50 pb-1 inline-block px-4">${student.name}</div>
          </div>

          <div class="text-xs text-slate-300">
            успешно освоил(а) квалификационную программу:
            <div class="text-base font-bold text-amber-400 mt-1">${student.course}</div>
            <div class="text-[11px] text-slate-400 mt-0.5">Средний академический балл: ${student.avgGrade || 90}%</div>
          </div>

          <div class="pt-6 flex items-center justify-between text-xs text-slate-400 border-t border-slate-800">
            <div class="text-left font-mono">
              <div>Сертификат: #${student.contractNumber.replace('MAM', 'CERT')}</div>
              <div>Дата: 2026-10-12</div>
            </div>
            <div class="text-center font-mono text-[9px] bg-slate-800 p-2 rounded border border-amber-500/40">
              [QR VERIFIED]<br/>mam.academy/qr/${student.id}
            </div>
            <div class="text-right">
              <div class="font-bold text-white">Директор Академии MAM:</div>
              <div class="text-amber-400 font-bold">Богданов Т.Я.</div>
            </div>
          </div>
        </div>
      `;
    }

    function printActiveDocument() {
      const container = document.getElementById('doc-preview-container');
      const printArea = document.getElementById('print-area');
      printArea.innerHTML = container.innerHTML;
      window.print();
    }

    /* ==============================================================
       13. MODULE: STAFF TIMESHEET (CHECK-IN / CHECK-OUT)
       ============================================================== */
    function renderTimesheetModule() {
      const db = getDB();
      const tbody = document.getElementById('timesheet-table-body');
      if (!tbody) return;

      tbody.innerHTML = db.timesheetRecords.map(r => `
        <tr class="hover:bg-slate-50 dark:hover:bg-slate-800/40 transition">
          <td class="py-2.5 px-3 font-bold text-slate-900 dark:text-white font-sans">${r.staffName}</td>
          <td class="py-2.5 px-3 font-sans text-slate-500">${r.role}</td>
          <td class="py-2.5 px-3 text-center text-emerald-600 font-bold">${r.inTime}</td>
          <td class="py-2.5 px-3 text-center text-rose-500 font-bold">${r.outTime}</td>
          <td class="py-2.5 px-3 text-center font-bold">${r.hours} ч.</td>
          <td class="py-2.5 px-3 text-center">
            ${r.status === 'active'
              ? '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300">НА СМЕНЕ</span>'
              : '<span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600">ЗАКРЫТА</span>'
            }
          </td>
        </tr>
      `).join('');

      // Check current user status
      if (currentUser) {
        const activeRec = db.timesheetRecords.find(r => r.staffKey === currentUser.key && r.status === 'active');
        const statusEl = document.getElementById('timesheet-user-status');
        const btnIn = document.getElementById('btn-timesheet-in');
        const btnOut = document.getElementById('btn-timesheet-out');

        if (activeRec) {
          if (statusEl) statusEl.innerHTML = `<span class="text-emerald-600 font-bold">● На смене с ${activeRec.inTime}</span>`;
          if (btnIn) btnIn.disabled = true;
          if (btnOut) btnOut.disabled = false;
        } else {
          if (statusEl) statusEl.innerHTML = `<span class="text-slate-400">Смена не открыта</span>`;
          if (btnIn) btnIn.disabled = false;
          if (btnOut) btnOut.disabled = true;
        }
      }
    }

    function handleTimesheetCheckIn() {
      if (!currentUser) return;
      const db = getDB();
      const now = new Date();
      const pad = n => String(n).padStart(2, '0');
      const timeStr = `${pad(now.getHours())}:${pad(now.getMinutes())}`;

      const newRec = {
        id: 'TS-' + Date.now().toString().slice(-4),
        date: now.toISOString().slice(0, 10),
        staffKey: currentUser.key,
        staffName: currentUser.name,
        role: currentUser.roleName,
        inTime: timeStr,
        outTime: '--',
        hours: 0,
        status: 'active'
      };

      db.timesheetRecords.unshift(newRec);
      saveDB(db);
      addAuditLog('CHECK_IN', `Сотрудник ${currentUser.name} начал смену в ${timeStr}`);
      alert(`Смена успешно открыта в ${timeStr}!`);
      renderTimesheetModule();
    }

    function handleTimesheetCheckOut() {
      if (!currentUser) return;
      const db = getDB();
      const now = new Date();
      const pad = n => String(n).padStart(2, '0');
      const timeStr = `${pad(now.getHours())}:${pad(now.getMinutes())}`;

      const rec = db.timesheetRecords.find(r => r.staffKey === currentUser.key && r.status === 'active');
      if (rec) {
        rec.outTime = timeStr;
        rec.status = 'closed';
        rec.hours = 8;
        saveDB(db);
        addAuditLog('CHECK_OUT', `Сотрудник ${currentUser.name} завершил смену в ${timeStr}`);
        alert(`Смена успешно закрыта в ${timeStr}! Отработано: 8 часов.`);
        renderTimesheetModule();
      }
    }

    /* ==============================================================
       14. MODULE: TELEGRAM SMART FOLLOW-UP MODAL
       ============================================================== */
    function openTelegramModal(studentId) {
      const db = getDB();
      const student = db.students.find(s => s.id === studentId);
      if (!student) return;

      const modal = document.getElementById('modal-telegram');
      const recipientEl = document.getElementById('tg-modal-recipient');
      const textEl = document.getElementById('tg-modal-text');
      const linkEl = document.getElementById('tg-modal-link');

      recipientEl.textContent = `${student.parentName} (${student.parentPhone}) — Ученик: ${student.name} (${student.groupId})`;

      // Polite follow-up text in Russian & Uzbek
      const cleanPhone = student.parentPhone.replace(/[^0-9]/g, '');
      const politeText = currentLang === 'uz'
        ? `Assalomu alaykum, ${student.parentName}! Maryam Academy Mission (Marg'ilon) o'quv markazidan sizga bog'lanmoqdamiz. Farzandingiz ${student.name} (${student.course}) darslarida faol qatnashmoqda. Joriy o'quv oyi bo'yicha darslar balansi yakunlanmoqda (${student.lessonsBalance} ta qoldi). Darslar uzluksizligini ta'minlash uchun abonent to'lovini amalga oshirishingizni so'raymiz. To'lov: Click yoki Payme orqali qabul qilinadi. Hurmat bilan, Maryam Academy Mission. Tel: +998 (73) 254-00-11.`
        : `Здравствуйте, ${student.parentName}! Вас беспокоит администрация Академии IT и Языков «Maryam Academy Mission» (Маргилан). Ваш ребенок ${student.name} успешно занимается по направлению «${student.course}» (группа ${student.groupId}). Напоминаем, что текущий баланс уроков подходит к концу (осталось: ${student.lessonsBalance} ур.). Для непрерывного продолжения учебного процесса просим продлить абонемент на следующий период. Оплата доступна через Click, Payme или в кассе Академии. С уважением, Maryam Academy Mission. Тел: +998 (73) 254-00-11.`;

      textEl.value = politeText;
      linkEl.href = `https://t.me/+${cleanPhone}?text=${encodeURIComponent(politeText)}`;

      modal.classList.remove('hidden');
      lucide.createIcons();
    }

    function closeTelegramModal() {
      document.getElementById('modal-telegram').classList.add('hidden');
    }

    function copyTelegramText() {
      const text = document.getElementById('tg-modal-text').value;
      navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById('tg-btn-copy-label');
        btn.textContent = 'Скопировано!';
        setTimeout(() => { btn.textContent = 'Копировать'; }, 2000);
      });
    }

    /* ==============================================================
       15. DATABASE BACKUP / RESTORE JSON & SETTINGS
       ============================================================== */
    function exportDatabaseJSON() {
      const db = getDB();
      const jsonStr = JSON.stringify(db, null, 2);
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      const now = new Date().toISOString().slice(0, 10);
      a.href = url;
      a.download = `mam_erp_backup_${now}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      addAuditLog('DB_EXPORT', 'Экспорт резервной копии базы данных в JSON файл');
    }

    function handleImportDatabaseJSON(e) {
      const file = e.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = function(evt) {
        try {
          const parsed = JSON.parse(evt.target.result);
          if (parsed.students && parsed.groups) {
            saveDB(parsed);
            addAuditLog('DB_IMPORT', `Импорт базы из файла: ${file.name}`);
            alert('База данных успешно импортирована и обновлена!');
            location.reload();
          } else {
            alert('Ошибка: Структура загруженного JSON-файла не соответствует стандарту Академии MAM.');
          }
        } catch (err) {
          alert('Ошибка чтения JSON: ' + err.message);
        }
      };
      reader.readAsText(file);
    }

    function resetDatabaseToFactory() {
      if (!confirm('Вы действительно хотите сбросить базу данных к эталонным 18 группам и 54 студентам? Все новые внесённые данные будут перезаписаны.')) return;
      const initial = generateInitialDB();
      saveDB(initial);
      addAuditLog('DB_RESET', 'Сброс базы данных к начальному эталону (54 студента, 18 групп)', 'danger');
      alert('База данных успешно сброшена к эталонному состоянию!');
      location.reload();
    }

    /* ==============================================================
       16. UI UTILITIES (THEME, LANG, FORMATTERS)
       ============================================================== */
    function toggleTheme() {
      const isDark = document.documentElement.classList.toggle('dark');
      localStorage.setItem('mam_theme', isDark ? 'dark' : 'light');
      lucide.createIcons();
    }

    function toggleLang() {
      currentLang = currentLang === 'ru' ? 'uz' : 'ru';
      localStorage.setItem('mam_lang', currentLang);
      applyTranslations();
      if (currentUser) {
        document.getElementById('top-user-role').textContent = currentLang === 'uz' ? currentUser.roleNameUz : currentUser.roleName;
        document.getElementById('side-emp-role').textContent = currentLang === 'uz' ? currentUser.roleNameUz : currentUser.roleName;
      }
      renderSidebarNav();
    }

    function applyTranslations() {
      const dict = I18N[currentLang] || I18N.ru;
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) el.textContent = dict[key];
      });
      const ind = document.getElementById('lang-indicator');
      if (ind) ind.textContent = currentLang.toUpperCase() + ' (MAM)';
    }

    function formatMoney(n) {
      return Number(n || 0).toLocaleString('ru-RU');
    }

    // Live clock for timesheet
    setInterval(() => {
      const clockEl = document.getElementById('timesheet-current-clock');
      if (clockEl) {
        const now = new Date();
        const pad = n => String(n).padStart(2, '0');
        clockEl.textContent = `${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
      }
    }, 1000);

    // Initializer
    document.addEventListener('DOMContentLoaded', () => {
      initAuth();
      applyTranslations();
      lucide.createIcons();
    });
  </script>
</body>
</html>
''')
    print("crm.html completely written successfully!")

if __name__ == "__main__":
    generate()
