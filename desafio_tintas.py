#Desafio com funções 

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: Rendimento, Altura e largura
O programa deve mostrar na tela a mensagem 'Você necessita de X latas de tintas'
'''

Rendimento = int(input ('Qual é o rendimento da lata? '))
altura = int(input ('Qual é a altura da parede? '))
largura = int(input ('Qual é a largura da parede? '))

def calculo_tinta():
    area = altura * largura
    total = area / Rendimento
    print(f'Você necessita de {total} latas de tintas')
calculo_tinta()