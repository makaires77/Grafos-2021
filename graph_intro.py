from IPython.display import HTML, Image, clear_output
from networkx.algorithms import bipartite
from tqdm.notebook import trange, tqdm
from matplotlib import animation, rc

import matplotlib.pyplot as plt
import shapefile as shp
import networkx as nx
import pandas as pd
import numpy as np
import warnings

pd.set_option('display.max_colwidth', None)
pd.set_option('colheader_justify', 'left')
warnings.filterwarnings("ignore", category=DeprecationWarning)

path = 'E:/'
shp_path = "E:\graph_kcolor\shp\estados_2010.shp"
sf = shp.Reader(shp_path, encoding='ISO-8859-15')

# Função de leitura do arquivo SHP
def read_shapefile(sf):
    """
    Uses the pyshp package read a shapefile into a Pandas dataframe with a 'coords' column holding the geometry information 
    """
    fields  = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps    = [s.points for s in sf.shapes()]

    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)

    return df

df = read_shapefile(sf)

coordenadas=[]
for i in df['coords']:
#     print(type(i), len(i))
    x_lon = np.zeros((len(i),1))
    y_lat = np.zeros((len(i),1))
    
    for ip in range(len(i)):
#         print(i[ip])
        x_lon[ip], y_lat[ip] = i[ip]
        
#     x_lon = np.array_split(df1, 2, axis=1)
    x0 = round(np.mean(x_lon),2)
    y0 = round(np.mean(y_lat),2)
    coordenadas.append(np.array([x0, y0])) 
    
pos = dict(zip(list(df['sigla']), coordenadas))
pos