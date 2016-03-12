#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nmap
import sys
import multiprocessing
#import libnmap
#import nmmapparser
import nmap_parser
#from libnmap import NmapParser, NmapParserException
#from libnmap import NmapProcess
import re



# start a new nmap scan on localhost with some specific options
def do_scan(targets, options):
    parsed = None
    nm = nmap.PortScanner()
    nm.scan(targets, options)
    print('----------------------------------------------------')
    print(nm.csv())
    print('----------------------------------------------------')
    #if rc != 0:
    #    print("nmap scan failed: {0}".format(nmproc.stderr))
    print(nm.csv())

   # try:
    #arsed = nmap_parser.parser[nm.csv()]
    # except NmapParserException as e:
    #     print("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed

def parser(xml):
    nm = nmap.PortScanner()
    print('----------------------------------------------------')
# Read output captured to a file
# Example : nmap -oX - -p 22-443 -sV 127.0.0.1 > nmap_output.xml

    with open(sys.argv[1], "r") as fd:
        content = fd.read()
        nm.analyse_nmap_xml_scan(content)
    print('----------------------------------------------------')
    print(nm.csv())
    print('----------------------------------------------------')

# print scan results from a nmap report
def print_scan(nmap_report):
    print("Starting Nmap {0} ( http://nmap.org ) at {1}".format(
        nmap_report.version,
        nmap_report.started))

    for host in nmap_report.hosts:
        if len(host.hostnames):
            tmp_host = host.hostnames.pop()
        else:
            tmp_host = host.address

        print("Nmap scan report for {0} ({1})".format(
            tmp_host,
            host.address))
        print("Host is {0}.".format(host.status))
        print("  PORT     STATE         SERVICE")

        for serv in host.services:
            pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    str(serv.port),
                    serv.protocol,
                    serv.state,
                    serv.service)
            if len(serv.banner):
                pserv += " ({0})".format(serv.banner)
            print(pserv)
    print(nmap_report.summary)


if __name__ == "__main__":
 #   print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**

    f =open(sys.argv[1],   'r')
    for ip in f:
        options = '-sV -sT -vvv -Pn -oA "/tmp/reconator_%s"' %  (ip)
        report = multiprocessing.Process(target=do_scan, args=ip)

     #   r = re.compile('/tmp/reconator_2...xml')
      #  e = open(r, 'r')
       # parser(e)
#    if report:
    #     print_scan(report)
    # else:
    #     print("No results returned")
    #

