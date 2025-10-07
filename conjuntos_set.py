#exemplo de de criação de conjunto (set)
frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

#exemplo de conjuntos
conjunto1 = {1, 2, 3,}
conjunto2 = {3, 4, 5,}

#união de conjuntos
uniao = conjunto1 | conjunto2
print("União:", uniao)  # saída: {1, 2, 3, 4, 5}

#interseção de conjuntos
intersecao = conjunto1 & conjunto2
print("Interseção:", intersecao)  # saída: {3}  

#diferença de conjuntos
diferenca = conjunto1 - conjunto2
print("Diferença:", diferenca)  # saída: {1, 2}

#diferença simétrica de conjuntos
diferenca_simetrica = conjunto1 ^ conjunto2
print("Diferença Simétrica:", diferenca_simetrica)  # saída: {

'''metodo de conjuntos (set)
add --> adicionar um elemento ao conjunto
remove --> remove o elemento do conjunto. se o elemento não exisitir gera um erro
discard --> remove um elemento do conjunto se estiver presente. se o elemento não existir, não faz nada
clear --> remove todos os elementos do conjunto
'''

#exemplos

frutas = {"maçã", "banana", "laranja"}

frutas.add("pera")  # Adiciona "pera" ao conjunto
print(frutas)

frutas.remove("banana")  # Remove "banana" do conjunto
print(frutas)

frutas.discard("uva")  # Tenta remover "uva", mas não faz nada pois não está no conjunto
print(frutas)

frutas.clear()  # Remove todos os elementos do conjunto
print(frutas)

