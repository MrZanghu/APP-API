#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_List_Group_App(Read_ini.Config):
    def __init__(self):
        super(Get_List_Group_App,self).read_ini()

    def run_data(self,gcid,token,couponUserPhone):
        self.get_list_group_app= {
            "gcid": gcid,
            "token": token,
            "couponUserPhone": couponUserPhone}
        return self.get_list_group_app

    def run_get_list_group_app_data(self,url,data):
        self.get_list_group_app_data= json.dumps(data)
        self.get_list_group_app_data_result= requests.post(
            url= url,
            data= self.get_list_group_app_data)
        return self.get_list_group_app_data_result



def test_get_list_group_app():
    GLGA= Get_List_Group_App()
    list_= GLGA.run_get_list_group_app_data(
        url= GLGA.url_youhuiquan+'get_list_group_app',
        data= GLGA.run_data(
            GLGA.gcid,
            GLGA.token,
            GLGA.phone)).json()

    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_get_list_group_app()
