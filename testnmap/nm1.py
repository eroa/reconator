#!/usr/bin/env python2
import nmap
import sys

ips = sys.argv[1]
nm = nmap.PortScanner()
nm.scan(hosts=str(ips) , arguments = '-sV -sT -Pn -nvvv -oN "/tmp/nm1"')
#nm.command_line()
si = str(nm.scaninfo())
sys.stdout.write(si)
all_hosts = str(nm.all_hosts())
print(str(nm.all_hosts()))
#results = str(nm.csv())
print(str(nm.csv()))




# if __name__ == "__main__":
    # nmapS(sys.argv[1])
