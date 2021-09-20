import os
import sys
import csv
import json

from DynamicBundleList import BuildList
from DocumentInterface.ClearFiles import ClearFiles
from WebInterface.Connection import Connection
from Reports.ReportManager import ReportManager
from PackageManager.RunInstaller import Installer
from PackageManager.PackageManager import PackageManager
from DocumentInterface.DocumentInterface import DocumentInterface
from EndorsementTable.EndorsementTable import EndorsementTable

from Settings import Settings


class Manager:
	"""
		1 - Dynamically Generate a list of packages in Select

		2 - Compare the download dates to the Soft Pro documents website
			- Pull ALL information from 
			- Download package if outdated
			- Download Required Dependencies.
				- Dependencies download recursively

		3 - Reinstall the packages into Select 

		4 - Updates all Endorsement Tables

		Notes:
		- All file management is currently located in: C:\\Softpro Bundle Management
	"""

	def SetEnviorment():

		print()
		print('Setting Enviorment --------------------------')
		Settings.SetEnviorment(sys.argv)

	def ClearFiles():
		print()
		print('Cleaning Files')
		ClearFiles.ClearFiles()
		print('Files Cleaned--------------------------------')

	def BuildBundleList():
		print()
		print('Dynamically Building Select Bundle List-----')
		BuildList.BuildList()

	def DownloadPackages():
		print()
		print('Generating Connection to SoftPros website----')
		Connection.GenerateConnection()

		print('Reading Bundle CSV Data----------------------')
		DocumentInterface.PullCSVData()

		print()
		print('Starting Online Package Manager--------------')
		PackageManager.ClassManager()

	# Wait until 9p
	def InstallUpdatedPackages():
		print()
		print('Starting Reinstallation Script----------------')
		Installer.RunInstaller()

	def PrintReport():
		print()
		print('Printing report')
		ReportManager.PrintReport()
		ReportManager.SendReports()
		print('Reports Complete-----------------------------')

	def UpdateEndorsementTables():
		print()
		print("Starting Endorsement Table Updater -----------")
		EndorsementTable.UpdateEndorsementTables()
		EndorsementTable.SendReport()
		print('Endorsement Tables Updated')




# try:
print('Starting Application')	
Manager.SetEnviorment()
Manager.ClearFiles()
Manager.BuildBundleList()
Manager.DownloadPackages()
Manager.InstallUpdatedPackages()
Manager.PrintReport()
# Manager.UpdateEndorsementTables()
print()
print("*"*50)
print("Program Complete")
# except Exception as e0001:
# 	# ReportManager.SendNotification(
# 	# 	"tmeyer@kvnational.com", 
# 	# 	"Bundle Updater Error ",
# 	# 	 str(e0001),
# 	# 	 []
# 	# )
# 	print(str(e0001))


# ReportManager.SendNotification(
# 		"tmeyer@kvnational.com", 
# 		"test ",
# 		 str(DocumentInterface.enviorment),
# 		 []
# 	)
# sys.exit(0)
# exit()