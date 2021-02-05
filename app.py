import mysql.connector
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi import FastAPI, Request


mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")

print(mydb)

if mydb:
    print("Connection Successful")

else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()
mycursor.execute("use heroku_cb8e53992ffbeaf")
mycursor.execute("select * from doctor")


for db in mycursor:
    print(db)
mydb.commit()

app = FastAPI(template_folder='Templates/')
templates = Jinja2Templates(directory="Templates/")
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.mount("/Templates", StaticFiles(directory="./Templates"), name="Templates")



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
    },
    {
        "doc_id": 2,
        "doc_name": "Dixit",
        "type": "Surgeon"
    },
    {
        "doc_id": 4,
        "doc_name": "Keval",
        "doc_type": "Physician"
    }
]
# Test Message

class Doctor(BaseModel):
    doc_id: int
    doc_name: str
    doc_type: str


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/test', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})

@app.get('/signup', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.get('/login', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get('/doctor')
def get_doc():
    # return doctor_list
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from doctor")
    doctor_list = []
    for x in mycursor:
        doctor_list.append(x)
    mydb.commit()
    return doctor_list


@app.get('/patient')
def get_doc():
    # return patient_list
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from patient")
    patient_list = []
    for x in mycursor:
        patient_list.append(x)
    mydb.commit()
    return patient_list


@app.get('/hospital')
def get_doc():
    # return hospital_list
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from hospital")
    hospital_list = []
    for x in mycursor:
        hospital_list.append(x)
    mydb.commit()
    return hospital_list


@app.get('/reports')
def get_doc():
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from reports")
    reports_list = []
    for x in mycursor:
        reports_list.append(x)
    mydb.commit()
    return reports_list


@app.get('/doctor/{doctor_id}')
def get_doctor_via_id(doc_id: int):
    return doctor_list[doc_id - 1]


@app.post('/doctor')
def add_doctor(doctor: Doctor):
    doctor_list.append(doctor.dict())
    return doctor_list[-1]


@app.delete('/doctor/{doctor_id}')
def delete_doctor_via_id(doc_id: int):
    doctor_list.pop(doc_id - 1)
    return {}

# uvicorn.run(app)
