# Obtenha um valor inteiro no intervalo entre 1 e 9 (inclusive) e conte quantos números são divisíveis pelo valor informado pelo usuário, dentro do intervalo de 1 a 1.000 (inclusive). Caso o usuário entre com um valor fora do intervalo de 1 a 9, avise-o e solicite novamente sua entrada. Solicite a entrada até que o valor seja válido ou que ele entre com o número 0 (nesse caso o programa encerra sem realizar o cálculo).  

entrada = int(input("Digite um valor de 1 a 9 (ou 0 para sair): "))

while entrada != 0 and (entrada < 1 or entrada > 9):
    print("Valor inválido!")
    entrada = int(input("Digite novamente um valor de 1 a 9 (ou 0 para sair): "))

if entrada != 0: 
    contador = 0
    i = 1

    
    while i <= 1000:
        if i % entrada == 0:
            contador = contador + 1
        i = i + 1  
    
    
    print(f"Existem {contador} números divisíveis por {entrada} entre 1 e 1000.")

else:
    print("Programa encerrado")
    