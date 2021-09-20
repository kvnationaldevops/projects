
import os
import time
import datetime

from Settings import Settings
from Reports.ReportManager import ReportManager
from PackageManager.RunInstaller import Installer


class EndorsementTable:

	def UpdateEndorsementTables():

		try:
			# Run C# Application
			path = Settings.applicationDirectory+"\\C#\\"+Settings.enviorment+"\\EndorsementTable\\"
			os.startfile(path +"EndorsementTableUpdater.exe")

		except Exception as e:
			now = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
			messageText = "Date Time: " + now + "\nError: Failed to Run"
			ReportManager.SendNotification("tmeyer@kvnational.com", "Error: Endorsement Table Updater", messageText,[])

	def SendReport():

		today = datetime.datetime.today().strftime('%Y%m%d')
		file = Settings.applicationDirectory+"\\Reports"+"\\"+today+"\\EndorementTableComplete.csv"

		fileExists = os.path.isfile(file) 

		while not fileExists:
			print("Awaiting Endorsements Report")
			time.sleep(5)
			fileExists = os.path.isfile(file)

		print("File Found")
		messageText = ""
		ReportManager.SendNotification("tmeyer@kvnational.com", "Endorsement Table Updater Report ", messageText,[file])