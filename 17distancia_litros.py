#declração das variáveis
quant_l: int
tempo: float
vel: int
dis: int
litros: float

#inicio
tempo = float(input('Insira o tempo do trajeto: '))
vel = int(input('Insira a velocidade: '))
dis = tempo * vel
litros = dis/12
print('A distãncia foi', dis ,'e os litros gastos foram ', litros)

#fim