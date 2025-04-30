import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geopandas.tools
import seaborn as sns
import matplotlib.colors as mcolors
import matplotlib.cm as cm
import matplotlib as mpl
import os
import logging

# Fazer um segundo mapa com círculos proporcionais e coloridos
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
ideb_municipios.boundary.plot(ax=ax, linewidth=1, color='black')
ideb_municipios.plot(column='ideb_2023', ax=ax, legend=True, cmap='viridis', edgecolor='black', linewidth=0.5)
for x, y, ideb in zip(ideb_municipios.geometry.centroid.x, ideb_municipios.geometry.centroid.y, ideb_municipios['ideb_2023']):
    circle = plt.Circle((x, y), radius=ideb*1000, color='blue', alpha=0.5)  # Ajuste o fator de escala conforme necessário
    ax.add_patch(circle)

    # Texto central com contorno branco
    ax.text(x, y, str(ideb), fontsize=8, ha='center', va='center', color='white', fontweight='bold', path_effects=[mpl.patheffects.withStroke(linewidth=3, foreground='black')])    

# Limitar visualização (x = longitude, y = latitude)
# consegui estas coordenadas no Google Maps
ax.set_xlim(-42.034520, -39.351673)
ax.set_ylim(-21.385750, -17.775498)

plt.title('IDEB dos Municípios do Espírito Santo (2023)', fontsize=15)
plt.axis('off')
plt.tight_layout()
plt.savefig('ideb_municipios_es_circulos.png', dpi=300, bbox_inches='tight')
plt.show()

# Exibir mensagem de conclusão
logging.info("Processo de visualização de dados concluído com sucesso.")