
import os

from Settings import Settings

class t:
	def test():


		files = [
			# r"C:\SoftProBundleManagement\Reports\20210913BundleReport.csv",)

			"\\Reports\\20210913BundleReport.csv"

		]
		for f in  files:
			
			r = open(Settings.applicationDirectory+f, "r").read()
			print(r)
			x = input()
