import os 
import pandas as pd
from bs4 import BeautifulSoup

df = pd.read_csv("crawlerlog.csv")

baby_names = pd.DataFrame(columns=['nomes','origem','significado'])

for index,row in df.iterrows():
    name = row['nome']
    file = f'oficial_req/{name}.html'
    with open(file,'r') as arquivo:
        conteudo = arquivo.read()
        soup = BeautifulSoup(conteudo, 'html.parser')

        significado = ''
        div_significado = soup.find('div', id='significado')
        if div_significado:
            texto_div = div_significado.get_text().strip()
            significado = texto_div

        p_origem = soup.find('p', id='origem')
        origem = ''
        if p_origem:
            link_origem = p_origem.find('a')
            if link_origem:
                texto_link_origem = link_origem.get_text().strip()
                origem = texto_link_origem
            else:
                print("Não foi encontrado um link dentro da tag <p id='origem'>")
        else:
            print("Não foi encontrada uma tag <p> com o id 'origem'")
        linha = {'nomes':name,'origem':origem,'significado':significado}
        baby_names = baby_names._append(linha,ignore_index=True)

baby_names.to_csv('result.csv')

