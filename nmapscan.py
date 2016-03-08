#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#import os
import sys
import nmap
import multiprocessing
nmap.PortScannerHostDict
def xscan(ipadd):
    nm = nmap.PortScanner()
    nm.scan(hosts=str(ipadd), arguments="-sV -sT -T4 -nvvv -Pn -oG '/tmp/fscratch_g_%s' -oN '/tmp/fscratch_%s'" % (ipadd,ipadd))
    print (str(nm.command_line()))
    print(str(nm.csv()))

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                print ('port : %s\tservice : %s' % (port, nm[host][proto][port]['product']))
                print ('port : %s\tinfo: %s' % (port, nm[host][proto][port]['extrainfo']))
                print ('port : %s\tversion : %s' % (port, nm[host][proto][port]['version']))
                # if report:
                #     (report)
                # else:  # if __name__=='__main__':
#TODO:parser reports

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    for ip in f:
        #jobs = []
        #fip = str(ip)
        p = multiprocessing.Process(target=xscan, args=(ip,))
        #jobs.append(p)
        p.start()
    f.close()

