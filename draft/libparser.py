#!/usr/bin/env python
import nmap
import libnmap

from libnmap.parser import NmapParser
from libnmap.process import NmapProcess

nm = NmapProcess(targets="127.0.0.1", options="-sV -sT -oA /tmp/libnmap", safe_mode=False)
rs = nm.run()

if nm.rs == 0:
    print(nm.stdout)
else:
    print(nm.stderr)


