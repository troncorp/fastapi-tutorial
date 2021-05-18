from fastapi import FastAPI

app = FastAPI(title = 'JobBoard',version = '0.1.0')

@app.get('/')
def hello():
    return {'hello':'world'}