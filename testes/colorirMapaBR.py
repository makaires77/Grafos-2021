from posicao import definir_posicao as pos
from plotarEstadosBR import plotar

shp_path = r'entradas/estados_2010.shp'
pos      = pos(shp_path)
titulos  = ['Ordem Grau Decrescente', 'Ordem Grau Crescente', 'Ordem Alfabética UF']

for titulo in titulos:
    plotar(pos,titulo)