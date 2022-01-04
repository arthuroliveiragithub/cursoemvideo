km = float(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias do aluguel: '))
preco = (60 * dias) + (0.15 * km)
print('O total a pagar é de R${:.2f}.'.format(preco))
