#!/usr/bin/env python3

import socket
from datetime import datetime
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start = datetime.now()

ports = {
        20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
        25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
        115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
        179: "BGP", 443: "https", 445: "MICROSOFT-DS",
        514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
        995: "POP35", 1080: "SOCKS", 1194: "OpenVPN",
        1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
        3268: "LDAP", 3306: "MySQL", 3389: "RDP",
        5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"}

host = input("[*] Enter the host to Scan ")

def portscanner(ports):
    for port in ports:
        try:
            sock.connect_ex((host, port))
        except socket.error:
            pass
        else:
            print('Port %d is open' % (port))
            sock.close()
ends = datetime.now()
print("<Time:{}>".format(ends - start))
portscanner(ports)
