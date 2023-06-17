#!/usr/bin/env python3

import ipaddress
import socket
def two_main():
    value = socket.gethostbyname('ipconfig.me')
    def main():
        ip1 = ipaddress.ip_address(value)
        print(ip1,'\n')
        print(ip1.is_global,ip1.is_private)
    return main()       
two_main()    


