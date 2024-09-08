#!/usr/bin/env python3

import collections
import requests
def fun():
    headers = {
            "User - Agent" : "i 2 != 0"
         }   


    response = requests.get("https://httpbin.org/get",headers=headers,params={'a':'b','c':'d'})
    print(response.headers)

    response = requests.post("https://httpbin.org/post",headers=headers,params={'a':'b','c':'d',10:12},json={'username':'supersecret'})
    print(response.headers)

    count = collections.Counter(response.text)
    print(count)

    response = requests.post('http://www.freebsd.org')
    response.raise_for_status()
    print(response.headers)
    return response.headers

if __name__=='__main__':
    with open('test.md','w') as f:
        f.write(str(fun()))
