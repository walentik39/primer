#!/usr/bin/env python3

from pprint import pprint
import json
from random import randint as rd, choice as ch

def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding= 'utf-8') as file:
        json.dump(data, file, indent = 4)


def read(filename):
    with open(filename, 'r', encoding = 'utf-8') as file:
        return json.load(file)

class User:
    def __init__(self):
        self.name = ch(['First','Second','Thrid'])
        self.age = rd(0, 70)
        self.id = rd(500, 1000)

data = { 
        "users" : []
        }

for i in range(100):
    data['users'].append(User().__dict__)

#write(data, 'data.json')
pprint(read('data.json'))
