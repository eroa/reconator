from itertools import product

import nmap
import os
import re
import multiprocessing
import subprocess
import csv


nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1' ,arguments='-sS -sV -sC -A -vvvv -oN "/tmp/grepsudo"', sudo=True)
nxml = nm.get_nmap_last_output()
ndict = nm.analyse_nmap_xml_scan()

for host in nm.all_hosts():
    print host
    print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('proto: {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        print('----------------------------------------------------')
        print lport
        lport.sort()
        for port in lport:
            print type(nm[host][proto][port])
            state = str(nm[host][proto][port])
            print('proto: {0}\tstate: {1})'.format(port, nm[host][proto][port]))
#TODO grep deeper dict
