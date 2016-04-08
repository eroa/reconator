import libnmap
import libnmap.process
import libnmap.parser
import libnmap.objects
from libnmap.process import NmapProcess, NmapTask
from libnmap.objects import NmapService, NmapHost, NmapReport
from libnmap.parser import NmapParser, NmapParserException


#Scanner TODO
nm = libnmap.process.NmapProcess(targets='127.0.0.1',arguments='-sV -sT -oN "/tmp/libnmap"')
rc= nm.run()
f = open("/tmp/libnmap.xml", 'w' )
f.write(nm.stdout)
f.close()


#Parser TODO
rep = libnmap.parser.NmapParser.parse_fromfile('/tmp/libnmap.xml')
print("nmap {0}/{1} hosts up".format(rep.hosts_up, rep.hosts_total))

