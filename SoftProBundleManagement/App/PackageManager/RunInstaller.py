import os
import csv
import datetime

from Settings import Settings

class Installer:


	def RunInstaller():
		print(" - Starting Installer")

		# Test files are available for download
		try:
			path = Settings.applicationDirectory+'\\CSVCodes\\BundlesLocations.csv'
			file = open(path)
			content = file.read()
			file.close()
		except:
			content = ""

		if content != "":
			
			Installer.Start()

		else:
			print(' - - No files to install ')

			# Print a blank CSV so it triggers reports to send
			today = datetime.datetime.today().strftime('%Y%m%d')
			filename =Settings.applicationDirectory + "\\Reports"+"\\"+today+"successfulinstalls.csv"
			with open(filename, "w") as csvfile:
				writer = csv.writer(csvfile)
				writer.writerow(['No Files to Install'])


	def Start():
		# Run C# Application
		path = Settings.applicationDirectory+"\\C#\\"+Settings.enviorment+"\\BundleInstaller\\"
		os.startfile(path +"BundleInstaller.exe")