import nmap
import msfrpc

client =msfrpc.Msfrpc({})
client.login('msf','caillou')
# TODO msfrpc support
# def sshenum(ho, po):
#     try:
#         res = client.call('console.create')
#         console_id = res['id']
#     except:
#         print "Console create failed\r\n"
#         sys.exit()
#
#     cmd = """use auxiliary/scanner/snmp/snmp_loginset RHOSTS %srun """ % host_listclient.call('console.write',[console_id, cmd])


def do_scan(ipad):
    nmt = nmap.PortScanner()
    nmt.scan(hosts=ipad, arguments='-sV  -sS -T4 -nvvv -/tmp/msgrpcnamp',sudo=True)
    for host in nmt.all_hosts():
        for proto in nmt[host].all_protocols():
            print('Protocol : {0}'.format(proto))
            lport = list(nmt[host][proto].keys())
            lport.sort()
            for port in lport:
                state = nmt[host][proto][port]
                print('TCP port : {0}\tstate : {1}'.format(port, nmt[host][proto][port]))
                if "ssh" in str(state):
                    print "TCP PORT:" + str(port) + "   gotcha (http via dict)!!!"
                    # formata = str(host)+":"+str(port)
                    multProc(sshenum, str(host), str(port))
                    #multProc(callscript, str(host), str(port))
                    # (------------------------------------')
                elif "ssh" in str(state):
                    multProc(sshenum, str(host), str(port))
                elif "snmp" in str(state):
                    multProc(snmpenum, str(host), str(port))
                elif "ftp" in str(state):
                    multProc(ftpenum, str(host), str(port))
                elif "smb" in str(state):
                    multProc(smbenum, str(host), str(port))
                elif "tor" in str(state):
                    multProc(torenum, str(host), str(port))
                elif "ms-sql" in str(state):
                    multProc(mssqlenum, str(host), str(port))

                    # for host in nm.allhosts():
                    #     ...
                    #   e   if nm[host].has_tcp(9050):
                    #         ...
                    #     print "zob"


                    # TODO utiliser resultats nmu

    print('#######################  nmt host: {0} '.format(targetformat))

if __name__ == "__main__":
    #    print(" RECONATOR : usage " + %s + "ip_list.txt" % sys.argv[0])**
    if os.path.isdir("/tmp/msfrpc") == True:
        print "/tmp/msfrpc exists"
    else:
        os.mkdir("/tmp/msfrpc", 0777)
    if os.path.isdir("/tmp/msfrpc/nmap") == True:
        print "/tmp/msfrpc/nmap exists"
    else:
        os.mkdir("/tmp/msfrpc/nmap", 0777)
    f = open(sys.argv[1], 'r')
    for ip in f:
        report = multiprocessing.Process(target=do_scan, args=(ip,))
        report.start()
f.close()
