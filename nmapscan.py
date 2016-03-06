#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#import os
import sys
import nmap
import multiprocessing


def xscan(ipadd):
    nm = nmap.PortScanner()
    nm.scan(hosts=str(ipadd), arguments="-sV -sT -T4 -nvvv -Pn -oN '/tmp/fscratch_%s'" % ipadd)
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
                # if report:
                #     (report)
                # else:  # if __name__=='__main__':

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    for ip in f:
        #jobs = []
        #fip = str(ip)
        p = multiprocessing.Process(target=xscan, args=(ip,))
        #jobs.append(p)
        p.start()
    f.close()

#nm.scan(hosts=str(sys.argv[]), arguments=' ,-sV -sS -O -sC -nvvv -Pn ')

#    f = open('results/exam/targets.txt', 'r') # CHANGE THIS!! grab the alive hosts from the discovery scan for enum
#    for scanip in f:
#        jobs = []
#        p = multiprocessing.Process(target=nmapScan, args=(scanip,))
#        jobs.append(p)
#        p.start()
#    f.close()
