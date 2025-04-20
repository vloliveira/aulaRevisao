#Exercício 1: Números Positivos e Negativos
"""Escreva um programa que leia 5 números inteiros e, para cada um, imprima se é positivo, negativo ou zero.
Use um laço de repetição para ler os números."""

for i in range (0, 5):
    num = int(input("Digite um número: "))
    if num < 0:
        print(f"{num} é negativo")
    elif num > 0:
        print(f"{num} é positivo!")
    else:
        print("O número digitado foi zero!")