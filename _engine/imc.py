# coding: iso-8859-1
import sys

peso = float(sys.argv[1])
altura = float(sys.argv[2])

imc = peso / (altura ** 2)

if imc < 16:
    classificacao = "magreza grave"
elif imc < 17:
    classificacao = "magreza moderada"
elif imc < 18.5:
    classificacao = "magreza leve"
elif imc < 25:
    classificacao = "saudável"
elif imc < 30:
    classificacao = "sobrepeso"
elif imc < 35:
    classificacao = "obesidade grau I"
elif imc < 40:
    classificacao = "obesidade grau II (severa)"
else:
    classificacao = "obesidade grau III (mórbida)"


print(f'Seu IMC vale {imc:.2f} e sua classificação é {classificacao}')