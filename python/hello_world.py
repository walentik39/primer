#!/usr/bin/env python3

import urllib.request
file = urllib.request.urlopen('https://spliff-guru.ru/message.txt')
message = file.read().decode('utf-8')
print(message)
with open('test.odt','a') as f:
    f.write(str(message))
