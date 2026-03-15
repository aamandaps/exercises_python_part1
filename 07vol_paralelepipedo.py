#declaração de variáveis
comp: int
alt: int
larg: int
volume: int

#inicio
comp = int(input('Digite o comprimento: '))
alt = int(input('Digite a altura: '))
larg = int (input('Digite a largura: '))
volume = comp * alt * larg
print('Volume do paralelepípedo = ', volume)

#fim