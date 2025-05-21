import os

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa...')

print('Olá seja bem-vindo','Escolha uma opção:','1.Banana','2.Maçã','3.Mamão','4.Abacaxi','5.Encerrar programa', sep='\n')
opcao = int(input('Digite:'))


if opcao == 1:
    print('Você escolheu Banana')
elif opcao == 2:
    print('Você escolheu Maçã')
elif opcao == 3:
    print('Você escolheu Mamão')
elif opcao == 4:
    print('Você escolheu Abacaxi')
elif opcao == 5:
    finalizar_app()
else:
    print('Erro')
