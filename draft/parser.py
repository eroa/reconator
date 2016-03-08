import nmap


nm = nmap.PortScanner()
#2 = libnmap.
nm.scan(hosts='127.0.0.1', arguments='-sV -sT -nvvv --open -oN "/tmp/parse-dev"')
nm.get_nmap_last_output()
print(str(nm))
nm.get_nmap_last_output()
print(nm.csv())
hosts = nm.all_hosts()
#for host in nm[host].all_hosts():
for host in hosts:
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port: %s\tstate : %s\tproto: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['product']))



