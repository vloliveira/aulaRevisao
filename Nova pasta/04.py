#Exercício 4: Adivinhe o Número
"""Gere um número aleatório entre 1 e 100 (use import random e random.randint(1, 100)).
Peça ao usuário para adivinhar o número.
A cada tentativa, informe se o palpite é maior ou menor que o número gerado.
O programa deve repetir até que o usuário acerte."""
import random

aleatorio = random.randint(1, 101)
print(aleatorio)
chute = 0
while chute != aleatorio:
    chute = int(input("Tente acertar o número: "))
    if chute > aleatorio:
        print("O número é menor!")
    elif chute < aleatorio:
        print("O número é maior!")
    else:
        print("Parabéns você acertou!")