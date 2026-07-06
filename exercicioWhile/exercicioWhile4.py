# Obtenha dois números inteiros os quais representam o limite inferior e o superior de um somatório. Caso o limite inferior seja de fato menor ou igual ao superior, calcule e apresente o resultado do somatório. Caso contrário avise o usuário e não realize o cálculo. Exemplo:
#lim. inf.: 5; lim sup.: 8; resultado: 26 → 5+6+7+8
#lim. inf.: 9; lim sup.: 2; resultado: impossível

limiteInferior = int(input("Digite o limite inferior: "))
limiteSuperior = int(input("Digite o limite superior: "))


if limiteInferior > limiteSuperior:
    print("Impossível realizar o cálculo.")
else:
    
    total = 0
    cont = limiteInferior
    
    
    while cont <= limiteSuperior:
        total = total + cont  
        cont = cont + 1
         
    print(f"Resultado: {total}")