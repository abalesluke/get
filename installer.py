import os, sys

ui = os.getuid()
try:
	if sys.platform != 'linux':
		print('sorry installer is for linux only!')
		exit(0)
	elif ui != 0:
		print('Error! detected! user is not root')
		print('Error! Try Excuting it with sudo')
	else:
		os.system('chmod 777 get')
		os.system('mv get /usr/bin/')
		print('installation complete!')
		print('you can now run "get" command anywhere in your terminal')
except:
	print('err')
