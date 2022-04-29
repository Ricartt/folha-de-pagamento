valorH = float(input('informe o valor da hora Trabalhada: '))
diasT = int(input('Informe a quantidade de dias Trabalhados: '))
qtdH_clt = 8
qtdH_trab = diasT * qtdH_clt
valorBruto = qtdH_trab * valorH
sindi = (valorBruto * 5) / 100

print('')
print('Salário bruto        \t\t\t\t{:.2f}R$ '.format(valorBruto))
print('Horas Trabalhadas     \t\t\t\t{:.2f}R$ '.format(qtdH_trab))
print('Valor da Hora        \t\t\t\t{:.2f}R$ '.format(valorH))
print('')
print('--------------- Descontos ---------------')
if valorBruto >= 1.200 and valorBruto >= 1.600:
    inss = (valorBruto * 9) / 100
    ir = (inss * 6) / 100
    salarioL = valorBruto - (inss + ir + sindi)

else:
    if valorBruto >= 1.200 and valorBruto <= 1.600:
        inss = valorBruto * 11 / 100
        ir = (inss * 9) / 100
        salarioL = valorBruto - (inss + ir + sindi)
    else:
        if valorBruto >= 2.400:
            inss = (valorBruto * 12) / 100
            ir = inss * 11 / 100
            salarioL = valorBruto - (inss + ir + sindi)
print('')
print("INSS            \t\t\t\t{:.2f}R$".format(inss))
print("IR              \t\t\t\t{:.2f}R$".format(ir))
print("SINDICATO       \t\t\t\t{:.2f}R$".format(sindi))

print("\n-------------SALÁRIO LÍQUIDO---------------")

print("SALÁRIO LIQUIDO \t\t\t\t{:.2f}R$".format(salarioL))
