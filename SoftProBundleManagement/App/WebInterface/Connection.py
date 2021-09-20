import time
import requests

from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from Settings import Settings
from Reports.ReportManager import ReportManager
from DocumentInterface.DocumentInterface import DocumentInterface


class Connection:

	auth = None

	def GenerateConnection():

		auth = DocumentInterface.GetSoftProToken()

		call = Connection.CallSoftPro('', auth)

		# Check for a clean connection
		if call == '{"error":"auth.forbidden","message":"Forbidden. You need to be authenticated to do that."}':
			auth = Connection.GenerateNewConnection()

		Connection.auth = auth


	def GenerateNewConnection():

		#
		# Generating New credentials uses selenium to login and access the local storage
		# Once the token is stripped to the essentials, it is store in the auth.txt and returned
		# for current session use. 
		#

		#
		# Selenium will require a Chrome Drive download for production
		# It will need to match the Chrome version type
		# It will also need to update the path
		#

		userName, pw  = DocumentInterface.GetSoftProLogin()

		path = Settings.applicationDirectory+"\\SeleniumDriver\\chromedriver"
		driver = webdriver.Chrome(path)
		driver.get("https://my.softprocorp.com/signin")

		time.sleep(1)

		userNameElem = driver.find_element_by_id("userName")
		userNameElem.send_keys(userName)
		passwordElem = driver.find_element_by_id("Password")
		passwordElem.send_keys(pw)

		time.sleep(2)
		
		passwordElem.send_keys(Keys.RETURN)
	
		time.sleep(2)

		# Execute script to pull auth from local storage
		try:
			local = driver.execute_script("return window.localStorage['persist:softpro_documents_production_root']")	# This KeyValPair updated?	
			clean = local.replace("\\", "").split('{"token":"')[1].split('","error":')[0]
		except:
			local = driver.execute_script("return window.localStorage['persist:softpro_documents_development_root']")	# This KeyValPair updated?	
			clean = local.replace("\\", "").split('{"token":"')[1].split('","error":')[0]





		# Format the token
		updatedAuth = 'Bearer '+ clean

		# Store new Key
		DocumentInterface.SetSoftProToken(updatedAuth)

		driver.close()

		return updatedAuth


	def CallSoftPro(parameters, auth):

		headers = {
			'accept': 'application/json',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'authorization': auth,
			'content-type': 'application/json',
			'origin': 'https://docs.softprocorp.com',
			'referer': 'https://docs.softprocorp.com/',
			'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
			'sec-ch-ua-mobile': '?0',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-site',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
		}

		return Connection.GetRequest( "https://docs-api.softprocorp.com/api/packages"+parameters, headers)


	def GetRequest(url, headers):

		r = requests.get(url, headers=headers)

		return r.text





