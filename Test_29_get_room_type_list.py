#-*- coding: UTF-8 -*-
import Test_27_get_item_list as GIL
import requests
import json
import Read_ini



class Get_Room_Type_List(Read_ini.Config):
    def __init__(self):
        super(Get_Room_Type_List,self).read_ini()

    def run_data(self,gcid,token,houseItemId):
        self.get_room_type_list= {
            "gcid": gcid,
            "token": token,
            "houseItemId": houseItemId}
        return self.get_room_type_list

    def run_get_room_type_list_data(self,url,data):
        self.get_room_type_list_data= json.dumps(data)
        self.get_room_type_list_data_result= requests.post(
            url= url,
            data= self.get_room_type_list_data)
        return self.get_room_type_list_data_result



def test_get_room_type_list():
    room_type_list= []
    GRTL= Get_Room_Type_List()
    for i in GIL.test_get_item_list('2018-09-06','desc'):
        room_type_list.append(GRTL.run_get_room_type_list_data(
            url= GRTL.url+'get_room_type_list',
            data= GRTL.run_data(
                GRTL.gcid,
                GRTL.token,
                i[1])).json()['result']['list'])
    for j in room_type_list:
        for k in range(0,len(j)):
            print json.dumps(j[k], encoding='UTF-8', ensure_ascii=False) + '\n'



if __name__ == '__main__':
    test_get_room_type_list()