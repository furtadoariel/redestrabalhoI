#coding: utf-8
import sys, os
import socket
from bs4 import BeautifulSoup
from req import *
from threading import Thread

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
		  Caso haja o http:// no inicio da string, é retirado com a função replace
		  Adiciona o link inicial à lista de links visitados
		  Faz a requisição http passando o link e a porta
		usando a biblioteca BEAUTIFULSOUP, converte a pagina para texto
		para então percorrer o texto em busca de links e imagens
		"""
		url = start_url.replace("http://", "")
		listaVisitados.append(start_url)
		
		r = req(url, 80)
		pag = BeautifulSoup(r)
		for a in pag.findAll('a',href=True):
			link = a['href']
			lista.append(link)
		for img in pag.findAll('img', src=True):
			imglink = img['src']
			listaimg.append(imglink)
	else:
		return
	for i in xrange(len(lista)):
		print lista[i]
	for i in xrange(len(listaimg)):
		print listaimg[i]	
		
	sys.exit()
prof = 0
url = ""
listaVisitados = []
if(len(sys.argv)>1):
	url = sys.argv[2]
	prof = sys.argv[1]
lista = webcrawler(prof, url, listaVisitados)
