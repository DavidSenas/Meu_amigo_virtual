from rotinas import *
from menu import *

div()
print()
print('Olá, siga os passos para criar seu amigo Virtual!')
print()
nome = str(input("Dê um nome ao seu amigo: ")).capitalize().strip()
amigo = Amigo(nome)
print(f'Olá, Adorei meu nome {amigo.nome}')
div()
Menu()
div()
while True:
    ação = int(input("Escolha uma ação para seu amiguinho! "))
    if ação == 1:
        amigo.Acordar()

    if ação == 2:
        amigo.Dentes()
    if ação == 10:
        break