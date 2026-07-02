#Obtenha um valor numérico via entrada do usuário e apresente um valor Lógico indicando se penúltimo dígito do número é ímpar. Considere que apenas números com mais do que 3 dígitos possam ser informados na entrada.

number = int (input("Digite um número com mais de 3 dígitos: "))

verifica = (number //10) %10

impar = (verifica %2  != 0)

print(impar)



    

 