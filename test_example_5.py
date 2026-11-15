# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-13
# Время: 21:13
# Описание: Код демонстрирует запись трассировки в Playwright.
# Скрипт записывает все действия в файл trace.zip
# Я добавила методы context.tracing.start() и context.tracing.stop() из раздела "Просмотр трассировки"

import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Здесь запускается браузер
    browser = playwright.chromium.launch(headless=False)
    # Создается изолированное окружение
    context = browser.new_context()
    page = context.new_page()
    
    # Добавлено: запись трассировки
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    # Переход в TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("water the plants")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    
    # Проверка колличества задач
    expect(page.get_by_test_id("todo-title")).to_have_count(1)
    
    # Проверка наличия элемента и его содержание
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("water the plants")
    
    # Галочка на "Toggle Todo" при наведении курсора
    page.get_by_role("checkbox", name="Toggle Todo").check()
    
    # Добавлено: завершение записи трассировки
    context.tracing.stop(path="trace.zip")

    # Закрытие контекста браузера
    context.close()
    # Закрытие браузера
    browser.close()

with sync_playwright() as playwright:
    run(playwright)