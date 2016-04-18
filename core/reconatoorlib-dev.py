
import nmapparser


# -*- coding: utf-8 -*-
import sys
import multiprocessing
import subprocess
import libnmap.process
import libnmap.parser
import libnmap.objects
import libnmap
from libnmap.parser import NmapParser, NmapParserException
from libnmap.process import NmapProcess
from libnmap.objects import NmapService
from libnmap.objects import  service, host, report
import re
import os
import nmap
import csv



#jobs = []
	#ip ="".join(scanip)
	#sip = str(ip)#!/usr/bin/env python

def multProc(targetin, scanip):
    jobs = []
    fp = multiprocessing.Process(target=targetin, args=(str(scanip),))
    jobs.append(fp)
    fp.start()
    return

def httpenum(target):
    print(" NIKTOSCAN" )
#    multProc("")
    NIKTO = "nikto -host "
    rp =multiprocessing.Process(target=NIKTO, args=str(target),)
    rp.start()
    #os.system("nikto -host localhost")
    #subprocess.call(["touch" "/tmp/recodev"])
    # TODO  check proof

def callscript(target;port):
    print "CALL SCRIPT /tmp/test.sh"


# start a new nmap scan on iplist.txt  with some specific options
def do_scan(targets):
    parsed = None
    a = str(targets)
    nm = NmapProcess(targets=targets, options='-sV -sT -oN "/tmp/recolib_%s" % targets')
    rnm = nm.run()
    npars= NmapParser()
    parsed = npars.parse(nmap_data=npars)
    do_reports(a, parsed)
    for host in parsed.hosts:
        services = host.services
        for service in services:
            if service.state == "open":
                print str(service)
                if "http" in str(service):
                    httpenum(str(host))
                    return parsedi

def do_reports(targets , parsed):
    rnm = NmapR


    # for host  in  parsed.hosts:
    #     if len(host.hostnames):
    #         tmphost = host.hostnames.pop()
    #     else:
    #         tmphost = host.address
    #     print ("nmap scan for {0} {1}".format(tmphost, host.address))
    #     print ("host is {0}.".format(host.STATE))
    #     print ("PORT    STATEi      SERVICE")
    #     for serv in host.services:
    #         pserv = "{0:>5s}/{1:3s} {2:12s} {3}".format(str(SERVICE.PORT), serv.protocol,serv.state,ser.service)
    #         if len(serv.banner):
    #             pserv +=  " ({0})".format(serv.banner)
    #         print(pserv)
    # print parsed.summary
  #  pars = NmapParser.parse(lnm.stdout)
#TODO grep service libnmap

    print('###########################################################')



#    return parsed


if __name__ == "__main__":
#    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    f =open(sys.argv[1],   'r')
    for ip in f:
        targets = str(ip)

        report = multiprocessing.Process(target=do_scan, args=(ip,))

    f.close()








