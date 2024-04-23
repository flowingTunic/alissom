import requests
import time
from unidecode import unidecode



def obter_cidades():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    resposta = requests.get(url)
    cidades = resposta.json()
    cidades_sem_acentos = remover_acentos_json(cidades)
    return cidades_sem_acentos

def remover_acentos(palavra):
    return unidecode(palavra)

def remover_acentos_json(objeto):
    if isinstance(objeto, str):
        return remover_acentos(objeto)
    elif isinstance(objeto, list):
        return [remover_acentos_json(item) for item in objeto]
    elif isinstance(objeto, dict):
        return {remover_acentos(chave): remover_acentos_json(valor) for chave, valor in objeto.items()}
    return objeto

def selection_sort():
    cidades = obter_cidades()
    tempo_inicio = time.time()
    comparacoes = 0
    n = len(cidades)
    for i in range(n):
        indice_min = i
        for j in range(i+1, n):
            comparacoes += 1
            if cidades[j]['nome'] < cidades[indice_min]['nome']:
                indice_min = j
        cidades[i], cidades[indice_min] = cidades[indice_min], cidades[i]
    tempo_execucao = time.time() - tempo_inicio
    return {"tempo_execucao": tempo_execucao, "comparacoes": comparacoes, "cidades_ordenadas": cidades}

def bubble_sort():
    cidades = obter_cidades()
    tempo_inicio = time.time()
    comparacoes = 0
    n = len(cidades)
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if cidades[j]['nome'] > cidades[j+1]['nome']:
                cidades[j], cidades[j+1] = cidades[j+1], cidades[j]
    tempo_execucao = time.time() - tempo_inicio
    return {"tempo_execucao": tempo_execucao, "comparacoes": comparacoes, "cidades_ordenadas": cidades}

def insertion_sort():
    cidades = obter_cidades()
    tempo_inicio = time.time()
    comparacoes = 0
    for i in range(1, len(cidades)):
        chave = cidades[i]
        j = i - 1
        while j >= 0 and cidades[j]['nome'] > cidades[i]['nome']:
            comparacoes += 1
            cidades[j + 1] = cidades[j]
            j -= 1
        cidades[j + 1] = chave
    tempo_execucao = time.time() - tempo_inicio
    return {"tempo_execucao": tempo_execucao, "comparacoes": comparacoes, "cidades_ordenadas": cidades}


def merge_sort():
    global comparacao1
    comparacao1 = 0

    def merge(esquerda, direita):
        resultado = []
        i = j = 0
        while i < len(esquerda) and j < len(direita):
            global comparacao1
            comparacao1 += 1 
            if esquerda[i]['nome'] < direita[j]['nome']:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    def merge_sort_auxiliar(cidades):
        if len(cidades) <= 1:
            return cidades, 0
        meio = len(cidades) // 2
        esquerda, comparacoes_esquerda = merge_sort_auxiliar(cidades[:meio])
        direita, comparacoes_direita = merge_sort_auxiliar(cidades[meio:])
        return merge(esquerda, direita), comparacoes_esquerda + comparacoes_direita

    cidades = obter_cidades()  # Certifique-se de que a função obter_cidades() está definida
    tempo_inicio = time.time()
    cidades_ordenadas, comparacoes = merge_sort_auxiliar(cidades)
    tempo_execucao = time.time() - tempo_inicio
    return {"tempo_execucao": tempo_execucao, "comparacoes": comparacao1, "cidades_ordenadas": cidades_ordenadas}

def quick_sort():
    def particionar(arr, baixo, alto):
        pivo = arr[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            if arr[j]['nome'] < pivo['nome']:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    def quick_sort_auxiliar(arr, baixo, alto):
        comparacoes = 0
        if baixo < alto:
            pi = particionar(arr, baixo, alto)
            comparacoes_esquerda = quick_sort_auxiliar(arr, baixo, pi - 1)
            comparacoes_direita = quick_sort_auxiliar(arr, pi + 1, alto)
            comparacoes = pi - baixo + 1 + comparacoes_esquerda + comparacoes_direita
        return comparacoes

    cidades = obter_cidades()
    tempo_inicio = time.time()
    comparacoes = quick_sort_auxiliar(cidades, 0, len(cidades) - 1)
    tempo_execucao = time.time() - tempo_inicio
    return {"tempo_execucao": tempo_execucao, "comparacoes": comparacoes, "cidades_ordenadas": cidades}
