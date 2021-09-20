import os
import json
import time
import zipfile
import requests
import datetime

from WebInterface.Connection import Connection
from WebInterface.PullWebData import PullWebData
from WebInterface.DownloadFile import DownloadFile

from Reports.ReportManager import ReportManager

from DocumentInterface.DocumentInterface import DocumentInterface

from .DependencyAnalyzer import DependencyAnalyzer

class PackageManager:

	"""

		1 - PullWebData stores all underwriter data in webData
				- This is used to search for web information without needing
				to call softpro recurrently 

		2 - CompareCSVDataToWebData determines if bundles needs an update
				- Items requiring updates are stored updatesRequired[]
				- Others are added to report manager as not to be duplicated

		3 - RunUpdates() pulls and downloads all packages needing updating.
				- The Dependency Updater runs recursively

	"""

	updatesRequired = []
	requiredDependencies = {}

	def ClassManager():

		print(' - Pulling WebData')
		PullWebData.PullWebData('','')

		print()
		print('Comparing CSV Data for Updates')
		PackageManager.CompareCSVDataToWebData()

		print()
		print('Running Initial Updates')
		print()
		PackageManager.RunUpdates(False)


	################################################################## Core Function

	def CompareCSVDataToWebData():

		for csvPackage in DocumentInterface.csvData:

			nameLower = csvPackage['name'].lower()

			PackageManager.GenerateReportItem(nameLower)
			ReportManager.report[nameLower]['softProLastUpdated'] = csvPackage['lastUpdated']

			# Search webData
			# Remove pkg from list for shor list seraches?
			for webPackage in PullWebData.webData['packages']:

				webLower = webPackage['name'].lower()

				if webLower == nameLower:

					#### Additional Checks for edge cases:
					importFailureList = ['fanh', 'staz', 'ftut', 'fnwv', 'stoh', 'wfnj']

					tempBlock = []#['fail','clta','cwnj','stnj','stna']
				
					noDownloads = [ # Downloads different than expected packages whem the package is opened
						'ftnh', 
						'ftmi', # FT => FF
						'ftpa', #### Potentail mistake
						'cwmi', # FFMI
						'cwnh', # FFNH / SPlite National / SPliteNewhampshire
						'fnsc' # Release notes only
					 ]

					if webLower in importFailureList or webLower in noDownloads or webLower in tempBlock:
						print('Passing known package failue: ' + webLower)
						continue
					#### Edge Cases complete
					

					ReportManager.report[nameLower]['isOnSoftProWebsite'] = True
					ReportManager.report[nameLower]['webLastUpdated'] = webPackage['updatedAt']

					SelectDate = PackageManager.CreateDateObjectFromSelect(csvPackage['lastUpdated'])
					SPWeb = PackageManager.CreateDateObjectFromSPWeb(webPackage['updatedAt'])

					# Generate a list of packages needing updating
					if SelectDate < SPWeb or not csvPackage['lastUpdated']:

						ReportManager.report[nameLower]['isUpdateRequired'] = True
						PackageManager.updatesRequired.append(webPackage)

					else:
						ReportManager.report[nameLower]['isUpdateRequired'] = False

				else:
					# Bundle Not found on Website
					ReportManager.report[nameLower]['isOnSoftProWebsite'] = False


	################################################################## Helper Functions

	def GenerateReportItem(nameLower):

		report = {
				'bundleName': nameLower,
				'softProLastUpdated': None,
				'isOnSoftProWebsite': None,
				'webLastUpdated':None,
				'isUpdateRequired': None,
				'isDownloadSuccessFull':None,
				'downloadError': None,
				'downloadedAsDependency': None,
				'downloadNotes':None,
				'downloadNotesUnique' : None,
				'downloadNotesOrginalNote' : None,
				'zipContents':None
			}

		if nameLower not in ReportManager.report:
			ReportManager.report[nameLower] = report

	def CreateDateObjectFromSelect(date):
		if date == "":
			return datetime.date(1984,1,1)
		date = date.split(" ")[0]
		day = date.split('/')[1]
		month = date.split('/')[0]
		year = date.split('/')[2]
		return datetime.date(int(year),int(month),int(day))

	def CreateDateObjectFromSPWeb(date):
		date = date.split(" ")[0]
		day = date.split('-')[2]
		month = date.split('-')[1]
		year = date.split('-')[0]
		return datetime.date(int(year),int(month),int(day))


	################################################################## Core Function

	def RunUpdates(dependencyState):

		if len(PackageManager.updatesRequired) > 0:

			remainingPackages = len(PackageManager.updatesRequired)

			while remainingPackages > 0: # For loop misses iterations without

				count = 0
				print()
				print("Downloading Package Reequirements")

				for webPackage in PackageManager.updatesRequired:

					count+=1
					print(" - Downloading: "+str(count)+"/"+str(remainingPackages))

					# Remove Item from Array
					PackageManager.updatesRequired.remove(webPackage)

					# Ensure Package is instanticated in report
					nameLower = webPackage['name'].lower()
					PackageManager.GenerateReportItem(nameLower)

					# inalize common variables
					webName = webPackage['name'].lower()
					webUpdatedAt = webPackage['updatedAt']
					webDownloadUrl = webPackage['downloadUrl']
					webDownloadNotes =  webPackage['downloadNotes']

					# Report
					ReportManager.report[webName]['downloadedAsDependency'] = dependencyState
					ReportManager.report[webName]['downloadNotes'] = webDownloadNotes
					
					# Download current package and store to package state
					DownloadFile.DownloadFile(webName, webDownloadUrl)

					# Identify additional dependcies
					if webDownloadNotes != None:

						# Initalize class with 'web notes' parameter and record analyzer output
						dependencyAnalyzerInfo =  DependencyAnalyzer(webDownloadNotes)
						dependencyInfo = dependencyAnalyzerInfo.DownloadNotesAnalyzer()

						# Report Unique, Unhandled sentances in analyser
						if len(dependencyInfo['unique']) > 0:
							ReportManager.report[webName]['unique'] = dependencyInfo['unique']
							ReportManager.report[webName]['orginalNote'] = dependencyInfo['unique']

						# Store dependcies for updating
						PackageManager.StoreDependencies(dependencyInfo['dependencies'])
		
				remainingPackages = len(PackageManager.updatesRequired)

			# Restart Recursion
			PackageManager.RunDependencyUpdates()
			PackageManager.RunUpdates(True)


	################################################################## Helper Functions

	def StoreDependencies(dependencies):

		for dependency in dependencies:
							
			category = dependency['category']

			try:
				# Create instances of categories for dependiences
				reqDepCategory = PackageManager.requiredDependencies[category]
			except:
				PackageManager.requiredDependencies[category] = []
				reqDepCategory = PackageManager.requiredDependencies[category] 

			for package in dependency['packages']:
				reqDepCategory.append(package.lower()) 


	def RunDependencyUpdates():
		print()
		print("Iterating Dependcies")

		PackagesAccountFor = 0
		UninstalledPackages = 0

		# Ensure the dependency is not already in system
		for category,dependencyPackages in PackageManager.requiredDependencies.items():
			
			for dependencyPackage in dependencyPackages:

				# add to Package Manager Updates Required list if not
				if dependencyPackage in ReportManager.report:
					PackagesAccountFor += 1

				else:
					# Add the webpackage, not just the name
					webPackage = PackageManager.GetWebPackage(category, dependencyPackage)

					if webPackage:
						PackageManager.updatesRequired.append(webPackage)
						UninstalledPackages+=1

					else:
						print(' - webpackage missing')
						print(dependencyPackage, category)

		# Reset Dependency Storage
		PackageManager.requiredDependencies = {}

		# Print New Count of item and update
		print(" - - Dependeices Accouted for: " +str(PackagesAccountFor) )
		print(" - - New Installations: " + str(UninstalledPackages))


	def GetWebPackage(category, dependencyPackage):

		for package in PullWebData.webData['packages']:
			if package['name'].lower() == dependencyPackage.lower():
				return package
				break

		return False