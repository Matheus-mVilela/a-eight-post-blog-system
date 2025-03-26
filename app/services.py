import requests


class GPTChatResponseError(Exception):
    pass


class ChatGPTClient:
    def __init__(self, api_key: str, model: str = 'gpt-3.5-turbo'):
        self.api_key = api_key
        self.model = model
        self.api_url = 'https://api.openai.com/v1/chat/completions'

    def chat(self, prompt: str) -> str:
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json',
            }
            body = {
                'model': self.model,
                'messages': [{'role': 'user', 'content': prompt}],
            }
            response = requests.post(self.api_url, headers=headers, json=body)
            response_data = response.json()

            if 'error' in response_data:
                raise GPTChatResponseError(
                    f"API Error: {response_data['error']['message']}"
                )

            return response_data['choices'][0]['message']['content']
        except Exception as e:
            raise GPTChatResponseError(f'Exception: {str(e)}')
