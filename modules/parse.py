from testnmap.libnmap import NmapParser
from testnmap.libnmap import NmapProcess

nm = NmapProcess("127.0.0.1, scanme.nmap.org")
nm.run()

nmap_report = NmapParser.parse(nm.stdout)

for scanned_hosts in nmap_report.hosts:
    print(scanned_hosts)
