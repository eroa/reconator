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
    #multProc("")
    #sNIKTO =
    os.system("nikto -host {0} |tee /tmp/nikto_reconatoor_{1}".format(targets, targets))
    #subprocess.call(["touch" "/tmp/recodev"])
    # TODO  check proof


# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    nm = nmap.PortScanner()
    nm.scan(hosts=targets,
            arguments='-sV -sT -T5 -vvv -Pn -oN "/tmp/reconator_%s"' % targets)

#   subprocess.process()

    ncsv = nm.csv()
    # ndict = nm.get_nmap_last_output()
    # nmdict = '/tmp/nm_dict_{0}'.format(ndict)
    nmenm = '/tmp/nm_reco_{0}'.format(targets)
    f = open(nmenm, 'w')
    f.write(ncsv)
    f.close()
    print('----------------------------------------------------')
    print("write nm_reco_*")
    print('----------------------------------------------------')
#    subprocess.call("/home/toxic/workspace/reconator/core/format_nm.sh")

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('SORT NM.ALL_HOSTS')
        print('----------------------------------------------------')
        print('Hostname')
        print('----------------------------------------------------')
        print('Host : {0} ({1})'.format(host, nm[host].hostname()))
        print('----------------------------------------------------')
        print("nm[host][proto].keys() lport sort")
        print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        lport.sort()
        for port in lport:
            print('port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
        print('----------------------------------------------------')


#    fncsv = ncsv.split("\n", 1)[1:]
    fncsv = ncsv.split("\n",1)
    print('----------------------------------------------------')
    print('csv')
    print('----------------------------------------------------')
    print(ncsv)
    print('----------------------------------------------------')

    for row in fncsv :
        if "http" in row:
            print(row)
            print("GOTCHA HTTP !!!!!")
#            print("launch nikto...")
            for host in nm.all_hosts():
                print("launch  proof %s " % str(host))
                fhost =str("".join(host))
                multProc(httpenum, fhost)
                # try:
            #subprocess.call('/usr/bin/nikto %s ' % host)
            #subprocess.call('echo zob > "/tmp/recotouch" ')

            #except:
             #   print('vnikto failed')
        else:
            print("pas de http")
            print('----------------------------------------------------')

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
