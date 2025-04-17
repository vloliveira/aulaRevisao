resposta = "sim"
while resposta == "sim":
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso/(altura*altura)
    mensagem = " "
    if imc < 18.6:
        mensagem = "abaixo do peso"
    elif imc >= 18.6 and imc <25:
        mensagem = "peso ideal (parabéns)"
    elif imc >= 25 and imc <30:
        mensagem = "levemente acima do peso."
    elif imc >= 30 and imc <35:
        mensagem = "obesidade grau I"
    elif imc >= 35 and imc <40:
        mensagem = "obesidade grau II (severa)"
    else:
        mensagem = "obesidade grau III (mórbida)"
    print(f"Seu IMC é: {imc} você está", mensagem)
    resposta = input("Deseja começar de novo?")