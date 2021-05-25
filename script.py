# Estruturando a aplicação

válido = False
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 >= 0 and num2 >= 0:
    válido = True
while not válido:
    num1 = int(input('Número inválido. Digite o primeiro valor positivo: '))
    num2 = int(input('Agora digite o segundo valor positivo: '))
    if num1 >= 0 and num2 >= 0:
        válido = True
print('_'*25)
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
    elif escolha == 1:
        print(f'{num1} + {num2} = {num1+num2}')
    elif escolha == 2:
        if num1 > num2:
            print(f'{num1} - {num2} = {num1-num2}')
        else:
            print(f'{num2} - {num1} = {num2 - num1}')
    elif escolha == 3:
        print(f'{num1} x {num2} = {num1*num2}')
    elif escolha == 4:
        print(f'{num1} / {num2} = {num1/num2:.1f}')
    elif escolha == 5:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    else:
        print('OPÇÃO INVÁLIDA. SELECIONE UMA OPÇÃO VÁLIDA')
print('OBRIGADO POR TESTAR A APLICAÇÃO! VOLTE SEMPRE!')
