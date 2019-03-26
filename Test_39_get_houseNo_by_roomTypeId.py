#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_38_get_roomTypeList_by_itemId

import sys
reload(sys)
sys.setdefaultencoding('utf8')



class Get_HouseNo_By_RoomTypeId(Read_ini.Config):
    # 房间只展示20%
    def __init__(self):
        super(Get_HouseNo_By_RoomTypeId,self).read_ini()

    def run_data(self,gcid,token,roomTypeId):
        self.get_houseNo_by_roomTypeId= {
            "gcid": gcid,
            "token": token,
            "roomTypeId": roomTypeId}
        return self.get_houseNo_by_roomTypeId

    def run_get_houseNo_by_roomTypeId_data(self,url,data):
        self.get_houseNo_by_roomTypeId_data= json.dumps(data)
        self.get_houseNo_by_roomTypeId_data_result= requests.post(
            url= url,
            data= self.get_houseNo_by_roomTypeId_data)
        return self.get_houseNo_by_roomTypeId_data_result



def test_get_houseNo_by_roomTypeId():
    GHBR= Get_HouseNo_By_RoomTypeId()
    houseNoList_dict= {}
    for i,j in Test_38_get_roomTypeList_by_itemId.test_get_roomTypeList_by_itemId().items():
        for k in j:
            houseNoList_dict[str(i)+'--'+str(k['roomTypeName'])]= (GHBR.run_get_houseNo_by_roomTypeId_data(
                url= GHBR.url+'get_houseNo_by_roomTypeId',
                data= GHBR.run_data(
                    GHBR.gcid,
                    GHBR.token,
                    k['roomTypeId'])).json()['result']['list'])
    for m,n in houseNoList_dict.items():
        print json.dumps(m, encoding='UTF-8', ensure_ascii=False),json.dumps(n, encoding='UTF-8', ensure_ascii=False)
    print
    print '*************************************************'
    print
    return houseNoList_dict



if __name__ == '__main__':
    test_get_houseNo_by_roomTypeId()