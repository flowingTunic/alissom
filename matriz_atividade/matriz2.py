matriz = [[int(input("Digite o elemento da matriz: ")) for _ in range(3)] for _ in range(3)]
print("\nMatriz original:")
[print(*linha) for linha in matriz]

k = int(input("\nDigite o valor de k: "))
matriz = [[valor * k if i == j else valor for j, valor in enumerate(linha)] for i, linha in enumerate(matriz)]
print("\nMatriz após a multiplicação:")
[print(*linha) for linha in matriz]
