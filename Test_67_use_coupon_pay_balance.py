#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Use_Coupon_Pay_Balance(Read_ini.Config):
    def __init__(self):
        super(Use_Coupon_Pay_Balance,self).read_ini()

    def run_data(self,gcid,token,cid,bid):
        self.use_coupon_pay_balance= {
            "gcid": gcid,
            "token": token,
            "json": [
                {"cid":cid,"bid":bid}
            ]
        }
        return self.use_coupon_pay_balance

    def run_use_coupon_pay_balance_data(self,url,data):
        self.use_coupon_pay_balance_data= json.dumps(data)
        self.use_coupon_pay_balance_data_result= requests.post(
            url= url,
            data= self.use_coupon_pay_balance_data)
        return self.use_coupon_pay_balance_data_result



def test_use_coupon_pay_balance(cid_list,bid_list):
    UCPB= Use_Coupon_Pay_Balance()
    list_= UCPB.run_use_coupon_pay_balance_data(
        url= UCPB.url+'use_coupon_pay_balance',
        data= UCPB.run_data(
            UCPB.gcid,
            UCPB.token,
            cid_list,
            bid_list)).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_use_coupon_pay_balance(['192aa225bd9e48b18b44164eb7d5ab72'],
                                ['87EC56DFMC40DI4D69PBEA7OFEDD2C043ED3'])