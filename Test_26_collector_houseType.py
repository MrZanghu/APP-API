#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Collector_HouseType(Read_ini.Config):
    def __init__(self):
        super(Collector_HouseType,self).read_ini()

    def run_data(self,gcid,token,houseUserName,phone,roomTypeId):
        self.get_favorites_list= {
            "gcid": gcid,
            "token": token,
            "houseUserName": houseUserName,
            "phone": phone,
            "roomTypeId": roomTypeId}
        return self.get_favorites_list

    def run_collector_houseType_data(self,url,data):
        self.collector_houseType_data= json.dumps(data)
        self.collector_houseType_data_result= requests.post(
            url= url,
            data= self.collector_houseType_data)
        return self.collector_houseType_data_result



def test_collector_houseType():
    CH= Collector_HouseType()
    list_= CH.run_collector_houseType_data(
        url= CH.url+ 'collector_houseType',
        data= CH.run_data(
            CH.gcid,
            CH.token,
            '你们都',
            15311305641,
            '38E3A01AF817034F5579A9BB28731DFB94B1')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_collector_houseType()