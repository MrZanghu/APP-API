#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini


class Get_Code(Read_ini.Config):
    def __init__(self):
        super(Get_Code,self).read_ini()

    def run_code(self,url,dicts):
        self.data= json.dumps(dicts)
        self.result= requests.post(
            url= url,data= self.data)
        return self.result



def test_get_code():
    getcode= Get_Code()
    list_= getcode.run_code(
        getcode.url+'get_code',
        {'phone':getcode.phone,
         'gcid':getcode.gcid}).json()
    # print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    # 打印出中文结果
    return list_['result']['code']



if __name__ == '__main__':
    test_get_code()