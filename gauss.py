def eliminacao_gauss(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        # encontra o pivo principal
        pivot = matriz[i][i]

        # se o pivo for zero troca a linha
        if pivot == 0:
            for j in range(i+1, linhas):
                if matriz[j][i] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    pivot = matriz[i][i]
                    break

        # Se não houver pivo retorna none
        if pivot == 0:
            return None

        # multiplica a linha do pivo para eliminar os elementos abaixo dele
        for j in range(i+1, linhas):
            factor = matriz[j][i] / pivot
            matriz[j] = [elem - factor * matriz[i][k] for k, elem in enumerate(matriz[j])]

    return matriz
