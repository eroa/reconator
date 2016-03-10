import nmap



print('----------------------------------------------------')
# Read output captured to a file
# Example : nmap -oX - -p 22-443 -sV 127.0.0.1 > nmap_output.xml

with open("./nmap_output.xml", "r") as fd:
    content = fd.read()
    nm.analyse_nmap_xml_scan(content)
    print(nm.csv())
