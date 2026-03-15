#declaração das variáveis
ano_nasc: int
ano_atual: int
idade_atual: int
idade_fut: int

#inicio
ano_nasc = int(input('Digite o ano que você nasceu: '))
ano_atual = int(input('Digite o ano atual: '))
idade_atual = ano_atual - ano_nasc
idade_fut = idade_atual + 17
print('Você tem',idade_atual,'anos,e daqui 17 anos vocẽ terá',idade_fut)

#fim