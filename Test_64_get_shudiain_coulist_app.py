#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini


class Get_Shudiain_Coulist_App(Read_ini.Config):
    def __init__(self):
        super(Get_Shudiain_Coulist_App,self).read_ini()

    def run_data(self,gcid,token,houseId,money,phone,type):
        self.get_shudiain_coulist_app= {
            "gcid": gcid,
            "token": token,
            "houseId": houseId,
            "money": money,
            "phone": phone,
            "type":type}
        return self.get_shudiain_coulist_app

    def run_get_shudiain_coulist_app_data(self,url,data):
        self.get_shudiain_coulist_app_data= json.dumps(data)
        self.get_shudiain_coulist_app_data_result= requests.post(
            url= url,
            data= self.get_shudiain_coulist_app_data)
        return self.get_shudiain_coulist_app_data_result



def test_get_shudiain_coulist_app(houseId,money):
    GSCA= Get_Shudiain_Coulist_App()
    list_= GSCA.run_get_shudiain_coulist_app_data(
        url= GSCA.url_youhuiquan+'get_shudiain_coulist_app',
        data= GSCA.run_data(
            GSCA.gcid,
            GSCA.token,
            houseId,
            money,
            GSCA.phone,
            3)).json()['result']
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    # 一个水电优惠券id


if __name__ == '__main__':
    test_get_shudiain_coulist_app('5d0854da0f4049f382e68b833a3d851c',10)
    # 充值100元显示可用优惠券