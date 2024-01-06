#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/Xiyad.404.xd/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf xd32.so')
       
except:
    pass
os.system('rm -rf xd32.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1mCOMMAND OFF\033[1;37m ')
bit = platform.architecture()[0]
if bit == '32bit':
    if not os.path.isfile('xd32.so'):
        os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/xd32.cpython-311.so?raw=true -o xd32.so') 
        import xd32  
    else:
        import xd32
elif bit == '64bit':

    exit('\033[1;31m\n Sorry System or 64bit device not supported ')
    
    

