***Settings***
Library    RequestsLibrary
Library    Collections
Library    CustomKeywords.py

Suite Setup    Create Session    jsonplaceholder    ${BASE_API_URL}    verify=True

***Variables***
${BASE_API_URL}    https://jsonplaceholder.typicode.com

***Test Cases***
Buscar Todos os Posts e Validar Resposta
    [Documentation]    Testa GET /posts, valida status 200 e conteúdo.
    [Tags]    api    robot
    ${response}=    GET On Session    jsonplaceholder    /posts
    Verificar Status da Resposta da API    ${response}    200
    Resposta da API Deve Conter Lista Não Vazia    ${response}

Criar Novo Post e Validar Resposta
    [Documentation]    Testa POST /posts, valida status 201 e dados criados.
    [Tags]    api    robot
    &{payload}=    Create Dictionary    title=Post Robot    body=Conteúdo via Robot    userId=101
    ${response}=    POST On Session    jsonplaceholder    /posts    json=${payload}
    Verificar Status da Resposta da API    ${response}    201
    ${json_response}=    Set Variable    ${response.json()}
    Should Be Equal As Strings    ${json_response}[title]    ${payload}[title]
    Should Be Equal As Strings    ${json_response}[body]    ${payload}[body]
    Should Be Equal As Integers    ${json_response}[userId]    ${payload}[userId]
    Dictionary Should Contain Key    ${json_response}    id

Buscar Post Inexistente e Validar 404
    [Documentation]    Testa GET /posts/{id} para um ID inexistente, valida status 404.
    [Tags]    api    robot    negativo
    ${response}=    GET On Session    jsonplaceholder    /posts/99999    expected_status=404
    Verificar Status da Resposta da API    ${response}    404
