#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_City_List(Read_ini.Config):
    def __init__(self):
        super(Get_City_List,self).read_ini()

    def run_data(self,gcid,token):
        self.get_city_list= {
            "gcid": gcid,
            "token": token}
        return self.get_city_list

    def run_get_city_list_data(self,url,data):
        self.get_city_list_data= json.dumps(data)
        self.get_city_list_data_result= requests.post(
            url= url,
            data= self.get_city_list_data)
        return self.get_city_list_data_result



def test_get_city_list():
    ID_city= []
    GCL= Get_City_List()
    city_list= GCL.run_get_city_list_data(
        url= GCL.url+ 'get_city_list',
        data= GCL.run_data(
            GCL.gcid,
            GCL.token)).json()['result']['list']
    for i in city_list:
        ID_city.append({i['name']:i['id']})
        # 截取关键字并生成新的字典后加入列表
    for j in ID_city:
        print json.dumps(j, encoding='UTF-8', ensure_ascii=False)
    print
    print '*************************************************'
    print
    return ID_city
    # 返回形式为列表



if __name__ == '__main__':
    test_get_city_list()