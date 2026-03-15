from math import sqrt
#declaração das variáveis
a: int
b: int
c: int
delta: float
x1: float
x2: float

#inicio
a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))
delta = (b**2) - 4 * a * c
x1 = (-b + (sqrt(delta)))/2*a
x2 = (-b - (sqrt(delta)))/2*a
print('As raízes da equação são: ', x1 ,'e', x2)

#fim
