from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


app = FastAPI()

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:''@localhost:3306/hms'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

doctor_list = [
    {
    "doc_id": 0,
    "doc_name": "Meet",
    "type": "Dentist"
    },
    {
        "doc_id": 1,
        "doc_name": "Hiren",
        "doc_type": "Cardiac"
    }
]


class Doctor(BaseModel):
    doc_id: int
    doc_name: str
    doc_type: str


@app.get('/doctor')
def get_doc():
    return doctor_list


@app.get('/doctor/{doctor_id}')
def get_doctor_via_id(doc_id: int):
    return doctor_list[doc_id-1]


@app.post('/doctor')
def add_doctor(doctor: Doctor):
    doctor_list.append(doctor.dict())
    return doctor_list[-1]


@app.delete('/doctor/{doctor_id}')
def delete_doctor_via_id(doc_id: int):
    doctor_list.pop(doc_id-1)
    return {}


uvicorn.run(app, host='0.0.0.0')