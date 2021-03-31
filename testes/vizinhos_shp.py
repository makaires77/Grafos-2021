import shapefile as shp
import pandas as pd
import numpy as np
from read_shp import read_shapefile as rshp

shp_estados = r'entradas/estados_2010.shp'
sf_estados = shp.Reader(shp_estados, encoding='ISO-8859-15')
df_estados = rshp(sf_estados)
print(df_estados)

shp_municipios = r'entradas/municipios_2010.shp'
sf_municipios = shp.Reader(shp_municipios, encoding='ISO-8859-15')
df_municipios = rshp(sf_municipios)
print(df_municipios)


# Fronteira é quando o ponto coincidir mas os nomes de municípios forem diferentes
# Detectar fronteira e armazenar a aresta: Origem,Destino


of = r"testes/error.txt"
# df_mun = rshp(sf)

# df_mask = df_mun['uf']=='CE'
# df_CE   = df_mun[df_mask]

# print(df_CE)

# # for point in df_mun['coords'][0]:
# #     print(point)

# shapes = sf_estados.shapeRecords()
shapes = sf_municipios.shapeRecords()
ids    = np.zeros(len(shapes))

output = open(of, 'w')
output.close()
output = open(of, 'a')

VIZINHOS=[]
c=0
for shp in shapes:
    print(shp.record[0:-1])
    lats = np.zeros(len(shp.shape.points))
    lons = np.zeros(len(shp.shape.points))
    for i in range(0, len(shp.shape.points)):
        point = shp.shape.points[i]
        nome = shp.record[1]
        ponto = np.array([nome, point[0], point[1]])
        print(ponto)

    # Get the bounding box of the 4th shape.
    # Round coordinates to 3 decimal places
    # bbox = shapes[c].bbox
    # ['%.3f' % coord for coord in bbox]
    c+=1

    # if max(lats)>86.5:
    #     print(shp.record[0])
    #     continue
    # if min(lats)<-79.2:
    #     print(shp.record[0])
    #     continue

    # identification of shapefiles crossing dateline - not needed here
    #if max(lons)>179.9: continue
    #if min(lons)<-179.9: continue
    # output.write(str(shp.record[0])+'\n')

output.close()
