# 1. Mostre todos os números ímpares no intervalo de 0 ao número informado pelo usuário. Mostre os ímpares apenas se a entrada for maior do que 1.

number = int(input("Digite um número: "))

contador = 0


if number <= 1:
    print("Erro: digite um númeor maior que 1")
    
while contador <= number:
    if contador %2 != 0:
        print(contador)
    contador = contador +1
    
    




        
    


