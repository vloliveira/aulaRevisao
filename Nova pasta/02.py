#Exercício 2: Tabuada Personalizada
"""Peça ao usuário um número inteiro entre 1 e 10.
Em seguida, use um laço for para exibir a tabuada desse número (de 1 a 10).
Se o número digitado estiver fora do intervalo, mostre: "Número inválido!"."""

multi = 0

num = int(input("Digite um número entre 1 e 10: "))
for i in range (0, 11):
    if num >= 0 and num <=10:
        multi = i * num
        print(f" {i} X {num}: {multi}")
        i+=1
    else:
        print("Numéro inválido!")
        break
