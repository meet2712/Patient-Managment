from fastapi import FastAPI
import uvicorn

app = FastAPI()


db = []

@app.get('/doctor')
def index():
    return {'key' : 'value'}


@app.post('/doctor')






uvicorn.run(app)