#jangan recode ya, jangan juga sub youtube saya
import time, os, sys, time
from platform import system

#banner nih gan
print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
print(';;;;;;    Code by : Riskis7         ;;;;;')
print(';;;;;;    Youtube : Riskis7 Channel ;;;;;')
print(';;;;;;    Team : Risecurity Spider  ;;;;;')
print(';;;;;;    Tools : haxmav v.2.1      ;;;;;')
print(';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;')
                                                                    

                                           
#periksa domaain
def periksadom():                       
    os.system('nmap -A -T4'+  pers)
print '\033[92m [MEMERIKSA DOMAIN]'
pers = raw_input('masukan domain : ')
time.sleep(1)
periksadom()
exit
       

         
#scansubdomain
def scanbug():
    print
    os.system('nmap -p 80 --script dns-brute.nse ' + a)

def mnu():
    print '\033[92m [scan subdomain]'
                     
print
print '\033[92m [scan normal subdomain]'
a = raw_input('[Masukan domain utama  : ')
time.sleep(1)
scanbug()

#cekbug
def cekbug():
    os.system('curl -I ' + tes)

def mnu():
    print '\033[92m [CEK DOMAIN 200 OK]'

print                             
print '\033[92m [CEK DOMAIN 200 OK]'
tes = raw_input('masukan Domain : ')
time.sleep(1)
cekbug()
exit

#lihat_source_code      
def sourcecode():             
    os.system('curl -L ' + scode)

def mnu():
    print '\033[92m [CEK DOMAIN 200 OK]'

print                             
print '\033[92m [MELIHAT SOURCE CODE]'
scode = raw_input('masukan Domain : ')
time.sleep(1)
sourcecode()
exit

#save source code 
def savescode():
    os.system('curl -L -o' + savecode)                                 
def mnu():               
    print '\033[92m [S]'
                                      
print                               
print '\033[92m [save source code]'
savecode = raw_input('masukan xx.html/x.php/ dll (x.html https//google.com) : ')
time.sleep(1)
savescode() 
exit


#dirhunt 
def dirweb():              
    os.system('dirhunt'+  dir)     
                           
print '\033[92m [DIR WEBSITE NORMAL]'
dir = raw_input('masukan url website : ')
time.sleep(1)
dirweb()
exit
                

# coding is life by riskis7 - team : security spider.
#python system
















