#Obtenha três valores numéricos via entrada do usuário e apresente um valor Lógico indicando se todos os valores são diferentes entre si.
#Exemplo: n1 → 1, n2 → 5, n3 → 9, apresenta True
#Exemplo: n1 → 1, n2 → 5, n3 → 1, apresenta False

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

if n1 != n2 and n1 != n3 and n2 != n3:
    print("True")
else:
    print("False")
    