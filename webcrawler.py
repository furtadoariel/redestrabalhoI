#coding: utf-8

import sys, os
import socket
from bs4 import BeautifulSoup
from req import *
from downloadContent import *
import threading


def webcrawler (deep, start_url, listaVisitados):
	"""
	Aqui se cria as listas para inserir os links e imagens
	"""
	lista = []
	listaimg = []
	"""
	Verifica-se se a url passada como parametro esta na lista de
	urls visitadas
	Caso nao esteja ele continua
	"""
	if (start_url not in listaVisitados):
		"""
		Passo a passo
		  Caso haja o http:// ou https:// no inicio da string, é retirado com a função replace
		  Adiciona o link inicial à lista de links visitados
		  Faz a requisição http passando o link e a porta
		usando a biblioteca BEAUTIFULSOUP, converte a pagina para texto
		para então percorrer o texto em busca de links e imagens
		"""
		if start_url.startswith("http://"):
			url = start_url.replace("http://","")
		elif start_url.startswith("https://"):
			url = start_url.replace("https://","")
			
			
#################################################################################

		lista.append(url)
		listaVisitados.append(url)		
		r = req(url, 80)
		pag = BeautifulSoup(r)
		
#################################################################################



		for a in pag.findAll('a',href=True):
			link = a['href']
			lista.append(link)
		for img in pag.findAll('img', src=True):
			imglink = img['src']
			listaimg.append(imglink)
	else:
		return
	
	for i in xrange(len(lista)):
		if deep == 0:
			break			
		else:
			webcrawler(deep-1, lista[i], listaVisitados)

	for link in lista:
		try:
			thread = threading.Thread(target = contentDownload, args = (link, ))
			thread.start()
			print link
			if(link+1 > len(lista)):
				break
			thread2 = threading.Thread(target = contentDownload, args = (link+1, ))
			thread2.start()
			link = link+1
			print link
			
		except Exception, ex:
			print ex
	for linkimg in listaimg:
		try:
			thread = threading.Thread(target = contentDownload, args = (linkimg, ))
			thread.start()
			if(link+1 > len(listaVisitados)):
				break
			thread2 = threading.Thread(target = contentDownload, args = (linkimg+1, ))
			thread2.start()
			link = link+1
			thread3 = threading.Thread(target = contentDownload, args = (linkimg+1, ))
			thread3.start()
			link = link+1
			thread4 = threading.Thread(target = contentDownload, args = (linkimg+1, ))
			thread4.start()
			link = link+1
		except Exception, ex:
			print ex
			

	sys.exit()
			
listaVisitados = []
#url = raw_input(">> ")

if(len(sys.argv)>1):
	url = sys.argv[2]
	prof = int(sys.argv[1])
#lista = webcrawler(prof, url, listaVisitados)

webcrawler(prof, url, listaVisitados)
