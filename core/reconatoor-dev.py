#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nmap
import sys
import multiprocessing
import subprocess

import os


def multProc(targetin, scanip, port):
    jobs = []
    fp = multiprocessing.Process(target=targetin, args=(scanip, port))
    jobs.append(fp)
    fp.start()
    return



def httpenum(targets, ports):
    if os.path.isdir("/tmp/results/nmap") == True:
        print "/tmp/results/nmap exists"
    else:
        os.mkdir("/tmp/results/nmap", 0777)
    print("NIKTOSCAN")
    targetformat = str(targets)
    portformat = str(ports)
    formata = str(targetformat) + ":" + str(portformat)
    print "targets; " + targetformat
    # multProc("")
    #	os.system("nikto -host {0} |tee /tmp/nikto_reco_{1}".format(targetformat, targetformat))
    # subprocess.call(["touch" "/tmp/recodev"])
    serv_dict = {}
    NIKTO = "nikto -host {0} -port {1}|tee /tmp/results/nikto_reco_{2}".format(targetformat, portformat, targetformat)
    # DIRB = "dirb http://{0}|tee /tmp/results/dirb_reco{1}".format(targetformat, targetformat)
    subprocess.call(NIKTO, shell=True)
    print subprocess.check_output(NIKTO)

    # Write XML and Normal output in /tmp/results
    TCPSCAN = "sudo nmap -vv -Pn -A -sC -sS -T 4  -oN '/tmp/results/nmap/%s.nmap' -oX '/tmp/results/nmap/%s_nmap_scan_import.xml' %s" % (
        str(targetformat), str(targetformat), str(targetformat))  # TODO  -p- à rajouter
    UDPSCAN = "sudo nmap -vv -Pn -A -sC -sU -T 4 --top-ports 10 -oN '/tmp/results/nmap/%sU.nmap' -oX '/tmp/results/nmap/%sU_nmap_scan_import.xml' %s" % (
        targetformat, targetformat, targetformat)  # TODO remttre top 200
    results = subprocess.check_output(TCPSCAN, shell=True)
    print "***************************************************************"
    print "TCPRESULTS:" + results
    print "***************************************************************"
    udpresults = subprocess.check_output(UDPSCAN, shell=True)
    print "UDPRESULTS:" + udpresults
    print "***************************************************************"
    lines = results.split("\n")


# subprocess.call(DIRB, shell=True)

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
    if os.path.isdir("/tmp/results/nmap") == True:
        print "/tmp/results/nmap exists"
    else:
        os.mkdir("/tmp/results/nmap", 0777)
    print("FTP scriptscan ")
    targetformat = str(targets)
    portformat = str(ports)
    print "ftp on " + targets + ":" + ports
    print "performing FTPscript scan on target"
    FTPSCAN = "nmap -sV -Pn -vv -p {0} --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221 -oA '/tmp/results/nmap/#{1}_ftp.nmap' {2}" % (
    portformat, targetformat, targetformat)
    results = subprocess.check_output(FTPSCAN, shell=True)
    outfile = "/tmp/results/" + targetformat + "_ftprecon.txt"
    f = open(outfile, "w")
    f.write(results)
    f.close()

    print "PERFORMING HYDRA BF AGAINST" + targetformat
    HYDRA = "hydra -L /home/toxic/git/oscp/paillasse/users.txt -P /home/toxic/git/oscp/paillasse/passwords.txt -f -o /tmp/results/{0]_ftphydra.txt -u {1} {21] ftp".format(
        targetformat, targetformat, portformat)
    subprocess.call(HYDRA,shell=True)

def torenum(targets, ports):
    print "tor on " + targets + ":" + ports


def msasql(targets, ports):
    print "mssql  on " + targets + ":" + ports


def writeTargets(targets, ports):
    d = []
    print "WRITE TARGET"
    text = "targets: " + targets + "\tports:" + ports
    f = open("/tmp/results/writeTargets_{0}_{1}".format(targets, ports), "w")
    f.write(text)
    f.close()
    os.system("cat /tmp/results/write* > targetsscanned")
    # t = open("/tmp/results/all_targ_n_port.txt", "w")
    # d.append(targets + ":" + ports)
    # t.writelines(d)
    # t.close()

def parsinglaunch(nm):
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            print('Protocol : {0}'.format(proto))
            lport = list(nm[host][proto].keys())
            lport.sort()
            for port in lport:
                state = nm[host][proto][port]
                print('TCP port : {0}\tstate : {1}'.format(port, nm[host][proto][port]))
                if "http" in str(state):
                    print "TCP PORT:" + str(port) + "   gotcha (http via dict)!!!"
                    # formata = str(host)+":"+str(port)
                    multProc(httpenum, str(host), str(port))
                    multProc(writeTargets, str(host), str(port))
                    # (------------------------------------')
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
                print('#######################  nm host: {0} port: {1} '.format(host, port))

# start a new nmap scan on localhost with some specific options
def do_scan(targets):
    parsed = None
    targetformat = str(targets)
    nmt = nmap.PortScanner()
    nmu = nmap.PortScanner()
    # nm.scan(hosts=targets,
    # arguments='-sV -sS -vvv -Pn -oN "/tmp/results/reconator_first_%s"' % targets, sudo=True)

    nmt.scan(hosts=targets, arguments="-vv -Pn   -sS -sV -sC  -oN '/tmp/results/nmap/first_{0}.nmap' {1} ".format(targetformat, targetformat), sudo=True)
    nmu.scan(hosts=targets,
             arguments="-vv -Pn -A -sC -sU -T 4 --top-ports 1 -oN '/tmp/results/nmap/#first_{0}_UDP.nmap' {1}".format(targetformat, targetformat), sudo=True)
    nmtxml = nmt.get_nmap_last_output()
    nmtcsv = nmt.csv()
    nmtdict = nmt.analyse_nmap_xml_scan()
    nmuxml = nmu.get_nmap_last_output()
    nmucsv = nmu.csv()
    nmudict = nmu.analyse_nmap_xml_scan()
    print "TCPSCAN: " + nmtcsv
    parsinglaunch(nmt)
    print "UDPSCAN: " + nmucsv
    parsinglaunch(nmu)

    return parsed

if __name__ == "__main__":
    #    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    if os.path.isdir("/tmp/results") == True:
        print "/tmp/results exists"
    else:
        os.mkdir("/tmp/results", 0777)
    if os.path.isdir("/tmp/results/nmap") == True:
        print "/tmp/results/nmap exists"
    else:
        os.mkdir("/tmp/results/nmap", 0777)
    f = open(sys.argv[1], 'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
f.close()
