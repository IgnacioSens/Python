"""
# Forma 1
numero = 1
while numero <10:
    print(numero)
    numero += 1

# Forma 2 
resposta = ''
while resposta != 'sim':
    resposta = input('Voce deseja encerrar?')

# Forma 2 (Mais otimizado)       
resposta = ''
while resposta.lower() != 'sim':
    resposta = input('Voce deseja encerrar?')

# Forma para sair com break
while True:
    comando = input("Digite 'sair' para sair: ")
    if comando.lower() == 'sair':
        break
"""

