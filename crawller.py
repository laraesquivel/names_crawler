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
        self.BASE_DIR = "https://www.dicionariodenomesproprios.com.br/"
        self.BASE_LOG = "crawlerlog.csv"
        self.BASE_ERROS_LOG = "crawlerErrosLog.csv"

    def search(self):
        if not os.path.exists(self.FILE_TEMP):
            os.makedirs(self.FILE_TEMP)
        

        for register in self.NOMES.__inter__():
            response = None
            temp_file = None
            print(register)
            url = f'{self.BASE_DIR}{register[1][0]}'
            print(url)
            try:
                response = requests.get(url)
                if response is not None and response.status_code != 404:
                    temp_file = tempfile.NamedTemporaryFile(prefix=register[1][0],dir=self.FILE_TEMP,delete=False)
                    temp_file.write(response.text.encode("utf-8"))
                    crawler_reg = f"{register[0]},{','.join(register[1])},{temp_file.name}\n"
                    with open(self.BASE_LOG,'a') as log:
                        log.write(crawler_reg)
                        #writer = csv.writer(log)
                        #writer.writerow(crawler_reg)
                    temp_file.close()
                    time.sleep(10)
                
                else:
                    with open(self.BASE_ERROS_LOG,'a') as erros:
                        crawler_erros = f"{register[0]},{','.join(register[1])},{str(erros)}\n"
                        #crawler_erros = register[0]*register[1]
                        #crawler_erros.append(404)
                        #writerE = csv.writer(erros)
                        #writerE.writerow(crawler_erros)
                        erros.write(crawler_erros)
                        if temp_file is not None:
                            try:
                                os.remove(f'{self.FILE_TEMP}/{temp_file.name}')
                            except:
                                pass
                        time.sleep(4)

                    
            except requests.exceptions.ConnectionError as e:
                traceback.print_exception(e)
                #crawler_erros = register[0]*register[1]
                #crawler_erros.append(e)
                with open(self.BASE_ERROS_LOG,'a') as erros:
                    #writerE = csv.writer(erros)
                    #writerE.writerow(crawler_erros)
                    crawler_erros = f"{register[0]},{','.join(register[1])},{str(erros)}\n"

                    if temp_file is not None:
                        try:
                            os.remove(f'{self.FILE_TEMP}/{temp_file.name}')
                        except:
                            pass
                    time.sleep(7200)

        
            except Exception as e:
                traceback.print_exception(e)
                
                #crawler_erros = register[0]*register[1]
                #crawler_erros.append(str(e))
                #print(crawler_erros)
                with open(self.BASE_ERROS_LOG,'a') as erros:
                    #writerE = csv.writer(erros)
                    #writerE.writerow(crawler_erros)
                    crawler_erros = f"{register[0]},{','.join(register[1])},{str(erros)}\n"
                    if temp_file is not None:
                        try:
                            os.remove(f'{self.FILE_TEMP}/{temp_file.name}')
                        except:
                            pass
            

craw = Crawler()
craw.search()