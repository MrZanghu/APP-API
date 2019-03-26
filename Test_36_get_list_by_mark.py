#-*- coding: UTF-8 -*-
import requests
import Read_ini
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class Get_List_By_Mark(Read_ini.Config):
    def __init__(self):
        super(Get_List_By_Mark,self).read_ini()

    def run_data(self,gcid,token,mark):
        self.get_list_by_mark= {
            "gcid": gcid,
            "token": token,
            "mark": mark}
        return self.get_list_by_mark

    def run_get_list_by_mark_data(self,url,data):
        self.get_list_by_mark_data= json.dumps(data)
        self.get_list_by_mark_data_result= requests.post(
            url= url,
            data= self.get_list_by_mark_data)
        return self.get_list_by_mark_data_result



def  test_get_list_by_mark(marks):
    try:
        os.remove('ID_marks.txt')
    except:
        pass
    GLBM= Get_List_By_Mark()
    list_= GLBM.run_get_list_by_mark_data(
        url= GLBM.url_zi_dian,
        data= GLBM.run_data(GLBM.gcid,GLBM.token,marks)).json()['result']['list']
        # json()后返回为dict
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False)+'\n'
        # 通过json方法打印出中文
        with open('ID_marks.txt','a+') as F:
            F.write(i['key']+':'+i['id']+',')



if __name__ == '__main__':
    # test_get_list_by_mark('0dc1fd1a-2991-4f43-8497-a144b644b3f0')
    ##资产配置
    test_get_list_by_mark('31841886-28ec-45dc-aaec-67c40f7a73fe')
    ##支付方式
