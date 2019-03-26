#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Cleaning_List(Read_ini.Config):
    def __init__(self):
        super(Get_Cleaning_List,self).read_ini()

    def run_data(self,gicd,token,phone):
        self.get_cleaning_list= {
            'gcid':gicd,
            'token':token,
            'phone':phone
        }
        return self.get_cleaning_list

    def run_get_cleaning_list_data(self,url,data):
        self.get_cleaning_list_data= json.dumps(data)
        self.get_cleaning_list_data_result= requests.post(
            url= url,
            data= self.get_cleaning_list_data)
        return self.get_cleaning_list_data_result



def test_get_cleaning_list():
    GCL= Get_Cleaning_List()
    list_= GCL.run_get_cleaning_list_data(
        url= GCL.url+'get_cleaning_list',
        data= GCL.run_data(
            GCL.gcid,
            GCL.token,
            GCL.phone)).json()['result']['list']
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False) + '\n'



if __name__ == '__main__':
    test_get_cleaning_list()