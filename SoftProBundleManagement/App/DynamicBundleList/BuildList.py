import os
import csv
import time

from Settings import Settings
from DocumentInterface.DocumentInterface import DocumentInterface


def BuildList():
	fileExists = CheckForCSVs()
	if not fileExists:
		DynamicBuild()

def CheckForCSVs():
	try:
		file = open(Settings.applicationDirectory+"\\CSVCodes\\DynamicBundleCodes.csv", 'r')
		content = file.read()
		file.close()
		if content != "":
			print(' - File Found')
			time.sleep(2)
			# Break Loop
			return True

	except Exception:
		return False


def DynamicBuild():

	# Run C# Application
	path = Settings.applicationDirectory+"\\C#\\"+Settings.enviorment+"\\DynamicCodes\\"
	os.startfile(path +"DynamicBundleList.exe")
	fileExists = False

	while not fileExists:
		print(' - awating CSV')
		time.sleep(3)
		fileExists = CheckForCSVs()