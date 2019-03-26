#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Renter_List(Read_ini.Config):
    def __init__(self):
        super(Get_Renter_List,self).read_ini()

    def run_data(self,indentChengzuId,token,indentType,phone):
        self.get_renter_list= {
            'indentChengzuId': indentChengzuId,
            'token':token,
            'indentType':indentType,
            'phone':phone
        }
        return self.get_renter_list

    def run_get_renter_list_data(self,url,data):
        self.get_renter_list_data_post= json.dumps(data)
        self.get_renter_list_result= requests.post(
            url= url,
            data= self.get_renter_list_data_post)
        return self.get_renter_list_result



def test_get_renter_list():
    # 用户可能有多个合同，使用list承接
    GRL= Get_Renter_List()
    chengzu_list_= []
    with open('ID_chengzu.txt','r') as C:
       for i in (C.read().split(',')):
           if i== '':
               # 切割后出现为空，去除
               pass
           else:
               chengzu_list_.append(GRL.run_get_renter_list_data(
                                url= GRL.url+'get_renter_list',
                                data= GRL.run_data(i,
                                                    GRL.token,
                                                    '1',
                                                    GRL.phone)).json()['result'])
                # 传1为预计支付账单，传2为历史账单
    print json.dumps(chengzu_list_, encoding='UTF-8', ensure_ascii=False)
    # for j in chengzu_list_:
    #     for k in j['result']['list']:
    #         # print json.dumps(k, encoding='UTF-8', ensure_ascii=False)+'\n'
    #         print k['type']['key'],k['id'],k['money'],k['predictTime']
    #         print



if __name__ == '__main__':
    test_get_renter_list()