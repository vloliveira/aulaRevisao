"""Verificador de Vogal
Peça uma letra ao usuário e diga se é uma vogal (a, e, i, o, u) ou consoante."""

letra = input("Digite uma letra: ")
if letra == "a" or  letra == "e" or  letra == "i" or letra == "o" or letra == "u":
    print("É uma volgal")
else:
    print("É consoante")