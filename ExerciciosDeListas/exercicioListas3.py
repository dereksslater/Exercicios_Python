# Recebe uma lista com conteúdos de diferentes tipos e mostra-os para o usuário em ordem inversa (essa função não tem retorno).


def mostrar_lista_inversa(lista):
    for item in reversed(lista):
        print(item)


minha_lista = ["Derek", 26, "Brasil", "outubro", 23, 56, 55, 44, 44]

mostrar_lista_inversa(minha_lista)
