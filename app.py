import mysql.connector
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

# app = FastAPI()
# #
# mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
#
# print(mydb)
#
# if mydb:
#     print("Connection Successful")
#
# else:
#     print("Connection Unsuccessful")
#
# mycursor = mydb.cursor()
# mycursor.execute("use heroku_cb8e53992ffbeaf")
# mycursor.execute("select * from doctor")
#
# for db in mycursor:
#     print(db)
# mydb.commit()
# mydb.close()

app = FastAPI(template_folder='Templates/')
templates = Jinja2Templates(directory="Templates/")
app.mount("/static", StaticFiles(directory="./static"), name="static")
app.mount("/Templates", StaticFiles(directory="./Templates"), name="Templates")

# doctor_list = [
#     {
#         "doc_id": 0,
#         "doc_name": "Meet",
#         "type": "Dentist"
#     },
#     {
#         "doc_id": 1,
#         "doc_name": "Hiren",
#         "doc_type": "Cardiac"
#     },
#     {
#         "doc_id": 2,
#         "doc_name": "Dixit",
#         "type": "Surgeon"
#     },
#     {
#         "doc_id": 4,
#         "doc_name": "Keval",
#         "doc_type": "Physician"
#     }
# ]


# class Doctor(BaseModel):
#     doc_id: int
#     doc_name: str
#     doc_type: str


#DATABASE_URL = os.environ.get('CLEARDB_DATABASE_URL')
# DATABASE_URL = 'mysql://b4b07506295099:90df5ad7@us-cdbr-east-03.cleardb.com/heroku_cb8e53992ffbeaf'
# database = databases.Database(DATABASE_URL,pool_pre_ping=True)
# metadata = sqlalchemy.MetaData()
#
# db = scoped_session(sessionmaker(bind=DATABASE_URL))
#
# db.commit()
#
#
#
# users = sqlalchemy.Table(
#     "user",
#     metadata,
#     sqlalchemy.Column("id",         sqlalchemy.String(100), primary_key=True),
#     sqlalchemy.Column("username",   sqlalchemy.String(100)),
#     sqlalchemy.Column("password",   sqlalchemy.String(100)),
#     sqlalchemy.Column("first_name",  sqlalchemy.String(100)),
#     sqlalchemy.Column("last_name",  sqlalchemy.String(100)),
#     sqlalchemy.Column("gender",     sqlalchemy.CHAR),
#     sqlalchemy.Column("create_at",  sqlalchemy.String(100)),
#     sqlalchemy.Column("status",  sqlalchemy.String(100)),
# )
#
#
#
# engine = sqlalchemy.create_engine(
#     DATABASE_URL
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# metadata.create_all(engine)
# Base = declarative_base()
#
#
# class UserList(BaseModel):
#     id          : str
#     username    : str
#     password    : str
#     first_name  : str
#     last_name   : str
#     gender      : str
#     create_at   : str
#     status      : str
#
#
# class UserEntry(BaseModel):
#     username : str = Field(..., example = "Meet")
#     password : str = Field(..., example = "Password")
#     first_name : str = Field(..., example = "First Name")
#     last_name : str = Field(..., example = "Last Name")
#     gender : str = Field(..., example = "M/F")
#
#
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()
#
#
# @app.get("/users", response_model=List[UserList])
# async def find_all_users():
#     query = users.select()
#     return await database.fetch_all(query)
#
#
# @app.post("/users", response_model=UserList)
# async def register_user(user: UserEntry):
#     gID = str(uuid.uuid1())
#     gDate = str(datetime.datetime.now())
#     query = users.insert().values(
#         id = gID,
#         username = user.username,
#         password = user.password,
#         first_name = user.first_name,
#         last_name = user.last_name,
#         gender = user.gender,
#         create_at = gDate,
#         status = "1"
#
#     )
#     await database.execute(query)
#     return{
#         "id" : gID,
#         **user.dict(),
#         "create_at": gDate,
#         "status": "1"
#     }




@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/test', response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse("test.html", {"request": request})


@app.get('/signup', response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get('/index2', response_class=HTMLResponse)
async def index2(request: Request):
    return templates.TemplateResponse("index2.html", {"request": request})




# @app.get('/doctor/{doctor_id}')
# def get_doctor_via_id(doc_id: int):
#     return doctor_list[doc_id - 1]
#
#
# @app.post('/doctor')
# def add_doctor(doctor: Doctor):
#     doctor_list.append(doctor.dict())
#     return doctor_list[-1]
#
#
# @app.delete('/doctor/{doctor_id}')
# def delete_doctor_via_id(doc_id: int):
#     doctor_list.pop(doc_id - 1)
#     return {}


# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi import Depends
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


# @app.post('/token')
# async def token(form_data: OAuth2PasswordRequestForm = Depends()):
#     return {'access_token': form_data.username + 'token'}

############################## This can be used ##########################
# @app.post('/token')
# async def token(username, password):
#     return {'access_token': username + password + 'token'}


#
# @app.get('/')
# async def index(token: str = Depends(oauth2_scheme)):
#     return {'the_token' : token}
import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from tortoise import fields
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model

# app = FastAPI()

JWT_SECRET = 'myjwtsecret'

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
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

    return {'access_token' : token, 'token_type' : 'bearer'}

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
    user_obj = User(username=user.username, password_hash=bcrypt.hash(user.password_hash))
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(user_obj)

@app.get('/users/me', response_model=User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user


@app.get('/patient')
async def get_doc(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor2 = mydb.cursor()
    mycursor2.execute("use heroku_cb8e53992ffbeaf")
    mycursor2.execute("select * from patient")
    patient_list = []
    for x in mycursor2:
        patient_list.append(x)
    mydb.commit()
    return patient_list


@app.get('/doctor')
def get_doc(user: User_Pydantic = Depends(get_current_user)):
    # return doctor_list
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor1 = mydb.cursor()
    mycursor1.execute("use heroku_cb8e53992ffbeaf")
    mycursor1.execute("select * from doctor")
    doctor_list = []
    for x in mycursor1:
        doctor_list.append(x)
    mydb.commit()
    return doctor_list


@app.get('/hospital')
def get_doc(user: User_Pydantic = Depends(get_current_user)):
    # return hospital_list
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor3 = mydb.cursor()
    mycursor3.execute("use heroku_cb8e53992ffbeaf")
    mycursor3.execute("select * from hospital")
    hospital_list = []
    for x in mycursor3:
        hospital_list.append(x)
    mydb.commit()
    return hospital_list


@app.get('/reports')
def get_doc(user: User_Pydantic = Depends(get_current_user)):
    mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
    mycursor4 = mydb.cursor()
    mycursor4.execute("use heroku_cb8e53992ffbeaf")
    mycursor4.execute("select * from reports")
    reports_list = []
    for x in mycursor4:
        reports_list.append(x)
    mydb.commit()
    return reports_list



register_tortoise(
    app,
    db_url='mysql://b4b07506295099:90df5ad7@us-cdbr-east-03.cleardb.com/heroku_cb8e53992ffbeaf',
    modules={'models': ['app']},
    generate_schemas=True,
    add_exception_handlers=True
)

#uvicorn.run(app)
