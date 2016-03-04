#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import nmap
import libnmap

if __name__ == "__main__":
    nm = nmap.PortScanner()
    iplist = sys.argv[1]
    print " RECONATOR : usage reconator.py ip_list.txt"
    list = open(iplist)
    for ip in list:
        nm.command_line("nmap -sP %s " % (str(ip)))
        print "host :" + (ip,nm._scan_result())


