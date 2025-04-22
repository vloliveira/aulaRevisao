#Exercício 3: Soma dos Pares
"""Crie um programa que solicite 10 números ao usuário e calcule a soma apenas dos números pares digitados.
Utilize um laço while para a repetição e condicionais para verificar se o número é par."""

soma = 0
i = 1
while i <= 10:
    num = int(input("Digite um número: "))
    if num%2 == 0:
        soma += num
    i += 1
print(soma)