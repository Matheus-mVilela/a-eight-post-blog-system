from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.database import session
from app.models import GPTPost
from app.services import ChatGPTClient, GPTChatResponseError
from settings import config

app = FastAPI()


# Definindo a estrutura esperada para o body com Pydantic
class BuildPost(BaseModel):
    topic: str


@app.post('/build-post')
def build_post(data: BuildPost):
    try:
        prompt = f"""
        Escreva um post de blog com no mínimo 800 palavra
        estruturando os títulos e subtítulos claramente,
        esse post não pode ter redundância de ideia e deve
        trazer as informações estruturadas e de fácil entendimento.
        O assunto do post é {data.topic}
        """
        client = ChatGPTClient(config.CHAT_GPT_API_KEY)
        response = client.chat(prompt)
        post = GPTPost(prompt=prompt, response=response)
        session.add(post)
        session.commit()

        return JSONResponse(
            content={'message': {'prompt': prompt, 'response': response}},
            status_code=200,
        )

    except GPTChatResponseError as exc:
        return HTTPException(status_code=422, detail={'message': str(exc)})


@app.get('/get-posts')
def get_posts():
    response = [
        {'id': post.id, 'prompt': post.prompt, 'response': post.response}
        for post in session.query(GPTPost).all()
    ]
    return JSONResponse(content={'message': response}, status_code=200)
