# Keywords Python personalizadas para Robot Framework
import requests
import logging
from robot.api.deco import keyword
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

BASE_API_URL = "https://jsonplaceholder.typicode.com"
FORM_TEST_URL_LAMBDATEST = (
    "https://www.lambdatest.com/selenium-playground/simple-form-demo"
)


@keyword("Verificar Status da Resposta da API")
def verificar_status_resposta_api(response, expected_status_code):
    """Verifica se o status code da resposta da API é o esperado."""
    logger.info(
        f"Verificando status. Esperado: {expected_status_code}, Recebido: {response.status_code}"
    )
    if int(response.status_code) != int(expected_status_code):
        raise AssertionError(
            f"Status da API incorreto. Esperado: {expected_status_code}, Recebido: {response.status_code}. Conteúdo: {response.text[:200]}"
        )
    logger.info("Status da API verificado com sucesso.")


@keyword("Resposta da API Deve Conter Lista Não Vazia")
def resposta_api_deve_conter_lista_nao_vazia(response):
    """Verifica se a resposta da API (JSON) é uma lista e não está vazia."""
    logger.info("Verificando se a resposta da API é uma lista não vazia.")
    try:
        data = response.json()
        if not isinstance(data, list):
            raise AssertionError(f"Resposta da API não é uma lista. Tipo: {type(data)}")
        if not data:
            raise AssertionError("Resposta da API é uma lista vazia.")
        logger.info(f"Resposta é uma lista com {len(data)} itens.")
    except ValueError:
        raise AssertionError(
            f"Resposta da API não é um JSON válido: {response.text[:200]}"
        )


@keyword("Título da Página Deve Conter")
def titulo_da_pagina_deve_conter(selenium_driver, expected_substring):
    """Verifica se o título da página atual contém a substring esperada."""
    logger.info(f"Verificando se o título da página contém '{expected_substring}'.")
    actual_title = selenium_driver.title
    if expected_substring not in actual_title:
        raise AssertionError(
            f"Título da página incorreto. Esperado conter '{expected_substring}', Recebido: '{actual_title}'"
        )
    logger.info(f"Título da página '{actual_title}' verificado com sucesso.")


@keyword("Preencher Formulário Simples e Validar Mensagem")
def preencher_formulario_simples_e_validar_mensagem(selenium_driver, mensagem):
    """Navega para a página de teste, preenche a mensagem e valida a saída."""
    logger.info(f"Acessando {FORM_TEST_URL_LAMBDATEST} para teste de formulário.")
    selenium_driver.get(FORM_TEST_URL_LAMBDATEST)

    input_field = WebDriverWait(selenium_driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-message"))
    )
    input_field.send_keys(mensagem)
    logger.info(f"Mensagem '{mensagem}' inserida no campo.")

    button = selenium_driver.find_element(By.ID, "showInput")
    button.click()
    logger.info("Botão 'Get Checked Value' clicado.")

    output_message_element = WebDriverWait(selenium_driver, 10).until(
        EC.presence_of_element_located((By.ID, "message"))
    )
    output_text = output_message_element.text
    logger.info(f"Mensagem de saída encontrada: '{output_text}'")

    if output_text != mensagem:
        raise AssertionError(
            f"Validação do formulário falhou. Esperado: '{mensagem}', Recebido: '{output_text}'"
        )
    logger.info("Formulário preenchido e validado com sucesso.")
