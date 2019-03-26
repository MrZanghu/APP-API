#-*- coding: UTF-8 -*-
import random
import string
import requests
import json
import csv
import time



class House_zi_dian():
    def __init__(self):
        self.gcid= '0371070'
        self.url= 'http://192.168.1.222/v2/sys/zi_dian/save'
        self.desc= ''
        self.id= ''.join(random.sample(string.ascii_letters + string.digits, 36))

    def run_data(self,key,parentId,typeId,sysDesc,order,value):
        self.zi_dians= {
            'key':key,
            'parentId':parentId,
            'typeId':typeId,
            'sysDesc':sysDesc,
            'order':order,
            'value':value,
            'desc':self.desc,
            'id':self.id,
            'gcid':self.gcid,
            'token':'7c7af195-3bb0-405e-8760-0a359eaf08ad',
            'userid':'8e9245d7c0cc43a6aaf5a7394c8e7d18'
        }
        return self.zi_dians

    def run_data2(self,key,parentId,sysDesc):
        self.zi_dians2= {
            'key':key,
            'parentId':parentId,
            'sysDesc':sysDesc,
            'desc':self.desc,
            'id':self.id,
            'gcid':self.gcid,
            'token':'7c7af195-3bb0-405e-8760-0a359eaf08ad',
            'userid':'8e9245d7c0cc43a6aaf5a7394c8e7d18'
        }
        return self.zi_dians2

    def run_house_zi_dian_data(self,url,data):
        self.run_house_zi_dian_data_post= json.dumps(data)
        self.run_house_zi_dian_data_result= requests.post(
            url= url,
            data= self.run_house_zi_dian_data_post
        )
        return self.run_house_zi_dian_data_result



if __name__ == '__main__':
    files= csv.reader(open('/Users/violet/Downloads/3level.csv', 'r'))
    for i in files:
        # test_zi_dian = House_zi_dian()
        # list_= test_zi_dian.run_house_zi_dian_data(
        #     url= test_zi_dian.url,
        #     data= test_zi_dian.run_data(
        #         i[0].decode('GB2312').encode('utf-8'),
        #         i[1],
        #         i[2],
        #         i[3],
        #         i[4],
        #         i[5]
        #     )
        # )
        # print list_.content
        ## 二级
        test_zi_dian = House_zi_dian()
        list_= test_zi_dian.run_house_zi_dian_data(
            url= test_zi_dian.url,
            data= test_zi_dian.run_data2(
                i[0].decode('GB2312').encode('utf-8'),
                i[1],
                i[2]
            )
        )
        print list_.content
    time.sleep(1)



