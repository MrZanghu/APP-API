#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_RoomType_Details(Read_ini.Config):
    def __init__(self):
        super(Get_RoomType_Details,self).read_ini()

    def run_data(self,gcid,token,id):
        self.get_roomType_details={
            "gcid": gcid,
            "token": token,
            "id": id}
        return self.get_roomType_details

    def run_get_roomType_details_data(self,url,data):
        self.get_roomType_details_data= json.dumps(data)
        self.get_roomType_details_data_result= requests.post(
            url= url,
            data= self.get_roomType_details_data)
        return self.get_roomType_details_data_result



def test_get_roomType_details(ids):
    GRTD= Get_RoomType_Details()
    list_= GRTD.run_get_roomType_details_data(
        url= GRTD.url+'get_roomType_details',
        data= GRTD.run_data(
            GRTD.gcid,
            GRTD.token,
            ids)).json()['result']
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    # 返回pic中为list，图片轮播用
    if list_['collectionStatus']== 1:
        return list_['collectionId']



if __name__ == '__main__':
    test_get_roomType_details("4ECCA851GE7C0X4134BA87BC7F8276D2CFD5")
