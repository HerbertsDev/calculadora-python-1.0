# Operações matemáticas

import math

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b


def potencia(a, b):
    return a ** b


def raiz(a):
    if a < 0:
        return "Erro: número negativo."
    return math.sqrt(a)