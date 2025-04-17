inicie = "sim"
decisao = input("Você deseja saber se o número é positivo, negativo, par ou ímpar?")

while decisao == inicie:
    num = int(input("Digitre um número: "))
    if num %2 == 0:
        print("Esse númer é par.")
    else:
        print("Esse número é ímpar.")
    if num >= 0:
        print("E um número positivo.")
    else:
        print("E um númer negativo.")
    decisao = input("Você deseja saber se o número é positivo, negativo, par ou ímpar?")

