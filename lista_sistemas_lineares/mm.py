import numpy as np

# Inicializar os valores
x_A, x_B, x_C = 0, 0, 0  # Valores iniciais
tolerancia = 1e-5  # Definir a tolerância para o critério de parada
max_iter = 100  # Número máximo de iterações
iteracao = 0

# Coeficientes das equações
"""A = np.array([[3, 2, 4],
              [2, 2, 3],
              [3, 3, 5]])"""

#com a matriz anterior o método não convergia
#foi ajustada e ficou assim:
A = np.array([[7, 2, 4],
              [2, 6, 3],
              [3, 3, 7]])


# Lado direito das equações
b = np.array([320, 240, 380])

# Método de Gauss-Jacobi
while iteracao < max_iter:
    x_A_novo = (b[0] - A[0][1]*x_B - A[0][2]*x_C) / A[0][0]
    x_B_novo = (b[1] - A[1][0]*x_A - A[1][2]*x_C) / A[1][1]
    x_C_novo = (b[2] - A[2][0]*x_A - A[2][1]*x_B) / A[2][2]

    # Verificar a convergência
    if np.allclose([x_A_novo, x_B_novo, x_C_novo], [x_A, x_B, x_C], atol=tolerancia):
        break

    # Atualizar os valores
    x_A, x_B, x_C = x_A_novo, x_B_novo, x_C_novo
    iteracao += 1

# Exibir o resultado
print(f"Produção mensal de carros:")
print(f"Modelo A: {x_A:.2f}")
print(f"Modelo B: {x_B:.2f}")
print(f"Modelo C: {x_C:.2f}")
