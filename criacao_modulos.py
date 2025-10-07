import meu_modulo # aqui estamos importando o modulo personalizado que criei chamado meu_modulo

meu_modulo.saudar("Eduardo") # aqui estamos chamando a função saudar do modulo meu_modulo
resultado = meu_modulo.calcular_soma(5, 3)
print(resultado)  # saída: 8

#organização do codigo em módulos
#exemplo:
#operacoes.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

#utilidades.py
def imprimir_mensagem(mensagem):
    print(mensagem)

def obter_nome_usuario():
    return input("Digite seu nome: ")

#exemplo continuação:
import operacoes
import utilidades #suponhando que esses modulos existam e estejam criados

resultado_soma = operacoes.somar(5, 3)
utilidades.imprimir_mensagem(f"O resultado da soma é: {resultado_soma}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá, {nome}!")

