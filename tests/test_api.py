# Testes de API com pytest e unittest para os endpoints da JSONPlaceholder.
import pytest
import unittest
import time
from app import api_client


@pytest.mark.api
def test_get_posts_status_code_and_content_pytest():
    """Testa GET /posts: status 200 e se a resposta é uma lista."""
    response = api_client.get_posts()
    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)
    assert len(response_data) > 0
    assert "userId" in response_data[0]


@pytest.mark.api
def test_create_post_pytest():
    """Testa POST /posts: status 201 e se o título enviado está na resposta."""
    payload = {
        "title": "Meu Novo Post Pytest",
        "body": "Conteúdo do post.",
        "userId": 1,
    }
    response = api_client.create_post(payload)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == payload["title"]
    assert response_data["body"] == payload["body"]
    assert response_data["userId"] == payload["userId"]
    assert "id" in response_data


@pytest.mark.api
def test_delete_post_pytest():
    """Testa DELETE /posts/1: status 200."""
    post_id_to_delete = 1
    response = api_client.delete_post(post_id_to_delete)
    assert response.status_code == 200


@pytest.mark.api
def test_get_posts_response_time_pytest():
    """Testa o tempo de resposta do GET /posts: inferior a 2 segundos."""
    start_time = time.time()
    api_client.get_posts()
    end_time = time.time()
    assert (end_time - start_time) < 2.0, "A requisição demorou mais de 2 segundos."


@pytest.mark.api
@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_post_by_id_parametrized_pytest(post_id):
    """Testa GET /posts/{id} com múltiplos IDs: status 200 e ID correto."""
    response = api_client.get_post(post_id)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["id"] == post_id


@pytest.mark.api
def test_get_non_existent_post_pytest():
    """Testa GET /posts/{id} para um ID inexistente: status 404."""
    non_existent_id = 99999
    response = api_client.get_post(non_existent_id)
    assert response.status_code == 404


@pytest.mark.api
def test_create_post_invalid_payload_pytest():
    """Testa POST /posts com payload parcialmente inválido ou inesperado."""
    payload = {
        "title": "Post com UserID String",
        "body": "Teste de tipo de dado.",
        "userId": "abc",
    }
    response = api_client.create_post(payload)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["title"] == payload["title"]
    assert str(response_data["userId"]) == str(payload["userId"])


@pytest.mark.api
class TestAPIUnittest(unittest.TestCase):
    def test_update_post_unittest(self):
        """Testa PUT /posts/1: status 200 e se os dados foram atualizados."""
        post_id_to_update = 1
        original_post_response = api_client.get_post(post_id_to_update)
        self.assertEqual(
            original_post_response.status_code, 200, "Falha ao obter post original."
        )

        payload = {
            "id": post_id_to_update,
            "title": "Título Atualizado Unittest",
            "body": "Corpo atualizado via unittest.",
            "userId": original_post_response.json().get("userId", 1),
        }
        response = api_client.update_post(post_id_to_update, payload)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["title"], payload["title"])
        self.assertEqual(response_data["body"], payload["body"])
        self.assertEqual(response_data["userId"], payload["userId"])
        self.assertEqual(response_data["id"], post_id_to_update)


if __name__ == "__main__":
    unittest.main()
