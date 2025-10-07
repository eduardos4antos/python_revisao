#exemplo de try 
try:
    #codigo que pode gerar uma exceção
    resultado = 10 / 0 #divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("erro: divisão por zero não é permitida")

#exemplo de except
try:
    #codigo que poderia gerar uma exceção
    resultado = 10 /0 #divisão por zero
    print(resultado)
except ZeroDivisionError:
    print("erro: divisão por zero não é permitida")
except ValueError:
        print("erro: valor inválido")
    
#exemplo de finaly
try:
     #codigo que pode gerar uma exceção
     arquivo = open("arquivo.txt", "r")
     #realizar operações com o arquivo
except FileNotFoundError:
        print("erro: arquivo não encontrado")
finally:
        arquivo.close() #garante que o arquivo será fechado sempre, mesmo se ocorrer uma exceção

        