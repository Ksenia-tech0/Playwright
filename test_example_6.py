# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-14
# Время: 18:03
# Описание: Я скопировала код из раздела "Начало работы - Библиотека".
# Этот скрипт открывает браузер WebKit, переходит на сайт Playwright и делает скриншот страницы.

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запуск браузера WebKit
    browser = p.webkit.launch()
    # Открытие новой страницы
    page = browser.new_page()
    # Переход на сайт Playwright
    page.goto("https://playwright.dev/")
    # Скриншот страницы и сохранение в файл example.png
    page.screenshot(path="example.png")
    # Закрытие браузера
    browser.close()