# ALUNOS:
    # João Victor Miranda Lyra
    # Kaio Vinicios da Silva Gois

import math

def f(x):
    return (math.exp(x) * math.sin(x)) / (1 + x ** 2)

def trapezios(f, a, b, n):
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n):
        soma += 2 * f(a + i * h)
    return (h / 2) * soma

def simpson_composto(f, a, b, n):
    if n % 2 != 0:
        print("A quantidade de subintervalos não pode ser ímpar.")
    h = (b - a) / n
    soma = f(a) + f(b)
    for i in range(1, n, 2):
        soma += 4 * f(a + i * h)
    for i in range(2, n, 2):
        soma += 2 * f(a + i * h)
    return (h / 3) * soma

a = 0
b = 2
intervalo_1 = 1
intervalo_2 = 5
intervalo_3 = 20

print("Trapézio para 1 subintervalo:", trapezios(f, a, b, intervalo_1))
print("Trapézio para 5 subintervalos:", trapezios(f, a, b, intervalo_2))
print("Trapézio para 20 subintervalos:", trapezios(f, a, b, intervalo_3))

print("Simpson para 1 subintervalo:", simpson_composto(f, a, b, intervalo_1))
print("Simpson para 5 subintervalos:", simpson_composto(f, a, b, intervalo_2))
print("Simpson para 20 subintervalos:", simpson_composto(f, a, b, intervalo_3))
