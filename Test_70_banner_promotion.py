#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_35_get_city_list



class Banner_Promotion(Read_ini.Config):
    def __init__(self):
        super(Banner_Promotion,self).read_ini()

    def run_data(self,gcid,token,cityId):
        self.banner_promotion= {
            "gcid": gcid,
            "token":token,
            "cityId":cityId,
            "equipment": "2"}
        # 2是APP的banner
        return self.banner_promotion

    def run_banner_promotion_data(self,url,data):
        self.banner_promotion_data= json.dumps(data)
        self.banner_promotion_data_result= requests.post(
            url= url,
            data= self.banner_promotion_data)
        return self.banner_promotion_data_result



def test_banner_promotion(ids):
    BP= Banner_Promotion()
    list_all= []
    for i in ids:
        for m,n in i.items():
            list_all.append(BP.run_banner_promotion_data(
                url= BP.url+'banner_promotion',
                data= BP.run_data(
                    BP.gcid,
                    BP.token,
                    n)).json()['result'])
    print json.dumps(list_all, encoding='UTF-8', ensure_ascii=False)




if __name__ == '__main__':
    test_banner_promotion(Test_35_get_city_list.test_get_city_list())
    # def a(n):
    #     x= n
    #     def b():
    #         return x+1
    #     return b()
    #
    # print a(1)