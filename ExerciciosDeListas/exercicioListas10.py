# Um texto em Python pode ser acessado via índices da mesma forma que uma lista. Exemplo: palavra = ‘abacaxi’ → palavra[0]: ‘a’, palavra[1]: ‘b’. Assim como numa lista, é possível utilizar a função len para obter o tamanho de um texto. Exemplo: len(palavra) → 7. Elabore uma função que receba um texto como parâmetro e retorna um valor lógico indicando se o texto é palíndromo. Um palíndromo é uma frase ou palavra que mantém o mesmo sentido quando lida de trás pra frente. Exemplos: reger, rir, radar, ele, esse, ama, aia, etc.


def palindromo(palavra):

    palavra_invertida = ""
    ind = -1
    while ind >= -len(palavra):
        palavra_invertida = palavra_invertida + palavra[ind]

        ind = ind - 1
    if palavra_invertida == palavra:
        return True
    else:
        return False


print(palindromo("ovo"))
