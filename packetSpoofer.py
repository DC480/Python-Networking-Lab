import logging
from scapy.all import *

logging.getLogger('scapy').setLevel(1)				# Tell scapy to fuck off with all its warnings

source = raw_input('Enter IP to spoof: ')			# Get all the data for the spoofed packet
destination = raw_input('Enter Destination IP: ')		
sport = raw_input('Enter Source Port: ')
dport = raw_input('Enter Destination Port: ')
data =raw_input('Enter Data: ')					# Whateva you want

packet = Ether() / IP(src=source, dst=destination) / UDP(sport=int(sport), dport=int(dport)) / 	data
								# Cant break this ^ up so onto more lines :/ This builds the packet and stores it

interface = raw_input('Enter interface to send packet over: ')	# Get the interface to use

sendp(packet, iface=interface)					# Send packet over interface
