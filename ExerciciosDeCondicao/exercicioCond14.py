'''Para que um aviador possa ingressar em um determinado curso de aviação, necessita satisfazer as condições a seguir. Obtenha a altura, idade, horas de voo e peso de um candidato, e informe se o mesmo está apto ou não para o curso. As condições a serem atendidas (todas deverão ser atendidas) são:
• altura maior ou igual a 1,75m;
• idade entre 22 e 40 anos (inclusive 22 e 40); 
• horas de vôo superior a 1600horas;
• peso entre 65 e 95 kg (inclusive 65 e 95).'''

altura = float(input("Digite sua altura, em metros (ex: 1.75):"))
idade = int(input("Digite sua idade: "))
horas = int(input("Digite suas horas de vôo, em horas: "))
peso = int(input("Digite seu peso em KG: "))

if altura >= 1.75 and idade>= 22 and idade <= 40 and horas > 1600 and peso >= 65 and peso <= 95:
    print("Você está apto para o curso")

else:
    print("Você não está apto para o curso")

