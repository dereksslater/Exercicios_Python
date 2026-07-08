# Recebe os valores de N e P e retorne o valor de S conforme a expressão (utilize a função criada no exercício 4):
# S=N!P!(N-P)!
import exercicioFuncao4



n = 10
p = 7

rspn =exercicioFuncao4.fatorial(n)
rspp = exercicioFuncao4.fatorial(p)

r1 = n - p
r2 = exercicioFuncao4.fatorial(r1)

r3 = rspp * r2
total = rspn / r3

print(f"S = {total}")