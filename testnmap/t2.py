# coding=utf-8
from libnmap.process import NmapProcess

from libnmap.process import NmapProcess
from time import sleep
from libnmap.parser import NmapParser, NmapParserException

def do_scan(targets, options):
    parsed = None
    nmap_proc = NmapProcess(targets="scanme.nmap.org", options="-sS -sV -sC -O -nvvv -T4 -Pn")
    nmap_proc.run_background()
    while nmap_proc.is_running():
        print("Nmap Scan running: ETC: {0} DONE: {1}%".format(nmap_proc.etc,
                                                              nmap_proc.progress))
        sleep(2)

    print("rc: {0} output: {1}".format(nmap_proc.rc, nmap_proc.summary))
    try:
            parsed = NmapParser.parse(nmap_proc.stdout)
    except NmapParserException as e:
        print("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed

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
    report = do_scan("127.0.0.1", "-sV")
    if report:
        print_scan(report)
    else:
        print("No results returned")