
import nmapparser
import libnmap
import nmap
import csv

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser

nm = libnmap.process.NmapProcess(targets='127.0.0.1', options='-sT -sV --open -nvvv')
rc = nm.run()
#nm.is_successful()
#nm.summary()

nmstd = nm.stdout
print nmstd
nmparsed= libnmap.parser.NmapParser.parse(nmstd)
for s in nmparsed.hosts:
    print s
for s in nmaparsed;
    print s
rnm = nmrx.get_raw_data()
print rnm


