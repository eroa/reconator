import nmap
import os
import re
import multiprocessing
import subprocess
import csv

nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1', arguments='-sT -sV  -vvv -oN /tmp/testgrep')
ncsv = nm.csv()
fncsv = ncsv.split("\n",1)
for row in fncsv :
	if "tor" in row:
		print(row)
        print("GOTCHA HTTP !!!!!")
#            print("launch nikto...")
        for host in nm.all_hosts():
            print("launch  proof %s " % str(host))
            fhost = str("".join(host))
            os.system("/usr/bin/touch /tmp/a")
if 'tor' in ncsv:
	print "victory"
else:
	print "zob"

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('SORT NM.ALL_HOSTS')
    print('----------------------------------------------------')
    print('Hostname')
    print('----------------------------------------------------')
    print('Host : {0} ({1})'.format(host, nm[host].hostname()))
    print('----------------------------------------------------')
    print("nm[host][proto].keys() lport sort")
    print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
        print('----------------------------------------------------')
        lprod = list(nm[host][proto][port].keys())
        lprod.sort()

        for prod in lprod:
	        print('prod : {0}'.format(nm[host][proto][port][product]))