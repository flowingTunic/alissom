#biblioteca para manipolar arquivo json
import json

reg01 = {"nome": "Fulano","idade" :10, "matriculado":True}
reg02 = {"nome": "beltrana","idade" :12, "matriculado":False}

dados = {"alunos":[reg01,reg02]}
print("dicionario payton")
print(dados)
#serealiza o dicionario para json
#dunps serializa 
json_str = json.dumps(dados)
print("string serializada - formato json")
print(json_str)
#salvar em arquivo
with open("aula_31_08_2023\dados.json", "w") as json_file:
    json.dump(dados,json_file)
