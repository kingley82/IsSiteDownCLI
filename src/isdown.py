#Copyright 2022 KingleyStudio Licensed under the Apache License, Version 2.0 (the «License»);

import os
import datetime
try:
	import requests
	from requests.exceptions import ConnectTimeout, ConnectionError
except:
	os.system("pip install requests -q --upgrade")

def define_resp(code):
	if code >= 200 and code < 300: return "Site WORKING!"
	if code >= 300 and code < 400: return "Site redirected!"
	if code >= 400 and code < 500: return "Site doesn't exist or URL is incorrect!"
	if code >= 500 and code < 600: return "Site is DOWN!"
	if code == 1020: return "Site protected by Cloudflare, check failed!"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
		   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}

dom = input("Site domain without protocol >> ")
html = input("Save HTML into file? [y/n] >> ")

print("Sending request")
try:
	r = requests.get(f"https://{dom}", headers=headers)
except ConnectTimeout:
	print("Request doesn't sended\n")
	print("- RESULTS -")
	print(f"Status code - 0")
	print("Cannot connect to this site (Time is up). Maybe, site blocked in your country. If no, try later.")
except ConnectionError:
	print("Request doesn't sended\n")
	print("- RESULTS -")
	print(f"Status code - 0")
	print("Cannot connect to this site (Host dropped connection). Maybe, site blocked in your country. If no, try later.")
else:
	print("Request sended\n")
	print("- RESULTS -")
	print(f"Status code - {r.status_code}")
	print(define_resp(r.status_code))
	if html.lower() in ["y", "yes"]:
		date = str(datetime.datetime.now().strftime("%d-%m-%Y--%H-%M-%S"))
		with open(date+".html", "w") as f: f.write(r.text)
		print(f"Writed HTML into {date}.html")

input()
