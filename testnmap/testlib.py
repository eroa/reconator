from testnmap.libnmap import NmapProcess

nm = NmapProcess("ssh.uhart.fr", options = "-sV -T4 ")
rc =nm.run()

if nm.rc == 0:
    print nm.stdout
else:
    print nm.stderr
