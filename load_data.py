#!/bin/python3
#
import os
import sys
import sqlite3

if len(sys.argv) != 2:
	print("Usage:ftp.py [year]")
	exit()

class datafile:
	def __init__(self,filename):
		data_file = open(filename,"r")
		self.lines = data_file.readlines()
	#---------------------------------------#
	# Method to read location from datafile #
	#---------------------------------------#
	def get_location(self):
		#
		location = self.lines[0].strip()
		#
		return location
	#---------------------------------------#
	# Method to read latitude from datafile #
	#---------------------------------------#
	def get_latitude(self):
		#
		latitude = self.lines[1].strip().split()[0]
		#
		return float(latitude)
	#----------------------------------------#
	# Method to read longitude from datafile #
	#----------------------------------------#
	def get_longitude(self):
		#		
		longitude = self.lines[1].strip().split()[1]
		#
		return float(longitude)
	#----------------------------------------#
	# Method to read elevation from datafile #
	#----------------------------------------#
	def get_elevation(self):
		#
		elevation = self.lines[1].strip().split()[2]
		#		
		return float(elevation)
	#------------------------------------------------#
	# Method to read meterlogical data from datafile #
	#------------------------------------------------#
	def get_meterodata(self):
		#---------------------------------------------------#
		# Initialize variables for Meterological Parameters #
		#---------------------------------------------------#
		self.year = []
		self.jday = []
		self.month = []
		self.day = []
		self.hour = []
		self.minute = []
		self.dt = []
		self.zen = []
		self.dw_solar = []
		self.uw_solar = []
		self.direct_n = []
		self.diffuse = []
		self.dw_ir = []
		self.dw_casetemp = []
		self.dw_dometemp = []
		self.uw_ir = []
		self.uw_casetemp = []
		self.uw_dometemp = []
		self.uvb = []
		self.par = []
		self.netsolar = []
		self.netir = []
		self.totalnet = []
		self.temp = []
		self.rh = []
		self.windspd = []
		self.winddir = []
		self.pressure = []
		#---------------------------------------------------------------#
		# Initialize Quality Control factor for Meterological Parameters #
		#---------------------------------------------------------------#
		self.dw_solar_qc = []
		self.uw_solar_qc = []
		self.direct_n_qc = []
		self.diffuse_qc = []
		self.dw_ir_qc = []
		self.dw_casetemp_qc = []
		self.dw_dometemp_qc = []
		self.uw_ir_qc = []
		self.uw_casetemp_qc = []
		self.uw_dometemp_qc = []
		self.uvb_qc = []
		self.par_qc = []
		self.netsolar_qc = []
		self.netir_qc = []
		self.totalnet_qc = []
		self.temp_qc = []
		self.rh_qc = []
		self.windspd_qc = []
		self.winddir_qc = []
		self.pressure_qc = []
		
		for line in self.lines[2:]:
			self.year.append(int(line.strip()[0:].split()[0]))
			self.jday.append(int(line.strip()[0:].split()[1]))
			self.month.append(int(line.strip()[0:].split()[2]))
			self.day.append(int(line.strip()[0:].split()[3]))
			#
			self.hour.append(int(line.strip()[0:].split()[4]))
			self.minute.append(int(line.strip()[0:].split()[5]))
			self.dt.append(float(line.strip()[0:].split()[6]))
			self.zen.append(float(line.strip()[0:].split()[7]))
			#	
			self.dw_solar.append(float(line.strip()[0:].split()[8]))
			self.dw_solar_qc.append(int(line.strip()[0:].split()[9]))
			#
			self.uw_solar.append(float(line.strip()[0:].split()[10]))
			self.uw_solar_qc.append(int(line.strip()[0:].split()[11]))
			#
			self.direct_n.append(float(line.strip()[0:].split()[12]))
			self.direct_n_qc.append(int(line.strip()[0:].split()[13]))
			#
			self.diffuse.append(float(line.strip()[0:].split()[14]))
			self.diffuse_qc.append(int(line.strip()[0:].split()[15]))
			#
			self.dw_ir.append(float(line.strip()[0:].split()[16]))
			self.dw_ir_qc.append(int(line.strip()[0:].split()[17]))
			#
			self.dw_casetemp.append(float(line.strip()[0:].split()[18]))
			self.dw_casetemp_qc.append(int(line.strip()[0:].split()[19]))
			#	
			self.dw_dometemp.append(float(line.strip()[0:].split()[20]))
			self.dw_dometemp_qc.append(int(line.strip()[0:].split()[21]))
			#	
			self.uw_ir.append(float(line.strip()[0:].split()[22]))
			self.uw_ir_qc.append(int(line.strip()[0:].split()[23]))
			#	
			self.uw_casetemp.append(float(line.strip()[0:].split()[24]))
			self.uw_casetemp_qc.append(int(line.strip()[0:].split()[25]))
			#
			self.uw_dometemp.append(float(line.strip()[0:].split()[26]))
			self.uw_dometemp_qc.append(int(line.strip()[0:].split()[27]))
			#	
			self.uvb.append(float(line.strip()[0:].split()[28]))
			self.uvb_qc.append(int(line.strip()[0:].split()[29]))
			#	
			self.par.append(float(line.strip()[0:].split()[30]))
			self.par_qc.append(int(line.strip()[0:].split()[31]))
			#	
			self.netsolar.append(float(line.strip()[0:].split()[32]))
			self.netsolar_qc.append(int(line.strip()[0:].split()[33]))
			#		
			self.netir.append(float(line.strip()[0:].split()[34]))
			self.netir_qc.append(int(line.strip()[0:].split()[35]))
			#	
			self.totalnet.append(float(line.strip()[0:].split()[36]))
			self.totalnet_qc.append(int(line.strip()[0:].split()[37]))
			#	
			self.temp.append(float(line.strip()[0:].split()[38]))
			self.temp_qc.append(int(line.strip()[0:].split()[39]))
			#	
			self.rh.append(float(line.strip()[0:].split()[40]))
			self.rh_qc.append(int(line.strip()[0:].split()[41]))
			#	
			self.windspd.append(float(line.strip()[0:].split()[42]))
			self.windspd_qc.append(int(line.strip()[0:].split()[43]))
			#	
			self.winddir.append(float(line.strip()[0:].split()[44]))
			self.winddir_qc.append(int(line.strip()[0:].split()[45]))
			#	
			self.pressure.append(float(line.strip()[0:].split()[46]))
			self.pressure_qc.append(int(line.strip()[0:].split()[47]))

		#print(year)
		
	def write_to_csv(self,outfile):
		outputfile = open(outfile, "w")
		outputfile.write("year,jday,month,day,hour,minute,dt,zen,dw_solar, \
uw_solar,direct_n,diffuse,dw_ir,dw_casetemp,dw_dometemp,uw_ir,uw_casetemp,uw_dometemp,uvb,\
par,netsolar,netir,totalnet,temp,rh,windspd,winddir,pressure,dw_solar_qc,uw_solar_qc,direct_n_qc,\
diffuse_qc,dw_ir_qc,dw_casetemp_qc,dw_dometemp_qc,uw_ir_qc,uw_casetemp_qc,uw_dometemp_qc,uvb_qc,par_qc,\
netsolar_qc,netir_qc,totalnet_qc,temp_qc,rh_qc,windspd_qc,winddir_qc,pressure_qc")
		for i in range(len(self.year)):
			string = year,jday,month,day,hour,minute,dt,zen,dw_solar, \
uw_solar,direct_n,diffuse,dw_ir,dw_casetemp,dw_dometemp,uw_ir,uw_casetemp,uw_dometemp,uvb,\
par,netsolar,netir,totalnet,temp,rh,windspd,winddir,pressure,dw_solar_qc,uw_solar_qc,direct_n_qc,\
diffuse_qc,dw_ir_qc,dw_casetemp_qc,dw_dometemp_qc,uw_ir_qc,uw_casetemp_qc,uw_dometemp_qc,uvb_qc,par_qc,\
netsolar_qc,netir_qc,totalnet_qc,temp_qc,rh_qc,windspd_qc,winddir_qc,pressure_qc
			outputfile.write()
		outputfile.close()
def write_to_json():
	pass
def write_to_sql():
	pass

data = datafile("bon15001.dat")
#print(dir(data))
#print(data.get_location())
#print(data.get_latitude())
#print(data.get_longitude())
#print(data.get_elevation())
print(data.get_meterodata())
data.write_to_csv("data.csv")
