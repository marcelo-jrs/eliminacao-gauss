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
        pivo =  encontrar_pivo(matriz[i:, :])
        
        if pivo is None:
        # Se não houver pivô, a eliminação está completa
            break
    
        linha_pivo, coluna_pivo = pivo
        
        linha_pivo += i  # Ajustar o índice da linha do pivô
        
        # Dividir a linha do pivô pelo valor do pivô para torná-lo igual a 1
        pivô = matriz[linha_pivo, coluna_pivo]
        matriz[linha_pivo, :] = np.divide(matriz[linha_pivo, :], pivô)

        
        # Eliminação - multiplicar o valor do pivô pela linha atual e subtrair dessa linha
        for k in range(linha_pivo + 1, nlinhas):
            coeficiente = matriz[k, coluna_pivo]
            matriz[k, :] -= coeficiente * matriz[linha_pivo, :]
    
    return matriz

# Exemplo de uso
AB = np.array([[3, 2, -1, 4],
 [2, -1, 3, 6],
 [1, 3, -2, 5]])

resultado = eliminacao_gauss(AB)

print("Resultado da eliminação de Gauss:")
print(resultado)
