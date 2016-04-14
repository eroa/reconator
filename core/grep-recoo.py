def scan:
    targetformat = str(targets)
    nmt = nmap.PortScanner()
    nmt.scan(hosts=targets, arguments="nmap -vv -Pn -A -sC -sS -T 4  -oN '/tmp/grep/nmap/%s.nmap'%s " % (
        targetformat, targetformat), sudo=True)
    nmtall = nmt.all_hosts()
    for host in nmtall:
        for proto in nmt[host].all_protocols():
            print('Protocol : {0}'.format(proto))
            lport = list(nmt[host][proto].keys())
            lport.sort()
            for port in lport:
                state = nmt[host][proto][port]
                print('port : {0}\tstate : {1}'.format(port, nmt[host][proto][port]))
                if "http" in str(state):
                    print "PORT:" + str(port) + "   gotcha (http via dict)!!!"
                    # formata = str(host)+":"+str(port)


if __name__ == "__main__":
    #    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    if os.path.isdir("/tmp/grep") == True:
        print "/tmp/grep exists"
    else:
        os.mkdir("/tmp/grep", 0777)
    if os.path.isdir("/tmp/grep/nmap") == True:
        print "/tmp/grep/nmap exists"
    else:
        os.mkdir("/tmp/grep/nmap", 0777)
    f = open(sys.argv[1], 'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
f.close()
