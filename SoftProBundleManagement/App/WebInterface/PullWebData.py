
import json
import time

from WebInterface.Connection import Connection
from WebInterface.DownloadFile import DownloadFile

class PullWebData:

	webData = { 'packages':[] }

	def PullWebData(search, category):

		if category == "":
			# iterate over all categories if no category is assigned
			categories = ['Underwriter','State','National','Land%20Title']
			print(' - - Pulling all categories web data')
		else:
			categories = [category]
			print(' - - Pulling specical web search: '+str(search)+ " "+ str(category))


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
				para2 = "&perPage=100&search="+str(search)+"&type="+str(category)+"&underwriter="
				parameters = para1 + para2

				# Use function from first section
				getWebData = Connection.CallSoftPro(parameters, Connection.auth)

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
				if package not in PullWebData.webData['packages']:
					PullWebData.webData['packages'].append(package)

			print(" - - - Category Pakcage Count:" + str(len(packages)))