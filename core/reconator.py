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
import csv


# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = nmap.PortScanner()
    nm.scan(hosts=targets, arguments='-sV -sT -T5 -vvv -Pn -oN "/tmp/reconator_%s"' % targets)
    print('----------------------------------------------------')
    print(nm.csv())

#:    fcsv = open('/tmp/nm_%s' %targets, "wb")
    print('----------------------------------------------------')
    ncsv = nm.csv()
    r = csv.reader(ncsv)
    nmenm = "/tmp/nm_reco_%s" % targets
    f = open(nmenm, 'w')
    f.write(ncsv)
    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : {0} ({1})'.format(host, nm[host].hostname()))
       #  print('State : {0}'.format(nm[host].state()))
       # # print('Product : {0}'.format(nm[host].product()))
        # print('ExtraInfo : {0}'.format(nm[host].extrainfo()))
        # print('Version : {0}'.format(nm[host].version()))
       #  print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
        # print ('port : %s\tservice : %s' % (port, nm[host][proto][port]['product']))
        # print ('port : %s\tinfo: %s' % (port, nm[host][proto][port]['extrainfo']))
        # print ('port : %s\tversion : %s' % (port, nm[host][proto][port]['version']))

    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))

        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))

   # r = csv.reader('ncsv', delimiters=";")
    #wfcsv = open (fcsv, delimiter=";", quotechar='"',quoting=csv.QUOTE_ALL % targets )

    # for l in r:
        # if re.search('http', l):
            # print('TODO TOOLS HTTP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# #            print(l)
#            nmap_parser.

       # else:
        #    print('ploooop')
#            print(l)
            #if rc != 0œ:w
    #    print("nmap scan failed: {0}".format(nmproc.stderr))
#    print(nm.csv())

   # try:
    #arsed = nmap_parser.parser[nm.csv()]
    # except NmapParserException as e:
    #     print("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed

# def parser(xml):
    # nm = nmap.PortScanner()
    # print('----------------------------------------------------')
# # Read output captured to a file
# # Example : nmap -oX - -p 22-443 -sV 127.0.0.1 > nmap_output.xml

    # with open(sys.argv[1], "r") as fd:
         # content = fd.read()
        # nm.analyse_nmap_xml_scan(content)
    # print('----------------------------------------------------')
    # print(nm.csv())
    # print('----------------------------------------------------')

# print scan results from a nmap report
# def print_scan(nmap_report):
    # print("Starting Nmap {0} ( http://nmap.org ) at {1}".format(
        # nmap_report.version,
        # nmap_report.started))

    # for host in nmap_report.hosts:
        # if len(host.hostnames):
            # tmp_host = host.hostnames.pop()
        # else:
            # tmp_host = host.address

        # print("Nmap scan report for {0} ({1})".format(
            # tmp_host,
            # host.address))
        # print("Host is {0}.".format(host.status))
        # print("  PORT     STATE         SERVICE")

        # for serv in host.services:
            # pserv = "{0:>5s}/{1:3s}  {2:12s}  {3}".format(
                    # str(serv.port),
                    # serv.protocol,
                    # serv.state,
                    # serv.service)
            # if len(serv.banner):
                # pserv += " ({0})".format(serv.banner)
            # print(pserv)
    # print(nmap_report.summary)


if __name__ == "__main__":
 #   print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**

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

