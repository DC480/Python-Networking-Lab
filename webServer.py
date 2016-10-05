import socket as sk					# To lazy to type socket over and over

HOST = ''						# Blank host since were binding a socket 
PORT = 8080						# Port to listen on

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)		# Make TCP socket
s.setsockopt(sk.SOL_SOCKET, sk.SO_REUSEADDR, 1) 	# Set socket options for bind socket	
s.bind((HOST, PORT))					# Bind socket
s.listen(10)						# Recieve up to 10 conncurrent connections
print 'Serving HTTP on port %s ...' % PORT		# Print message on successful start
while True:						# Client handling loop
	try:						# Dont die horribly on errors
		client = s.accept()[0]			# Recieve client and store for handling
		request = client.recv(1024)		# Store client sent connection data
		print request				# Print client data

		response = "HTTP/1.1 200 OK\r\n\r\n
		Hello, World!\r\n\r\n"			# Set web page variable				
		client.sendall(response)		# Send page
		client.close()				# Close connection
	except:						# Ignore death threats
		pass					# (aka erros :( )
