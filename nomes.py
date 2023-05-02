import csv
import sys

class Nomes:
    def __init__(self,path,save_path="nomes.py",error_path="errosFile.py"):
        self.names_matriz = []
        last_line = None
        try:
            with open(path,"r") as f:
                reader = csv.reader(f,delimiter=',')
                for linha in enumerate(reader):
                    llast_line = linha
                    self.names_matriz.append(linha)
        except csv.Error as e:
            with open(error_path,"a") as fw:
                error_line = [last_line[0]*last_line[1]]
                writer = csv.writer(fw)
                writer.writerow(error_line)
        
    def __inter__(self):
        for name_register in self.names_matriz:
            yield name_register

n = Nomes("babynamestest - names.csv")



