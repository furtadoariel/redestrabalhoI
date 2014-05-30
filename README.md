Alunos: Ariel Furtado Azevedo(11200290), Michel Silveira Pedroso (11108257)
---------------------------------------------------------------------------
Universidade Federal de Pelotas
---------------------------------------------------------------------------
Professor: Mauricio Pilla
---------------------------------------------------------------------------
Disciplina: Redes de Computadores
---------------------------------------------------------------------------
Trabalho 1 - WebCrawler multithreaded
===========================================================================

Implementação:
===========================================================================
A linguagem utilizada foi Python, devido a sua agilidade e facilidade para
implementações em recursos relacionado a protocolos de Internet.
O arquivo req.py realiza a conexão com a página, onde será aplicado o
webcrawler, conectando o ip e a porta em um socket, retornando para o arquivo
webcrawler.py os dados necessários para uma conexão sem erros.
A implementação contém recursividade, imposta na descrição do trabalho, onde
a primeira função a ser chamada é "webcrawler(deep,url,listaVisitados)" e as
próximas chamadas da função decrementam a variavel deep, acessando cada nivel
de profundidade recursivamente.
O arquivo "webcrawler.py" contém 8 Threads trabalhando em paralelo, com uma
lista de links a serem visitados, cada thread acessa o primeiro link não 
visitado retornando depois da execução para o próximo link não visitado por
ele e nem por outra Thread.

Arquivos: 
===========================================================================
- webcrawler.py
- req.py
- Readme
- executeme
- bs4 (pasta da biblioteca BeautifulSoup)

Execução:
===========================================================================
Dentro do arquivo enviado contém o script executeme, onde será necessário
executar no terminal com o comando "sh executeme".
Antes de executar o script, deve ser feito o download da biblioteca BeautifulSoup, 
utilizando o comando "sudo apt-get install python-bs4" ou mantendo a biblioteca
junto com os arquivos de execução.

Problemas:
===========================================================================
Durante o desenvolvimento do trabalho, ocorrou um problema no envio dos arquivos
para o GitHud, onde varios arquivos foram enviados por engano(repetidos,desnecessários...).
Foi necessário remover todos os arquivos do repositório para conseguir estabilizar a
situação.
