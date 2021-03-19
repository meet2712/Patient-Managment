# import http.client
#
# conn = http.client.HTTPSConnection("patient-managment-api.herokuapp.com")
# y = 'Bearer '
# x =  y + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzEsInVzZXJuYW1lIjoiZGl4aXQ1NDIwMCIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkQ2hkUUdXQXZHZERsandraVQwVzdEZW5mUFYvUFJqM250L29BMEdhTDhvNS5KamtRM3lJU08ifQ.XGMl7uZddG34rqjsZRGRTabKOXd8wYGS8rEuWOSmK4s'
# payload = ''
# headers = {
#   #'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzEsInVzZXJuYW1lIjoiZGl4aXQ1NDIwMCIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkQ2hkUUdXQXZHZERsandraVQwVzdEZW5mUFYvUFJqM250L29BMEdhTDhvNS5KamtRM3lJU08ifQ.XGMl7uZddG34rqjsZRGRTabKOXd8wYGS8rEuWOSmK4s'
#     'Authorization' : x
# }
# conn.request("GET", "/doctor", payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))

# import requests
# import json
#
# url = "https://patient-managment-api.herokuapp.com/token"
# x = 'meet2712'
# y = 'meet.2712'
# payload={'username': x,
# 'password': y}
# files=[
#
# ]
# headers = {}
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
# json_data = json.loads(response.text)
# print(type(json_data))
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
#
# import requests
#
# url = "https://patient-managment-api.herokuapp.com/patient"
#
# payload={}
# headers = {
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
# json_data = response.json()
# print(json_data[0]['p_id'])
# # print(type(json_data))
# # for item in json_data:
# #     print(item['p_id'])

mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
mycursor = mydb.cursor()


doc_type = "Cardiologist"
doc_name = "Meet Vaghasia"
date1 = "2021-03-06"
time1 = "16:00:00"
p_name = "Meet"
doc_id = 4
p_id = 4
schedule_id = 4

status = 0
tuple6 = (date1, time1, doc_id, p_id, schedule_id, status)
mycursor = mydb.cursor()
query_for_pid = """ insert into appointment (app_date, app_time, doc_id, p_id, schedule_id, status) VALUES ( %s, %s, %s, %s, %s, %s) """
mycursor.execute("use heroku_cb8e53992ffbeaf")
mycursor.execute(query_for_pid, tuple6)
mydb.commit()