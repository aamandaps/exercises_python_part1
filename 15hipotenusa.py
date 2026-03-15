from math import sqrt
#declaração das variáveis
a:int
b:int
c:int

#inicio
b = int(input('Insira o valor do primeiro cateto: '))
c = int(input('Insira o valor do segundo cateto: '))
a = sqrt ((b**2)+(c**2))
print('A hipotenusa é: ', a)

#fim