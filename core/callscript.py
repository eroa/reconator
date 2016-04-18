import os
import nmap
import sys

targets = sys.argv[1]
ports = sys.argv[2]
text = "targets: " + targets + "\tports:" + ports
f = open("/tmp/callscript_{0}_{1}".format(targets, ports), "w")
f.write(text)
f.close()