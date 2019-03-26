#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_App_Dikou_Money(Read_ini.Config):
    def __init__(self):
        super(Get_App_Dikou_Money,self).read_ini()

    def run_data(self,gcid,token,cid,bid):
        self.get_app_dikou_money= {
            "gcid": gcid,
            "token": token,
            "json": [
                {"cid": cid,"bid": bid}
            ]
        }
        return self.get_app_dikou_money

    def run_get_app_dikou_money_data(self,url,data):
        self.get_app_dikou_money_data= json.dumps(data)
        self.get_app_dikou_money_data_result= requests.post(
            url= url,
            data= self.get_app_dikou_money_data)
        return self.get_app_dikou_money_data_result



def test_get_app_dikou_money(cid_list,bid_list):
    GADM= Get_App_Dikou_Money()
    list_= GADM.run_get_app_dikou_money_data(
        url= GADM.url_youhuiquan+'get_app_dikou_money',
        data= GADM.run_data(
            GADM.gcid,
            GADM.token,
            cid_list,
            bid_list)).json()['result']
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)


if __name__ == '__main__':
    test_get_app_dikou_money(['192aa225bd9e48b18b44164eb7d5ab72'],
                             ['34042ec7ba554955afbe27f409ec4bd6','736327aebfb945cdaf68bd502ac2133d'])