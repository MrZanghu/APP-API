#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class WeChat_Remote_Unlocking(Read_ini.Config):
    def __init__(self):
        super(WeChat_Remote_Unlocking,self).read_ini()

    def run_data(self,gcid,token,houseId,userPhone,lockId,lockType):
        self.weChatRemoteUnlocking= {"gcid": gcid,
                                     "token": token,
                                     "houseId": houseId,
                                     "userPhone": userPhone,
                                     "lockId": lockId,
                                     "lockType": lockType}
        return self.weChatRemoteUnlocking

    def  run_weChatRemoteUnlocking_data(self,url,data):
        self.weChatRemoteUnlocking_data= json.dumps(data)
        self.weChatRemoteUnlocking_data_result= requests.post(
            url= url,
            data= self.weChatRemoteUnlocking_data)
        return self.weChatRemoteUnlocking_data_result



def test_weChatRemoteUnlocking():
    WRU= WeChat_Remote_Unlocking()
    list_= WRU.run_weChatRemoteUnlocking_data(
        url= WRU.url+'weChatRemoteUnlocking',
        data= WRU.run_data(
            WRU.gcid,
            WRU.token,
            '2c9965ba41a846728ff8c698292f873c',
            WRU.phone,
            WRU.lock_id,
            '2')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_weChatRemoteUnlocking()