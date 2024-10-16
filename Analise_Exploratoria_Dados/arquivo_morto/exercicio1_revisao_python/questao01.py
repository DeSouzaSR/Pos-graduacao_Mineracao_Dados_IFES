"""
Questão 1. Crie um script que solicite ao usuário dois números e qual operação ele deseja
realizar (+, -, *, /). Seu programa deve exibir o resultado da operação desejada pelo
usuário com os dois números digitados.
"""
# Entrada
numero1 = float(input("Entre com o número 1: "))
numero2 = float(input("Entre com o número 2: "))
operacao = input("Entre com a operação: [+, -, *, /]: ")

# Processamento e resultado
operacoes = {'+', '-', '*', '/'}
if operacao in operacoes:
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else :
        if numero2 == 0:
            resultado = 'Divisão por zero'
        else:
            resultado = numero1 / numero2

    print(f'{numero1} {operacao} {numero2} = {resultado}')
else:
    print(f'{operacao} é uma operação inválida')

