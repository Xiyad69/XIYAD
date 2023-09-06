#<\>!python3.11
#<\>coded by XIYAD
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/Xiyad.XD/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf xd.so')
except:
    pass
os.system('rm -rf xd.so')
os.system('git pull')
os.system('clear')
exit('\033[91;1m 
 .o88b.  .d88b.  .88b  d88. .88b  d88.  .d8b.  d8b   db d8888b.       .d88b.  d88888b d88888b 
d8P  Y8 .8P  Y8. 88'YbdP`88 88'YbdP`88 d8' `8b 888o  88 88  `8D      .8P  Y8. 88'     88'     
8P      88    88 88  88  88 88  88  88 88ooo88 88V8o 88 88   88      88    88 88ooo   88ooo   
8b      88    88 88  88  88 88  88  88 88~~~88 88 V8o88 88   88      88    88 88~~~   88~~~   
Y8b  d8 `8b  d8' 88  88  88 88  88  88 88   88 88  V888 88  .8D      `8b  d8' 88      88      
 `Y88P'  `Y88P'  YP  YP  YP YP  YP  YP YP   YP VP   V8P Y8888D'       `Y88P'  YP      YP      
                                                                                              
                                                                                               \033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('xd.so'):
        os.system('curl -L https://github.com/Xiyad69/XIYAD/blob/main/xd.cpython-311.so?raw=true -o xd.so') 
        import xd  
    else:
        import xd
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    

