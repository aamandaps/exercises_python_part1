#declaração de variáveis
quant_kg: int
dias: int

#inicio
quant_kg = int(input('Digite a quantidade de alimento em quilo: '))
dias = (quant_kg * 1000)/50
print('A quantidade de alimento irá durar: ',dias)

#fim