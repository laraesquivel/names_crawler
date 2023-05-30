import os
import pandas as pd


df = pd.read_csv("crawlerlog.csv")
print(df.head())

def renomear_arquivos():
    for index,row in df.iterrows():
        path = row['path']
        name = row['nome']
        file = f'oficial_req/{name}.html'
        os.rename(path,file)

renomear_arquivos()