import re


text = """
Please also install the ALTA package


While on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the ALTA forms


While on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the TLTA forms

After installation of these packages please install the Old Republic National package

After installation of this Underwriter package please also install the ALTA  and OTIRB packages

After installation of this Underwriter package please also install the ALTA package

After installation of this Underwriter package please also install the CLTA package

After installation of this Underwriter package please also install the DTIRB package

After installation of this Underwriter package please also install the NJRB package

After installation of this Underwriter package please also install the NMLTA package

After installation of this Underwriter package please also install the OTIRB package

After installation of this Underwriter package please also install the TIRSA package

After installation of this Underwriter package please also install the TLTA package

After installation of this Underwriter package please install the Fidelity Family - National package

After installation of this Underwriter package please install the Fidelity Family National package

After installation of this package please install the Fidelity Family - National package

Also if the Release Notes indicate that Endorsements have been added and/or changed or if this is your first install of this package please contact Support for assistance with the Endorsement lookup table configurationAfter installation of this Underwriter package please install the First National - National package

Also install the ALTA package

Also please install the 3 packages below

Also please install the NJRB package from the "Land Title" list of packages

If the Release Notes indicate that Endorsements have been added and/or changed or if this is your first install of this package please contact Support for assistance with the Endorsement lookup table configurationAfter installation of this Underwriter package please also install the Investors Title package

Please also install the ALTA package

Please also install the CLTA package

Please also install the Fidelity Family - National package

Please also install the LATISSO package

Please also install the NJRB package

Please also install the OTIRB package

Please also install the TIRBOP package

Please also install the TLTA package

While on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the ALTA and TLTA forms

While on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the ALTA forms

You will need to install the Underwriter Redirects package to complete redirects for the ALTA forms
  Also while on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the TLTA forms
 Also while on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the ALTA forms
 Also while on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the TLTA forms
 Please also install the OTIRB package
 While on the "Land Title" page you will need to install the Underwriter Redirects package to complete redirects for the ALTA forms
After installation of this Underwriter package please also install the ALTA and OTRIB packages
After installation of this Underwriter package please also install the ALTA package
After installation of this Underwriter package please also install the Agents Title - National package
After installation of this Underwriter package please also install the Agents Title National package
After installation of this Underwriter package please also install the AmTrust Title National package
After installation of this Underwriter package please also install the Attorneys' Title Guaranty Fund - National package
After installation of this Underwriter package please also install the CATIC - National package
After installation of this Underwriter package please also install the CATIC National package
After installation of this Underwriter package please also install the Fidelity Family - Alabama package
After installation of this Underwriter package please also install the First American - National package
After installation of this Underwriter package please also install the First American National package
After installation of this Underwriter package please also install the Investors Title National package
After installation of this Underwriter package please also install the Investors Title package
After installation of this Underwriter package please also install the LATISSO package
After installation of this Underwriter package please also install the North American National package
After installation of this Underwriter package please also install the Old Republic - National package
After installation of this Underwriter package please also install the Old Republic National package
After installation of this Underwriter package please also install the TLTA package
After installation of this Underwriter package please also install the Title Resources Guaranty National package
After installation of this Underwriter package please also install the Westcor - National package
After installation of this Underwriter package please also install the Westcor National package
After installation of this Underwriter package please also install the following packages: 1
After installation of this Underwriter package please install the Alliant National - National package
After installation of this Underwriter package please install the Alliant National package
After installation of this Underwriter package please install the AmTrust National package
After installation of this Underwriter package please install the Conestoga - National package
After installation of this Underwriter package please install the Fidelity Family - Arizona package
After installation of this Underwriter package please install the Fidelity Family - National package
After installation of this Underwriter package please install the Fidelity Family National package
After installation of this Underwriter package please install the Fidelity National package
After installation of this Underwriter package please install the First American National package
After installation of this Underwriter package please install the First National - National package
After installation of this Underwriter package please install the General Title - National package
After installation of this Underwriter package please install the North American - National package
After installation of this Underwriter package please install the North American National package
After installation of this Underwriter package please install the Old Republic - National package
After installation of this Underwriter package please install the Old Republic National package
After installation of this Underwriter package please install the Premier Land Title - National package
After installation of this Underwriter package please install the Real Advantage - National package
After installation of this Underwriter package please install the Security Title Guarantee Corp
After installation of this Underwriter package please install the Security Title National package
After installation of this Underwriter package please install the Stewart Title - National package
After installation of this Underwriter package please install the Stewart Title Guaranty -  National package
After installation of this Underwriter package please install the Title Resources - National package
After installation of this Underwriter package please install the Title Resources Guaranty Co
After installation of this Underwriter package please install the Title Resources National package
After installation of this Underwriter package please install the WFG National package
After installation of this Underwriter package please install the Westcor - National package
After installation of this Underwriter package please install the Westcor National package
After installation of this package please also install the ALTA and TLTA packages
After installation of this package please also install the Fidelity Family - South Carolina package
After installation of this package please install the Investors Title - National package
After installation of this package please install the Investors Title National package
After installation of this package please install the North American National package
After installation of this package please install the Old Republic National package
After installation of this package please install the Security Title Guarantee Corp
If the Release Notes indicate that Endorsements have been added and/or changed or if this is your first install of this package please contact Support for assistance with the Endorsement lookup table configurationAfter installation of this Underwriter package please also install the First American National package
NoneAfter installation of this Underwriter package please also install the ALTA package
NoneAfter installation of this Underwriter package please also install the Agents Title National package
NoneAfter installation of this Underwriter package please also install the CATIC National package
NoneAfter installation of this Underwriter package please also install the First American National package
NoneAfter installation of this Underwriter package please also install the Old Republic - National package
NoneAfter installation of this Underwriter package please also install the Old Republic National package
NoneAfter installation of this Underwriter package please also install the Westcor National package
NoneAfter installation of this Underwriter package please install the Alliant National - National package
NoneAfter installation of this Underwriter package please install the Alliant National package
NoneAfter installation of this Underwriter package please install the Fidelity Family - National package
NoneAfter installation of this Underwriter package please install the North American National package
NoneAfter installation of this Underwriter package please install the Old Republic National package
NoneAfter installation of this Underwriter package please install the Premier Land Title - National package
NoneAfter installation of this Underwriter package please install the Security Title Guarantee Corp
NoneAfter installation of this Underwriter package please install the Stewart Title Guaranty -  National package
NoneAfter installation of this package please also install the Fidelity Family - South Carolina package
NoneAfter installation of this package please also install the First American National package
NoneAfter installation of this package please install the North American National package
NoneNoneAfter installation of this Underwriter package please also install the Title Resources Guaranty National package
NoneNoneAfter installation of this Underwriter package please install the WFG National package
NoneNoneNoneAfter installation of this Underwriter package please also install the AmTrust Title National package
NonePlease also install the Attorneys Title - National package
Please also install the Attorneys Title - National package
Please also install the Fidelity Family - California package
Please also install the Fidelity Family - Colorado package
Please also install the Fidelity Family - Connecticut package
Please also install the Fidelity Family - Florida package
Please also install the Fidelity Family - Georgia package
Please also install the Fidelity Family - Illinois package
Please also install the Fidelity Family - Indiana package
Please also install the Fidelity Family - Kansas package
Please also install the Fidelity Family - Louisiana package
Please also install the Fidelity Family - Maryland package
Please also install the Fidelity Family - Massachusetts package
Please also install the Fidelity Family - Minnesota package
Please also install the Fidelity Family - Missouri package
Please also install the Fidelity Family - National package
Please also install the Fidelity Family - Nebraska package
Please also install the Fidelity Family - Nevada package
Please also install the Fidelity Family - New Jersey package
Please also install the Fidelity Family - Ohio package
Please also install the Fidelity Family - Rhode Island package
Please also install the Fidelity Family - South Carolina package
Please also install the Fidelity Family - Texas package
Please also install the Fidelity Family - Utah package
Please also install the Fidelity Family - Virginia package
Please also install the Fidelity Family - West Virginia package
Please also install the Fidelity Family -Wisconsin package
Please also install the First American - National package
Please also install the Old Republic National package
Please also install the Title Resources - National package
Please also install the Title Resources Guaranty -  National package
Please also install the Title Resources Guaranty National package
Please also install the Title Resources National package
Please also install the Westcor National package
Please install the Fidelity Family - Virginia package
"""


s = text.split('\n')




allRequests = []
for text in s:

	if text != "":

		#
		# From testing this regex only returned one
		# item in each list.
		# The expression continues on this assumption.
		# If the len <> 1 throw execption.
		exp = '(install the [\w\W]+ package)'
		isolatedRequest = re.findall(exp, text)

		if len(isolatedRequest) == 1:
			formattedRequest = isolatedRequest[0].split("the ")[1]

			if formattedRequest not in allRequests:
				allRequests.append(formattedRequest)

		else:
			# Please install the 
			# "Security Title Guarantee Corp" 
			# Or similar is primary expection
			# print("*"*50)
			# print(text)
			# print("*"*50)
			pass

#
# Regular expression for potential Requests
#
# Initalize all regex strings then compare
# each regex against text.
# Elif the results, so if it can only match one category.
# Every request will end in an array.
#
singlePackage = '[\w]+ package'
singlePackageWithCarrier = '[\w\W]* - [\w\W]* package'
twoPackages = '[\w\W]* and [\w\W]*package'

allSinglePackage = []
allSinglePackageWithCarrier = []
allTwoPackages = []
notCategorized = []

for request in allRequests:

	if re.match(singlePackage, request):
		allSinglePackage.append(request)

	# Must come before Carrier
	elif re.match(twoPackages, request):
		allTwoPackages.append(request)

	elif re.match(singlePackageWithCarrier, request):
		allSinglePackageWithCarrier.append(request)

	else:
		notCategorized.append(request)




#
# After categorized, return assumed
# required packages
#
# print("*"*50 +'\n single')
# for request in allSinglePackage:
# 	package = request.split(" ")[0]
# 	if package != '3' and package != "following":
# 		print(package)


# print("*"*50 +'\n carrier')
# for request in allSinglePackageWithCarrier:

# 	#
# 	# Tests from Underwriters indicate that 
# 	# All results are either 
# 	# "Fedlity Family" or National Packages
# 	#

# 	if "Fidelity Family" in request:
# 		package = request.split(" - ")[1].replace('package', "")
# 		#print(package)

# 	elif 'National package' in request:
# 		package = request.split(' -')[0]
# 		print(package)
# 	else:
# 		# Inject Error Handling Here
# 		pass


# print("*"*50 +'\n allTwoPackages')
# for request in allTwoPackages:
# 	packages = request.split('and')
# 	for pkg in packages:
# 		package = pkg.replace('package', '').strip()
# 		print(package)

print("*"*50 +'\n notCategorized')
nopCategorizedSorted = sorted(notCategorized)
for request in nopCategorizedSorted:

	#
	# Strong Majority are National PKGS
	#
	if "National package" in request:
		package = request.replace("National package", '')
		#print(package)
	else:
		# Unhandeled at moment 
		# Produces 3 unique cases at this time
		print(request)



"""














			















file_object = open('text.txt', 'r')
raw = file_object.read()

text = raw.replace('-', "")
text = raw.replace(',', "")


sentances = text.split('.')



#
# The majority of additional information is
# seperate packages that need installation.
# "Browse all" and "install the" identify the
# syntax and work flow for most additional installs.
#
# Begin here by seperating them into categories
#
# Then on each result, there are regexs to pull
# the key words to automate the flow.
#
uniqueSentances = []
browseAll = []
alsoInstall = []
for sentance in sentances:

	lowercase = sentance.lower()

	#
	# Add releaseNotesBool
	#


	if "browse all" in lowercase:
		if sentance not in browseAll:
			browseAll.append(sentance)

	elif "install the" in lowercase:
		if sentance not in alsoInstall:
			alsoInstall.append(sentance)
	else:
		if sentance not in uniqueSentances:
			uniqueSentances.append(sentance)		




def FilterBrowseAll(text):

	# Modify Quotations to be uniform
	text = text.replace('“', '"').replace('”','"')

	# Isolate the Categorey Filter
	FilterCategory =  text.split('"')[1]

	#
	# Multiple package installs are possible
	# Isolate package name with Regex
	# Then concat with a "-" delimiter
	pkgRe = '([a-z]+ package)'
	packages = re.findall(pkgRe, text.lower())
	packagesString = ""
	for pkg in packages:
		if "update" not in pkg and "underwriter" not in pkg:
			packagesString+=pkg+'-'

	CategoryAndPackages = FilterCategory +"|"+ packagesString

	return CategoryAndPackages






print("*"*20)
print("------ Browse All ------")
browseAllSorted = sorted(browseAll)
for sentance in browseAllSorted:
	filterBrowseAll = FilterBrowseAll(sentance)
	print(filterBrowseAll)



print("*"*20)
print("------ Also Install ------")
alsoInstallSorted = sorted(alsoInstall)
for sentance in alsoInstallSorted:
	print(sentance)

print("*"*20)
print("------ Uniquie Sentances ------")
uniqueSentancesorted = sorted(uniqueSentances)
for sentance in uniqueSentancesorted:
	print(sentance)

# pattern = r'(Please also install the)[\s]*[A-Za-z]*'
# #[\s]+[A-Za-z0-9]+[\s]+' #(From the Browse All page)
# #'[A-Za-z]+'

# expression = re.findall(pattern, text)
# print(expression[0])

# print(len(expression))




#
# Logging and Notifications
#
'''

Email report after running
- errors included
- Way to search Doc Trees


Log table written to 
(within Select)(keep information consolidated)(Simple)
(Links to logs)
Outside Select
-Log File / Detail Email



'''

"""

