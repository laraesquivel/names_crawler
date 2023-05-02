import traceback
import time
import requests
import tempfile
import os
import csv

from nomes import Nomes

class Crawler():
    def __init__(self,names_path="babynamestest - names.csv",file_temp_dir='cache_request'):
        self.NOMES = Nomes(names_path)
        self.FILE_TEMP = file_temp_dir
        self.BASE_DIR = "www.dicionariodenomesproprios.com.br/"
        self.BASE_LOG = "crawlerlog.csv"
        self.BASE_ERROS_LOG = "crawlerErrosLog.csv"

    def search(self):
        if not os.path.exists(self.FILE_TEMP):
            os.makedirs(self.FILE_TEMP)

        for register in self.NOMES.__inter__():
            response = None
            url = self.BASE_DIR + register[1][0]
            try:
                response = requests.get(url)
                if response is not None:
                    temp_file = tempfile.NamedTemporaryFile(prefix=register[1][0],dir=self.FILE_TEMP,delete=False)
                    temp_file.write(response.text.encode("utf-8"))
                    crawler_reg = [register[0]*register[1]*temp_file.name]
                    with open(self.BASE_LOG) as log:
                        writer = csv.writer(log)
                        writer.writerow(crawler_reg)
                    temp_file.close()
                    time.sleep(20)
                    
            except requests.exceptions.ConnectionError as e:
                traceback.print_exception()
                crawler_erros = [register[0]*register[1]*e]
                with open(self.BASE_ERROS_LOG) as erros:
                    writerE = csv.writer(erros)
                    writerE.writerow(crawler_erros)
                    temp_file.delete()
                    time.sleep(7200)

            except Exception as e:
                traceback.print_exception()
                crawler_erros = [register[0]*register[1]*e]
                with open(self.BASE_ERROS_LOG) as erros:
                    writerE = csv.writer(erros)
                    writerE.writerow(crawler_erros)
                    temp_file.delete()
                
                    