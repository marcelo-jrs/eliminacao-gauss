from fractions import Fraction
import numpy as np

def encontrar_pivo(matriz):
    nlinhas, ncolunas = matriz.shape
    
    for i in range(nlinhas):
        pivo = None
        
        # Procurar o pivô não nulo na linha atual
        for j in range(ncolunas):
            if matriz[i, j] != 0:
                pivo = (i, j)
                break
        
        # Se não encontrou um pivô não nulo, procurar nas linhas abaixo
        if pivo is None:
            for k in range(i+1, nlinhas):
                if matriz[k, i] != 0:
                    pivo = (k, i)
                    matriz[[i, k]] = matriz[[k, i]]  # Trocar as linhas i e k
                    break
        
        if pivo is not None:
            return pivo
    
    return None

def eliminacao_gauss(matriz):
    nlinhas, ncolunas = matriz.shape
    
    for i in range(nlinhas):
        # Encontrar o pivô
        pivo = encontrar_pivo(matriz[i:, :])
        
        if pivo is None:
            # Se não houver pivô, a eliminação está completa
            break
    
        linha_pivo, coluna_pivo = pivo
        
        linha_pivo += i  # Ajustar o índice da linha do pivô
        
        # Dividir a linha do pivô pelo valor do pivô para torná-lo igual a 1
        pivô = matriz[linha_pivo, coluna_pivo]
        matriz[linha_pivo, :] = [Fraction(elemento, pivô) for elemento in matriz[linha_pivo, :]]
        
        # Eliminação - multiplicar o valor do pivô pela linha atual e subtrair dessa linha
        for k in range(linha_pivo + 1, nlinhas):
            coeficiente = matriz[k, coluna_pivo]
            matriz[k, :] = [linha_k - coeficiente * linha_pivo for linha_k, linha_pivo in zip(matriz[k, :], matriz[linha_pivo, :])]
    
    return matriz

def substituicao_retroativa(matriz):
    nlinhas, ncolunas = matriz.shape
    solucao = np.zeros(nlinhas, dtype=object)
    
    for i in range(nlinhas-1, -1, -1):
        solucao[i] = matriz[i, ncolunas-1]
        
        for j in range(i+1, nlinhas):
            solucao[i] -= matriz[i, j] * solucao[j]
        
        solucao[i] /= matriz[i, i]
    
    return solucao

# Exemplo de uso
AB = np.array([[Fraction(2), Fraction(1), Fraction(-3), Fraction(5)],
               [Fraction(1), Fraction(-2), Fraction(1), Fraction(-1)],
               [Fraction(3), Fraction(-1), Fraction(4), Fraction(2)]])

resultado = eliminacao_gauss(AB)
solucao = substituicao_retroativa(resultado)

print("Resultado da eliminação de Gauss:")
print(resultado)

print("Solução do sistema:")
print(solucao)
