#!/bin/python3
import ftplib
import sys
from pathlib import Path
from datetime import datetime
import os

if len(sys.argv) != 2:
	print("Usage:ftp.py [year]")
	exit()

locations = ["bon"]
yr = int(sys.argv[1])
yr_list = list(range(yr,yr+1,1))

print(yr_list)
for year in yr_list:
	for location in locations:
		start = datetime.now()
		source = "./data/radiation/surfrad/" + location + "/" + str(year) + "/"
		destination = "data/radiation/surfrad/" + location + "/" + str(year) + "/"
		print("Connecting to ftp.gml.noaa.gov")
		ftp = ftplib.FTP("ftp.gml.noaa.gov")
		ftp.login("anonymous", "ftplib-example-1")
		print("Connected to ftp.gml.noaa.gov")
		ftp.cwd(source)
		files = ftp.nlst()
		strs = 'mkdir -p '+ destination
		print(strs)
		print("Done with creating " + destination)
		print("Downloading datasets...")
		for file in files:
			local_start = datetime.now()
			#print("Creating " + strs)
			strs = "mkdir -p "+ destination
			os.system(strs)
			ftp.retrbinary(f'RETR {file}', open(str(Path(destination) / file), 'wb').write)
			local_end = datetime.now()
			local_lapse = str(local_end - local_start)
			global_lapse = str(local_end - start)
			print("Downloading " + file + " from " + source + " to " + destination + "/"+ file+ " | Elapsed time : " + local_lapse + "s | Total Elapsed time:" + global_lapse)
		ftp.quit()
