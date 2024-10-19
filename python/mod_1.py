#!/usr/bin/env python3

import ipaddress
import socket
import sys
import subprocess
class My:
    def two_main(self):
        value = socket.gethostbyname('openbsd.net')
        def main(self):
            ip1 = ipaddress.ip_address(value)
            print(ip1,'\n')
            print(ip1.is_global,ip1.is_private)
        return main(self)       

    def three_main(self):
        result = subprocess.run(['ping','-c3','8.8.8.8'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,encoding='utf-8')
                                
        return result
if __name__=='__main__':
    m = My()
    result1 = m.two_main()
    print(''.join(str(result1)))
    res = m.three_main()
    print(''.join(str(res)))

