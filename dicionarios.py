#exemplo de criação de dicionario
pessoa = {"nome" : "João", "idade": 25, "cidade": "madrid"} 

# acessar os valores do dicionario
print(pessoa["nome"])  # saída: João
print(pessoa["idade"])  # saída: 25
print(pessoa["cidade"])  # saída: madrid

'''metodos de dicionarios
 keys() --> retorna uma visualização de todas as chaves do dicionario
 values() --> retorna uma visualização de todos os valores do dicionario
 items() --> retorna uma visualização de todos os apres chaves-valor do dicionario
 update() --> atualiza o dicionario com os pares chaves-valor de outro dicionario
 '''

#exemplo de metodos de dicionarios
pessoa = {"nome" : "João", "idade": 25, "cidade": "madrid"}

print(pessoa.keys())  # saída: dict_keys(['nome', 'idade', 'cidade'])

print(pessoa.values())  # saída: dict_values(['João', 25, 'madrid'])

print(pessoa.items())  # saída: dict_items([('nome', 'João'), ('idade', 25), ('cidade', 'madrid')])

pessoa.update({"profissão": "Engenheiro"})  # adiciona um novo par chave-valor

print(pessoa)


