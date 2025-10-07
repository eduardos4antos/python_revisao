#exemplo de função
def saudacao() :
    print("olá, mundo")

saudacao() #chama a função e imprime "olá, mundo"

#exemplo de função com parâmetros
def saudacao(nome):
    print(f"olá, {nome}")

saudacao("joão") # chama a função e imprime "olá, joão"
saudacao("maria") # chama a função e imprime "olá, maria"

#exemplo de função com retorno
def soma(a, b):
    return a + b

resultado = soma(3, 4) # chama a função e armazena o resultado na variável
print|(resultado) #imprime 7

#exemplo de função anonima (lambda, ou lambada kkk)
quadrado =  lambda x: x ** 2
print(quadrado(5)) #imprime 25

#exemplo de escopo de variaveis (local VS global)
def funcao():
    variavel_local = 10 
    print(variavel_local) # acessivel dentro da função

variavel_global = 20

def funcao2():
    print(variavel_global) #acessivel de qualquer lugar

funcao() #imprime 10
funcao2() #imprime 20
print(variavel_global) #imprime 20
print(variavel_local) # gera um erro, a variavel não está definida nesses escopo.

#exemplo de funções com numero variavel de argumentos
def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        return total

print(soma_variavel(1, 2, 3)) #imprime 6
print(soma_variavel(4, 5, 6, 7)) #imprime 22


'''
além das funçõe definidas pelo usuario,
python tambem fornece uma ampla gama de
funções incorporadas que podemos utilizar
diretamente, como:

--> print()
--> len()
--> range()
entre varias outras
'''

