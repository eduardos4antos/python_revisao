#em python pode se abrir arquivos em diferentes modos, como: leitura ("r"), escrita ("w"), anexação ("a"),

#leitura e escrita de arquivos
arquivo = open("dados.txt", "r") #abre o arquivo em modo de leitura
conteudo = arquivo.read() #lê todo o conteúdo do arquivo    
print(conteudo) #imprime o conteúdo do arquivo
arquivo.close() #fecha o arquivo

#escrita de arquivos
arquivo = open("dados.txt", "w") #abre o arquivo em modo de escrita
arquivo.write("olá, mundo") #escreve no arquivo
arquivo.close() #fecha o arquivo

#lembre de sempre fechar o arquivo depois de utilizar para liberar recursos do sistema

#usando with para manejar a abertura e fechamento de arquivos de forma automatica
with open("dados.txt", "r") as arquivo: #abre o arquivo em modo de leitura
    conteudo = arquivo.read() #lê todo o conteúdo do arquivo
    print(conteudo) #imprime o conteúdo do arquivo

    