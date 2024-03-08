#!/usr/bin/env python3

import subprocess
import random
ip_list = ['8.8.4.4','127.0.1.1','test.me','37.14.18.10','8.8.8.8']
ip_choice = random.choice(ip_list)
for ip in ip_choice:
    result = subprocess.run(['ping','-c 1',ip],stderr=subprocess.DEVNULL,
                            stdout=subprocess.PIPE,encoding='utf-8')
    print(result.stdout)
