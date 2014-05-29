import socket
import sys
import urlparse

def req (site, porta): 
	get = "Get "
	http = " HTTP/1.1\r\nHost: "
	barra = "\r\n\r\n"
	
	so = socket.socket ( socket.AF_INET, socket.SOCK_STREAM ) #Cria o objeto socket TCP
	if so:
		partesUrl = site.split('/')#Retira separador
	else:
		print "Erro ao ciar o Socket"
	if(len(partesUrl) > 1):
		host = partesUrl[0]#Recebe primeiro link
		caminho = site.replace(host,"",1)
		print "Host: " + host
		print "Caminho: " + caminho
	else:
		host = site
		caminho = '/'

	ip = socket.gethostbyname (host)#Recebe ip
	so = socket.create_connection((ip,porta))#Conecta o socket com o ip e a porta 80, do http

	mensagem = get+caminho+http+host+barra
	so.send ( mensagem ) #envia mensagem

	resposta = ''
	package = so.recv(4096)
	while package:
		resposta += package
		package = so.recv(4096)
	return resposta
