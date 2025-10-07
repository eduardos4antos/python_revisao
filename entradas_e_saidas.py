#entrada de dados do usuario
nome = input("digite seu nome:")
idade = input("digite sua idade:")

print("olá,"  + nome +  "!")
print("você tem" + idade + "anos.")

'''na função input(), sempre vai retornar uma cadeia de texto.
se precisar de outro tipo de dado, como numeros inteiros ou flutuantes,
é necessario uma conversão explicita usando funções como int() ou float()
'''
idade = int(input("digite sua idade:"))

if idade >= 18:
    print("você é maior de idade.")
else:
    print("você é menor de idade.")
 
