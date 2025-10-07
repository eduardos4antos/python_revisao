frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")  # Adiciona "pera" ao final da lista
print(frutas)

frutas.insert(1, "uva")  # Insere "uva" na posição 1
print(frutas)

frutas.remove("banana")  # Remove "banana" da lista
print(frutas)

fruta_removida =frutas.pop()  # Remove o último item da lista
print(frutas)
print(fruta_removida)

frutas.sort()  # Ordena a lista em ordem alfabética
print(frutas)

frutas.reverse()  # Inverte a ordem da lista
print(frutas)


