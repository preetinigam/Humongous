import os
comIn = ''
curIP = ''
x = 0
numberOfIPs = 0
IPlist = []
p = os.popen('curl https://api.ipify.org')#this transfers data from that address, the address contains our external IP in plain text
while 1:
    IP = p.readline()
    if not IP: break
    comIn = comIn + IP
IPlist.append(comIn)
p = os.popen('nmap -sn 10.0.0.1/24')#this scans the LAN to find all IP addresses connected to the router
while 1:
    IP = p.readline()
    if not IP: break
    comIn = comIn + IP
while(len(comIn) > x):
    if(comIn[x].isdigit() or comIn[x] == '.'):#moves all the digits and periods to a the current possible IP
        curIP = curIP + comIn[x]
    elif(len(curIP) > 0 and curIP != '10.0.0.1' and (curIP[0] == '1' and curIP[1] == '0')):#makes sure that the digit is an IP and isn't the routers IP
        IPlist.append(curIP)
        curIP = ''
        numberOfIPs = numberOfIPs + 1
    elif(comIn[x] == '\n'):#This will reset the current IP string if a new line happens
        curIP = ''
    x = x + 1
print(IPlist)
