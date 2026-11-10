# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-10
# Время: 22:04
# Описание: Я скопировала код из раздела "Using fixtures". 
# Он демонстрирует использование фикстуры pytest с областью видимости "function" и autouse=True. 
# Фикстура автоматически выполняет переход на стартовую страницу и выводит сообщения.
import pytest
from playwright.sync_api import Page, expect

# Декоратор @pytest.fixture для фикстуры(специального блока, который выполняется до/после каждого теста).
# scope="function" - фикстура запускается для каждой функции отдельно.
# autouse=True - фикстура применяется автоматически.
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("before the test runs")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield
    
    print("after the test runs")

# Тестовая функция - "test_" (для автоматического обнаружения тестов)
# Page - встроенная фикстура, которая предоставляет объект страницы.
def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")