# -*- coding: utf-10 -*-
#!/usr/bin/env python2

import subprocess
import multiprocessing
from multiprocessing import Process, Queue
import os
import time
from httmock import HTTMock
import nmap
import sys


def multiProc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip, port)
    jobs.append(p
    return


def nmapScan(ip_address):
   ip_address = ip_address.strip()
   print "INFO: Running general TCP/UDP nmap scans for " + ip_address
   serv_dict = {}
   TCPSCAN = "nmap -vv -Pn -A -sC -sS -T 4 -p- -oN '/root/scripts/recon_enum/results/exam/%s.nmap' -oX '/root/scripts/recon_enum/results/exam/nmap/%s_nmap_scan_import.xml' %s"  % (ip_address, ip_address, ip_address)
   UDPSCAN = "nmap -vv -Pn -A -sC -sU -T 4 --top-ports 200 -oN '/root/scripts/recon_enum/results/exam/%sU.nmap' -oX '/root/scripts/recon_enum/results/exam/nmap/%sU_nmap_scan_import.xml' %s" % (ip_address, ip_address, ip_address)
   results = subprocess.check_output(TCPSCAN, shell=True)
   udpresults = subprocess.check_output(UDPSCAN, shell=True)
   lines = results.split("\n")
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

   print "INFO: TCP/UDP Nmap scans completed for " + ip_address
   return


# grab the discover scan results and start scanning up hosts
print "############################################################"
print "####                      RECONATOR                     ####"
print "####            A multi-process service scanner         ####"
print "####        http, ftp, dns, ssh, snmp, smtp, ms-sql     ####"
print "############################################################"



if __name__=='main__':
    # f = open (/tmp/targets.txt', 'r')
    f = open ('sys.argv[1]' 'r')
    for  scanip in f:
        jobs = []
        p=  multiprocessing.Process(targets=nmapScan, args=(scanip,))
        jobs.append(p)
        p.start()
    f.close()


"'dgea"
