#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Contract_By_Id(Read_ini.Config):
    def __init__(self):
        super(Get_Contract_By_Id,self).read_ini()

    def run_data(self,gcid,token,id):
        self.get_contract_by_id_list= {
            'gcid':gcid,
            'token':token,
            'id':id
        }
        return self.get_contract_by_id_list

    def run_get_contract_by_id_data(self,url,data):
        self.get_contract_by_id_data= json.dumps(data)
        self.get_contract_by_id_data_result= requests.post(
            url= url,data= self.get_contract_by_id_data)
        return self.get_contract_by_id_data_result



def test_get_contract_by_id():
    GCBI= Get_Contract_By_Id()
    list_= []
    with open('ID_chengzu.txt') as C:
        for i in (C.read().split(',')):
            if i == '':
                # 切割后出现为空，去除
                pass
            else:
                list_.append(GCBI.run_get_contract_by_id_data(
                    url= GCBI.url+'get_contract_by_id',
                    data= GCBI.run_data(GCBI.gcid,
                                        GCBI.token,
                                        i)).content)
    for j in list_:
        print j+'\n'



if __name__ == '__main__':
    test_get_contract_by_id()