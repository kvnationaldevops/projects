import sys
import pathlib

class Settings:

	applicationDirectory = ""
	enviorment = ""

	def SetEnviorment(arguments):
		### Default Env
		if len(arguments) != 2:
			print("Please Select an Enviorment to run: [dev] [devops] [prod]")
			exit()
			# print(" - - Runing Default env: Devops ")
			# DocumentInterface.enviorment = 'devops'
			# Installer.enviorment = 'devops'
			
		else:
			### Check for proper ENV Args
			env = sys.argv[1].lower()	
			if env != "dev" and env != "devops" and env != "prod":
				print("Please Select an Enviorment to run: [dev] [devops] [prod]")
				exit()

			print()
			print('Enviorment Set at: '+ env)
			Settings.enviorment = env

		applicationDirectory = pathlib.Path(__file__).parent.parent.resolve()
		Settings.applicationDirectory = str(applicationDirectory)