import nmap



nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1', arguments='-sS -sV  -oN "/tmp/grepsimple"', sudo='True')

nlast = nm.get_nmap_last_output()
ndict = nm.analyse_nmap_xml_scan()

ndict.itervalues()
a = ndict.viewvalues()
print "***********************"
print "***********************"
print str(a)
for host in nm.all_hosts():
    print host
    print('----------------------------------------------------')
    for proto in nm[host].all_protocols():
        print('proto: {0}'.format(proto))
        lport = list(nm[host][proto].keys())
        print('----------------------------------------------------')
        print lport
        lport.sort()
        for port in lport:
            print type(nm[host][proto][port])
            state = str(nm[host][proto][port])
            print('proto: {0}\tstate: {1})'.format(port, nm[host][proto][port]))
            lstate = list(nm[host][proto][port].keys())
            lstate.sort()
            print "###########" + lstate + "#############"""
            # lsta
            for ar in lstate:
                if "cpe" in ar:
                    print 'victory: {0}'.format(ar[0, 3, 7])
#TODO grep deeper dict

