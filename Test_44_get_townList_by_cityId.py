#-*- coding: UTF-8 -*-
import Test_35_get_city_list
import requests
import Read_ini
import json



class Get_TownList_by_CityId(Read_ini.Config):
    def  __init__(self):
        super(Get_TownList_by_CityId,self).read_ini()

    def run_data(self,gcid,token,cityId):
        self.get_townList_by_cityId= {
            "gcid": gcid,
            "token": token,
            "cityId": cityId}
        return self.get_townList_by_cityId

    def run_get_townList_by_cityId_data(self,url,data):
        self.get_townList_by_cityId= json.dumps(data)
        self.get_townList_by_cityId_result= requests.post(
            url= url,
            data= self.get_townList_by_cityId)
        return self.get_townList_by_cityId_result



def test_get_townList_by_cityId():
    GTC= Get_TownList_by_CityId()
    townlist_= []
    for i in Test_35_get_city_list.test_get_city_list():
        list_= GTC.run_get_townList_by_cityId_data(
            url= GTC.url+'get_townList_by_cityId',
            data= GTC.run_data(
                GTC.gcid,
                GTC.token,
                i.values()[0])).json()['result']['list'] #i.values()返回字典的值是个list
        for j in list_:
            townlist_.append((j['cityName'],j['cityId'],j['townName'],j['id']))
            #  返回值为（城市、城市ID、区域、区域ID）
    # print json.dumps(townlist_, encoding='UTF-8', ensure_ascii=False)
    # print
    # print '*************************************************'
    # print
    return townlist_



if __name__ == '__main__':
    test_get_townList_by_cityId()