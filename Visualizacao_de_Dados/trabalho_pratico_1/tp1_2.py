"""
Atividade 2 - TP1
A imagem do arquivo "imagem_carro.png" corresponde à parte traseira de um 
carro. Como pode ser observado, a imagem está escura. Elabore um algoritmo
em Python para responder aos seguintes questionamentos:

Valor: 5 pontos

a) Aparentemente a imagem está em tons de cinza, mas a escala do arquivo 
é realmente em tons de cinza? Dica: verifique o número de canais do arquivo.
Se tiver 3 canais será RGB, se possuir apenas um, estará na escala de cinzas
real (grayscale).

b) Realize ajustes na imagem, como modificação de contraste, equalização do
histograma, binarização adaptativa, binarização pelo método de OTSU,
aplicação de operações morfológicas ou outro método de sua preferência, com
o objetivo de identificar a placa do carro. Dica: Avalie cada método 
separadamente ou combine-os, caso necessário, para atingir o objetivo desejado.
"""

# Importanto bibliotecas
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image 
from skimage import exposure 

# Carregando a imagem
img = Image.open("imagem_carro.png")
img = np.array(img) 

# Verificando o número de canais da imagem
# Confirma se a imagem é RGB ou tons de cinza

print('\n')
print("-" * 80)
print("Resposta da questão 2a:")
if len(img.shape) == 3 and img.shape[2] == 3:
  print("A imagem é RGB.")
elif len(img.shape) == 2 or (len(img.shape) == 3 and img.shape[2] == 1):
  print("A imagem é em tons de cinza.")
else:
  print("Não foi possível determinar se a imagem é RGB ou tons de cinza.")
