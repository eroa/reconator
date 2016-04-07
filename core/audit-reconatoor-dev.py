#!/usr/bin/env python

import nmap
import sys
import multiprocessing
import subprocess
# import libnmap
# import nmmapparser
# import nmap_parser
# from libnmap import NmapParser, NmapParserException
# from libnmap import NmapProcess
import re
import csv
import os


# jobs = []
# ip ="".join(scanip)
# sip = str(ip)

def multProc(targetin, scanip, port):
    jobs = []
    fp = multiprocessing.Process(target=targetin, args=(scanip,port))
    jobs.append(fp)
    fp.start()
    return


def httpenum(targets, ports):
    print("NIKTOSCAN")
    targetformat=  str(targets)
    portformat = str(ports)
    formata = str(targetformat) + ":" + str(portformat)
    print "targets; " + targetformat
    # multProc("")
    os.system("nikto -host {0} |tee /tmp/reconatoor_{1}".format(targetformat, targetformat))

    # TODO  add port suppport


# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = nmap.PortScanner()
    nm.scan(hosts=targets,
            arguments='-sV -sT -T5 -vvv -Pn -oN "/tmp/results/reconator_%s"' % targets)

    #   subprocess.process()

    ncsv = nm.csv()

    nmcsv = '/tmp/nm_csv_{0}'.format(targets)
    f = open(nmcsv, 'w')
    f.write(ncsv)
    f.close()
    print('----------------------------------------------------')
    print("write nm_csv_*")
    print('----------------------------------------------------')

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            print('Protocol : {0}'.format(proto))
            lport = list(nm[host][proto].keys())
            lport.sort()
            for port in lport:
                state = nm[host][proto][port]
                print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
                if "http" in str(state):
                    print "PORT:" + str(port) + "   gotcha (http via dict)!!!"
                    #TODO stock dans tuple?
                    formata = str(host)+":"+str(port)
                    multProc(httpenum, str(host),str(port))
                    print('----------------------------------------------------')
                else:
                    print "no http"
    # fncsv = ncsv.split("\n", 1)
    # print('----------------------------------------------------')
    # print('csv')
    # print('----------------------------------------------------')
    # print(ncsv)
    # print('----------------------------------------------------')
    #
    # for row in fncsv:
    #     if "http" in row:
    #         print(row)
    #         print("GOTCHA http (via csv) !!!!!")
    #         #            print("launch nikto...")
    #         for host in nm.all_hosts():
    #             print("launch  httpenum_{0}".format(str(host)))
    #             fhost = str("".join(host))
    #             multProc(httpenum, fhost)
    #     else:
    #         print("pas de http")
    #         print('----------------------------------------------------')


            # matchttp = re.search(r'http', str(row))
    print('###########################################################')

    return parsed


if __name__ == "__main__":
    #    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    os.mkdir("/tmp/results", 0777)
    f = open(sys.argv[1], 'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
    f.close()
