#!/usr/bin/env python3

import ipaddress
import socket
import sys
import subprocess

def two_main():
    value = socket.gethostbyname('freebsd.org')
    def main():
        ip1 = ipaddress.ip_address(value)
        print(ip1,'\n')
        print(ip1.is_global,ip1.is_private)
    return main()       

def three_main(name):
    result = subprocess.run(['ping','-c','3','8.8.4.4'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    return result

if __name__=='__main__':
    res = three_main(two_main())
    print(''.join(str(res)))
    with open('test.docs','w') as file:
        file.write(''.join(str(res)))
