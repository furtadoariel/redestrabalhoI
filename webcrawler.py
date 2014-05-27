import sys
import socket
from bs4 import BeautifulSoup
import requests

def webcrawler (deep, start_url):
	deep = deep
	lista = []
	listaimg = []
	i = 0
	j = 0
	r = requests.get(start_url)
	soup = BeautifulSoup(r.text)
	for d in xrange(deep):
		print d
		if d == 0:
			
			for a in soup.findAll('a',href=True):
				link = a['href']
				i += 1
				print link
				lista.append(link)
				#links = str(link).strip('[]').replace("http://", "").replace("u", "")
				link = link.replace("http://", "")
				links = str(link)
				print str(i) + ") " + str(links)
			for img in soup.findAll('img', src=True):
				imglink = img['src']
				j += 1
				print imglink
				listaimg.append(imglink)
		else:
			for lenght in xrange(len(lista)):
				#print lista[lenght]
				webcrawler(d, lista[lenght] )
				
				
			
	print "\n>> Total = %d \n" % i + "\n>> Total Imagens = %d \n" % j
	sys.exit()

	
		
			

url = raw_input(">> ")
webcrawler(2, url)
