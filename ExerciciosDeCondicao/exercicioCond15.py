#Um caixa eletrônico contém somente cédulas de R$50,00, R$10,00 e R$5,00. Um usuário deseja fazer um saque. Obtenha o valor do saque e verifique se o valor solicitado pelo usuário pode ser entregue. Se for possível,  apresente a quantidade mínima de cada tipo de cédula para atender ao usuário. Caso contrário, exiba a mensagem: Valor indisponível, dirija-se a outro caixa.

valor = int(input("Digite o valor que você quer sacar: "))

if valor % 5 != 0:
    print("Valor indisponível, dirija-se a outro caixa")
else:   
    qt50 = valor //50
    valor = valor % 50
    
    
    qt10 = valor //10
    valor = valor % 10
    
    qt5 = valor //5
    valor = valor % 5
    
    print(f"Notas de R$ 50: {qt50}")
    print(f"Notas de R$ 10: {qt10}")
    print(f"Notas de R$ 5: {qt5}")
  