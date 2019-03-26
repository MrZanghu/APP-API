#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Reservation_List(Read_ini.Config):
    def __init__(self):
        # 数据库中processstatus为4时不查询
        super(Get_Reservation_List,self).read_ini()

    def run_data(self,gcid,token,phone):
        self.get_reservation_list= {
            "gcid": gcid,
            "token": token,
            "phone": phone}
        return self.get_reservation_list

    def run_get_reservation_list_data(self,url,data):
        self.get_reservation_list_data= json.dumps(data)
        self.get_reservation_list_data_result= requests.post(
            url= url,
            data= self.get_reservation_list_data)
        return self.get_reservation_list_data_result



def test_get_reservation_list():
    GRL= Get_Reservation_List()
    list_= GRL.run_get_reservation_list_data(
        url= GRL.url+'get_reservation_list',
        data= GRL.run_data(
            GRL.gcid,
            GRL.token,
            GRL.phone)).json()['result']['renterInfoArr']
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_get_reservation_list()