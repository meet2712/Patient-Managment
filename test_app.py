from fastapi.testclient import TestClient
import requests
from app import app
import http.client

# app = FastAPI()

# @app.get('/')
# async def read_root():
#     return {"message" : "Hello World"}


client = TestClient(app)

#
# def test_read_app():
#     response = client.get('/')
#     assert response.status_code == 200


def test_doctor_app():
    url = "https://patient-managment-api.herokuapp.com/hospital"
    # url = client.base_url + "/doctor"
    payload = {}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwiZW1haWwiOiJtZWV0LmJkYTE3MjlAaWN0LmdudS5hYy5pbiIsInVzZXJ0eXBlIjoiYWRtaW4iLCJwYXNzd29yZF9oYXNoIjoiJDJiJDEyJDNLZHpXZHF6RUN6TlU5RmRmWmVwM3VIcmhXajUuU3dpdjFNaHVRTWlMcVJaTFJHcUVaMnVDIn0.gKzJs32Z-a3SS-k5qZ-hVyhiyKoWXQKauyXHRojDzG8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    assert response.status_code == 200
    assert response.json() == [{"hospital_id": 4,"hospital_name": "Cims"},{ "hospital_id": 5,"hospital_name": "Zydus"},{"hospital_id": 6,"hospital_name": "Sterling" },{ "hospital_id": 7,"hospital_name": "KD"},{"hospital_id": 8, "hospital_name": "Kiran"},{"hospital_id": 9, "hospital_name": "Masum" },{ "hospital_id": 10, "hospital_name": "Solar"},{"hospital_id": 11,"hospital_name": "Apollo"},{"hospital_id": 12,"hospital_name": "Shalby"},{ "hospital_id": 13,"hospital_name": "Vaghasia Trust"}]

