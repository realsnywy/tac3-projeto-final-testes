# Testes de automação web utilizando Selenium e Playwright.
import pytest
from app import web_automation
from selenium.webdriver.common.by import By

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/"
FORM_TEST_URL_LAMBDATEST = (
    "https://www.lambdatest.com/selenium-playground/simple-form-demo"
)


@pytest.mark.web
@pytest.mark.selenium
def test_selenium_check_title_jsonplaceholder(selenium_driver):
    """Testa se o título da página JSONPlaceholder contém 'JSONPlaceholder' com Selenium."""
    assert web_automation.selenium_check_title(
        selenium_driver, JSONPLACEHOLDER_URL, "JSONPlaceholder"
    )


@pytest.mark.web
@pytest.mark.selenium
def test_selenium_verify_element_jsonplaceholder(selenium_driver):
    """Testa a presença de um elemento (link /guide/) na página JSONPlaceholder com Selenium."""
    assert web_automation.selenium_verify_element_presence(
        selenium_driver, JSONPLACEHOLDER_URL, By.CSS_SELECTOR, "a[href='/guide']"
    )


@pytest.mark.web
@pytest.mark.playwright
def test_playwright_check_title_and_screenshot_jsonplaceholder(playwright_page):
    """Testa título e captura screenshot da página JSONPlaceholder com Playwright."""
    assert web_automation.playwright_check_title_and_screenshot(
        playwright_page,
        JSONPLACEHOLDER_URL,
        "JSONPlaceholder",
        "jsonplaceholder_playwright.png",
    )


@pytest.mark.web
@pytest.mark.playwright
def test_playwright_verify_element_jsonplaceholder(playwright_page):
    """Testa a presença de um elemento (link /guide/) na página JSONPlaceholder com Playwright."""
    assert web_automation.playwright_verify_element_presence(
        playwright_page, JSONPLACEHOLDER_URL, "a[href='/guide'].mr-4"
    )


@pytest.mark.web
@pytest.mark.selenium
def test_selenium_fill_form_lambdatest(selenium_driver):
    """Testa o preenchimento de formulário e validação com Selenium no site LambdaTest."""
    assert web_automation.selenium_fill_form_and_validate(
        selenium_driver, FORM_TEST_URL_LAMBDATEST
    )


@pytest.mark.web
@pytest.mark.playwright
def test_playwright_navigation_interaction_performance_jsonplaceholder(playwright_page):
    """Testa navegação, interação e loga performance na página JSONPlaceholder com Playwright."""
    assert web_automation.playwright_navigate_interact_and_log_performance(
        playwright_page, JSONPLACEHOLDER_URL
    )
