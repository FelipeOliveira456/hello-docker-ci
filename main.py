from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/hello", response_class=PlainTextResponse)
def hello() -> str:
    return "Hello World 2"
