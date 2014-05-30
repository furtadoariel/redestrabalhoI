import socket
import sys
import urlparse

def req (site, porta): 
	
	so = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
	if so:
		partesUrl = site.split('/')
	else:
		print "erro ao ciar o socket"
	if(len(partesUrl) > 1):
		host = partesUrl[0]
		caminho = site.replace(host,"",1)
		print "Host: " + host
		print "Caminho: " + caminho
	else:
		host = site
		caminho = '/'

	ip = socket.gethostbyname (host)
	so = socket.create_connection((ip,porta))

	mensagem = "GET "+caminho+" HTTP/1.1\r\nHost: "+host+"\r\n\r\n"
	so.send ( mensagem ) #envia mensagem
	resposta = ''
	package = so.recv(4096)
	while package:
		resposta += package
		package = so.recv(4096)
	return resposta
