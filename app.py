import mysql.connector
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
import jwt
import json
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model


app = FastAPI(template_folder='Templates/')
templates = Jinja2Templates(directory="Templates/")
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.mount("/Templates", StaticFiles(directory="./Templates"), name="Templates")




@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/test', response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse("appointment.html", {"request": request})


@app.get('/signup', response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})



JWT_SECRET = 'myjwtsecret'

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50)
    username = fields.CharField(50, unique=True)
    usertype = fields.CharField(50)
    password_hash = fields.CharField(128)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user

@app.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    user_obj = await User_Pydantic.from_tortoise_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)
    row_headers = ['access_token', 'token_type']
    result = [token, 'bearer']
    json_data = []
    json_data.append(dict(zip(row_headers, result)))
    return json_data

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )

    return await User_Pydantic.from_tortoise_orm(user)


@app.post('/users', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = User(name = user.name, username=user.username, password_hash=bcrypt.hash(user.password_hash))
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(user_obj)

@app.get('/users/me', response_model=User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user





# @app.get('/trial',)
# async def trial(user: User_Pydantic = Depends(get_current_user)):
#
#     if user.usertype == 'admin':
#
#
#     else :
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='Not an ADMIN USER'
#         )
#

@app.get('/patient')
async def get_patient(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from patient")
    patient_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in patient_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/doctor')
def get_doc(user: User_Pydantic = Depends(get_current_user)):
    if user.usertype == 'doctor':
        # return doctor_list
        mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
        mycursor = mydb.cursor()
        mycursor.execute("use heroku_cb8e53992ffbeaf")
        mycursor.execute("select * from doctor")
        doctor_list = mycursor.fetchall()
        row_headers = [x[0] for x in mycursor.description]
        mydb.commit()
        json_data = []
        for result in doctor_list:
            json_data.append(dict(zip(row_headers, result)))
        return json_data
    else :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not an ADMIN USER'
        )

##############################
@app.get('/hospital')
def get_hospital(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from hospital")
    hospital_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in hospital_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/reports')
def get_report(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute("select * from reports")
    reports_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in reports_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/schedule/{doctor_id}')
def get_schedule_doc(doctor_id, user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    tuple1 = (doctor_id,)
    query = """ select schedule_id, doc_id, cast(date as CHAR) as date, cast(time as CHAR) as time, status from schedule where doc_id = %s """
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query, tuple1)
    schedule_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in schedule_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/schedule/{doctor_id}/{date}')
def get_schedule_doc_date(doctor_id, date, user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    tuple1 = (doctor_id, date)
    query = """ select schedule_id, doc_id, cast(avail_date as CHAR) as date, cast(avail_time as CHAR) as time, status from schedule where doc_id = %s and avail_date = %s """
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query, tuple1)
    schedule_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in schedule_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data



@app.get('/appointment')
def get_schedule_doc_date(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    #tuple1 = (doctor_id, date)
    query = """ select appointment_id, schedule_id, cast(date as CHAR) as date, cast(time as CHAR) as time, status from appointment"""
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query)
    schedule_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in schedule_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/appointment_trial')
def get_schedule_doc_date(doc_type,name,date,user: User_Pydantic = Depends(get_current_user)):
    #appointment logic
    doc_type_value = 'Cardiologist'
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")

    #for selecting doctor type
    mycursor = mydb.cursor()
    tuple1 = (doc_type,)
    query_for_doc = """ select doc_name from doctor where doc_type = %s """
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query_for_doc,tuple1)
    doc_list = mycursor.fetchone()
    print(doc_list)

    tuple2 = (name, date)
    mycursor = mydb.cursor()
    query_for_time = """ select  cast(avail_time as CHAR) as avail_time from schedule where doc_id = (select doc_id from doctor where doc_name = %s ) AND avail_date = %s AND status = 1 """
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query_for_time,tuple2)
    time_list = mycursor.fetchall()
    mydb.commit()
    print(time_list)
    return doc_list, time_list


register_tortoise(
    app,
    db_url='mysql://b4b07506295099:90df5ad7@us-cdbr-east-03.cleardb.com/heroku_cb8e53992ffbeaf',
    modules={'models': ['app']},
    generate_schemas=True,
    add_exception_handlers=True
)

