from fastapi.testclient import TestClient

from app import app

# app = FastAPI()

# @app.get('/')
# async def read_root():
#     return {"message" : "Hello World"}


client = TestClient(app)

def test_read_app():
    response = client.get('/')
    assert response.status_code == 200

