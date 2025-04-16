nome = 'FACENS'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
x = 2
palavra = 'milho'

# as três funções abaixo vão printar um caracteres por vez de cada string
# for i, digito in enumerate(numeros):
#    print(i)


# for letra in nome:
#    print(letra)


# for numero in lista:
#    print(numero)

# essa indica o indice e o valor que ele representa
#for y in enumerate(palavra):  
#    print(y)


# a função abaixo vai repetir pela quantidade de vezes que o usuario pedir
# qtd = int(input('Quantas vezes esse loop deve rodar? '))

# for n in range(1, qtd+1):
#    print(f'Imprimindo {n}')


# a função abaixo pede quantas vezes o loop, os numeros e depois soma
'''
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print('')

print(f'{soma}')
'''

# neste ele apenas não tem quebra de linha
'''
for letra in nome:
    print(letra, end='')
'''

# De 10 até 2, decrescendo de 2 em 2
'''
for i in range(100, 1, -3):
    print(i)
'''

# vai repetir a string ateé 10 vezes (da pra fazer com emotes tambem, nesse site: https://apps.timwhitlock.info/emoji/tables/unicode, ex. U+1F602 fica U0001F602)
'''
nome = 'Roberto '
for num in range(1, 11):
    print(f'{nome * num}')

for _ in range(4):
    for num in range(1,11):
        print('\U0001F602 '* num)
'''
'''
# forma 1
for num in range(11):
    print(num)

# forma 2
for num in range(5, 11):
    print(num)

# forma 3
for num in range(5, 20, 2):
    print(num)

#forma 4
for num in range(50, 0, -2):
    print(num)

#forma 5
lista2 = list(range(112))
print(lista2)

# Forma com break
for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saiu do loop')


'''


