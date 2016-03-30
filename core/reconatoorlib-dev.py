
import nmapparser


# -*- coding: utf-8 -*-
import sys
import multiprocessing
import subprocess
#import libnmap
#import nmmapparser
#import nmap_parser
#from libnmap import NmapParser, NmapParserException
#from libnmap import NmapProcess
import re
import os
import nmap
import csv
import libnmap
import libnmap.parser
import libnmap.process

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser


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
    nm = libnmap.process.NmapProcess(targets="127.0.0.1", options="-sT -sV -oN '/tmp/recolib'", safe_mode=false)
    rnm = nm.run()
    # nm = NmapProcess('192.168.11.227', options='-sT -sV --open -nvvv')
    print nm.is_successful()
    nm.stdout
    nmstd= nm.stdout
    print nmstd
    parsed = libnmap.parser.NmapParser(nmstd)
    #return pnmstd
    for host  in  parsed.hosts:
        if len(host.hostnames):
            tmphost = host.hostnames.pop()
        else:
            tmphost = host.address
        print ("nmap scan for {0} {1}".format(tmphost, host.address))
        print ("host is {0}.".format(host.STATE))
        print ("PORT    STATEi      SERVICE")
        for serv in host.services:
            pserv = "{0:>5s}/{1:3s} {2:12s} {3}".format(str(SERVICE.PORT), serv.protocol,serv.state,ser.service)
            if len(serv.banner):
                pserv +=  " ({0})".format(serv.banner)
            print(pserv)
    print parsed.summary
  #  pars = NmapParser.parse(lnm.stdout)
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



#    return parsed


if __name__ == "__main__":
#    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    f =open(sys.argv[1],   'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))

    f.close()








