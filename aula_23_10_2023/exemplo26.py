def sem_parammetros():
    #sem retorno 
    print("comando 1")
    for i in range(10):
        print(i)
    print("comando 2")
def sem_parametros_com_retorno():
    print("comando 3")
    valor = input("digite s ou n: ")
    if valor == "s":
        return 100
    print("comando 4")
    return "comando 4"

def com_parametro_com_retorno(valor1, valor2):
    #função  vai comparar se valor1 == valor2
    if valor1 == valor2:
        return "sao iguais"
    else:
        #poderia ter outro comando
        return "sao diferentes"
    
def com_parametro_sem_retorno(valor1, valor2):
    #função  vai comparar se valor1 == valor2
    if valor1 == valor2:
        print("sao iguais")
    else:
        #poderia ter outro comando
        print("sao diferentes")



if __name__ == "__main__":
    print("inicio")
    #sem_parammetros()#a função vai ser chamada 
    #numero = sem_parametros_com_retorno()
    #print('depois da chamada da função ')
    #print(numero)
    #auxiliar = com_parametro_sem_retorno(4.56,4.56)
    #print(auxiliar)
    #print("chamada 2")
    #auxiliar = com_parametro_sem_retorno("chapeuzinho vermelho","chapeuzinho")
    #print(auxiliar)
    com_parametro_sem_retorno(8.8)