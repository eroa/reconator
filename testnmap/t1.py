#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import nmap
import libnmap

if __name__ == "__main__":
    nm = nmap.PortScanner()
    print " RECONATOR : usage " + sys.argv[0] + "ip_list.txt"
    list = open(sys.argv[1])
    for ip in list:
        nm.command_line("nmap -sP %s " % (str(ip))
        print "host :" + (ip,nm._scan_result())


