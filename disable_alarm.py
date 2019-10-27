from OpenWebNet import OpenWebNet

#create a server
server = OpenWebNet("192.168.1.35","20000","12345")

#send a standard request to the server 
#the command that disable alarm is *5*9##
#but OpenWebNet does not allow you to enable and disable alarm with a command by default.
#But it can be done with a workaround, defining an auxiliary command in the alarm control unit and make it executing *5*9##
#for example define: *9*7*9## -> *5*9##
res = server.request("*9*7*9##")