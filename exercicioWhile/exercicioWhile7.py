# Obtenha números inteiros quaisquer via entrada do usuário até que o usuário entre com o número 0. Informe a quantidade números digitados, o somatório e a média dos números.

entrada = int(input("Digite um número (0 para sair): "))

quantidade = 0
soma = 0

while entrada != 0:
    quantidade = quantidade + 1
    soma = soma + entrada
    entrada = int(input("Digite um novo número: "))
    entrada = entrada 
    
        
if quantidade >0:
    media = soma / quantidade   
    print(f"Quantidade: {quantidade}, média: {media}, somatório: {soma}")
else:
    print("Você não digitou nenhum número válido")
    
    
    
  