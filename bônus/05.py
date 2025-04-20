"""Exercício 5: Classificação de Idades
Faça um programa que leia a idade de 20 pessoas. Para cada idade, classifique em:
Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos) ou
Idoso (60+ anos).
No final, exiba quantas pessoas estão em cada categoria. Use um laço for e estruturas condicionais."""

crianca = 0
adolescente = 0
adulto = 0
idoso = 0

for i in range(1,21):
    idade = int(input("Digite a idade: "))
    if idade >= 0 and idade <= 12:
        crianca += 1
    elif idade >12 and idade <= 17:
        adolescente += 1
    elif idade > 17 and idade <= 59:
        adulto += 1
    else:
        idoso += 1
print(f"Foram digitadas {crianca} crianças, {adolescente} adolescentes, {adulto} adultos e {idoso} idosos.")