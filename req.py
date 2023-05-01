#!/usr/bin/env python3

import grequests
import requests

class R:
    def main_func():
        r = requests.get('https://distrowatch.com')
        print(f"{r.headers}-{r.status_code}")
    main_func()


if __name__=='__main__':
    R
