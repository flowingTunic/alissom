import json
#"r" - abrir para leitura
#"w" - abrir para escrita (sobreescrever)
#"a" - abrir para escrita (anexa no fim)
with open("aula_31-08_2023\dados.json", "r") as arquivo:
    registros = json.load(arquivo)

print(registros)