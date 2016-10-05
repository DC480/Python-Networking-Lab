import socket as sk						# To lazy to write socket.socket

host = "irc.freenode.net"					# IRC host to connect to
port = 6667							# Port to connect on

nick = "Repeater_Man"						# Nickname and Name for IRC

s = sk.socket()							# Create a socket and connect to host
s.connect((host, port))

buff = ""							# Buffer for recieving information

s.send("NICK %s\r\n" % nick)					# IRC protocol joining commands
s.send("USER %s * 8 : %s\r\n" % (nick, nick))
s.send("JOIN #dc480\r\n")

while 1:							# Run while true :)
	buff = buff+s.recv(1024)				# Recieve data from IRC server
	temp = str.split(buff, "\n")				# Split by lines and store for the rest for loop
	buff=temp.pop()						# Pop off latest data from buffer so its free for more next round

	for line in temp:					# Run loop for all lines in temp
		line = str.rstrip(line)				# Remove extra whitestpace from line
		line = str.split(line)				# Split line on spaces

		if(line[0] == "PING"):				# Check for IRC protocol ping command and send pong reply if present
			s.send("PONG %s\r\n" % line[1])		# Send pong reply with same number from ping
		if(line[1] == "PRIVMSG"):			# IRC command for sending message to specific channel or person
			size = len(line)			# This bot echos what you send it, so it need to know how long the text is 
			echo = ""
			for i in range(3, len(line)): 			# Increment over words in line variable
				echo += line[i] + " "		# Adds words and spaces between them to echo variable
				i = i + 1			# Increment loop
			echo.lstrip(":")			# Remove everything before the ':' character, since it isn't part of the message
			s.send("PRIVMSG #dc480 %s \r\n" % echo) # Send message to channel
