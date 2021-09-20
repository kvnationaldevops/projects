import os
import csv
import time
import datetime
import smtplib, ssl
from os.path import basename
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from pathlib import Path
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders

from Settings import Settings
from PackageManager.RunInstaller import Installer

class ReportManager:

	report = {}
	CSVReports = []

	def Error(error):
		to = ['tmeyer@kvnational.com']
		dateAndTime = str(datetime.datetime.now())
		subject = "SoftPro Bundle Management Automation Error"
		message = """
		    	The following error has occured at """+dateAndTime+"""
		    </p>
		    <p>
		    Error:"""+error
		attachements = []
		ReportManager.SendNotification(to, subject, message, attachements)
		
		print("a fatal error has occured")
		print("program quitting")
		exit()


	def SendReports():

		reportLocations =[
			Settings.applicationDirectory+"\\CSVCodes\\DynamicBundleCodes.csv",
			Settings.applicationDirectory+"\\CSVCodes\\ExcpetionCodes.csv",
			Settings.applicationDirectory+"\\CSVCodes\\BundlesLocations.csv",
		]

		for location in reportLocations:
			try:
				ReportManager.CSVReports.append(location)
			except Exception as e:
				pass

		today = datetime.datetime.today().strftime('%Y%m%d')
		subject = today + ' Bundle Report'
		message = 'Todays Bundle Report CSVs attached.'

		# send report
		ReportManager.SendNotification(['tmeyer@kvnational.com'], subject, message, ReportManager.CSVReports)



	def PrintReport():

		allReportsPrinted = False

		while not allReportsPrinted:
			allReportsPrinted = ReportManager.AllReportsPrinted()


		today = datetime.datetime.today().strftime('%Y%m%d')
		path = Settings.applicationDirectory+'\\Reports\\'
		filename = today+'BundleReport.csv'
		csvFilePath = os.path.join(path, filename)

		with open(csvFilePath, 'w') as csvfile:

			fieldnames = [
				'bundleName',
				'isUpdateRequired',
				'softProLastUpdated',
				'webLastUpdated',
				'isOnSoftProWebsite',
				'isDownloadSuccessFull',
				'downloadError',
				'downloadedAsDependency',
				'downloadNotes',
				'downloadNotesUnique' ,
				'downloadNotesOrginalNote',
				'unique',
				'orginalNote',
				'zipContents'
			]

			# Headers
			writer = csv.writer(csvfile, delimiter=",")
			writer.writerow(fieldnames)

			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			for key,value in ReportManager.report.items():
				writer.writerow(value)



	def AllReportsPrinted():

		time.sleep(3)
		today = datetime.datetime.today().strftime('%Y%m%d')

		try:
			# Chck for c# errors
			location = Settings.applicationDirectory+"\\Reports\\c#Error.csv"
			if os.path.isfile(location):
				Installer.Start()
				os.remove(location)	
		except Exception as e:
			print("Restart Error - Report manager")
			print(str(e))	



		try:
			successfulInstallations = Settings.applicationDirectory+"\\Reports"+"\\"+today+"\\successfullinstalls.csv"
			file = open(successfulInstallations, 'r')
			content = file.read()
			file.close()

			ReportManager.CSVReports.append(successfulInstallations)

			try:
				unsuccessfulInstallations = Settings.applicationDirectory+"\\Reports\\"+today+"\\unsuccessfullinstalls.csv"
				file = open(unsuccessfulInstallations, 'r')
				content = file.read()
				file.close()
				ReportManager.CSVReports.append(unsuccessfulInstallations)
			except:
				pass

			return True
		
		except Exception as e:

			print(' - awaiting bundles report')
			return False




	def SendNotification(to,subject, messageText,attachements):

		sender_email = "noreply@kvnational.com"
		receiver_email = "tmeyer@kvnational.com"
		password = ''

		message = MIMEMultipart("alternative")
		message["Subject"] = subject
		message["From"] = sender_email
		message["To"] = receiver_email

		dateAndTime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

		html = """
		<html>
		  <body>
		    <p>
		    	"""+dateAndTime+"""
		    	"""+messageText+"""
		    </p>
		  </body>
		</html>
		"""
		part2 = MIMEText(html, "html")
		message.attach(part2)


		for path in attachements:
			try:
				part = MIMEBase('application', "octet-stream")
				with open(path, 'rb') as file:
					part.set_payload(file.read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition',
				                'attachment; filename={}'.format(Path(path).name))
				message.attach(part)

			except:
				print(' - - Send Notifications Error - Path missing: '+ str(path))

		# Create secure connection with server and send email
		context = None# ssl.create_default_context()
		with smtplib.SMTP("kvnational-com.mail.protection.outlook.com", 25 ) as server:
		    #server.login(sender_email, password)
		    server.sendmail(
		        sender_email, receiver_email, message.as_string()
		    )