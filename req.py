import socket
import sys
import urlparse

site = ""
profundidade = 0

def req (site, porta): 
	so = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
	host = site
	caminho = "/"

	partesUrl = site.split(caminho)
	if(len(partesUrl) > 1):
		host = partesUrl[0]
		caminho = site.replace(host,"",1)
		print "Host: " + host
		print "Caminho: " + caminho

	ip = socket.gethostbyname (host)
	so.connect ((ip,porta))

	http = " HTTP/1.1\r\nHost: "
	get = "GET "
	barras = "\r\n\r\n"
	mensagem = get + caminho + http + host + barras
	so.send ( mensagem ) #envia mensagem

	resposta = ''
	repeticao = 0

	buff = so.recv(4096)
	for i in range (0,5):
		if (buff == ""):
			repeticao +=1
		resposta += buff
	so.close()
	return resposta

if (len(sys.argv) > 1):
	link = sys.argv[1]
	profundidade = int(sys.argv[2])

teste = req(link,80)
print teste
#print link
#print profundidade
