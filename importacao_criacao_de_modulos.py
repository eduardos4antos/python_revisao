# exemplo de importação de um módulo
import math

resultado = math.sqrt(25) # calcula a raiz quadrada de 25
print(resultado)  # saída: 5.0
# importou o módulo math e fez uso da função sqrt() para calcular a raiz quadrada de 25

#exemplo de importação de um módulo apenas chamando o sqrt do math
from math import sqrt

resultado = sqrt(25)
print(resultado)  #imprime 5.0
# nesse caso, se fez apenas a importação da função sqrt() do módulo math

#funcoes e classes de módulos padrão
'''
math--> funções matemáticas, como sqrt(), sin(), cos(), etc
random--> geração de números aleatórios, como random(), randint(), choice(), etc
datetime--> manipulação de datas e horas, como datetime(), date(), time(), etc
'''

# exemplo
import random
import datetime

numero_aleatorio = random.randint(1, 10) # gera um número aleatório entre 1 e 10
print(numero_aleatorio) # saída: um número aleatório entre 1 e 10

data_atual = datetime.datetime.now() # obtém a data e hora atual
print(data_atual) # saída: data e hora atual no formato AAAA-MM-DD HH:MM:SS.mmmmmm
# importou o módulo random para gerar um número aleatório e o módulo datetime para obter a data e hora atual

