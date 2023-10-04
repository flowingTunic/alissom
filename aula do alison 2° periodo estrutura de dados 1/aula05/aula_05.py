# jogo da forca
segredo = "CANETA".strip().upper()
acertos = [] #lista vaziaz
erros = []
# inicializar a lista com
for _ in range(len(segredo)):
    acertos.append("_")


while "_" in acertos:
    chute = input("digite uma letra").upper()[0]
    posicao = 0
    for letra in segredo:
    
        if chute.upper() == letra.upper():
        
            acertos[posicao] = chute
        posicao = posicao + 1
    if chute not in acertos and (chute in erros):
        erros.append(chute)
    print(f"acertos {acertos}")
    print(f"erros {erros}")
    print(f"vidas = {11-len(erros)}")
    if len(erros) > 10:
        print("enforcou! game over ")
        break
if len(erros) <= 10:
    print("voce acertou a palavra !!!!")


