#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class ServiceRating(Read_ini.Config):
    def __init__(self):
        super(ServiceRating,self).read_ini()
        # 数据库表名为item_evaluation_

    def run_data(self,gcid,token,
                 serviceAttitude,
                 processingSpeed,
                 hardwareFacilities,
                 environmentalHygiene,
                 safetyManagement,
                 userId,
                 houseItemId,
                 remark):
        self.serviceRating= {
            "gcid": gcid,
            "token": token,
            "serviceAttitude": serviceAttitude,
            "processingSpeed": processingSpeed,
            "hardwareFacilities": hardwareFacilities,
            "environmentalHygiene": environmentalHygiene,
            "safetyManagement": safetyManagement,
            "userId": userId,
            "houseItemId": houseItemId,
            "remark": remark}
        return self.serviceRating

    def run_serviceRating_data(self,url,data):
        self.serviceRating_data= json.dumps(data)
        self.serviceRating_data_result= requests.post(
            url= url,
            data= self.serviceRating_data)
        return self.serviceRating_data_result



def test_serviceRating():
    SR= ServiceRating()
    list_= SR.run_serviceRating_data(
        url= SR.url+'serviceRating',
        data= SR.run_data(
            SR.gcid,
            SR.token,
            '5',
            '5',
            '5',
            '5',
            '5',
            SR.userid,
            '9D84E5A96DBB6L4CE2KAEA7VDB182AB8087A',
            '测试备注')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_serviceRating()
