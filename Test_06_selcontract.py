#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Selcontract(Read_ini.Config):
    def __init__(self):
        super(Selcontract,self).read_ini()

    def run_data(self,gcid,token,id):
        self.get_selcontract= {
            'gcid':gcid,
            'token':token,
            'id':id
        }
        return self.get_selcontract

    def run_selcontract(self,url,data):
        self.selcontract_data= json.dumps(data)
        self.selcontract_data_result= requests.post(
            url= url,
            data= self.selcontract_data
        )
        return self.selcontract_data_result



def test_selcontract():
    S= Selcontract()
    list_= []
    with open('ID_chengzu.txt') as C:
        for i in (C.read().split(',')):
            if i == '':
                # 切割后出现为空，去除
                pass
            else:
                list_.append(S.run_selcontract(
                    url= S.url+'selcontract',
                    data= S.run_data(
                        S.gcid,
                        S.token,
                        i)).content)
    for j in list_:
        print j+'\n'



if __name__ == '__main__':
    test_selcontract()