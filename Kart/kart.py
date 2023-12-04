def ler_dados():
    corredores = []
    tempos = []
    for i in range(6):
        corredor = input("Nome do corredor {}: ".format(i + 1))
        tempos.append([])
        for j in range(10):
            volta = float(input("Tempo da volta {} do corredor {}: ".format(j + 1, corredor)))
            tempos[-1].append(volta)
        corredores.append(corredor)
    return corredores, tempos


def melhor_volta(tempos):
    melhor_volta = tempos[0][0]
    melhor_volta_corredor = 0
    for i in range(6):
        for j in range(10):
            if tempos[i][j] < melhor_volta:
                melhor_volta = tempos[i][j]
                melhor_volta_corredor = i
    return melhor_volta_corredor, melhor_volta


def classificacao(tempos):
    classificacao = []
    for i in range(6):
        classificacao.append((i, sum(tempos[i])))
    classificacao.sort(key=lambda x: x[1])
    return classificacao


def volta_media_mais_rapida(tempos):
    voltas_medias = []
    for i in range(6):
        voltas_medias.append(sum(tempos[i]) / 10)
    return max(voltas_medias)


corredores, tempos = ler_dados()
print("Melhor volta:", melhor_volta(tempos)[0], "da volta", melhor_volta(tempos)[1])
print("Classificação final:")
for i in classificacao:
    print("{}º: {} com tempo de {} segundos".format(i[0] + 1, corredores[i[0]], i[1]))
print("Volta com a média mais rápida:", volta_media_mais_rapida(tempos))