#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_35_get_city_list



class Business_Recommendation(Read_ini.Config):
    def __init__(self):
        super(Business_Recommendation,self).read_ini()

    def run_data(self,gcid,token,cityId):
        self.business_recommendation= {
            "gcid":gcid,
            "token":token,
            "cityId":cityId}
        return self.business_recommendation

    def run_business_recommendation_data(self,url,data):
        self.business_recommendation_data= json.dumps(data)
        self.business_recommendation_data_result= requests.post(
            url= url,
            data= self.business_recommendation_data)
        return self.business_recommendation_data_result



def test_business_recommendation(ids):
    list_all= []
    BR= Business_Recommendation()
    for i in ids:
        for m,n in i.items():
            list_all.append(BR.run_business_recommendation_data(
                url= BR.url+'business_recommendation',
                data= BR.run_data(
                    BR.gcid,
                    BR.token,
                    n)).json()['result'])
    print json.dumps(list_all, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_business_recommendation(Test_35_get_city_list.test_get_city_list())