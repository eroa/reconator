#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nmap
import sys
import multiprocessing
import subprocess
#import libnmap
#import nmmapparser
#import nmap_parser
#from libnmap import NmapParser, NmapParserException
#from libnmap import NmapProcess
import re
import csv
import os

# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = nmap.PortScanner()
    nm.scan(hosts=targets, arguments='-sV -sT -T5 -vvv -Pn -oN "/tmp/reconator_%s"' % targets)
#    subprocess.process()
#     print('----------------------------------------------------')
#     print("CSV")
#     print('----------------------------------------------------')
    print(nm.csv())
    print('----------------------------------------------------')
    ncsv = nm.csv()
    r = csv.reader(ncsv)
    nmenm = "/tmp/nm_reco_%s" % targets
    f = open(nmenm, 'w')
    f.write(ncsv)
    f.close()
    print('----------------------------------------------------')
    print("write nm_reco_*")
    print('----------------------------------------------------')
    subprocess.call("/home/toxic/workspace/reconator/core/format_nm.sh")
    for host in nm.all_hosts():
        # print('----------------------------------------------------')
        # print('Hostname')
        # print('----------------------------------------------------')
        print('Host : {0} ({1})'.format(host, nm[host].hostname()))
        # print('----------------------------------------------------')
        # print("nm[host][proto].keys() lport sort")
        # print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
        print('----------------------------------------------------')
    for host in nm.all_hosts():
        res = open('/tmp/nm_reco_%s' % host)
        #TODO fix nom nm_reco (quote + $)
        print('----------------------------------------------------')
        print("read csv writed")
        print('----------------------------------------------------')
        for row in res :
            print(row)

        data = res.read()
        matchttp = re.search(r'http', row)
        matchttps = re.search(r'https', row)
        matchssh = re.search(r'ssh', row)
        matchftp = re.search(r'ftp', row)
        matchtelnet = re.search(r'telnet', row)
        matchsnmp = re.search(r'snmp', row)
        matchsmtp = re.search(r'smtp', row)

        if matchttp:
            print("GOTCHA!!!!!")
            print("launch nikto...")
            try:
                subprocess.call('/usr/bin/nikto %s ' % host)
            except:
                print('vnikto failed')

    return parsed


if __name__ == "__main__":
#    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    f =open(sys.argv[1],   'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
    f.close()

     #   r = re.compile('/tmp/reconator_2...xml')
      #  e = open(r, 'r')
       # parser(e)
#    if report:
    #     print_scan(report)
    # else:
    #     print("No results returned")
    #

