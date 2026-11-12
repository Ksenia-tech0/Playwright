# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-12
# Время: 10:34
# Описание: Код сгенерирован через Codegen для записи действий в браузере. 
# Он открывает браузер, переходит на TodoMVC и добавляет задачу.
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
    # Повторный переход
    page.goto("https://demo.playwright.dev/todomvc/#/")
    # Клик по полю ввода задачи
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Введение тестового значения
    page.get_by_role("textbox", name="What needs to be done?").fill("assert value")
    # Нажатие клавиши Enter для добавления задачи
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    # Клик по кнопке удаления
    page.get_by_role("button", name="Delete").click()
    # Клик по тексту демонстрации
    page.get_by_text("This is just a demo of").click()
    # Повторный клик по тому же тексту
    page.get_by_text("This is just a demo of").click()
    # Снова клик по полю ввода
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Клик по элементу html для сброса фокуса
    page.locator("html").click()
    # Очередной клик по полю ввода
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Введение пустой строки
    page.get_by_role("textbox", name="What needs to be done?").fill("")
    # Клик по полю ввода
    page.get_by_role("textbox", name="What needs to be done?").click()
    # Введение текста новой задачи
    page.get_by_role("textbox", name="What needs to be done?").fill("water the plants")
    # Нажатие Enter для добавления задачи в список
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    # Клик по заголовку задачи
    page.get_by_test_id("todo-title").click()
    # Повторный клик по заголовку задачи
    page.get_by_test_id("todo-title").click()
    # Галочка на "Toggle Todo" при наведении курсора
    page.get_by_role("checkbox", name="Toggle Todo").check()
    # Проверка наличия элемента и его содержание
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    # Проверка, что элемент содержит нужный текст
    expect(page.get_by_test_id("todo-title")).to_contain_text("water the plants")

    # ------------------------------
    # Закрытие контекста браузера
    context.close()
    # Закрытие браузера
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
