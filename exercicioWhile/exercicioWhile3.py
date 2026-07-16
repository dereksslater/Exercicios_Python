# 3. Obtenha via entrada do usuário um número inteiro positivo qualquer e exiba a tabuada desse número. Apresente da seguinte forma (exemplo com o número 2 como entrada):
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 10 = 20

n1 = int(input("Digite um número: "))


contador = 1

if n1 < 1:
    print("Erro: número negativo não pode ser escrito")
else:
    while contador <= 10:
        resultado = n1 * contador
        print(f"{n1} x {contador} = {resultado}")
        contador = contador + 1
