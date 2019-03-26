#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Send_Verification_Code(Read_ini.Config):
    def __init__(self):
        super(Send_Verification_Code,self).read_ini()

    def run_data(self,gcid,token,phone,houseId):
        self.send_verification_code= {"gcid": gcid,
                                      "token": token,
                                      "phone": phone,
                                      "houseId": houseId}
        return self.send_verification_code

    def run_send_verification_code_data(self,url,data):
        self.send_verification_code_data= json.dumps(data)
        self.send_verification_code_data_result= requests.post(
            url= url,
            data= self.send_verification_code_data)
        return self.send_verification_code_data_result



def test_send_verification_code():
    SVC= Send_Verification_Code()
    list_= SVC.run_send_verification_code_data(
        url= SVC.url_XiuGaiMenSuo,
        data= SVC.run_data(
            SVC.gcid,
            SVC.token,
            SVC.phone,
            '2cb32cf2ad694f6eb064484ccb892a84')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_send_verification_code()