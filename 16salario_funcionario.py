#declaração de variáveis
quant_h: int
valor_h: int
perc: float
num_d: int
sal_b: int
sal_l: int

#inicio
quant_h = int(input('Insira a quantidade de horas trabalhadas: '))
valor_h = int(input('Insira o valor por hora: '))
perc = float(input('Insira o percentual do desconto: '))
num_d = int(input('Insira o número de dependentes: '))
sal_b = quant_h * valor_h
sal_l = sal_b - (perc/100) + num_d * 100
print('O salário é igual: ', sal_l)

#fim