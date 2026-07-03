#Solicite ao usuário dois valores numéricos e informe se o primeiro valor é múltiplo do segundo.

numb1 = int(input("Digite o primeiro valor"))
numb2 = int(input("Digite o segundo valor"))

if numb2 == 0:
    print("Não é possivel dividir por zero")

elif numb1 % numb2  == 0:
    print(f"O valor{numb1}, é multiplo do {numb2} ")

else:
    print("os valores não são multiplos ")
          