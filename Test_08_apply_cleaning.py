#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Apply_Cleaning(Read_ini.Config):
    def __init__(self):
        super(Apply_Cleaning,self).read_ini()

    def run_data(self,gcid,token,customer,customerCalls,houseId,repairServiceContent,description,expectCompletionTime):
        self.apply_cleaning= {
            "gcid": gcid,
            "token": token,
            "customer": customer,
            "customerCalls": customerCalls,
            "houseId": houseId,
            "repairServiceContent": repairServiceContent,
            "description": description,
            "expectCompletionTime": expectCompletionTime}
        return self.apply_cleaning

    def run_apply_cleaning_data(self,url,data):
        self.apply_cleaning_data= json.dumps(data)
        self.apply_cleaning_data_result= requests.post(
            url= url,
            data= self.apply_cleaning_data)
        return self.apply_cleaning_data_result



def test_apply_cleaning():
    AC= Apply_Cleaning()
    list_= AC.run_apply_cleaning_data(
        url= AC.url+'apply_cleaning',
        data= AC.run_data(
            AC.gcid,
            AC.token,
            '租客姓名1',
            '15311305641',
            '2c9965ba41a846728ff8c698292f873c',
            '标题 【备注】',
            '详细描述',
            '2018-07-11 15:42:32')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_apply_cleaning()