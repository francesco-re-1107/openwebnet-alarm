from OpenWebNet import OpenWebNet

server = OpenWebNet("192.168.1.35","20000","12345")
res = server.stato_allarme()

#check result
if res == "*5*8*##": #alarm is enabled
    print "1"
elif res == "*5*9*##": #alarm is disabled
    print "0"