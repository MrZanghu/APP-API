#-*- coding: UTF-8 -*-
import Pics_Lists_for_all as PLFA
import requests
import Read_ini
import json



class Apply_Maintain(Read_ini.Config):
    def __init__(self):
        super(Apply_Maintain,self).read_ini()

    def run_data(self,gcid,token,customer,customerCalls,houseId,
                 repairServiceContent,description,typeId,urls,
                 fileType,picName,expectCompletionTime,noOneCanRepair):
        self.apply_maintain= {
            "gcid": gcid,
            "token": token,
            "customer": customer,
            "customerCalls": customerCalls,
            "houseId": houseId,
            "repairServiceContent": repairServiceContent,
            "description": description,
            "typeId": typeId,
            "urls":urls,
            "fileType": fileType,
            "picName": picName,
            "expectCompletionTime": expectCompletionTime,
            "noOneCanRepair": noOneCanRepair}
        return self.apply_maintain

    def run_apply_maintain_data(self,url,data):
        self.apply_maintain_data= json.dumps(data)
        self.apply_maintain_data_result= requests.post(
            url= url,
            data= self.apply_maintain_data)
        return self.apply_maintain_data_result



def test_apply_maintain():
    PL= PLFA.Pics_lits('Picture')
    url_list= []
    for i in PL.get_P_list():
        url_list.append(PLFA.Insert_Pic(i).re_url()['url'])
    AM= Apply_Maintain()
    list_= AM.run_apply_maintain_data(
        url= AM.url+ "apply_maintain",
        data= AM.run_data(
            AM.gcid,
            AM.token,
            '翟伯洋测试',
            '15311305641',
            '2c9965ba41a846728ff8c698292f873c',
            '标题【备注】',
            '详细描述',
            'a44525e651de4bc6807cc63c7d624cb3',
            url_list,
            'pass',
            'pass',
            '2018-08-27 16:42:32',
            '2')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_apply_maintain()