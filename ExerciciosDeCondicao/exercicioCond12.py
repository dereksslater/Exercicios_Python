#Uma empresa de vendas oferece para seus clientes um desconto calculado em função do valor da compra do cliente. Esse desconto é de 15% se o valor da compra for igual ou superior a R$6999,00 e 5% se for inferior. Solicite ao usuário o valor da compra, informe qual foi o desconto obtido e o valor final da compra.
valor = float(input("Digite o valor da compra: "))

descont5 = 0.05
descont15 = 0.15

if valor < 6999:
 resultado = valor * descont5
 total = valor - resultado
 print(f"Foi aplicado um cupom de desconto de 5%...")
 print(f"Valor total a pagar: {total: .2f} reais") 

elif valor >= 6999:
    resultado2 = valor * descont15
    total2 = valor - resultado2
    print(f"Foi aplicado um cumpom de desconto de 15%...")
    print(f"Valor total a pagar: R$ {total2: .2f} reais")
    
    