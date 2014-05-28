import socket
import sys
import urlparse
	
def req ( site, porta ): 

	try:
		so = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

	except socket.error:
		print "Erro"
		sys.exit ( )	

	host = site
	caminho = "/"

	partesUrl = site.split("/")
	if(len(partesUrl) > 1):
		host = partesUrl[0]
		caminho = site.replace(host,"",1)
		print "Host: " + host
		print "Path: " + caminho

	try:
		ip = socket.gethostbyname ( host )

	except socket.gaierror:
		print "Nao conseguiu converter"
		sys.exit ( )

	so.connect ( ( ip, porta ) )
	
	http = " HTTP/1.1\r\nHost: "
	get = "GET "
	x = "\r\n\r\n"
	mensagem = get + caminho + http + host + x
	try:
		so.send ( mensagem )

	except socket.error:
		print "Erro ao enviar mensagem"
		sys.exit ( )

	resposta = ''

	repeticao = 0
	
	while (True):
		buff = so.recv(4096)
		if (buff == ""):
			repeticao += 1
		if (repeticao == 5):
			break
		resposta += buff
		
	so.close()
	return resposta
	
teste = req("yahoo.com.br",80)
print teste
