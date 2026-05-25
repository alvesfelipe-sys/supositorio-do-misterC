# Exercício 4 (Desafio) - Lista de números pares de 1 a 20

pares = []

for numero in range(1, 21):
    if numero % 2 == 0:
        pares.append(numero)

print("Pares:", pares)              # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("Quantidade:", len(pares))    # 10
