import re
import json

from Reports.ReportManager import ReportManager

class DependencyAnalyzer():

	#
	# Currenly Uniques sentance 13 expections on 620+ entries
	# And some are duplicates
	# Unhandled exceptions on bottom
	#

	def __init__(self, note):
		self.note = note

	def DownloadNotesAnalyzer(self):

		formattedNote = self.note.replace('-', "").replace(',', "").replace(r'\n',"")
		sentances = formattedNote.split('.')

		"""
		DependencyManager analysis the download notes 
		for information reguarding dependencies
		
		
		Main Outcomes:
		* Isolating Dependencies Names
			- Noting Endorsements
			- Isolating unique sentances
	
		"""

		uniqueSentances = []
		DownloadInstructions = []
		endorsed = False
		underwriterRedirect = False

		for sentance in sentances:

			lowercase = sentance.lower()

			twoPackages = self.TwoPackages(sentance)

			# Common Redirect Required Phrase
			if 'install the underwriter redirects package' in lowercase:
				# Only "Land Title" accounted for
				underwriterRedirect =  True


			# Eliminate Common Sentances
			blacklist = self.Blacklist(lowercase)
			if blacklist:
				pass # do nothing

			# Common phrase indicating important other installations
			elif "do not install unless you are also installing" in lowercase:
				pass # Common sentance to pass on, no useful informaiton in it

			# Common download instructions phrase
			elif "browse all" in lowercase:
				
				## How to pull Category from previous instructions?
				DownloadInstructions.append(sentance)


			elif 'endorsement' in lowercase:
				endorsed = True

			else:
				if sentance != "":
					uniqueSentances.append(sentance)


		#
		# Run individual sequences and return results
		#

		dependencies = []
		for sentance in DownloadInstructions:
			dependencies.append( self.DownloadInstructions(sentance) )


		output = {
			'orginalNote': self.note,
			'underwriterRedirect': underwriterRedirect,
			'endorsement': endorsed,
			'dependencies':dependencies,
			'unique':uniqueSentances
		}

		return output



	def DownloadInstructions(self, text):

		instruction = {
			'category':None,
			'packages':[]
		}

		# Modify Quotations to be uniform
		text = text.replace('“', '"').replace('”','"')

		# Isolate the Categorey Filter
		# Typical syntax would be ' Browse From the "National" ' 
		# Splitting on '"' seperates the sentance on its category 
		# EX:
		# ' the "National" page' => ['the', 'National','page']
		# 	[1]=> National
		instruction['category'] =  text.split('"')[1]

		# Multiple package installs are possible
		# Isolate package name with Regex
		# Then concat with a "-" delimiter
		pkgRe = '([a-z]+ package)'
		packages = re.findall(pkgRe, text.lower())
		for pkg in packages:
			if "update" not in pkg and "underwriter" not in pkg:
				formatPkg = pkg.replace('package',"").strip()
				instruction['packages'].append(formatPkg)

		return instruction


	def TwoPackages(self, sentanceLower):
		if '2 packages within this download' in sentanceLower:
			return True
		if 'filter again for' in sentanceLower:
			return True

		return False

	def Blacklist(self, sentanceLower):

		if sentanceLower == ' national package':
			# Example:
			# "Please install the Security Title Guarantee Corp. National package."
			# Error from Corp(.)
			return True

		if sentanceLower == ' please ensure that both are installed':
			return True

		if sentanceLower == ' 2' or sentanceLower == ' 3':
			return True

		# Conatins Checking 
		if "install the" in sentanceLower:
			return True

		if "this is not a standalone package" in sentanceLower:
			return True

		if "there are 2 additional packages that need to be downloaded" in sentanceLower:
			return True

		if 'please contact support for assistance with this package as it requires additional packages to be installed' in sentanceLower:
			return True 

		if '2 packages within this download' in sentanceLower:
			return True

		if 'Please contact support for additional details on possible lookup table changes' in sentanceLower:
			return True

		alsoInstall = 'the [\w\W]* package also needs to be installed'
		if re.match(alsoInstall, sentanceLower):
			return True


		return False


'''
	## Important and unhandled ##

	" Also while on the \"Land Title\" page you will need to install the Underwriter Redirects package to complete redirects for the ALTA forms",
	
	## May not be handled properly by Browse All
	"Underwriter Redirects need to also be installed. From the Browse All page, select "Land Title" and download the Underwriter Redirects package to complete redirects for the ALTA forms"
	
	These 3 come one after the other
	"Please note, the Underwriter has replaced the Commitment, Owners Policy and Loan Policy with a blank schedule"
	If you do not currently have their standard exceptions in your UW template or lookup tables you may contact support to request those'
	' This was done to allow you more flexibility from order to order when issuing your Owners Policies'

	' Then filter again for OTIRB**
	Currently in Two Packages

	['\nAlso after install confirm that the lookup code for your Attorneys’ Title Fund Services contact is set to AF', ' If it is currently set to something other than AF contact the support team at support@softprocorp', 'com as further rate changes and lookup table changes may be required', '']


'''