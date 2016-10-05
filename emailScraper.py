import requests
import re

page = requests.get(raw_input('Enter page to grab emails from: ')).text		# Get web page text
emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", page)	# Use regex to search page for emails

print emails									# Print found emails
