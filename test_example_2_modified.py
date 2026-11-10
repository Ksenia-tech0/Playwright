# ФИО: Волкова Ксения Руслановна
# Дата: 2026-11-10
# Время: 22:31
# Описание: Я модифицировала тест из раздела "Using fixtures".
# Изменила ссылку в фикстуре с главной страницы на раздел документации Python.
# Зачем: чтобы показать, как фикстура используется для подготовки страницы перед тестом.
# Добавила одидание появления заголовка.
# Зачем: для стабильности при медленной загрузке сети.

import pytest
from playwright.sync_api import Page, expect

# Декоратор @pytest.fixture создаёт фикстуру — специальный блок, выполняющийся до/после каждого теста.
# scope="function" означает, что фикстура запускается отдельно для каждой тестовой функции.
# autouse=True означает, что фикстура применяется автоматически ко всем тестам в файле.
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page):
    
    print("Начало настройки теста (фикстура)")
    
    # Переход сразу на страницу документации Python.
    page.goto("https://playwright.dev/python/docs/intro")
    
    # Ожидание заголовка.
    page.wait_for_selector("h1")
    
    yield
    
   
    print("Завершение работы теста, очистка")

# Тестовая функция - "test_" (для автоматического обнаружения тестов)
# Page - встроенная фикстура, которая предоставляет объект страницы.
def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/python/docs/intro")