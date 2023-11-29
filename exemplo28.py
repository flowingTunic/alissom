# 1 o professor deseja dividir uma turma com N alunos em dois grupos : um com M alunos e outro com (N-M) alunos. Fasa o programa que le o valor de N e M e informe o numero de combinacoes possiveis 
#_Numero de combinacoes he igal a N!/(M!*(N-M)!)
#_Use funcoes para evitar repeticao de codigo

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

turma = ["Miguel","Arthur","Gael","Théo","Heitor","Ravi","Davi","Bernardo","Noah","Gabriel","Samuel","Pedro","Anthony","Isaac","Benício","Benjamin","Matheus","Lucas","Joaquim","Nicolas","Lucca","Lorenzo","Henrique","João Miguel","Rafael","Henry","Murilo","Levi","Guilherme","Vicente","Felipe","Bryan","Matteo","Bento","João Pedro","Pietro","Leonardo","Daniel","Gustavo","Pedro Henrique","João Lucas","Emanuel","João","Caleb","Davi Lucca","Antônio","Eduardo","Enrico","Caio","José","Enzo Gabriel","Augusto","Mathias","Vitor","Enzo","Cauã","Francisco","Rael","João Guilherme","Thomas","Yuri","Yan","Anthony Gabriel","Oliver","Otávio","João Gabriel","Nathan", "Davi Lucas","Vinicius","Theodoro","Valentim","Ryan","Luiz Miguel","Arthur Miguel","João Vitor","Léonovo","Ravi Lucca","Apollo","Thiago","Tomás","Martin","José Miguel","Erick","Liam","Josué","Luan","Asafe","Raul", "José Pedro","Dominic","Kauê","Kalel","Luiz Henrique","Dom","Davi Miguel","Estevão","Breno","Davi Luiz","Thales","Israel"]
quantidade = len(turma) // 2

# Leitura dos valores de N e M
N = len(turma)
M = quantidade
print("Valor de N:", N)
print("Valor de M:", M)

# Cálculo do número de combinações
comb = fatorial(N) / (fatorial(M) * fatorial(N-M))

# Impressão do resultado
print("O número de combinações possíveis é:", comb)

# Função para dividir a turma em dois grupos
def dividir_turma(turma, n):
    for i in range(0, len(turma), n):
        yield turma[i:i + n]

# Divisão da turma em dois grupos
turmaDividida = list(dividir_turma(turma, quantidade))

# Impressão dos grupos
print(turmaDividida)
print("Número total de alunos:", len(turma))

# 2 Fasa uma funcao que informe o status do aluno a partir da sua media de acordo com a tabela a seguir :
#_nota acima de 6 -> "Aprovado"
#_nota entre 4 e 6 -> "Verificacao Suplementar"
#_nota abaixo de 4 -> "Reprovado"

nome = input("digite seu nome")
nota = input("digite sua nota de 0 a 10 ")
    