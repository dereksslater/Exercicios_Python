# Sabe-se que um triângulo é formado por três lados cujas medidas não podem ser escolhidas aleatoriamente. Só irá existir um triângulo se, e somente se, todos os seus lados obedecerem à seguinte regra: um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados. Solicite ao usuário as medidas dos lados de um triângulo e apresente uma mensagem informando se existe ou não um triângulo. Realize a verificação apenas se os valores das entradas forem positivos, avise o usuário caso ele tenha entrado algum valor negativo.


a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Erro: Todos os lados devem ser maiores que zero.")

else:
    condicao1 = abs(b - c) < a < (b + c)
    condicao2 = abs(a - c) < b < (a + c)
    condicao3 = abs(a - b) < c < (a + b)

    if condicao1 and condicao2 and condicao3:
        print("Os valores formam um triângulo.")
    else:
        print("Os valores não formam um triângulo.")
