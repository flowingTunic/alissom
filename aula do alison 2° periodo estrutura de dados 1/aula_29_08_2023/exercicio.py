"""
vamos supor que precisamos criar um programa para cadastrar alunos em uma escola , armazenando informaçoes como nome ,idade e nota. podemos utiliizar um dicionario para representar cada aluno , onde a chave sera o numero de matricula e o valor sera outro dicionario contendo as informações do aluno.
"""
dicionario ={}
opcao = 1
while opcao !=3:
    print("="*30)
    print("===MENU===")
    print("1. Adicionar")
    print("2. Consultar")
    print("3. Sair")
    opcao = int(input(">>>>"))
    