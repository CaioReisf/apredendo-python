# DESAFIO 46 FEITO #####

# import pygame
# for c in range(0, 10):
#    print(c+1)
#   pygame.time.delay(1000)
# print('BOOM!!!')

# DESAFIO 47 FEITO #####

# for c in range(0, 50, 2):
#    print(c)

# DESAFIO 48 FEITO #####

# s = 0
# cont = 0
# for c in range(1, 500+1, 2):
#    if (c % 3 == 0):
#        s += c
#        cont = cont + 1
# print(f'a soma dos {cont} valores eh de {s}')

# DESAFIO 49 FEITO ####

# num = int(input('digite um numero: '))
# tab = 0
# for c in range(0, 11):
#    tab = num * c
#    print(f'{num} X {c} = {tab}')

# DESAFIO 50

s = 0
cont = 0
for c in range(0, 6):
    num = int(input('digite um numero:'))
    if (num % 2 == 0):
        s += num
        cont = cont + 1
print(f'a soma dos {cont} numeros pares eh de {s}')
