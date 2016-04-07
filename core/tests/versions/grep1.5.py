from itertools import product

import nmap
import os
import re
import multiprocessing
import subprocess
import csv

from tests.libnmap import ndict

nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1', arguments='-sT -sV  -vvv -oN /tmp/testgrep')

ncsv = nm.csv()
#ndict = nm.analyse_nmap_xml_scan(())
nlast = nm.get_nmap_last_output()
#nmdict = '/tmp/nm_dict_{0}'.format(ndict)
nmlast = '/tmp/nm_last_{0}'.format(nlast)
nmcsv = '/tmp/nm_csv_{0}'.format("localhost")
f = open(nmcsv, 'w')

for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        print('Protocol : {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            state =  nm[host][proto][port]
            print('port : {0}\tstate : {1}'.format(port, state))
            if "tor" in str(state):
                print "AAAAAAAAAAAAAAAAAAAAAAAAAA"
        print('----------------------------------------------------')
        lprod = list(nm[host][proto][port].keys())
        lprod.sort()
        print str(lprod)
        print "ZZZZ:" + lprod.pop(4)
        print "ZZZZ" + lprod[5]
        foo = lprod[4]
        # print foo
        # for prod in lprod:
        #     print('prod : {0}'.format(nm[host][proto][port][product]))
