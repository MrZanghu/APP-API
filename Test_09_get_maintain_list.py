#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Maintain_List(Read_ini.Config):
    def __init__(self):
        super(Get_Maintain_List,self).read_ini()

    def run_data(self,gcid,token,phone):
        self.get_maintain_list= {
            "gcid": gcid,
            "token": token,
            "phone": phone}
        return self.get_maintain_list

    def run_get_maintain_list_data(self,url,data):
        self.get_maintain_list_data= json.dumps(data)
        self.get_maintain_list_data_result= requests.post(
            url= url,
            data= self.get_maintain_list_data)
        return self.get_maintain_list_data_result



def test_get_maintain_list():
    GML= Get_Maintain_List()
    list_= GML.run_get_maintain_list_data(
        url= GML.url+'get_maintain_list',
        data= GML.run_data(
            GML.gcid,
            GML.token,
            GML.phone)).json()['result']['list']
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False) + '\n'



if __name__ == '__main__':
    test_get_maintain_list()