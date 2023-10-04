"""
escreva um programa que remova todos os elementos da primeira lista que tambem esta presente na segunda lista.
A= [4,5,2,3,1,2,5]
B= [3,1,5,8,9]

"""
listaA = [4,5,2,3,1,2,5]
listaB = [3,1,5,8,9]

lA = set(listaA)
lB = set(listaB)
# trazer lA-lB
lR = lA.difference(lB)
print(lR)

