#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Get_Coupon_List_By_App(Read_ini.Config):
    def __init__(self):
        super(Get_Coupon_List_By_App,self).read_ini()

    def run_data(self,gcid,token,chengzuId,phone):
        self.get_coupon_list_by_app= {
            "gcid": gcid,
            "token": token,
            "chengzuId": chengzuId,
            "phone": phone
        }
        return self.get_coupon_list_by_app

    def run_get_coupon_list_by_app_data(self,url,data):
        self.get_coupon_list_by_app_data= json.dumps(data)
        self.get_coupon_list_by_app_data_result= requests.post(
            url= url,
            data= self.get_coupon_list_by_app_data)
        return self.get_coupon_list_by_app_data_result



def test_get_coupon_list_by_app():
    CID= []
    # 用来存成租ID
    with open('ID_chengzu.txt') as C:
        for i in (C.read().split(',')):
            if i == '':
                # 切割后出现为空，去除
                pass
            else:
                CID.append(i)
    for j in CID:
        GCLA= Get_Coupon_List_By_App()
        list_= GCLA.run_get_coupon_list_by_app_data(
        url= GCLA.url_youhuiquan+'get_coupon_list_by_app',
        data= GCLA.run_data(
            GCLA.gcid,
            GCLA.token,
            j,
            #在我的账单模块，传为空即可
            GCLA.phone)).json()['result']['list']
        for k in list_:
            print json.dumps((k['id'],k['couponTitle'],k), encoding='UTF-8', ensure_ascii=False)+'\n'
        print



if __name__ == '__main__':
    test_get_coupon_list_by_app()