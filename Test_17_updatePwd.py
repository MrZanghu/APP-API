#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class UpdatePwd(Read_ini.Config):
    def __init__(self):
        super(UpdatePwd,self).read_ini()

    def run_data(self,gcid,token,userphone,lockid,password,code,lockType):
        self.updatePwd= {"gcid": gcid,
                 "token": token,
                 "userphone": userphone,
                 "lockid": lockid,
                 "password": password,
                 "code": code,
                 "lockType": lockType}
        return self.updatePwd

    def run_updatePwd_data(self,url,data):
        self.updatePwd_data= json.dumps(data)
        self.updatePwd_data_result= requests.post(
            url= url,
            data= self.updatePwd_data)
        return self.updatePwd_data_result



def test_updatePwd():
    lock_cokes= raw_input('输入验证码:'+'\n')
    UP= UpdatePwd()
    list_= UP.run_updatePwd_data(
        url= UP.url+'updatePwd',
        data= UP.run_data(
            UP.gcid,
            UP.token,
            UP.phone,
            UP.lock_id,
            '963852',
            lock_cokes,
            '2')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_updatePwd()