#estrutura de dados 
notas = (8.0,5.5,1.5)
#print (notas [2])
#print (notas [3]) indice invalido precisa ser 0 1 ou 2
#tam =  len(notas) # #len -> length - comprimento da ED
#print(tam)

media = (notas[0]+notas[1]+notas[2])/3
print(f"media ={media:.2f}")

media2 = (notas[0]+notas[1]+notas[2])/len(notas)#aqui temos a vantagem no qual se adicionarmos notas novas ele automaticamente vai ler por quanto vai ter que dividir
print(f"media ={media2:.2f}")

# notas3 = (8.0,5.5,1.5,9.0)
# media3 = (notas3[0],notas3[1],notas3[2],notas3[3])/len(notas3)

print('---for---')
notas3 = (8.0,5.5,1.5,9.0)
# exemplo do for para percorrer a estrutura de dados
soma = 0
for indice in range(len(notas3)):
    #print(indice, end=">>>>")
    #print(notas3[indice])
    soma = soma + notas3[indice]
    #print(f"soma parcial {soma}")
####
media = soma/len(notas3)
print(f"media final={media}")



# notas4 = [] #criando uma estrutura de dados vazia
# print(notas4)#alterando elemento
# notas4 = [4]
# print(notas4)

notas5 = []
print(notas5)
notas5.append(4)
print(notas5)
notas5.append(7)
print(notas5)