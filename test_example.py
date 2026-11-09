# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-09
# Время: 11:46
# Описание: Здесь два теста для библиотеки Playwright:
# 1. test_has_title (проверяет, что заголовок страницы содержит слово "Playwright")
# 2. test_get_started_link (кликает по ссылке и проверяет отображение заголовка "Installation")
# Я добавила сохранение ссылки
# Добавлено свечение элемента для визуального эффекта
# Добавлено скрытие подсветки, чтобы было понятно, когда курсор не наведен на элемент
# Добавлен клик по ссылке
# Зачем: подсветка добавлена для визуального контроля

import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Сохранение ссылки
    link = page.get_by_role("link", name="Get started")
    
    # Подсвечивание элемента
    link.highlight()
    
    # Скрытие подсветки
    link.hide_highlight()
    
    # Клик по ссылке
    link.click()
    
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()