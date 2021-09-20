import os
import csv
import time
import json
import zipfile
import datetime
import requests
from Settings import Settings
from WebInterface.Connection import Connection
from Reports.ReportManager import ReportManager



class DownloadFile:

	today = datetime.datetime.today().strftime('%Y%m%d')
	downloadPath = "C:\\SoftProBundleManagement\\Downloads\\"
	#Settings.applicationDirectory+"\\Downloads\\"


	def DownloadFile(webName, webDownloadUrl):
		try:

			# Create PKG Folder if missing
			path = DownloadFile.downloadPath+DownloadFile.today
			if not os.path.exists(path):
				os.makedirs(path)

			# Download File
			token = "?access_token="+Connection.auth.split(" ")[1]
			r = requests.get(webDownloadUrl+token)

			# Save to folder, pull filename and date
			filename = r.headers.get('content-disposition').split('filename=')[1]
			open(path+"\\"+filename, 'wb').write(r.content)

			ReportManager.report[webName]['isDownloadSuccessFull'] = "True"
			ReportManager.report[webName]['downloadError'] = str(None)

			# Unzip file and note the contents
			DownloadFile.UnzipAndAppendFilesToCSV(webName, path, filename)

		except Exception as e:
			ReportManager.report[webName]['isDownloadSuccessFull'] = "False"
			ReportManager.report[webName]['downloadError'] = str(e)




	def UnzipAndAppendFilesToCSV(webName, zipPath, zipName):

		try:
			downloadsPath = DownloadFile.downloadPath+DownloadFile.today
			# print(downloadsPath)
			# print(Settings.applicationDirectory)
			# input()

			bundlesIncluded = []
			temp = zipPath+"\\temp"
			with zipfile.ZipFile(zipPath+"\\"+zipName, 'r') as zip_ref:
				zip_ref.extractall(temp)

			for file in os.listdir(temp):
				if file.endswith(".bnd"):

					try:
						# Note Bundle Name in report
						bundlesIncluded.append(file)

						# Move Bundle File out of temp
						os.rename(temp+"\\"+file, downloadsPath+"\\"+file)

						# Note in CSV Bundle Location 			
						DownloadFile.AddToCSV(downloadsPath+"\\"+file)

					except Exception as e: # Bundle already in location
						# print(e)
						# print(1)
						# input()
						ReportManager.report[webName]['isDownloadSuccessFull'] = "False"
						ReportManager.report[webName]['downloadError'] = str(e)

				else:		
					# Clean File
					os.remove(temp+"\\"+file)

			# Remove Orginal Zip			
			os.remove(zipPath+"\\"+zipName)

			ReportManager.report[webName]['zipContents'] = bundlesIncluded

		except Exception as e:
			# print(e)
			# print(2)
			# input()
			ReportManager.report[webName]['isDownloadSuccessFull'] = "False"
			ReportManager.report[webName]['downloadError'] = str(e)


	def AddToCSV(filelocation):

		filename = Settings.applicationDirectory+'\\CSVCodes\\BundlesLocations.csv'  # Package--Dates.csv'
		with open(filename, 'a') as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow([filelocation])