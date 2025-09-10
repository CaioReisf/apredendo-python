# DESAFIO 36 FEITO ########

# casa = float(input('valor da casa:'))
# salario = float(input('seu salario:'))
# anos = float(input('quantos anos:'))
# parcela = casa / anos
# if (30*salario) / 100 < parcela:
#    print('emprestimo NEGADO! voce na pode arcar com as parcelas')
# else:
#    print(' emprestimo APROVADO! voce pagara {}R$ por mes durante {} anos'.format(parcela, anos))

# DESAFIO 37 EM ABERTO --------

# DESAFIO 38 FEITO ######

# n1 = int(input('primeiro numero:'))
# n2 = int(input('segundo numero:'))
# if n1 > n2:
#    print('o PRIMEIRO numero eh o maior {} > {}'.format(n1, n2))
# elif n1 < n2:
#    print('o SEGUNDO numero eh o maior {} > {}'.format(n2, n1))
# elif n1 == n2:
#    print('o numeros sao IGUAIS {} = {}'.format(n1, n2))

# DESAFIO 39 FEITO ######

# ano = int(input('qual sua o seu ano de nascimento?'))
# idade =  2025 - ano
# prazo = 18 - idade
# if idade < 18:
#    print('com {} anos ainda nao esta na hora do alistamento faltam {} para voce completar 18'.format(idade,prazo ))
# elif idade == 18:
#    print('voce tem {} anos, ESTA NA HORA DE SE ALISTAR!'.format(idade))
# elif idade >  18:
#    print('voce ja tem {} anos, ESTA ATRASADO {} ANOS PARA O ALISTAMENTO'.format(idade, prazo))

# DESAFIO 40 FEITO ######

# n1 = float(input('Primeira nota:'))
# n2 = float(input('Segundo nota:'))
# media = (n1 + n2) /2
# if media < 5.0:
#    print('Media {} - REPROVADO!'.format(media))
# elif media <= 6.9:
#    print('Media {} - RECUPERACAO!'.format(media))
# elif media >=7.0:
#    print('Media {} - APROVADO!'.format(media))

# DESAFIO 41 FEITO ####

# ano = int(input('qual o seu ano de nascimento?'))
# idade =  2025 - ano
# if idade <= 9:
#    print('com {} voce eh MIRIM'.format(idade))
# elif idade <= 14:
#    print('com {} voce eh INFANTIL'.format(idade))
# elif idade <= 19:
#   print('com {} voce eh JUNIOR'.format(idade))
# elif idade <= 20:
#    print('com {} voce eh SENIOR'.format(idade))
# elif idade > 20:
#   print('com {} voce eh MASTER'.format(idade))

# DESAFIO 42 FEITO #####

# a = float(input('reta 1:'))
# b = float(input('reta 2:'))
# c = float(input('reta 3:'))
# if a + b > c and a + c > b and b + c > a and a == b ==c:
#    print('essas retas formam um triangulo EQUILATERO!')
# elif a + b > c and a + c > b and b + c > a and (a == b or b == c or a ==c):
#    print('essas retas NAO formam um triangulo ISOSCELES!')
# elif a + b > c and a + c > b and b + c > a and a != b != c:
#   print('essas retas NAO formam um triangulo ESCALENO!')

# DESAFIO 43 FEITO #####

# peso = float(input('seu peso:'))
# altura = float(input('sua altura:'))
# imc = peso / (altura*altura)
# if imc < 18.5:
#    print('IMC: {} - Abaixo do peso! '.format(imc))
# elif imc < 25:
#   print('IMC: {} - peso ideal!'.format(imc))
# elif imc < 30:
#    print('IMC: {} - sobrepeso!'.format(imc))
# elif imc < 40:
#    print('IMC: {} - obesidade!'.format(imc))
# elif imc > 40:
#    print('IMC: {} - obesidade morbida!'.format(imc))

# DESAFIO 44 FEITO ######

# preco = float(input('qual o preco?'))
# escolha = int(input(
#    'forma de pagamento: [1]Dinheiro/cheque'
#    '[2] Cartao 5%'
#    '[3] 2x cartao [4] 3x + cartao'
#    'QUAL A SUA ESCOLHA: '))
# if escolha == 1:
#    a1 = 10 / 100
#    a2 =preco*a1
#    a3 = preco - a2
#    print('o valor de R${} com o desconta de 10% no dinheiro fica R${}'.format(preco, a3))
# elif escolha == 2:
#    b1 = 5 / 100
#    b2 = preco*b1
#    b3 = preco - b2
#    print('o valor de R${} com o desconta de 5% no cartao fica R${}'.format(preco, b3))
# elif escolha == 3:
#    print('o valor ficara com o original de R${}'.format(preco))
# elif escolha == 4:
#   c1 = 20 / 100
#   c2 = preco*c1
#   c3 = preco - c2
#   print('o valor de R${} com o desconta de 20% no cartao R${}'.format(preco, c3))

# DESAFIO 45

import random
escolha = str(input('ESCOLHA: Papel // Tesoura // Pedra: '))
lista = 'papel', 'tesoura', 'pedra'
jo = random.choice(lista)

if jo == escolha:
    print('empate')
else:
    print('nada')
