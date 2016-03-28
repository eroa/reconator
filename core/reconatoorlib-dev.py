
import nmapparser
import libnmap
import nmap
import csv
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser




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



	#jobs = []
	#ip ="".join(scanip)
	#sip = str(ip)#!/usr/bin/env python

def multProc(targetin, scanip):
    jobs = []
    fp = multiprocessing.Process(target=targetin, args=(str(scanip), ))
    jobs.append(fp)
    fp.start()
    return

def httpenum(targets):
    print("2DO NIKTOSCAN" )
#    multProc("")
    #sNIKTO =
    os.system("nikto -host localhost")
    #subprocess.call(["touch" "/tmp/recodev"])
    # TODO  check proof


# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = NmapProcess('192.168.11.227', options='-sT -sV --open -nvvv')
    print nm.is_successful()
    call(nm.stdout())
    nmr = nm.stdout
    print nmr
    nmrx = NmapParser.parse(nmr)
    for s in nmrx.hosts:
        print s
    for s in nmrx.hosts_total:
        print si
    rnm = nmrx.get_raw_data()
    pars = NmapParser.parse(lnm.stdout)
#TODO grep service libnmap
#     for row in fncsv :
#         if "http" in row:
#             print(row)
#             print("GOTCHA HTTP !!!!!")
# #            print("launch nikto...")
#             for host in nm.all_hosts():
#                 print("launch  proof %s " % str(host))
#                 fhost =str("".join(host))
#                 multProc(httpenum, fhost)
#                 # try:
            #subprocess.call('/usr/bin/nikto %s ' % host)
            #subprocess.call('echo zob > "/tmp/recotouch" ')

            #except:
        #      #   print('vnikto failed')
        # else:
        #     print("pas de http")
        #     print('----------------------------------------------------')

       # matchttp = re.search(r'http', str(row))
    print('###########################################################')



    return parsed


if __name__ == "__main__":
#    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    f =open(sys.argv[1],   'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
    f.close()








