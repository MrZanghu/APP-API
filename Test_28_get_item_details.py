#-*- coding: UTF-8 -*-
import Test_27_get_item_list as GIL
import requests
import json
import Read_ini



class Get_Item_Details(Read_ini.Config):
    def __init__(self):
        super(Get_Item_Details,self).read_ini()

    def run_data(self,gcid,token,houseItemId):
        self.get_item_details= {
            "gcid": gcid,
            "token": token,
            "houseItemId": houseItemId}
        return self.get_item_details

    def run_get_item_details_data(self,url,data):
        self.get_item_details_data= json.dumps(data)
        self.get_item_details_data_result= requests.post(
            url= url,
            data= self.get_item_details_data)
        return self.get_item_details_data_result



def test_get_item_details():
    item_details_list= []
    GID= Get_Item_Details()
    for i in GIL.test_get_item_list('2018-08-20','desc'):
        item_details_list.append(
            GID.run_get_item_details_data(
                url= GID.url+'get_item_details',
                data= GID.run_data(
                    GID.gcid,
                    GID.token,
                    i[1])).json()['result'])
    for j in item_details_list:
        print json.dumps(j, encoding='UTF-8', ensure_ascii=False) + '\n'



if __name__ == '__main__':
    test_get_item_details()

