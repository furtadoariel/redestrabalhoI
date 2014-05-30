#coding: utf-8

import sys, os
import socket
from bs4 import BeautifulSoup
from req import *
import thread


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
			url = start_url.replace("http://", "")
		elif start_url.startswith("https://"):
			url = start_url.replace("https://", "")
			
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
	"""
	pega o tamanho de lista para repartir em threads para realizar
	as próximas buscas
	"""
	
	for i in xrange(len(lista)):
		if deep == 0:
			return listaVisitados
		else:
			webcrawler(deep-1, lista[i], listaVisitados)
	sys.exit()
			
listaVisitados = []
#url = raw_input(">> ")
if(len(sys.argv)>1):
	url = sys.argv[2]
	prof = int(sys.argv[1])
lista = webcrawler(prof, url, listaVisitados)
