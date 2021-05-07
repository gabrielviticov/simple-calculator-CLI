# Versão da Aplicação - versão 3.0
    #Iniciando interatividade

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

print('-'*25)
print('SIMPLE CALCULATOR ON CLI')
print('_'*25)

while True:
    print('''
    [1] SOMA 
    [2] SUBTRAÇÃO
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO
    [5] NOVOS VALORES
    [0] SAIR
    ''')
    escolha = int(input('Informe a escolha desejada: '))
    print('-'*25)
    if escolha == 0:
        break
    elif escolha == 5:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
print('OBRIGADO POR TESTAR A APLICAÇÃO! VOLTE SEMPRE!')