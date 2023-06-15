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

def eliminacao(matriz):
    n = len(matriz)

    for i in range(n):
        # Verificar se o pivô é zero e trocar de linha, se necessário
        if matriz[i][i] == 0:
            for j in range(i + 1, n):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break
            else:
                continue  # Se não encontrou uma linha para trocar, prossegue para a próxima coluna

        # Zerar os coeficientes abaixo do pivô
        for j in range(i + 1, n):
            multiplicador = matriz[j][i] / matriz[i][i]
            for k in range(i, n + 1):
                matriz[j][k] -= multiplicador * matriz[i][k]

    return matriz


def decomposicao_LU(matriz):
    n = len(matriz)
    l = np.eye(n)
    u = matriz.copy()
    p = np.eye(n)

    for i in range(n):
        pivot_index = np.argmax(np.abs(u[i:, i])) + i

        if pivot_index != i:
            p[[i, pivot_index]] = p[[pivot_index, i]]

        for j in range(i + 1, n):
            multiplicador = u[j, i] / u[i, i]
            l[j, i] = multiplicador
            u[j, i:] -= multiplicador * u[i, i:]

    return l, u, p


def substituicao_retroativa(matriz):
    n = len(matriz)
    solucao = [0] * n

    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += matriz[i][j] * solucao[j]
        solucao[i] = (matriz[i][n] - soma) / matriz[i][i]

    return solucao

def eliminacao_gauss(a, b):
    matrizAB = np.concatenate((a, np.expand_dims(b, axis=1)), axis=1)
    elimina = eliminacao(matrizAB)
    resultado = substituicao_retroativa(elimina)

    return resultado

