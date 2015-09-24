import os
p = os.popen('curl https://api.ipify.org',"r")
while 1:
    externalIP = p.readline()
    if not externalIP: break
p = os.popen('nmap -sn 10.0.0.2/24')
while 1:
    localIPs = p.readline()
    if not localIPs: break
print(localIPs)
