#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class GetDiscount_ClientApp(Read_ini.Config):
    def __init__(self):
        super(GetDiscount_ClientApp,self).read_ini()

    def run_data(self,gcid,token,houseId,startTime,endTime):
        self.getDiscount_clientApp= {
            "gcid": gcid,
            "token": token,
            "houseId": houseId,
            "startTime": startTime,
            "endTime": endTime}
        return self.getDiscount_clientApp

    def run_getDiscount_clientApp_data(self,url,data):
        self.getDiscount_clientApp_data= json.dumps(data)
        self.getDiscount_clientApp_data_result= requests.post(
            url= url,
            data= self.getDiscount_clientApp_data)
        return self.getDiscount_clientApp_data_result



def test_getDiscount_clientApp(houseIds):
    GDC= GetDiscount_ClientApp()
    Discount= []
    list_= GDC.run_getDiscount_clientApp_data(
        url= GDC.url+'getDiscount_clientApp',
        data= GDC.run_data(
            GDC.gcid,
            GDC.token,
            houseIds,
            '2018-11-22',
            '2019-11-21')).json()['result']['list']
    # print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    for i in list_:
        Discount.append({i['activeName']:i['id']})
    return Discount



if __name__ == '__main__':
    print json.dumps(test_getDiscount_clientApp('fc4a88b685e54148bb216847a93eca79'),
                     encoding='UTF-8', ensure_ascii=False)

