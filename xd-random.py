#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdrdg-open https://facebook.com/Xiyad.404.xdrd/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf xdrd.so')
        os.system('rm -rf xdrd32.so')
except:
    pass
os.system('rm -rf xdrd.so')
os.system('rm -rf xdrd32.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('xdrd.so'):
        os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/xdrd.cpython-311.so?raw=true -o xdrd.so') 
        import xdrd  
    else:
        import xdrd
elif bit == '32bit':
	if not os.path.isfile('xdrd32.so'):
		os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/xdrd32.cpython-311.so?raw=true -o xdrd32.so') 
		import xdrd32  
	else:
		import xdrd32 
   # exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    