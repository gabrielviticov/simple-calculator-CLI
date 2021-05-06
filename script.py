# Versão da Aplicação - versão 2.0
    #Aprimorando Menus

print('-'*25)
print('SIMPLE CALCULATOR ON CLI')
print('_'*25)
while True:
    print('''
    [1] SOMA 
    [2] SUBTRAÇÃO
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO
    [0] SAIR
    ''')
    escolha = int(input('Informe a escolha desejada: '))
    if escolha == 0:
        break
print('OBRIGADO POR TESTAR O BETA! VOLTE SEMPRE!')