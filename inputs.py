#!usr/bin/env python3

"""
esse programa faz operações atraves de valores atribuidos por inputs

soma -> {
n1 + n2 = x
}

subtração -> {
n1 - n2 = x
}

multiplicação -> {
n1 * n2 = x
}

divisão -> {
n1 / n2 = x
}

"""
__version__ = "0.1.0"


import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("Digite a Operação que você deseja EXECUTAR: ")
    n1 = input("Digite o Primeiro Valor: ")
    n2 = input("Digite o Segundo Valor: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Quantidade de Argumentos Insuficiente! ")
    print("ex: `sum 10 7`")
    sys.exit(1)

