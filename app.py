from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()
doctor_list = []

class Doctor(BaseModel):
    name: str
    type: str

@app.get('/doctor')
def get_doctor():
    return doctor_list

@app.get('/doctor/{doctor_id}')
def get_doctor_via_id(doctor_id: int):
    return doctor_list[doctor_id-1]

@app.post('/doctor')
def add_doctor(doctor: Doctor):
    doctor_list.append(doctor.dict())
    return doctor_list[-1]

@app.delete('/doctor/{doctor_id}')
def delete_doctor_via_id(doctor_id: int):
    doctor_list.pop(doctor_id-1)
    return {}

uvicorn.run(app)