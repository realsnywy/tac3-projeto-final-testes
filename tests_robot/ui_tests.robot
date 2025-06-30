***Settings***
Library    SeleniumLibrary
Library    CustomKeywords.py

Suite Setup       Abrir Navegador Para Testes JSONPlaceholder
Suite Teardown    Close All Browsers

***Variables***
${BROWSER}              Chrome
${JSONPLACEHOLDER_URL}  https://jsonplaceholder.typicode.com/

***Keywords***
Abrir Navegador Para Testes JSONPlaceholder
    Open Browser    ${JSONPLACEHOLDER_URL}    ${BROWSER}
    Maximize Browser Window

***Test Cases***
Verificar Título da Página JSONPlaceholder com Selenium
    [Documentation]    Abre a página JSONPlaceholder e verifica o título.
    [Tags]    ui    robot    selenium
    Go To    ${JSONPLACEHOLDER_URL}
    ${driver}=    Get WebDriver Instance
    Título da Página Deve Conter    ${driver}    JSONPlaceholder

Preencher Formulário Simples e Validar com Selenium
    [Documentation]    Abre a página de teste de formulário, preenche e valida.
    [Tags]    ui    robot    selenium    formulario
    ${message}=    Set Variable    Olá Robot Framework!
    ${driver}=    Get WebDriver Instance
    Preencher Formulário Simples e Validar Mensagem    ${driver}    ${message}
