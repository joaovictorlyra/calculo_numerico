import numpy as np

# Constantes
g = 9.81  # Aceleração devido à gravidade (m/s^2)
m = 68.1  # Massa do objeto (kg)
cd = 0.25  # Coeficiente de arrasto (kg/m)

# Função para calcular a velocidade v(t)
def v(t):
    return np.sqrt(g * m / cd) * np.tanh(np.sqrt(g * cd / m) * t)


def trapezoidal_rule(func, a, b, n):
    # Calculando o tamanho do subintervalo
    h = (b - a) / n
    
    # Avaliando os valores da função nos pontos de divisão
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        integral += func(a + i * h)
    
    # Multiplicando pelo tamanho do subintervalo
    integral *= h
    return integral

# Definir o intervalo de tempo
a = 0  
b = 10

n2 = 2
distancia_2_subintervalos = trapezoidal_rule(v, a, b, n2)

n10 = 10
distancia_10_subintervalos = trapezoidal_rule(v, a, b, n10)


print(f"Distância percorrida com 2 subintervalos: {distancia_2_subintervalos} metros")
print(f"Distância percorrida com 10 subintervalos: {distancia_10_subintervalos} metros")
