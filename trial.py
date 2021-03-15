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

import requests
import json

url = "https://patient-managment-api.herokuapp.com/token"
x = 'meet2712'
y = 'meet.2712'
payload={'username': x,
'password': y}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
json_data = json.loads(response.text)
print(type(json_data))


