from itertools import product

import nmap
import os
import re
import multiprocessing
import subprocess
import csv

from tests.libnmap import ndict

nm = nmap.PortScanner()
nm.scan(host='127.0.0.1' ,arguments='-sS -sV -sC -A -vvvv -oN "/tmp/grepsudo"', sudo=True)
nxml = nm.get_nmap_last_output()
ndict = nm.analyse_nmap_xml_scan()

for host in nm.all_hosts():
    print host
    for proto in nm[host].all_protocols():
        print
        print('proto: {0}\tstate: {1}).format(port, nm[host][proto][port]))

