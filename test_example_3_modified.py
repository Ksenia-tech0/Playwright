# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-12
# Время: 16:54
# Описание: Я модифицировала исходный код
# Удалила дублирующиеся строки.
# Зачем: Чтобы код стал понятнее
# Добавила клик по ссылке "Completed".
# Зачем: чтобы показать, как переключаться между фильтрами задач.

import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Здесь запускается браузер
    browser = playwright.chromium.launch(headless=False)
    # Создается изолированное окружение
    context = browser.new_context()
    page = context.new_page()
    
    # Переход в TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")
    
    # Клик по полю ввода задачи
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Введение тестового значения
    page.get_by_role("textbox", name="What needs to be done?").fill("assert value")
    # Нажатие клавиши Enter для добавления задачи
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    # Клик по кнопке удаления
    page.get_by_role("button", name="Delete").click()
    
    # Снова клик по полю ввода
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Клик по элементу
    page.locator("html").click()
    
    # Очередной клик по полю ввода
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Ввод пустой строки
    page.get_by_role("textbox", name="What needs to be done?").fill("")
    # Клик по полю ввода
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Введение текста новой задачи
    page.get_by_role("textbox", name="What needs to be done?").fill("water the plants")
    # Нажатие Enter для добавления задачи
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    
    # Клик по заголовку задачи
    page.get_by_test_id("todo-title").click()
    # Галочка на "Toggle Todo" при наведении курсора
    page.get_by_role("checkbox", name="Toggle Todo").check()
    
    # Проверка наличия элемента и его содержание
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("water the plants")
    
    # добавлено: клик по ссылке "Completed" для переключения на выполненные задачи
    page.get_by_role("link", name="Completed").click()
    
    # Закрытие контекста браузера
    context.close()
    # Закрытие браузера
    browser.close()

with sync_playwright() as playwright:
    run(playwright)