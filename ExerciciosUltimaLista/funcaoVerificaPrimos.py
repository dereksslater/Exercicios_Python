# Esse arquivo só faz o teste de UM número por vez
def eh_primo(numero):
    if numero <= 1:
        return False

    divisor = 2

    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor = divisor + 1

    return True


# guardarFuncoes funcaoVerificaPrimos.py e o def é eh_primo
