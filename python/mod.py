#!/usr/bin/env python3

import ipaddress
import socket
import sys
import subprocess

def two_main():
    value = socket.gethostbyname('test.me')
    def main():
        ip1 = ipaddress.ip_address(value)
        print(ip1,'\n')
        print(ip1.is_global,ip1.is_private)
    return main()       
two_main()    

def three_main():
    result = subprocess.run(['ping','-c','3','8.8.8.0'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    return result

res = three_main()
print(''.join(str(res)))

