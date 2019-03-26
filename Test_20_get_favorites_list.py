#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Favorites_List(Read_ini.Config):
    def __init__(self):
        super(Get_Favorites_List,self).read_ini()

    def run_data(self,gcid,token,phone):
        self.get_favorites_list= {
            "gcid": gcid,
            "token": token,
            "phone": phone}
        return self.get_favorites_list

    def run_get_favorites_list_data(self,url,data):
        self.get_favorites_list_data= json.dumps(data)
        self.get_favorites_list_data_result= requests.post(
            url= url,
            data= self.get_favorites_list_data)
        return self.get_favorites_list_data_result



def test_get_favorites_list():
    GFL= Get_Favorites_List()
    list_= GFL.run_get_favorites_list_data(
        url= GFL.url+'get_favorites_list',
        data= GFL.run_data(
            GFL.gcid,
            GFL.token,
            GFL.phone)).json()['result']['list']
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False)+'\n'


if __name__ == '__main__':
    test_get_favorites_list()