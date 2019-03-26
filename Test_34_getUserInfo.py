#-*- coding: UTF-8 -*-
import requests
import Read_ini
import json



class GetUserInfo(Read_ini.Config):
    def __init__(self):
        super(GetUserInfo,self).read_ini()

    def run_data(self,gcid,token):
        self.getUserInfo={
            "gcid": gcid,
            "token": token}
        return self.getUserInfo

    def run_getUserInfo_data(self,url,data):
        self.getUserInfo_data= json.dumps(data)
        self.getUserInfo_data_result= requests.post(
            url= url,
            data= self.getUserInfo_data)
        return self.getUserInfo_data_result



def test_getUserInfo():
    GUI= GetUserInfo()
    list_= GUI.run_getUserInfo_data(
        url= GUI.url+'getUserInfo',
        data= GUI.run_data(
            GUI.gcid,
            GUI.token)).json()['result']

    for i,j in list_.items():
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False) +':'+\
              json.dumps(j, encoding='UTF-8', ensure_ascii=False)

    return list_



if __name__ == '__main__':
    test_getUserInfo()
