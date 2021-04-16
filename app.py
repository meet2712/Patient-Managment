import mysql.connector
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import jwt
import os
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model
from fastapi import *
from fastapi.responses import FileResponse

import metadata



app = FastAPI(
    openapi_tags=metadata.tags_metadata,
    title = "Patient Management API",
    description = "Patient Management API system will provide access to external entities to securely request access to data in the HMS. Building a cloud-based corpus of mock data for a HMS that includes patient records, test results, images etc. Develop a set of APIs to provide access to the data for authenticated users.",
    template_folder='Templates/')
templates = Jinja2Templates(directory="Templates/")
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.mount("/Templates", StaticFiles(directory="./Templates"), name="Templates")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get('/')
# async def read_root():
#     return {"message" : "Hello World"}



JWT_SECRET = 'myjwtsecret'

class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50)
    username = fields.CharField(50, unique=True)
    email = fields.CharField(50, unique = True)
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

@app.post('/token', tags=["Token Generation"])
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
    return {'access_token': token, 'token_type' : 'bearer'}

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


@app.post('/users', tags=["Create Users"], response_model=User_Pydantic)
async def create_user(name,username,email,password):
    user_obj = User(name = name, username=username,email=email, password_hash=bcrypt.hash(password), usertype="normal")
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

@app.get('/patient', tags=['Patient'])
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


@app.get('/doctor', tags=['Doctor'])
def get_doc(user: User_Pydantic = Depends(get_current_user)):
    # if user.usertype == 'doctor':
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
    # else :
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail='Not an ADMIN USER'
    #     )


@app.get('/hospital',tags=['Hospital'])
def get_hospital(user: User_Pydantic = Depends(get_current_user)):
    # if user.usertype == 'doctor':

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



@app.get('/create_doctor',tags=['Create Doctor'])
def create_doctor(doc_name , doc_type , doc_ph_no, doc_email, hospital_id,user: User_Pydantic = Depends(get_current_user)):
    if user.usertype == 'admin':

        mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
        mycursor = mydb.cursor()
        mycursor.execute("use heroku_cb8e53992ffbeaf")

        query = '''INSERT INTO heroku_cb8e53992ffbeaf.doctor(doc_name, doc_type, doc_ph_no, doc_email, hospital_id) VALUES(%s, %s,%s,%s,%s)'''
        tuple = (doc_name , doc_type , doc_ph_no, doc_email, hospital_id)
        mycursor.execute(query , tuple)
        mydb.commit()
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Not an ADMIN USER'
        )


@app.get('/create_patient',tags=['Create Patient'])
def create_patient(p_ph_no , p_name ,user: User_Pydantic = Depends(get_current_user)):
    user_id_fk = user.id
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    query = '''INSERT INTO heroku_cb8e53992ffbeaf.patient(p_ph_no , p_name, user_id_fk ) VALUES(%s, %s, %s)'''
    tuple = (p_ph_no , p_name, user_id_fk)
    mycursor.execute(query , tuple)
    mydb.commit()

# @app.get('/reports',tags=[''])
# def get_report(user: User_Pydantic = Depends(get_current_user)):
#     mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
#     mycursor = mydb.cursor()
#     mycursor.execute("use heroku_cb8e53992ffbeaf")
#     mycursor.execute("select * from reports")
#     reports_list = mycursor.fetchall()
#     row_headers = [x[0] for x in mycursor.description]
#     mydb.commit()
#     json_data = []
#     for result in reports_list:
#         json_data.append(dict(zip(row_headers, result)))
#     return json_data


@app.get('/schedule/{doctor_id}',tags=['Schedule of Specific Doctor'])
def get_schedule_doc(doctor_id, user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    tuple1 = (doctor_id,)
    query = """ select schedule_id, doc_id, cast(avail_date as CHAR) as date, cast(avail_time as CHAR) as time, status from schedule where doc_id = %s """
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query, tuple1)
    schedule_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in schedule_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/schedule/{doctor_id}/{date}', tags=['Schedule of Specific Doctor of Specific Date'])
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



@app.get('/booked_appointment',tags=['List of Booked Appointment'])
def get_schedule_doc_date(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()

    query = """ select appointment_id, schedule_id, cast(app_date as CHAR) as date, cast(app_time as CHAR) as time, status from appointment"""
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query)
    schedule_list = mycursor.fetchall()
    row_headers = [x[0] for x in mycursor.description]
    mydb.commit()
    json_data = []
    for result in schedule_list:
        json_data.append(dict(zip(row_headers, result)))
    return json_data


@app.get('/appointment',tags=['Module to Book Appointment'])
def get_schedule_doc_date(doc_name,date1,time1,p_name, User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    tuple3 = (p_name,)
    mycursor1 = mydb.cursor()
    query_for_pid = """ select p_id from patient where p_name = %s """
    mycursor1.execute("use heroku_cb8e53992ffbeaf")
    mycursor1.execute(query_for_pid, tuple3)
    pid = mycursor1.fetchone()
    p_id = pid[0]
    mydb.commit()


    tuple4 = (doc_name,)
    mycursor2 = mydb.cursor()
    query_for_pid = """ select doc_id from doctor where doc_name = %s """
    mycursor2.execute("use heroku_cb8e53992ffbeaf")
    mycursor2.execute(query_for_pid, tuple4)
    docid = mycursor2.fetchone()
    doc_id = docid[0]
    mydb.commit()


    tuple5 = (doc_id, date1, time1)
    mycursor3 = mydb.cursor()
    query_for_pid = """ select schedule_id from schedule where doc_id = %s and avail_date = %s and avail_time = %s"""
    mycursor3.execute("use heroku_cb8e53992ffbeaf")
    mycursor3.execute(query_for_pid, tuple5)
    scheduleid = mycursor3.fetchall()
    schedule_id = scheduleid[0]
    mydb.commit()


    status = 0
    tuple6 = (date1, time1, doc_id, p_id, schedule_id[0], status)
    tuple7 = (schedule_id[0],)
    mycursor = mydb.cursor()
    query_for_pid = """ insert into appointment (app_date, app_time, doc_id, p_id, schedule_id, status) values ( %s, %s, %s, %s, %s, %s) """
    query_for_status = """ update schedule set status = 0 where schedule_id = %s """
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    mycursor.execute(query_for_pid, tuple6)
    mycursor.execute(query_for_status, tuple7)
    mydb.commit()

import tempfile

@app.post('/upload_report',tags  = ['Upload Report'])
def create_report(p_id,file: UploadFile = File(...), User_Pydantic = Depends(get_current_user)):

    data = file.file.read()
    tuple = (p_id, data)
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    sql = '''Insert into files (p_id, file_data) values ( %s, %s)'''
    mycursor.execute(sql, tuple)
    mydb.commit()


@app.get('/get_report/{id}', tags = ['Get Report From report_id'])
def create_report(id, User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor = mydb.cursor()
    mycursor.execute("use heroku_cb8e53992ffbeaf")
    sql = '''select file_data from files where id = %s'''
    mycursor.execute(sql,(id, ))
    l = mycursor.fetchone()

    temp = tempfile.NamedTemporaryFile(suffix='.pdf', prefix='meet', delete=False)
    while l:
        temp.write(l[0])

        l = mycursor.fetchone()

    x = tempfile.gettempdir()
    print(x)
    y = temp.name
    print(y)
    mydb.commit()
    return FileResponse(y)



@app.get('/cleartemp')
def clear_temp(User_Pydantic = Depends(get_current_user)):
    dir_path = tempfile.gettempdir()
    print(dir_path)

    try:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.startswith('meet'):
                    path = os.path.join(dir_path, file)
                    print(path)
                    os.remove(path)
    except PermissionError:
        print("File Used by Other Process")

register_tortoise(
    app,
    db_url='mysql://b4b07506295099:90df5ad7@us-cdbr-east-03.cleardb.com/heroku_cb8e53992ffbeaf',
    modules={'models': ['app']},
    generate_schemas=True,
    add_exception_handlers=True
)

