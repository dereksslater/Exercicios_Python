# Recebe uma lista de números e retorna quantos números primos a lista possui. Importe sua função para verificação de primos diretamente do módulo em que ela se encontra (arquivo .py) e utilize-a para resolver esse exercício.
from funcaoVerificaPrimos import eh_primo

lista = [1, 2, 4, 5, 6, 7]
ind = 0
total = 0
tam = len(lista)

while ind < tam:
    numero_atual = lista[ind]

    if eh_primo(numero_atual):
        total = total + 1

    ind = ind + 1

print(total)
