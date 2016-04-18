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
#nlast = nm.get_nmap_last_output()
#nmdict = '/tmp/nm_dict_{0}'.format(ndict)
#nmlast = '/tmp/nm_last_{0}'.format(nlast)
nmcsv = '/tmp/nm_csv_{0}'.format("localhost")
f = open(nmcsv, 'w')
f.write(ncsv)
f.close()

for host in nm.all_hosts():
    for proto in nm[host].all_protocols():
        print('Protocol : {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            state =  str(nm[host][proto][port])
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
            if "tor" in str(state):
                print "PORT:"+ str(port) +"   gotcha tor !!!"
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


#GREP RECONSCAN ORI parse .nmap
# lines = results.split("\n")
for line in lines:
  ports = []
  line = line.strip()
  if ("tcp" in line) and ("open" in line) and not ("Discovered" in line):
while "  " in line:
	line = line.replace("  ", " ");
	linesplit= line.split(" ")
	service = linesplit[2] # grab the service name
port = line.split(" ")[0] # grab the port/proto
if service in serv_dict:
	ports = serv_dict[service] # if the service is already in the dict, grab the port list

	ports.append(port)
serv_dict[service] = ports # add service to the dictionary along with the associated port(2)

# go through the service dictionary to call additional targeted enumeration functions
for serv in serv_dict:
	ports = serv_dict[serv]
	if (serv == "http"):
for port in ports:
	port = port.split("/")[0]
	multProc(httpEnum, ip_address, port)
	elif (serv == "ssl/http") or ("https" in serv):
for port in ports:
	port = port.split("/")[0]
	multProc(httpsEnum, ip_address, port)
	elif "ssh" in serv:
for port in ports:
	port = port.split("/")[0]
	multProc(sshEnum, ip_address, port)
	elif "smtp" in serv:
for port in ports:
	port = port.split("/")[0]
	multProc(smtpEnum, ip_address, port)
	elif "snmp" in serv:
for port in ports:
	port = port.split("/")[0]
	multProc(snmpEnum, ip_address, port)
	elif ("domain" in serv):
for port in ports:
	port = port.split("/")[0]
	multProc(dnsEnum, ip_address, port)
	elif ("ftp" in serv):
for port in ports:
	port = port.split("/")[0]
	multProc(ftpEnum, ip_address, port)
	elif "microsoft-ds" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(smbEnum, ip_address, port)
	elif "ms-sql" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(httpEnum, ip_address, port)lines = results.split("\n")
for line in lines:
	ports = []
	line = line.strip()
	if ("tcp" in line) and ("open" in line) and not ("Discovered" in line):
		while "  " in line:
			line = line.replace("  ", " ");
	 		linesplit= line.split(" ")
	 		service = linesplit[2] # grab the service name
 		port = line.split(" ")[0] # grab the port/proto
	 		if service in serv_dict:
		ports = serv_dict[service] # if the service is already in the dict, grab the port list
				ports.append(port)
				serv_dict[service] = ports # add service to the dictionary along with the associated port(2)

# go through the service dictionary to call additional targeted enumeration functions
for serv in serv_dict:
  	ports = serv_dict[serv]
if (serv == "http"):
	for port in ports:
		port = port.split("/")[0]
		multProc(httpEnum, ip_address, port)
elif (serv == "ssl/http") or ("https" in serv):
	for port in ports:
		port = port.split("/")[0]
		multProc(httpsEnum, ip_address, port)
elif "ssh" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(sshEnum, ip_address, port)
elif "smtp" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(smtpEnum, ip_address, port)
elif "snmp" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(snmpEnum, ip_address, port)
elif ("domain" in serv):
	for port in ports:
		port = port.split("/")[0]
		multProc(dnsEnum, ip_address, port)
elif ("ftp" in serv):
	for port in ports:
		port = port.split("/")[0]
		multProc(ftpEnum, ip_address, port)
elif "microsoft-ds" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(smbEnum, ip_address, port)
elif "ms-sql" in serv:
	for port in ports:
		port = port.split("/")[0]
		multProc(httpEnum, ip_address, port)
