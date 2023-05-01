#!/usr/bin/env python3

import requests
headers = { 
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "GNU/linux", 
    }
response = requests.get("https://httpbin.org/get",headers=headers)

if response.status_code == 200:
    print("Всё хорошо!")
print(response.json())
print(response.json()['headers'])

if response.ok:
    print("Ok!")

response = requests.get('https://rambler.ru')
response.raise_for_status()
print(response.headers)
