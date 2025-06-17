# Projeto Final de Testes: Integração com APIs e Testes Automatizados

Este projeto demonstra testes automatizados para a API JSONPlaceholder e cenários web, utilizando Pytest, Unittest, Selenium, Playwright e Robot Framework.

## 📦 Estrutura do Projeto

```
tac3-projeto-final-testes/
├── app/                  # Módulos de cliente API e automação web
│   ├── api_client.py
│   └── web_automation.py
├── tests/                # Testes com Pytest/Unittest
│   ├── test_api.py
│   ├── test_web.py
│   └── conftest.py
├── tests_robot/          # Testes com Robot Framework
│   ├── api_tests.robot
│   ├── ui_tests.robot
│   └── CustomKeywords.py
├── requirements.txt
├── pytest.ini
├── test_run.log          # Log dos testes Pytest
└── README.md             # Este arquivo
```

## 🛠️ Ferramentas Utilizadas

- **Linguagem:** Python
- **Testes de API:** Requests, Pytest, Unittest
- **Testes Web:** Selenium, Playwright
- **Testes de Aceitação:** Robot Framework (RequestsLibrary, SeleniumLibrary)
- **Documentação/Design de API (opcional):** Apidog

## ⚙️ Configuração do Ambiente

1. **Crie e ative um ambiente virtual Python:**

    ```bash
    python -m venv venv
    # Windows: venv\Scripts\activate
    # macOS/Linux: source venv/bin/activate
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Instale o Playwright (usado com Pytest):**

    ```bash
    playwright install
    ```

4. **Configure o Selenium:**
    - Certifique-se de que o `chromedriver` (ou driver do seu navegador) está no `PATH` do sistema.

## 🚀 Execução dos Testes

### Testes com Pytest (`tests/`)

- **Executar todos os testes:**

    ```bash
    pytest
    ```

- **Execução detalhada e logs no console:**

    ```bash
    pytest -v -s
    ```

- **Executar por marcador (ex: `api`, `web`):**

    ```bash
    pytest -m api
    ```

- **Log da execução:** salvo em `test_run.log`.

### Testes com Robot Framework (`tests_robot/`)

- **Executar todos os testes:**

    ```bash
    robot tests_robot/
    ```

- **Executar um arquivo específico:**

    ```bash
    robot tests_robot/api_tests.robot
    ```

- **Executar por tag (ex: `api`, `formulario`):**

    ```bash
    robot -i api tests_robot/
    ```

- **Relatórios:** `log.html` e `report.html` são gerados no diretório raiz.

## 📁 Descrição dos Diretórios

- **`app/`**: Módulos de integração HTTP (`api_client.py`) e automação web (`web_automation.py`).
- **`tests/`**: Suítes de teste com Pytest/Unittest. `conftest.py` gerencia fixtures e logging.
- **`tests_robot/`**: Testes Robot Framework (`.robot`) e keywords Python reutilizáveis (`CustomKeywords.py`).

## 💡 Ferramentas Opcionais

- **Apidog:** Para design, documentação e execução de testes de API via interface gráfica.
- **Robot Framework:** Implementado em `tests_robot/` para testes de aceitação automatizados de API e UI.

## 📚 Referências

- [Pytest Documentation](https://docs.pytest.org/)
- [Robot Framework](https://robotframework.org/)
- [Playwright Python](https://playwright.dev/python/)
- [Selenium Python](https://selenium-python.readthedocs.io/)

---

> *Projeto desenvolvido para a disciplina TAC-3 - Tópicos Avançados em Computação III - Testes.*
>
> *Última revisão: 17/06/2025*
