from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.api.app import app
from app.services import GPTChatResponseError
from app.models import GPTPost


@pytest.fixture
def client():
    return TestClient(app)


def test_build_post_success(client):
    prompt = 'Test Prompt'
    expected_result = {
        'message': {
            'prompt': f"""
        Escreva um post de blog com no mínimo 800 palavra
        estruturando os títulos e subtítulos claramente,
        esse post não pode ter redundância de ideia e deve
        trazer as informações estruturadas e de fácil entendimento.
        O assunto do post é {prompt}
        """,
            'response': 'Generated content from ChatGPT',
        }
    }

    with patch(
        'app.services.ChatGPTClient.chat',
        return_value='Generated content from ChatGPT',
    ):
        response = client.post('/build-post', json={'topic': prompt})
    assert response.status_code == 200
    assert response.json() == expected_result


def test_build_post_error(client):
    prompt = 'Test Prompt'
    error_message = 'ChatGPT response error'

    with patch(
        'app.services.ChatGPTClient.chat',
        side_effect=GPTChatResponseError(error_message),
    ):
        response = client.post('/build-post', json={'topic': prompt})
    expected_result = {'status_code': 422, 'detail': {'message': error_message}, 'headers': None}
    assert response.json() == expected_result


def test_get_posts(client):
    mock_posts = [
        GPTPost(**{'id': 1, 'prompt': 'Test Prompt 1', 'response': 'Test Response 1'}),
        GPTPost(**{'id': 2, 'prompt': 'Test Prompt 2', 'response': 'Test Response 2'}),
    ]
    with patch('app.database.session.query') as mock_query:
        mock_query.return_value.all.return_value = mock_posts

        response = client.get('/get-posts')

    assert response.status_code == 200

    expected_result = [{
            'id': 1,
            'prompt': 'Test Prompt 1',
            'response': 'Test Response 1',
        },
        {
            'id': 2,
            'prompt': 'Test Prompt 2',
            'response': 'Test Response 2',
        }
    ]
    assert response.json() == {'message': expected_result}
