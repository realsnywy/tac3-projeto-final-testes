# Módulo com scripts de automação web utilizando Selenium e Playwright.
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playwright.sync_api import Page, expect

logger = logging.getLogger(__name__)

JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/"
FORM_TEST_URL = "https://www.lambdatest.com/selenium-playground/simple-form-demo"


def selenium_check_title(driver, url, expected_title_substring):
    """Verifica se o título da página contém uma substring esperada com Selenium."""
    logger.info(
        f"Selenium: Acessando {url} para verificar se o título contém '{expected_title_substring}'"
    )
    driver.get(url)
    actual_title = driver.title
    logger.info(f"Selenium: Título encontrado '{actual_title}'")
    return expected_title_substring in actual_title


def playwright_check_title_and_screenshot(
    page: Page, url, expected_title_substring, screenshot_path="screenshot.png"
):
    """Verifica se o título da página contém substring e tira screenshot com Playwright."""
    logger.info(
        f"Playwright: Acessando {url} para verificar se o título contém '{expected_title_substring}' e tirar screenshot em {screenshot_path}"
    )
    page.goto(url)
    actual_title = page.title()
    page.screenshot(path=screenshot_path)
    logger.info(
        f"Playwright: Título encontrado '{actual_title}', screenshot salvo em {screenshot_path}."
    )
    expect(page).to_have_title(actual_title)
    return expected_title_substring in actual_title


def selenium_verify_element_presence(driver, url, by_method, value):
    """Verifica a presença de um elemento na página com Selenium."""
    logger.info(
        f"Selenium: Acessando {url} para verificar presença do elemento {by_method}='{value}'"
    )
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((by_method, value))
        )
        present = True
        logger.info(f"Selenium: Elemento {by_method}='{value}' encontrado.")
    except Exception as e:
        present = False
        logger.warning(
            f"Selenium: Elemento {by_method}='{value}' NÃO encontrado. Erro: {e}"
        )
    return present


def playwright_verify_element_presence(page: Page, url, selector):
    """Verifica a presença de um elemento na página com Playwright."""
    logger.info(
        f"Playwright: Acessando {url} para verificar presença do elemento com seletor '{selector}'"
    )
    page.goto(url)
    element = page.query_selector(selector)
    present = element is not None
    if present:
        expect(page.locator(selector)).to_be_visible()
        logger.info(
            f"Playwright: Elemento com seletor '{selector}' encontrado e visível."
        )
    else:
        logger.warning(f"Playwright: Elemento com seletor '{selector}' NÃO encontrado.")
    return present


def selenium_fill_form_and_validate(driver, url=FORM_TEST_URL):
    """Preenche um formulário simples e valida a mensagem de resposta com Selenium."""
    logger.info(f"Selenium: Acessando {url} para preencher formulário.")
    driver.get(url)

    message = "Olá Mundo Selenium!"
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-message"))
    )
    input_field.send_keys(message)
    logger.info(f"Selenium: Mensagem '{message}' inserida no campo.")

    button = driver.find_element(By.ID, "showInput")
    button.click()
    logger.info("Selenium: Botão 'Get Checked Value' clicado.")

    output_message_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    output_text = output_message_element.text
    logger.info(f"Selenium: Mensagem de saída encontrada: '{output_text}'")

    return output_text == message


def playwright_navigate_interact_and_log_performance(
    page: Page, url=JSONPLACEHOLDER_URL
):
    """Navega, interage e loga métricas de performance com Playwright."""
    logger.info(
        f"Playwright: Acessando {url} para navegação, interação e coleta de performance."
    )
    page.goto(url, wait_until="networkidle")

    guide_link_selector = "a[href='/guide/']"
    if page.query_selector(guide_link_selector):
        logger.info(f"Playwright: Link '{guide_link_selector}' encontrado. Clicando...")
        page.click(guide_link_selector)
        page.wait_for_load_state("domcontentloaded")
        logger.info(f"Playwright: Nova URL após clique: {page.url}")
        expect(page).to_have_url(f"{JSONPLACEHOLDER_URL}guide/")
    else:
        logger.warning(
            f"Playwright: Link '{guide_link_selector}' não encontrado na página inicial."
        )

    performance_metrics = page.evaluate(
        "() => JSON.stringify(window.performance.timing)"
    )
    logger.info(
        f"Playwright: Métricas de performance (window.performance.timing): {performance_metrics}"
    )

    metrics = page.metrics()
    logger.info(f"Playwright: Métricas da página (page.metrics()): {metrics}")

    return True
