
import nmapparser
import libnmap
import nmap
import csv

from libnmap.process import NmapProcess
from libnmap.parser import NmapParser
from libnmap.objects.service import NmapService
nm = libnmap.process.NmapProcess(targets='127.0.0.1', options='-sT -sV --open -nvvv')
rc = nm.run()
nmout =  nm.stdout
print nmout
succes  = nm.is_successful()
print "succes {0}".format(succes)
pars = NmapParser(nmout)

serv = NmapService(nm)
nm.

nmstd = nm.stdout
print nmstd
nmparsed= libnmap.parser.NmapParser.parse(nmstd)
for s in nmparsed.hosts:
    print s
for s in nmaparsed;
    print s
rnm = nmrx.get_raw_data()
print rnm


