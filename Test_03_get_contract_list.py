#-*- coding: UTF-8 -*-
import requests
import Read_ini
import json
import os



class Get_Contract_List(Read_ini.Config):
    def __init__(self):
        super(Get_Contract_List,self).read_ini()

    def run_data(self,gcid,phone,token):
        self.get_contract_list_data= {
            'gcid':gcid,
            'phone':phone,
            'token':token
        }
        return self.get_contract_list_data

    def run_get_contract_list_data(self,url,data):
        self.get_contract_list_data_post= json.dumps(data)
        self.get_contract_list_result= requests.post(
            url= url,
            data= self.get_contract_list_data_post)
        # 返回的为字符串格式
        return self.get_contract_list_result



def test_get_contract_list():
    try:
        os.remove('ID_chengzu.txt')
    except:
        pass
    GCL= Get_Contract_List()
    list_= GCL.run_get_contract_list_data(
        url= GCL.url+'get_contract_list',
        data= GCL.run_data(GCL.gcid,GCL.phone,GCL.token)).json()['result']['list']
        # json()后返回为dict
    if len(list_)== 0:
        with open('ID_chengzu.txt','a+') as F:
            F.write('')
    else:
        for i in list_:
            print json.dumps(i, encoding='UTF-8', ensure_ascii=False)+'\n'
            # 通过json方法打印出中文
            with open('ID_chengzu.txt','a+') as F:
                F.write(i['chengzuId']+',')



if __name__ == '__main__':
    test_get_contract_list()

