#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_23_get_roomType_details



class Cancel_HouseCollection(Read_ini.Config):
    def __init__(self):
        super(Cancel_HouseCollection,self).read_ini()

    def run_data(self,gcid,token,roomTypeId,phone,collectionId):
        self.cancel_houseCollection= {
            "gcid": gcid,
            "token": token,
            "roomTypeId": roomTypeId,
            "phone": phone,
            "collectionId":collectionId}
        return self.cancel_houseCollection

    def run_cancel_houseCollection_data(self,url,data):
        self.cancel_houseCollection_data= json.dumps(data)
        self.cancel_houseCollection_data_result= requests.post(
            url= url,
            data= self.cancel_houseCollection_data)
        return self.cancel_houseCollection_data_result



def test_cancel_houseCollection(roomTypeIds,collectionIds):
    CHC= Cancel_HouseCollection()
    list_= CHC.run_cancel_houseCollection_data(
        url= CHC.url+'cancel_houseCollection',
        data= CHC.run_data(
            CHC.gcid,
            CHC.token,
            roomTypeIds,
            CHC.phone,
            collectionIds)).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_cancel_houseCollection('38E3A01AF817034F5579A9BB28731DFB94B1',
                                Test_23_get_roomType_details.test_get_roomType_details(
                                    '38E3A01AF817034F5579A9BB28731DFB94B1'))
