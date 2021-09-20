
import os
import datetime

from Settings import Settings

class ClearFiles:

	def ClearFiles():
		today = datetime.datetime.today().strftime('%Y%m%d')

		files = [
			"\\CSVCodes\\BundleProfileAssignments.csv",
			"\\CSVCodes\\DynamicBundleCodes.csv",

			"\\Reports\\ProgramComplete.csv"
			"\\CSVCodes\\BundlesLocations.csv",
			"\\CSVCodes\\ExcpetionCodes.csv",
			"\\Reports"+"\\"+today+"\\successfullinstalls.csv",
			"\\Reports\\"+today+"\\unsuccessfullinstalls.csv",
			"\\Reports\\c#Error.csv",
			"\\Reports"+"\\"+today+"\\EndorementTableComplete.csv"
		]
		for f in  files:
			root = Settings.applicationDirectory
			try:
				os.remove(root+f)
			except:
				pass

		try:
			downloads = "C:\\SoftProBundleManagement\\Downloads"+"\\"+today
			for file in os.listdir(downloads):
				if file.endswith(".bnd"):
					os.remove(downloads+"\\"+file)
		except Exception as e:
			pass


