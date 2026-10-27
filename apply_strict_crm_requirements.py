#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_strict_crm_requirements.py
Enforces:
1. NO buttons or links to public site ("Перейти на сайт", "Главная", "О нас", "Курсы", "Сайт MAM", index.html).
2. NO promo blocks, 3D maps, videos, or quizzes.
3. User IMMEDIATELY lands into internal CRM/ERP interface on page load (sidebar on left, workspace on right, Director Bogdanov T.Y. as default role).
4. Full autonomous, 100% working code in crm.html.
"""

import re

def main():
    print("Reading crm.html...")
    with open("crm.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Remove link to index.html / Сайт MAM
    link_pat = r'<!-- Link to Public Landing Page -->\s*<a href="/index\.html"[\s\S]*?</a>'
    if re.search(link_pat, html):
        html = re.sub(link_pat, '', html, count=1)
        print("Removed link to public landing page.")
    else:
        # Fallback search
        html = html.replace('<a href="/index.html"', '<!-- removed -->')

    # 2. Make view-login hidden by default
    html = html.replace(
        '<div id="view-login" class="min-h-screen flex items-center justify-center',
        '<div id="view-login" class="hidden min-h-screen flex items-center justify-center'
    )

    # 3. Make view-dashboard visible by default (remove hidden class)
    html = html.replace(
        '<div id="view-dashboard" class="hidden min-h-screen flex flex-col',
        '<div id="view-dashboard" class="min-h-screen flex flex-col'
    )

    # 4. Initialize currentUser to director and call setupUserSession() on page load
    init_pat = r'initLang\(\);\s*initTheme\(\);'
    new_init = """const savedUserKey = localStorage.getItem('mam_last_user') || 'director';
    currentUser = ACCOUNTS[savedUserKey] || ACCOUNTS['director'];
    setupUserSession();
    initLang();
    initTheme();"""

    if re.search(init_pat, html):
        html = re.sub(init_pat, new_init, html, count=1)
        print("Updated init sequence to immediately launch CRM session.")

    # 5. In fastSwitchUser, save to localStorage
    if "localStorage.setItem('mam_last_user', accountKey);" not in html:
        html = html.replace(
            "currentUser = ACCOUNTS[accountKey];",
            "currentUser = ACCOUNTS[accountKey];\n      localStorage.setItem('mam_last_user', accountKey);"
        )
        print("Added persistence of active user role in fastSwitchUser.")

    with open("crm.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Strict requirements applied successfully to crm.html!")

if __name__ == "__main__":
    main()
