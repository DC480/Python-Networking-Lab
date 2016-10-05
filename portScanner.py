import socket

targetIP    = raw_input("Enter host IP to scan: ")		# Store host to connect to

for port in range(1,1025):  					# For loop for port range to scan
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Socket for TCP port connections
    result = sock.connect_ex((targetIP, port))			# Store success/failure from trying to connect to target port
    if result == 0:						# If connection was successful, report port as open
        print "Port %s: Open" % port
    sock.close()						# Close socket cause this port is done
