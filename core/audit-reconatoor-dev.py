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
    fp = multiprocessing.Process(target=targetin, args=(scanip, port))
    jobs.append(fp)
    fp.start()
    return


def httpenum(targets, ports):
    print("NIKTOSCAN")
    targetformat = str(targets)
    portformat = str(ports)
    formata = str(targetformat) + ":" + str(portformat)
    print "targets; " + targetformat
    # multProc("")
    os.system("nikto -host {0} |tee /tmp/nikto_reco_{1}".format(targetformat, targetformat))


# subprocess.call(["touch" "/tmp/recodev"])
# TODO  add port suppport


def smtpenum(targets, ports):
    print "smtpon " + targets + ":" + ports


def snmpenum(targets, ports):
    print "smtp on " + targets + ":" + ports


def smbenum(targets, ports):
    print "smb on " + targets + ":" + ports


def sshenum(targets, ports):
    print "ssh on " + targets + ":" + ports


def ftpenum(targets, ports):
    print "ftp on " + targets + ":" + ports


def torenum(targets, ports):
    print "tor on " + targets + ":" + ports


def mssql(targets, ports):
    print "mssql  on " + targets + ":" + ports


def callscript(targets, ports):
    print "CALL SCRIPT"
    text = "targets: " + targets + "\tports:" + ports
    f = open("/tmp/callscript_{0}_{1}".format(targets, ports), "w")
    f.write(text)
    f.close()


# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = nmap.PortScanner()


nmhttp = nmap.PortScanner()
nm.scan(hosts=targets,
        arguments='-sV -sS -vvv -Pn -oN "/tmp/results/reconator_%s"' % targets, sudo=True)
# TODO add sudo port scan

#   subprocess.process()

ncsv = nm.csv()

nmcsv = '/tmp/nm_csv_{0}'.format(targets)
f = open(nmcsv, 'w')
f.write(ncsv)
f.close()
print('----------------------------------------------------')
print("write nm_csv_{0}".format(targets))
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
                # TODO multiserv
                # formata = str(host)+":"+str(port)
                multProc(httpenum, str(host), str(port))
                multProc(callscript, str(host), str(port))
                nmhttp.scan(hosts=targets,
                            arguments='"-sV -Pn -vv -p %s --script=http-vhosts,http-userdir-enum,http-apache-negotiation,http-backup-finder,http-config-backup,http-default-accounts,http-email-harvest,http-methods,http-method-tamper,http-passwd,http-robots.txt" % port',
                            sudo=True)
                # TODO ecriture resultats dans results
            print('----------------------------------------------------')
            elif "ssh" in str(state):
                multProc(sshenum, str(host), str(port))
            elif "snmp" in str(state):
                multProc(snmpenum, str(host), str(port))
            elif "ftp" in str(state):
                multProc(ftpenum, str(host), str(port))
            elif "smb" in str(state):
                multProc(smbenum, str(host), str(port))
            elif "tor" in str(state):
                multProc(torenum, str(host), str(port))
            elif "ms-sql" in str(state):
                multProc(mssqlenum, str(host), str(port))

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
    if os.path.isdir("/tmp/results") == True:
        print "/tmp/results exists"
    else:
        os.mkdir("/tmp/results", 0777)
    f = open(sys.argv[1], 'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
f.close()
