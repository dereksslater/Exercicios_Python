# Recebe um texto por parâmetro e retorna uma lista com 3 elementos, sendo eles: a quantidade de vogais, de consoantes e de números presentes na string. Dica: como todo caractere tem uma representação numérica, é possível compará-los utilizando os operadores relacionais. Exemplo ‘a’ <= ‘z’ → True. O mesmo vale para um caractere representando um número: ‘1’ > ‘2’ → False.


def tabelaAscii(texto):

    vogais = 0
    consoantes = 0
    numeros = 0

    lista_vogais = "aeiouAEIOU"

    for caractere in texto:
        if "0" <= caractere <= "9":
            numeros += 1

        elif ("a" <= caractere <= "z") or ("A" <= caractere <= "Z"):
            if caractere in lista_vogais:
                vogais += 1
            else:
                consoantes += 1

    return [vogais, consoantes, numeros]


print(tabelaAscii("derekeeII233"))
