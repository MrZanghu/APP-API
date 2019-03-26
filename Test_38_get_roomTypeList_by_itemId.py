#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_37_get_itemList_by_cityId



class Get_RoomTypeList_By_ItemId(Read_ini.Config):
    def __init__(self):
        super(Get_RoomTypeList_By_ItemId,self).read_ini()

    def run_data(self,gcid,token,houseItemId):
        self.get_roomTypeList_by_itemId={
            "gcid": gcid,
            "token": token,
            "houseItemId": houseItemId}
        return self.get_roomTypeList_by_itemId

    def run_get_roomTypeList_by_itemId_data(self,url,data):
        self.get_roomTypeList_by_itemId_data= json.dumps(data)
        self.get_roomTypeList_by_itemId_data_result= requests.post(
            url= url,
            data= self.get_roomTypeList_by_itemId_data)
        return self.get_roomTypeList_by_itemId_data_result



def test_get_roomTypeList_by_itemId():
    GRBI= Get_RoomTypeList_By_ItemId()
    roomTypeList_= {}
    for i in Test_37_get_itemList_by_cityId.test_get_itemList_by_cityId():
        for k in i.values():
            for m in range(0,len(k)):
                roomTypeList_[k[m]['houseItemName']]= (GRBI.run_get_roomTypeList_by_itemId_data(
                    url= GRBI.url+'get_roomTypeList_by_itemId',
                    data= GRBI.run_data(
                        GRBI.gcid,
                        GRBI.token,
                        k[m]['id'])).json()['result']['list'])
                # 添加字典，键为项目名称，值为项目房型s
    for j,h in roomTypeList_.items():
        print json.dumps(j, encoding='UTF-8', ensure_ascii=False),json.dumps(h, encoding='UTF-8', ensure_ascii=False)+'\n'
    print
    print '*************************************************'
    print
    return roomTypeList_



if __name__ == '__main__':
    test_get_roomTypeList_by_itemId()
