#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Suggestions(Read_ini.Config):
    def __init__(self):
        super(Suggestions,self).read_ini()

    def run_data(self,gcid,token,customer,customerCalls,contractNumber,houseId,repairContent,repairServiceContent):
        self.suggestions= {
            "gcid": gcid,
            "token": token,
            "customer": customer,
            "customerCalls": customerCalls,
            "contractNumber": contractNumber,
            "houseId": houseId,
            "repairContent": repairContent,
            "repairServiceContent": repairServiceContent}
        return self.suggestions

    def run_suggestions_data(self,url,data):
        self.suggestions_data= json.dumps(data)
        self.suggestions_data_result= requests.post(
            url= url,
            data= self.suggestions_data)
        return self.suggestions_data_result



def test_suggestions(contractNumber,houseId):
    SG= Suggestions()
    list_= SG.run_suggestions_data(
        url= SG.url+'suggestions',
        data= SG.run_data(
            SG.gcid,
            SG.token,
            '测试投诉建议姓名2',
            SG.phone,
            contractNumber,
            houseId,
            '投诉内容2',
            '投诉标题2')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_suggestions('7849C3C0S9345W4CB5M8706TD985BF9A2605','e0f505f4d0ed466c82d8967754a1af65')