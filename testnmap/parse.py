

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


# grab the discover scan results and start scanning up hosts
print" nmap  parser"

if __name__=='__main__':
   f = open('results/scan.nmap', 'r') # CHANGE THIS!! grab the alive hosts from the discovery scan for enum
   serv_dict = {}
   lines = f.split("\n")
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
        print " http " serv + port
        #multProc(httpEnum, ip_address, port)
      elif (serv == "ssl/http") or ("https" in serv):
	 for port in ports:
	    port = port.split("/")[0]
        print " https " serv  + port
	    #multProc(httpsEnum, ip_address, port)
      elif "ssh" in serv:
	 for port in ports:
	    port = port.split("/")[0]
        print " ssh  " serv  + port
	    #multProc(sshEnum, ip_address, port)
      elif "smtp" in serv:
	 for port in ports:
	    port = port.split("/")[0]
        print " smtp  " serv  + port

	    #multProc(smtpEnum, ip_address, port)
      elif "snmp" in serv:
 	 for port in ports:
	    port = port.split("/")[0]
        print " snmp  " serv  + port

	    #multProc(snmpEnum, ip_address, port)
      elif ("domain" in serv):
 	 for port in ports:
	    port = port.split("/")[0]
        print " dnsEnum  " serv  + port
	    #multProc(dnsEnum, ip_address, port)
      elif ("ftp" in serv):
 	 for port in ports:
	    port = port.split("/")[0]
        print " ftpEnum   " serv  + port
	    #multProc(ftpEnum, ip_address, port)
      elif "microsoft-ds" in serv:
 	 for port in ports:
 	    port = port.split("/")[0]
        print " smbEnum   " serv + port
	    #multProc(smbEnum, ip_address, port)
      elif "ms-sql" in serv:
 	 for port in ports:
	    port = port.split("/")[0]
        print " smbEnum   " serv + port
	    #multProc(httpEnum, ip_address, port)

   print "INFO: TCP/UDP Nmap scans completed for " + serv
   return

