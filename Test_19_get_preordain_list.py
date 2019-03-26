#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Preordain_List(Read_ini.Config):
    def __init__(self):
        super(Get_Preordain_List,self).read_ini()

    def run_data(self,gcid,token,phone):
        self.get_preordain_list= {
            "gcid": gcid,
            "token": token,
            "phone": phone}
        return self.get_preordain_list

    def run_get_preordain_list_data(self,url,data):
        self.get_preordain_list_data= json.dumps(data)
        self.get_preordain_list_data_result= requests.post(
            url= url,
            data= self.get_preordain_list_data)
        return self.get_preordain_list_data_result



def test_get_preordain_list():
    null_list= []
    GPL= Get_Preordain_List()
    list_= GPL.run_get_preordain_list_data(
        url= GPL.url+'get_preordain_list',
        data= GPL.run_data(
            GPL.gcid,
            GPL.token,
            GPL.phone)).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    print
    for i in range(0,len(list_['result']['list'])):
        null_list.append((list_['result']['list'][i]['id'],
                          list_['result']['list'][i]['tbsId']))
    return null_list
    # 返回字典中result的值，为预定列表，取(预定id,收支id)



if __name__ == '__main__':
    print test_get_preordain_list()