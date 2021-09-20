import csv
import shutil
import datetime

from Settings import Settings
from tempfile import NamedTemporaryFile
from Reports.ReportManager import ReportManager

class DocumentInterface:
	
	csvData = None

	def PullCSVData():

		#
		# Read and store Package Information 
		CSV_PackageInformation = []
		with open( Settings.applicationDirectory+'\\CSVCodes\\DynamicBundleCodes.csv') as f:

			fields = ['packageName', 'lastUpdated', 'notes']
			reader = csv.DictReader(f, fieldnames=fields)
			
			# Skip Headers
			next(reader)

			for row in reader:

				# Ensure the line exists
				if row['packageName'] != "" and row['packageName'] != None:

					# Create & append Info Obj
					CSV_PackageInformation.append({
						'name' : row['packageName'],
						'lastUpdated' : row['lastUpdated'],
						'notes': row['notes']
					})

		DocumentInterface.csvData = CSV_PackageInformation
		print(" - CSV Items: " + str(len(DocumentInterface.csvData)))


	def GetSoftProToken():
		# Pull last used authorization token
		auth_file = open(Settings.applicationDirectory+'\\App\\Documents\\auth.txt', 'r')
		auth = auth_file.read()
		auth_file.close()

		return auth


	def SetSoftProToken(updatedAuth):
		auth_file = open(Settings.applicationDirectory+'\\App\\Documents\\auth.txt', 'w')
		auth_file.truncate()
		auth_file.write(updatedAuth)
		auth_file.close()


	def GetSoftProLogin():
		#'kvconnect@kvnational.com'
		username = 'tmeyer@kvnational.com'
		pw_file = open(Settings.applicationDirectory+'\\App\\Documents\\pw.txt', 'r')
		pw = pw_file.read()
		pw_file.close()

		return username, pw

