#i importa as Bibliotecas 
import os
import time

contador = int(input('Informe um numero inteiro: '))
os.system('cls')

while contador > 0:

    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -=1


print('Boom!!!') 