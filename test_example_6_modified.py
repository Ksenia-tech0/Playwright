# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-15
# Время: 22:57
# Описание: Я модифицировала код из раздела "Первый сценарий".
# Я заменила браузер WebKit на Chromium.
# Зачем: чтобы показать, что Playwright поддерживает 3 браузера.
# Добавила headless=False
# Зачем: чтобы увидеть, как работает браузер

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Изменено: запуск Chromium вместо WebKit
    browser = p.chromium.launch(headless=False)
    # Открытие новой страницы
    page = browser.new_page()
    # Переход на сайт Playwright
    page.goto("https://playwright.dev/")
    # Изменено: сохранение скриншота в другой файл
    page.screenshot(path="example_modified.png")
    # Закрытие браузера
    browser.close()