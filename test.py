import tempfile
import traceback
import os
import requests
import time
class Test_Inter:
    def __init__(self) -> None:
        self.arr = ["lara","amanda"]
        self.BASE_DIR = "https://www.dicionariodenomesproprios.com.br/"
        self.FILE_TEMP = 'cache_request'
    
    def __inter__(self):
        for name_register in self.arr:
            yield name_register

    def search(self):
        if not os.path.exists(self.FILE_TEMP):
                os.makedirs(self.FILE_TEMP)

        for register in self.__inter__():
                response = None
                url = self.BASE_DIR + register +"/"
                try:
                    response = requests.get(url)
                    temp_file = tempfile.NamedTemporaryFile(prefix=register,dir=self.FILE_TEMP,delete=False)
                    print(response.text)
                    temp_file.write(response.text.encode('utf-8'))
                    time.sleep(20)
                    temp_file.close()
                except Exception as e:
                    traceback.print_exc()

t =Test_Inter()
t.search()