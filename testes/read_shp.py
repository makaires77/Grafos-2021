def read_shapefile(sf):
        import shapefile
        import pandas as pd

        #grab the shapefile's field names (omit the first psuedo field) 
        fields  = [x[0] for x in sf.fields][1:]
        records = sf.records()
        shps    = [s.points for s in sf.shapes()]

        #write the records into a dataframe 
        df = pd.DataFrame(columns=fields, data=records)

        #add the coordinate data to a column called "coords" 
        df = df.assign(coords=shps) 
    
        return df

