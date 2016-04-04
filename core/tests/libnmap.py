import nmap

nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1', arguments='-sV -sT -oN "/tmp/libnmap.{0}.format(hosts)"')
ncsv = nm.csv()
nlast = nm.get_nmap_last_output()
ndict = nm.analyse_nmap_xml_scan()

print('----------------------------------------------------')
print "CSV:"
print(type(ncsv))
print ncsv


print('----------------------------------------------------')
print "XML last"
print(type(nlast))
print nlast


print('----------------------------------------------------')
print "Dico"
print(type(ndict))
print ndict
# nmdict.itervalues()
# nmdict.viewkeys()
# nmdict.viewitems()
# nmdict.values()
# %hist
