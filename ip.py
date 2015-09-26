import os
localIPs = ''
externalIP = ''
curIP = ''
x = 0
numberOfIPs = 0
IPlist = []
p = os.popen('curl https://api.ipify.org')
while 1:
    IP = p.readline()
    if not IP: break
    externalIP = externalIP + IP
p = os.popen('nmap -sn 10.0.0.2/24')
while 1:
    IP = p.readline()
    if not IP: break
    localIPs = localIPs + IP
print(externalIP)
print(localIPs)
while(len(localIPs) > x):
    if(localIPs[x].isdigit() or localIPs[x] == '.'):
	curIP = curIP + localIPs[x]
    elif(localIPs[x] == '\n' and len(curIP) > 0 and curIP != '10.0.0.1' and (curIP[0] == '1' and curIP[1] == '0')):
	IPlist.append(curIP)
	curIP = ''
	numberOfIPs = numberOfIPs + 1
    x = x + 1
print(IPlist)
