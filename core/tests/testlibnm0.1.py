
import nmapparser
import libnmap
import nmap
import csv
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser

nm = NmapProcess(targets='127.0.0.1', options='-sT -sV --open -nvvv')
rc = nm.run()
nm.is_successful()
#nm.summary()
nm.stdout
nmr = nm.stdout
print nmr
nmrx = NmapParser.parse(nmr)
for s in nmrx.hosts:
    print s
for s in nmrx.hosts_total:
    print si
rnm = nmrx.get_raw_data()
print rnm


