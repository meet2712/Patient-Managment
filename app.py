import uvicorn
from fastapi.responses import HTMLResponse
import mysql.connector
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")

templates = Jinja2Templates(directory="Templates/")

print(mydb)

if mydb:
    print("Connection Successfull")

else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()
mycursor.execute("use heroku_cb8e53992ffbeaf")
mycursor.execute("select * from doctor")

for db in mycursor:
    print(db)

# DATABASE_URL = 'mysql://b4b07506295099:90df5ad7@us-cdbr-east-03.cleardb.com/heroku_cb8e53992ffbeaf?reconnect=true'
# database = databases.Database(DATABASE_URL)


app = FastAPI(template_folder='Templates/')

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


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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


#uvicorn.run(app)
