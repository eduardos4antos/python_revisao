#exemplo de tupla
ponto = (3, 4)

print(ponto[0])  # saída: 3
print(ponto[1])  # saída: 4

#exemplo de metodos de tuplas
minha_tupla = (1, 2, 3, 2, 4, 2)

print (minha_tupla.index(2))  # saída: 1 (primeira ocorrência de 2)

print (minha_tupla.index(2, 2)) # saída: 3 (ocorrência de 2 a partir do índice 2)

print (minha_tupla.index(2, 2, 4)) # saída: 3 (ocorrência de 2 entre os índices 2 e 4)

# count--> devolve o numero de vezes que um elemento aparecee na tupla
# index--> devolve o indice da primeira ocorrencia do elemento na tupla
# len--> não é um metodo de tupla, mas sim uma função incorporada, devolve o comprimento da tupla
