#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_39_get_houseNo_by_roomTypeId



class Get_House_Details(Read_ini.Config):
    def __init__(self):
        super(Get_House_Details,self).read_ini()

    def run_data(self,gcid,token,houseId):
        self.get_house_details= {
            "gcid": gcid,
            "token": token,
            "houseId": houseId}
        return self.get_house_details

    def run_get_house_details_data(self,url,data):
        self.get_house_details_data= json.dumps(data)
        self.get_house_details_data_result= requests.post(
            url= url,
            data= self.get_house_details_data)
        return self.get_house_details_data_result



def test_get_house_details():
    GHD= Get_House_Details()
    house_detail_dict= {}
    for i,j in Test_39_get_houseNo_by_roomTypeId.test_get_houseNo_by_roomTypeId().items():
        for m in range(0,len(j)):
            # 如果遇到房型下没有房间则rang(0,0)直接跳过
            house_detail_dict[j[m]['houseId']]= GHD.run_get_house_details_data(
                    url= GHD.url+'get_house_details',
                    data= GHD.run_data(
                        GHD.gcid,
                        GHD.token,
                        j[m]['houseId'])).json()['result']
    for k,l in house_detail_dict.items():
        print json.dumps(k, encoding='UTF-8', ensure_ascii=False),json.dumps(l, encoding='UTF-8', ensure_ascii=False)+'\n'
    print
    print '*************************************************'
    print
    return house_detail_dict


if __name__ == '__main__':
    test_get_house_details()