"""
Questão 2. Faça um programa na linguagem Python para ler uma temperatura dada na
escala Fahrenheit e exibir o equivalente em Celsius.
"""

def fahr2celsius(f):
    """Converte temperatura fahrenheit para celsius"""
    return (5*(f - 32))/9


# Entradao
temperatura_fahrenheit = float(input('Entre com a temperatura na escala Fahrenheit: '))

# Processamento
temperatura_celsius = fahr2celsius(temperatura_fahrenheit)

# Saída
print(f'{temperatura_fahrenheit} em graus celsius é: {temperatura_celsius:0.4f}')
