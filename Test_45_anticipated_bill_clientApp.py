#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Anticipated_Bill_ClientApp(Read_ini.Config):
    def __init__(self):
        super(Anticipated_Bill_ClientApp,self).read_ini()

    def run_data(self,gcid,token,beginDate,
                 endDate,houseId,feiYongTypeId,
                 payTypeId,monthMoney,dids,yaJin):
        self.anticipated_bill_clientApp= {
            "gcid": gcid,
            "token": token,
            "beginDate": beginDate,
            "endDate": endDate,
            "prepaymentDaysType": '1',
            "prepaymentDays": '1',
            "houseId": houseId,
            "feiYongTypeId": feiYongTypeId,
            "payTypeId": payTypeId,
            "monthMoney": monthMoney,
            "dids":dids,
            "yaJin": yaJin,
            "type": '1',
            "isJizhong": '1',
            "signType":'1'}
        return self.anticipated_bill_clientApp

    def run_anticipated_bill_clientApp_data(self,url,data):
        self.anticipated_bill_clientApp_data= json.dumps(data)
        self.anticipated_bill_clientApp_data_result= requests.post(
            url= url,
            data= self.anticipated_bill_clientApp_data)
        return self.anticipated_bill_clientApp_data_result



def test_anticipated_bill_clientApp():
    ABC= Anticipated_Bill_ClientApp()
    list_= ABC.run_anticipated_bill_clientApp_data(
        url= ABC.url_zhangdan+'anticipated_revenue_kangqiaoExpend',
        data= ABC.run_data(
            ABC.gcid,
            ABC.token,
            "2018-11-22",
            "2019-01-21",
            "fc4a88b685e54148bb216847a93eca79",
            "933283b8-3447-4582-b893-9ac266f387ce",
            "f47a2e66827e4c34b53d3d1b058b6eee",
            "6940",
            [],
            "6940")).json()['result']['list']

    for i in list_:
        i['typeId']= i['feiYongTypeId']
        i['isIncludeDJ']= 0
        i['beginTime']= i['bqBeginDate']
        i['desc']= i['feiYongDesc']
        i['endTime']= i['bqEndDate']
        i['money']= i['bqMonthMoney']
        i['predictTime']= i['bqBackPayDate']
        i.pop('feiYongTypeId')
        i.pop('bqBeginDate')
        i.pop('feiYongDesc')
        i.pop('bqEndDate')
        i.pop('bqMonthMoney')
        i.pop('bqBackPayDate')
    # for k in list_:
    #     print json.dumps(k, encoding='UTF-8', ensure_ascii=False)+'\n'
    return list_
    # 替换key值给48在线签约使用



if __name__ == '__main__':
    test_anticipated_bill_clientApp()