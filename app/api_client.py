# Módulo com funções para requisições HTTP utilizando a biblioteca requests.
import requests
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts():
    """Busca todos os posts."""
    logger.info(f"Realizando GET em {BASE_URL}/posts")
    try:
        response = requests.get(f"{BASE_URL}/posts", timeout=10)
        response.raise_for_status()
        logger.info(
            f"GET /posts - Status: {response.status_code}, Resposta (primeiros 100 chars): {response.text[:100]}"
        )
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição GET /posts: {e}")
        raise


def get_post(post_id):
    """Busca um post específico pelo ID."""
    logger.info(f"Realizando GET em {BASE_URL}/posts/{post_id}")
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
        logger.info(f"GET /posts/{post_id} - Status: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição GET /posts/{post_id}: {e}")
        raise


def create_post(payload):
    """Cria um novo post."""
    logger.info(f"Realizando POST em {BASE_URL}/posts com payload: {payload}")
    try:
        response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
        response.raise_for_status()
        logger.info(
            f"POST /posts - Status: {response.status_code}, Resposta: {response.json()}"
        )
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição POST /posts: {e}")
        raise


def update_post(post_id, payload):
    """Atualiza um post existente."""
    logger.info(f"Realizando PUT em {BASE_URL}/posts/{post_id} com payload: {payload}")
    try:
        response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload, timeout=10)
        response.raise_for_status()
        logger.info(
            f"PUT /posts/{post_id} - Status: {response.status_code}, Resposta: {response.json()}"
        )
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição PUT /posts/{post_id}: {e}")
        raise


def delete_post(post_id):
    """Deleta um post."""
    logger.info(f"Realizando DELETE em {BASE_URL}/posts/{post_id}")
    try:
        response = requests.delete(f"{BASE_URL}/posts/{post_id}", timeout=10)
        response.raise_for_status()
        logger.info(f"DELETE /posts/{post_id} - Status: {response.status_code}")
        return response
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisição DELETE /posts/{post_id}: {e}")
        raise
