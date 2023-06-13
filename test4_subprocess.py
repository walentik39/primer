#!/usr/bin/env python3

from pprint import pprint
import platform
import subprocess

def ping_ip_list(ip_list):
    pingable = []
    unpingable = []
    if platform.system().lower() == "windows":
        cmd = ['ping','-n','1']
    else:
        cmd = ['ping','-c','1']
    processes = []
    for ip in ip_list:
        p = subprocess.Popen(
            cmd + [ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            encoding="utf-8"
            )
        processes.append(p)
    for ip, process in zip(ip_list, processes):
        returncode = process.wait()
        if returncode == 0:
            pingable.append(ip)
        else:
            unpingable.append(ip)
    return pingable, unpingable



if __name__=='__main__':
    ip_list = ["8.8.4.4","test.me","127.0.1.1","8.8.8.8","12.124.12.22"]
    result = ping_ip_list(ip_list)
    pprint(result)
