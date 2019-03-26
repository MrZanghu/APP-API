#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Complaint_Letter_List(Read_ini.Config):
    def __init__(self):
        super(Get_Complaint_Letter_List,self).read_ini()

    def run_data(self,gcid,token,customerCalls):
        self.get_complaint_letter_list= {
            "gcid": gcid,
            "token": token,
            "customerCalls": customerCalls}
        return self.get_complaint_letter_list

    def run_get_complaint_letter_list_data(self,url,data):
        self.get_complaint_letter_list_data= json.dumps(data)
        self.get_complaint_letter_list_data_result= requests.post(
            url= url,
            data= self.get_complaint_letter_list_data)
        return self.get_complaint_letter_list_data_result



def test_get_complaint_letter_list():
    GCLL= Get_Complaint_Letter_List()
    list_= GCLL.run_get_complaint_letter_list_data(
        url= GCLL.url+'get_complaint_letter_list',
        data= GCLL.run_data(
            GCLL.gcid,
            GCLL.token,
            GCLL.phone)).json()['result']['list']
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False)+'\n'



if __name__ == '__main__':
    test_get_complaint_letter_list()