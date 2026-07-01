#Obtenha o nome e o ano de nascimento do usuário (via entrada) e apresente como resposta a respectiva idade (considerando o ano atual).
#Para obtenção do nome, apresente a seguinte mensagem: 
#Qual seu nome? Exemplo: Fulano Beltrano
#Para obtenção do ano de nascimento, apresente a seguinte mensagem: 
#Qual seu ano de nascimento? Exemplo: 1999
#Após o cálculo da idade apresente o nome do usuário e sua idade. 
#Saída: Fulano Beltrano, você tem 22 anos de idade.

nome = input("Qual o seu nome? ")

anonasci = int(input("Qual seu ano de nascimento?"))

idade = 2026 - anonasci

print(f"{nome} voê tem {idade} anos de idade")
