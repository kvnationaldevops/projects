	

'''
Run From Main Application Folder

'''



import json
import time

import csv
import shutil
import datetime

from Settings import Settings
from tempfile import NamedTemporaryFile
from Reports.ReportManager import ReportManager


from WebInterface.Connection import Connection
from WebInterface.DownloadFile import DownloadFile


class Program:

	webData = { 'packages':[] }
	csvData = []

	auth = None

	def GetSoftProToken():
		# Pull last used authorization token
		auth_file = open('Documents\\auth.txt', 'r')
		auth = auth_file.read()
		auth_file.close()

		Program.auth = auth

	def PullCSVData():

		# Read and store Package Information 
		CSV_PackageInformation = []
		with open("BundlesRateTables.csv") as f:

			reader = csv.reader(f)
			
			for row in reader:

				Program.csvData.append(row[0])

		print("Count: " + str(len(Program.csvData)))




	def PullWebData():

		categories = ['Underwriter','State','National','Land%20Title']
		

		# Build list and append to webdata
		for category in categories:

			print(" - Pulling "+str(category))

			page = 0
			packages = []
			proceed = True

			while proceed:

				page+=1

				# Prepare Parameters for SP Docs call
				para1 = "?edition=select&orderBy=updated_at&orderByDir=desc&page="+str(page)
				para2 = "&perPage=100&search=&type="+str(category)+"&underwriter="
				parameters = para1 + para2

				# Use function from first section
				getWebData = Connection.CallSoftPro(parameters, Program.auth)

				# Convert to obj
				webData = json.loads(getWebData)

				# Update user on progress:
				totalpages = webData['lastPage']
				print(' - - Working on page '+str(page)+ ' of '+str(totalpages))

				# Iterate over each package 
				webPackages = webData['data']

				for webPackage in webPackages:
					packages.append(webPackage)
					
				# Pause before next call
				time.sleep(1)

				# Break Web Call Loop
				if len(webPackages) == 0 or page == totalpages:
					proceed = False

			for package in packages:
				if package not in Program.webData['packages']:
					Program.webData['packages'].append(package)

			print(" - - - Category Pakcage Count:" + str(len(packages)))



	bundleUpdatedAt = []

	def CompareCSVDataToWebData():

		for csvPackage in Program.csvData:

			nameLower = csvPackage.lower()

			for webPackage in Program.webData['packages']:

				webLower = webPackage['name'].lower()

				if webLower == nameLower:

					bnd = webPackage['name'] +","+ webPackage['updatedAt']
					Program.bundleUpdatedAt.append(bnd)

					print(webPackage['name'])
					print(webPackage['updatedAt'])
					print("--------")


	def printBundleUpdates():

		f = open('BundleUpdatedAtList.csv', 'w')

		# create the csv writer
		writer = csv.writer(f)

		# write a row to the csv file
		for bnd in Program.bundleUpdatedAt:
			writer.writerow([bnd])



Program.GetSoftProToken()
Program.PullCSVData()
Program.PullWebData()
Program.CompareCSVDataToWebData()
Program.printBundleUpdates()