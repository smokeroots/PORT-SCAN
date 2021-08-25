########################################
# ->         Smoke Root             <- #
# ->                                <- #
# ->          PORT SCAN             <- #
# ->          DEVELOPED             <- #
# ->             IN                 <- #
# ->           PYTHON               <- #
# ->                                <- #
# ->       DATE: 08/21/2021         <- #
########################################

import socket

ip = raw_input("ENTER IP OR ADDRESS: ") # IP EX: 192.0.0.1 > ADDRESS EX: www.google.com

ports = []
count = 0

while count < 10:
    ports.append(int(raw_input("INSERT PORT: ")))
    count += 1


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print str(port) + " -> OPEN PORT"
    else:
        print str(port) + " -> CLOSE PORT"

print "SCAN FINISHED"