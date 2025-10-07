# pacotes são muitos uteis para organizar os modulos em diretorios
#exemplo:
meu pacote/ 
    __init__.py
    modulo1.py
    modulo2.py

# __init__.py pode estar vazio ou pode conter código de inicialização do pacote

#exemplo 2
from meu_pacote import modulo1, modulo2
modulo1.funcao1()
modulo2.funcao2()  
