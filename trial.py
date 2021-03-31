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
# import mysql.connector
# import uvicorn
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi import FastAPI, Request
# import jwt
# import json
# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.hash import bcrypt
# from tortoise import fields
# from tortoise.contrib.fastapi import register_tortoise
# from tortoise.contrib.pydantic import pydantic_model_creator
# from tortoise.models import Model
# #
# # import requests
# #
# # url = "https://patient-managment-api.herokuapp.com/patient"
# #
# # payload={}
# # headers = {
# #   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE'
# # }
# #
# # response = requests.request("GET", url, headers=headers, data=payload)
# # json_data = response.json()
# # print(json_data[0]['p_id'])
# # # print(type(json_data))
# # # for item in json_data:
# # #     print(item['p_id'])
#
# # mydb = mysql.connector.connect(host="us-cdbr-east-03.cleardb.com", user="b4b07506295099", passwd="90df5ad7")
# # mycursor = mydb.cursor()
# #
# #
# #
# # import http.client
# # import mimetypes
# # from codecs import encode
# #
# # conn = http.client.HTTPSConnection("patient-managment-api.herokuapp.com")
# # dataList = []
# # boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
# # dataList.append(encode('--' + boundary))
# # dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('/E:\College\Sem8\Patient Management\Patient Management\invoice.pdf')))
# #
# # fileType = mimetypes.guess_type('E:\College\Sem8\Patient Management\Patient Management\invoice.pdf')[0] or 'application/octet-stream'
# # dataList.append(encode('Content-Type: {}'.format(fileType)))
# # dataList.append(encode(''))
# #
# # with open('E:\College\Sem8\Patient Management\Patient Management\invoice.pdf', 'rb') as f:
# #   dataList.append(f.read())
# # dataList.append(encode('--'+boundary+'--'))
# # dataList.append(encode(''))
# # body = b'\r\n'.join(dataList)
# # payload = body
# # headers = {
# #   'accept': 'application/json',
# #   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE',
# #   'Content-Type': 'multipart/form-data',
# #   'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
# # }
# # conn.request("POST", "/upload_report", payload, headers)
# # res = conn.getresponse()
# # data = res.read()
# # print(data.decode("utf-8"))
#
#
# # import requests
# # x = "14"
# # url = "https://patient-managment-api.herokuapp.com/get_report/"+ x
# #
# # payload={}
# # headers = {
# #   'accept': 'application/json',
# #   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE'
# # }
# #
# # response = requests.request("GET", url, headers=headers, data=payload)
# #
# # print(response.text)
#
# # import http.client
# # import mimetypes
# # from codecs import encode
# #
# # conn = http.client.HTTPSConnection("patient-managment-api.herokuapp.com")
# # dataList = []
# # boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
# # dataList.append(encode('--' + boundary))
# # dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('/E:/College/Sem8/Patient Management/Patient Management/ER-diagram.png')))
# #
# # fileType = mimetypes.guess_type('/E:/College/Sem8/Patient Management/Patient Management/ER-diagram.png')[0] or 'application/octet-stream'
# # dataList.append(encode('Content-Type: {}'.format(fileType)))
# # dataList.append(encode(''))
# #
# # with open('/E:/College/Sem8/Patient Management/Patient Management/ER-diagram.png', 'rb') as f:
# #   dataList.append(f.read())
# # dataList.append(encode('--'+boundary+'--'))
# # dataList.append(encode(''))
# # body = b'\r\n'.join(dataList)
# # payload = body
# # headers = {
# #   'accept': 'application/json',
# #   'Content-Type': 'multipart/form-data',
# #   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE',
# #   'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
# # }
# # conn.request("POST", "/upload_report", payload, headers)
# # res = conn.getresponse()
# # data = res.read()
# # print(data.decode("utf-8"))
# #
# # import requests
# #
# # url = "https://patient-managment-api.herokuapp.com/upload_report"
# #
# # payload={}
# # files=open('invoice.pdf', mode='r')
# # headers = {
# #   'accept': 'application/json',
# #   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE',
# #   'Content-Type': 'multipart/form-data'
# # }
# #
# # response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
# # print(response.text)
#
#


# import requests
# x ="3"
# url = "https://qr-code-scanning.herokuapp.com/retrieve_qrcode/" + x
#
# payload={}
# headers = {
#   'accept': 'application/json'
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

# import requests
#
# url = "https://patient-managment-api.herokuapp.com/upload_report"
#
# payload={}
# files=[
#   ('file',('invoice.pdf',open('./invoice.pdf','rb'),'application/pdf'))
# ]
# headers = {
#   'accept': 'application/json',
#   'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwibmFtZSI6Im1lZXQiLCJ1c2VybmFtZSI6Im1lZXQyNzEyIiwidXNlcnR5cGUiOiJhZG1pbiIsInBhc3N3b3JkX2hhc2giOiIkMmIkMTIkM0tkeldkcXpFQ3pOVTlGZGZaZXAzdUhyaFdqNS5Td2l2MU1odVFNaUxxUlpMUkdxRVoydUMifQ.OmmTbiqaHTcslkz2ch1RRy9IrVDYfeGWmP1cw8T0tjE',
#   'Content-Type': 'multipart/form-data'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
#
# print(response.text)

# import requests
#
# url = "https://patient-managment-api.herokuapp.com/users?name=trial&username=trial&password=trial&usertype=normal"
#
# payload={}
# headers = {
#   'accept': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)

# import http.client
#
# conn = http.client.HTTPSConnection("patient-managment-api.herokuapp.com")
# payload = ''
# headers = {
#   'accept': 'application/json'
# }
# w = "trial"
# x = "trial"
# y = "trial"
# z = "normal"
# string = "/users?name="+w+"&username="+x+"&password="+y+"&usertype="+z
# conn.request("POST", string, payload, headers)
# res = conn.getresponse()
# data = res.read()
# print(data.decode("utf-8"))
