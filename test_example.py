# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-10
# Время: 13:23
# Описание: Здесь два первых теста из Playwright. 
# Первый тест (test_has_title) открывает сайт и проверяет наличие слова "Playwright".
# Второй тест (test_get_started_link) кликает на ссылку "Get started".
import re
from playwright.sync_api import Page, expect

# Переход на страницу
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    # Создание локатора и клик по нему
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()