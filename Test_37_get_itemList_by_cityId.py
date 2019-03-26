#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_35_get_city_list



class Get_ItemList_By_CityId(Read_ini.Config):
    def __init__(self):
        super(Get_ItemList_By_CityId,self).read_ini()

    def run_data(self,gcid,token,cityId):
        self.get_itemList_by_cityId={
            "gcid": gcid,
            "token": token,
            "cityId": cityId}
        return self.get_itemList_by_cityId

    def run_get_itemList_by_cityId_data(self,url,data):
        self.get_itemList_by_cityId_data= json.dumps(data)
        self.get_itemList_by_cityId_result= requests.post(
            url= url,
            data= self.get_itemList_by_cityId_data)
        return self.get_itemList_by_cityId_result



def test_get_itemList_by_cityId():
    GIBC= Get_ItemList_By_CityId()
    itemList_= []
    for i in Test_35_get_city_list.test_get_city_list():
        for j,k in i.items():
            itemList_.append({j:GIBC.run_get_itemList_by_cityId_data(
                url= GIBC.url+'get_itemList_by_cityId',
                data= GIBC.run_data(
                    GIBC.gcid,
                    GIBC.token,
                    k)).json()['result']['list']})
                    # 生成{城市:项目}字典
    for m in itemList_:
        print json.dumps(m, encoding='UTF-8', ensure_ascii=False)
    print
    print '*************************************************'
    print
    return itemList_



if __name__ == '__main__':
    test_get_itemList_by_cityId()