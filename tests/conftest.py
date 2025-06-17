# Configuração de fixtures do pytest.
import pytest
import logging
from selenium import webdriver
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def base_api_url():
    """URL base para a API JSONPlaceholder."""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Configura o logging para os testes."""
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("test_run.log", mode="w"),
            logging.StreamHandler(),
        ],
    )
    logging.info("Logging configurado para a sessão de testes.")


@pytest.fixture(scope="function")
def selenium_driver():
    """Fixture para o WebDriver do Selenium (Chrome)."""
    logging.info("Inicializando WebDriver do Selenium (Chrome)")
    driver = webdriver.Chrome()
    yield driver
    logging.info("Fechando WebDriver do Selenium")
    driver.quit()


@pytest.fixture(scope="function")
def playwright_page():
    """Fixture para uma página Playwright (Chromium)."""
    logging.info("Inicializando Playwright e abrindo nova página (Chromium)")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        logging.info("Fechando navegador Playwright")
        browser.close()
