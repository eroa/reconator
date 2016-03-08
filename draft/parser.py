import nmap


nm = nmap.PortScanner()
#2 = libnmap.
nm.scan(hosts='192.168.1.0/24', arguments='-sV -sT -nvvv --open -oN "/tmp/parse-dev"')
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
            print('host: %s\tport: %s\tstate : %s\tproto: %s' % (nm[host]['addresses'],port, nm[host][proto][port]['state'], nm[host][proto][port]['product']))



