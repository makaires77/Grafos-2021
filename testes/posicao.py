"""
Marcos Aires
Março de 2021

Função para extrair posição para Sigla dos estados brasileiros como rótulo a partir do ponto médio de um shapefile
parâmetro: String com o caminho para o arquivo .shp
  retorna: Dicionário com Siglas de estado como chave e par ordenado de valores como posições no plano cartesiano
"""
def definir_posicao(shp_path):
    import shapefile as shp
    import pandas as pd
    import numpy as np

    # Função de leitura do arquivo SHP
    def read_shapefile(sf):
        
        #grab the shapefile's field names (omit the first psuedo field) 
        fields  = [x[0] for x in sf.fields][1:]
        records = sf.records()
        shps    = [s.points for s in sf.shapes()]

        #write the records into a dataframe 
        df = pd.DataFrame(columns=fields, data=records)

        #add the coordinate data to a column called "coords" 
        df = df.assign(coords=shps) 
    
        return df

    #read file, parse out the records and shapes 
    
    # shp_path = pathlib.Path(os.getcwd(), "entradas/estados_2010.shp") # caso precisar de ser um WindowsPath
    sf = shp.Reader(shp_path, encoding='ISO-8859-15')
    df = read_shapefile(sf)

    coordenadas=[]
    for i in df['coords']:
        x_lon = np.zeros((len(i),1))
        y_lat = np.zeros((len(i),1))
        
        for ip in range(len(i)):
            x_lon[ip], y_lat[ip] = i[ip]
            
    #     x_lon = np.array_split(df1, 2, axis=1)
        x0 = round(np.mean(x_lon),2)
        y0 = round(np.mean(y_lat),2)
        coordenadas.append(np.array([x0, y0])) 

    # Definição da posição de cada vértice no plano para geração da plotagem    
    pos = dict(zip(list(df['sigla']), coordenadas))
    
    return pos