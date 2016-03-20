import nmap
import re
import multiprocessing
import subprocess
import csv

nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1', arguments='-sT -sV -T5 -vvv -oA /tmp/testgrep')
ncsv = nm.csv()
if 'http' in ncsv:
        print "victory"
else:
        print "zob"

