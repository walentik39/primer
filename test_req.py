#!/usr/bin/env python3

import collections
import requests
response = requests.get("https://distrowatch.com")

if response.status_code == 200:
    print("Всё хорошо!")
print(response.headers)
count = collections.Counter(response.headers)
print(count)
if response.ok:
    print("Ok!")

response = requests.get('https://rambler.ru')
response.raise_for_status()
print(response.headers)
