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

import requests

url = "https://patient-managment-api.herokuapp.com/patient"

payload={}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE'
}

response = requests.request("GET", url, headers=headers, data=payload)
json_data = response.json()
print(json_data[0]['p_id'])
# print(type(json_data))
# for item in json_data:
#     print(item['p_id'])