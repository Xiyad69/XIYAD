#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
os.system('xdg-open https://facebook.com/Xiyad.XD/')
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf xnx.so')
except:
    pass
os.system('rm -rf xnx.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('xnx.so'):
        os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/xnx.cpython-311.so?raw=true -o xnx.so') 
        import xnx
    else:
        import xnx
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    
