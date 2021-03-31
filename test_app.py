import pytest
from fastapi.testclient import TestClient
import requests
from app import app


# app = FastAPI()

# @app.get('/')
# async def read_root():
#     return {"message" : "Hello World"}


client = TestClient(app)

from multiprocessing import Process

import pytest
import requests
import uvicorn
from fastapi import FastAPI





#
# def test_read_main(server):
#     response = requests.get("http://localhost:8000/")
#     assert response.status_code == 200
#     #assert response.json() == {"msg": "Hello World"}





# def test_read_main():
#
#     headers = {
#         'accept': 'application/json',
#         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwiZW1haWwiOiJtZWV0LmJkYTE3MjlAaWN0LmdudS5hYy5pbiIsInVzZXJ0eXBlIjoiYWRtaW4iLCJwYXNzd29yZF9oYXNoIjoiJDJiJDEyJDNLZHpXZHF6RUN6TlU5RmRmWmVwM3VIcmhXajUuU3dpdjFNaHVRTWlMcVJaTFJHcUVaMnVDIn0.gKzJs32Z-a3SS-k5qZ-hVyhiyKoWXQKauyXHRojDzG8'
#     }
#     response = client.get("/", headers=headers)
#     assert response.status_code == 200
#     #assert response.json() == {"msg": "Hello World"}



# def test_doctor_app():
#     url = "http://localhost:8000/hospital"
#     #url = "https://testserver/hospital"
#     payload = {}
#     headers = {
#         'accept': 'application/json',
#         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwiZW1haWwiOiJtZWV0LmJkYTE3MjlAaWN0LmdudS5hYy5pbiIsInVzZXJ0eXBlIjoiYWRtaW4iLCJwYXNzd29yZF9oYXNoIjoiJDJiJDEyJDNLZHpXZHF6RUN6TlU5RmRmWmVwM3VIcmhXajUuU3dpdjFNaHVRTWlMcVJaTFJHcUVaMnVDIn0.gKzJs32Z-a3SS-k5qZ-hVyhiyKoWXQKauyXHRojDzG8'
#     }
#
#     response = requests.request("GET", url, headers=headers, data=payload)
#
#     print(response.status_code)
#     assert response.status_code == 200
#     assert response.json() == [{"hospital_id": 4,"hospital_name": "Cims"},{ "hospital_id": 5,"hospital_name": "Zydus"},{"hospital_id": 6,"hospital_name": "Sterling" },{ "hospital_id": 7,"hospital_name": "KD"},{"hospital_id": 8, "hospital_name": "Kiran"},{"hospital_id": 9, "hospital_name": "Masum" },{ "hospital_id": 10, "hospital_name": "Solar"},{"hospital_id": 11,"hospital_name": "Apollo"},{"hospital_id": 12,"hospital_name": "Shalby"},{ "hospital_id": 13,"hospital_name": "Vaghasia Trust"}]
# def test_doctor_app1():
#     url = "http://localhost:8000/"
#     response = requests.request("GET", url)
#     assert response.status_code == 200




def test_doctor_app():
    url = "https://patient-managment-api.herokuapp.com/doctor"
    #url = "https://testserver/hospital"
    payload = {}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwiZW1haWwiOiJtZWV0LmJkYTE3MjlAaWN0LmdudS5hYy5pbiIsInVzZXJ0eXBlIjoiYWRtaW4iLCJwYXNzd29yZF9oYXNoIjoiJDJiJDEyJDNLZHpXZHF6RUN6TlU5RmRmWmVwM3VIcmhXajUuU3dpdjFNaHVRTWlMcVJaTFJHcUVaMnVDIn0.gKzJs32Z-a3SS-k5qZ-hVyhiyKoWXQKauyXHRojDzG8'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.status_code)
    assert response.status_code == 200
    assert response.json() == [
  {
    "doc_id": 4,
    "doc_name": "Meet Vaghasia",
    "doc_type": "Cardiologist",
    "doc_ph_no": 9409299016,
    "doc_email": "meet.bda1729@ict.gnu.ac.in",
    "hospital_id": 4
  },
  {
    "doc_id": 14,
    "doc_name": "Dixit Kasodariya",
    "doc_type": "Surgeon",
    "doc_ph_no": 7990688061,
    "doc_email": "dixit.bda1710@ict.gnu.ac.in",
    "hospital_id": 5
  },
  {
    "doc_id": 24,
    "doc_name": "Hiren Koradiya",
    "doc_type": "dentist",
    "doc_ph_no": 9409299015,
    "doc_email": "hiren.bda1711@ict.gnu.ac.in",
    "hospital_id": 6
  },
  {
    "doc_id": 34,
    "doc_name": "Keval Patel",
    "doc_type": "ortho",
    "doc_ph_no": 9409299014,
    "doc_email": "keval.bda1716@ict.gnu.ac.in",
    "hospital_id": 7
  },
  {
    "doc_id": 44,
    "doc_name": "Dhruv Patel",
    "doc_type": "Paediatrician",
    "doc_ph_no": 9765433525,
    "doc_email": "dhruv.patel@gmail.com",
    "hospital_id": 4
  },
  {
    "doc_id": 54,
    "doc_name": "Yash Patel",
    "doc_type": "Psychiatrists",
    "doc_ph_no": 9878786565,
    "doc_email": "yash.patel@gmail.com",
    "hospital_id": 5
  },
  {
    "doc_id": 64,
    "doc_name": "Rahul Patel",
    "doc_type": "Audiologist",
    "doc_ph_no": 7898763483,
    "doc_email": "rahul.patel@gmail.com",
    "hospital_id": 8
  },
  {
    "doc_id": 74,
    "doc_name": "Komal Solanki",
    "doc_type": "Neurologist",
    "doc_ph_no": 7676898765,
    "doc_email": "komal.solanki@gmail.com",
    "hospital_id": 9
  },
  {
    "doc_id": 84,
    "doc_name": "Babu Iyer",
    "doc_type": "ortho",
    "doc_ph_no": 8767654476,
    "doc_email": "babu.iyer@gmail.com",
    "hospital_id": 5
  },
  {
    "doc_id": 94,
    "doc_name": "Palak Shah",
    "doc_type": "Psychiatrists",
    "doc_ph_no": 9847628467,
    "doc_email": "palak.shah@gmail.com",
    "hospital_id": 6
  }
]


def test_doctor_app():
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
    assert response.json() == [
  {
    "schedule_id": 4,
    "doc_id": 4,
    "date": "2021-03-06",
    "time": "16:00:00",
    "status": 0
  },
  {
    "schedule_id": 44,
    "doc_id": 4,
    "date": "2021-03-06",
    "time": "13:00:00",
    "status": 0
  },
  {
    "schedule_id": 54,
    "doc_id": 4,
    "date": "2021-03-06",
    "time": "16:00:00",
    "status": 1
  }
]

