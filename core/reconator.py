# -*- coding: utf-8 -*-


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#import os
import sys
import nmap
import multiprocessing

#
#
def multProc(targetin, scanip, port):
    jobs = []
    p = multiprocessing.Process(target=targetin, args=(scanip,port))
    jobs.append(p)
    p.start()
    return
#
#

# def altscan(ip_address, port):
#     print "INFO: Detected DNS on " + ip_address + ":" + port
#     if port.strip() == "53":dz
#        SCRIPT = "./altscan.py %s" % (ip_address)# execute the python script
#        subprocess.call(SCRIPT, shell=True)
#     return



def xscan(ipadd):
    nm = nmap.PortScanner()
    nm.scan(hosts=str(ipadd),
            arguments="-sV -sT -T4 -nvvv -Pn -oG '/tmp/reconator_g_%s' -oN '/tmp/reconator_%s'" % (ipadd, ipadd))
    print (str(nm.command_line()))
    print(str(nm.csv()))
    nm.get_nmap_last_output()
    print(str(nm))
    #m.get_nmap_last_output()
    #rint(nm.csv())
    hosts = nm.all_hosts()
    serv_dict={}
    #   for host in nm[host].all_hosts():
    for host in hosts:
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            lport.sort()
            for port in lport:
                print('host: %s\tport: %s\tstate : %s\tproto: %s' % (nm[host]['addresses'],port, nm[host][proto][port]['state'], nm[host][proto][port]['product']))
                if "htttp" in nm[host][proto][port]['product']:
                    print("GREP VICTORY + %s" % str(nm[host][proto][port]['product']))
                services = nm[host][proto][port]['product']
                if htt

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

