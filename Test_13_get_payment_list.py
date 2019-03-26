#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Payment_List(Read_ini.Config):
    def __init__(self):
        super(Get_Payment_List,self).read_ini()

    def run_data(self,gcid,token,deptId):
        self.get_payment_list= {"gcid": gcid,
                                "token": token,
                                "deptId": deptId}
        return self.get_payment_list

    def run_get_payment_list_data(self,url,data):
        self.get_payment_list_data= json.dumps(data)
        self.get_payment_list_data_result= requests.post(
            url= url,
            data= self.get_payment_list_data)
        return self.get_payment_list_data_result



def test_get_payment_list():
    GPL= Get_Payment_List()
    list_= GPL.run_get_payment_list_data(
        url= GPL.url_ShuiDianBiao,
        data= GPL.run_data(
            GPL.gcid,
            GPL.token,
            '2d9dbec9ed72404eb834a7ed79eb4be4')).json()['result']['list']
    for i in list_:
        for j,k in i.items():
            print json.dumps(j, encoding='UTF-8', ensure_ascii=False),json.dumps(k, encoding='UTF-8', ensure_ascii=False)
        print '\n'



if __name__ == '__main__':
    test_get_payment_list()