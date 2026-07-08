#Crie uma nova versão da função do exercício 1, porém agora com um parâmetro opcional o qual informa se o intervalo é aberto ou fechado, ou seja, se os valores de início e fim do intervalo também são considerados na verificação. (Teste a execução dessa função com e sem o parâmetro opcional).
# Função com o parâmetro opcional 'fechado' que por padrão é True
def verificar_intervalo(numero, inicio, fim, fechado=True):
    if fechado:
        
        if numero >= inicio and numero <= fim:
            return f"O número {numero} ESTÁ dentro do intervalo FECHADO [{inicio}, {fim}]."
        else:
            return f"O número {numero} NÃO está dentro do intervalo FECHADO [{inicio}, {fim}]."
    else:
       
        if numero > inicio and numero < fim:
            return f"O número {numero} ESTÁ dentro do intervalo ABERTO ]{inicio}, {fim}[."
        else:
            return f"O número {numero}  NÃO está dentro do intervalo ABERTO ]{inicio}, {fim}[."



print(verificar_intervalo(5, 5, 10)) 


print(verificar_intervalo(5, 5, 10, fechado=False))


print(verificar_intervalo(7, 5, 10, fechado=False))