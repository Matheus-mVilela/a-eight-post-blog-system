from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def run_root():
    return 'Run root'
