#ALUNOS:
    # João Victor Miranda Lyra
    # Kaio Vinicios da Silva Gois

import numpy as np

def resolve_sistema_gauss_seidel(matriz_coeficientes, termos_independentes, 
                                  tentativa_inicial=None, precisao=1e-10, 
                                  maximo_iteracoes=10000):

    if tentativa_inicial is None:
        tentativa_inicial = np.zeros(len(termos_independentes))
    
    solucao_atual = tentativa_inicial.copy()
    
    num_variaveis = len(termos_independentes)
    
    for numero_iteracao in range(maximo_iteracoes):
        solucao_anterior = solucao_atual.copy()
        for i in range(num_variaveis):
            soma_outros_termos = sum(matriz_coeficientes[i][j] * solucao_atual[j] for j in range(num_variaveis) 
                if j != i
            )
            
            solucao_atual[i] = (termos_independentes[i] - soma_outros_termos) / matriz_coeficientes[i][i]
        
        erro_maximo = max(
            abs(solucao_atual[j] - solucao_anterior[j]) 
            for j in range(num_variaveis)
        )
        if erro_maximo < precisao:
            break
    
    return solucao_atual, numero_iteracao + 1

matriz_coeficientes = [
    [80, 0, 30, 10],     
    [0, 80, 10, 10],     
    [16, 20, 60, 72],    
    [4, 0, 0, 8]        
]

termos_independentes = [450, 325, 640, 565]  

# Resolve o sistema
solucao, num_iteracoes = resolve_sistema_gauss_seidel(matriz_coeficientes, termos_independentes,precisao=1e-10)

print("Resultado do Sistema de Equações:")
for i, valor in enumerate(solucao, 1):
    print(f"x{i} = {valor:.10f}")

print(f"\nNúmero de iterações: {num_iteracoes}")

