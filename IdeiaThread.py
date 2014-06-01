th = []
count = 1
for i in xrange(len(lista)):
		if deep == 0:
			return listaVisitados
		else:
			th[count] = Thread(target=webcrawler,args=(deep-1, lista[i], listaVisitados))
			th[count].start()
			count++
			if(count == 8):
				count = 1
"""podemos inserir dentro do proprio for, um contador que vai ate o numero de threads que vamos usar
quando o contador for igual ao numero maximo, zeramos o contador e utilizar a primeira thread novamento,
que ja vai ter executado, seguindo ate o tamanho da lista
TO MANDANDO EM OUTRO ARQUIVO PRA NAO ACONTECER DE NOVO O PROBLEMA COM OS ARQUIVOS xD"""
			
