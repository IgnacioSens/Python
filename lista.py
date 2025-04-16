lista = [1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 19, 123]
lista2 = ['f', 'a', 'c', 'e', 'n', 's']
"""
# Teste sobre as listas (arrays em C)

lista = [1, 2, 3, 4, 5, 6, 19, 123]
x = 0

while x != 150:
    if x in lista:
        print(f'{x} está na lista')
    else:
        print(f'{x} não está na lista')
    x += 1

print(lista.count(3))

lista.append(101)

lista.append([102, 20, 203]) # Adiciona na lista mantendo o formato lista

lista.extend([89, 78, 76]) # Adiciona na lista separando da lista

lista.insert(2, 'Novo valor')

lista.sort() # Orgazina a lista de forma ordenada 

lista.reverse() # Organiza de forma inversa

lista3 = sorted(lista) # Organiza em uma nova lista sem alterar a primeira

lista.extend(lista2) # Resulta na adição da lista 2 na lista 1 a partir no do ultimo elemento da lista 1

lista.len() # Retorna o tamanho da lista (quantidade de elementos)

lista.pop(x) # Retorna  o ultimo elemento e retira ele da lista (x pode significar a posição do elemento)

lista.clear() #Limpa  a lista

lista = lista * x  # x é um inteiro para multiplicar a lista dentro dela

string = 'A faculdade de Engenharia de Sorocaba'
lista = string.split()                                # Transforma a string em uma lista

"""
