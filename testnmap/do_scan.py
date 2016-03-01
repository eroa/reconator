#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libnmap
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException

import subprocess
import multiprocessing
from multiprocessing import Process, Queue

def do_scan(targets, options):
    parsed = None
    nmproc = NmapProcess(targets, options)
    rc = nmproc.run()
    if rc != 0:
        print("nmap scan failed: {0}".format(nmproc.stderr))
    print(type(nmproc.stdout))

    try:
        parsed = NmapParser.parse(nmproc.stdout)
    except NmapParserException as e:
        print("Exception raised while parsing scan: {0}".format(e.msg))

    return parsed



