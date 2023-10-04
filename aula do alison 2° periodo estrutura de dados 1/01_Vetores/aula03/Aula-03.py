# faça uma estrutura com tudo que aprendeu

#armazenar as notas de 10 alunos em uma lista. a nota 
#cada alumo sera informada pelo teclado

n_alunos = 10
notas = []
for i in range(n_alunos):
    nota = float(input("digite nota: "))
    notas.append(nota)
    print(notas)

# - o sum subistitui e sinplifica tudo isso
#soma = 0
#for indice in range(len(notas)):
    #print(indice, end=">>>>")
    #print(notas[indice])
 #   soma = soma + notas[indice]
    #print(f"soma parcial {soma}")

# sum - é a soma dos valores presentes na lista 
# len - a quantidade de valores presentes na lista 

media = sum(notas)/len(notas)
print(f"media final={media}")