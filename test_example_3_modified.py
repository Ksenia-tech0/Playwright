import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("assert value")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("button", name="Delete").click()
    page.get_by_text("This is just a demo of").click()
    page.get_by_text("This is just a demo of").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.locator("html").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("water the plants")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_test_id("todo-title").click()
    page.get_by_test_id("todo-title").click()
    page.get_by_role("checkbox", name="Toggle Todo").check()
    expect(page.get_by_test_id("todo-title")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("water the plants")
    page.get_by_role("link", name="Completed").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)