#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Cancel_Appointment(Read_ini.Config):
    def __init__(self):
        super(Cancel_Appointment,self).read_ini()

    def run_data(self,gcid,token,id,phone):
        self.get_reservation_list= {
            "gcid": gcid,
            "token": token,
            "id":id,
            "phone": phone}
        return self.get_reservation_list

    def run_get_reservation_list_data(self,url,data):
        self.get_reservation_list_data= json.dumps(data)
        self.get_reservation_list_data_result= requests.post(
            url= url,
            data= self.get_reservation_list_data)
        return self.get_reservation_list_data_result



def test_get_reservation_list():
    CA= Cancel_Appointment()
    list_= CA.run_get_reservation_list_data(
        url= CA.url+'cancel_appointment',
        data= CA.run_data(
            CA.gcid,
            CA.token,
            '2824f406f415430f8a0f9f4c6311d213',
            CA.phone)).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_get_reservation_list()