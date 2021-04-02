import pytest
from fastapi.testclient import TestClient
import requests
from app import app


client = TestClient(app)


def test_doctor_app():
    url = "https://patient-managment-api.herokuapp.com/doctor"
    #url = "https://testserver/hospital"
    payload = {}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwiZW1haWwiOiJtZWV0LmJkYTE3MjlAaWN0LmdudS5hYy5pbiIsInVzZXJ0eXBlIjoiYWRtaW4iLCJwYXNzd29yZF9oYXNoIjoiJDJiJDEyJDNLZHpXZHF6RUN6TlU5RmRmWmVwM3VIcmhXajUuU3dpdjFNaHVRTWlMcVJaTFJHcUVaMnVDIn0.gKzJs32Z-a3SS-k5qZ-hVyhiyKoWXQKauyXHRojDzG8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    assert response.status_code == 200


def test_hospital():
    url = "https://patient-managment-api.herokuapp.com/schedule/4"
    #url = "https://testserver/hospital"
    payload = {}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwiZW1haWwiOiJtZWV0LmJkYTE3MjlAaWN0LmdudS5hYy5pbiIsInVzZXJ0eXBlIjoiYWRtaW4iLCJwYXNzd29yZF9oYXNoIjoiJDJiJDEyJDNLZHpXZHF6RUN6TlU5RmRmWmVwM3VIcmhXajUuU3dpdjFNaHVRTWlMcVJaTFJHcUVaMnVDIn0.gKzJs32Z-a3SS-k5qZ-hVyhiyKoWXQKauyXHRojDzG8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    assert response.status_code == 200

