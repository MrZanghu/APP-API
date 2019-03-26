#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_11_mineDianBiao
import Test_12_mineShuiBiao



class Use_Couponlist_Pay_Shuidian(Read_ini.Config):
    def __init__(self):
        super(Use_Couponlist_Pay_Shuidian,self).read_ini()

    def run_data(self,gcid,token,couponids,houseId,num,payType,totalFee,meterId,deptId):
        self.use_couponlist_pay_shuidian={
            "gcid": gcid,
            "token": token,
            "couponids":couponids,
            "houseId": houseId,
            "num": num,
            "payType": payType,
            "totalFee": totalFee,
            "meterId": meterId,
            "deptId": deptId}
        return self.use_couponlist_pay_shuidian

    def run_use_couponlist_pay_shuidian(self,url,data):
        self.use_couponlist_pay_shuidian_data= json.dumps(data)
        self.use_couponlist_pay_shuidian_data_result= requests.post(
            url= url,
            data= self.use_couponlist_pay_shuidian_data)
        return self.use_couponlist_pay_shuidian_data_result



def test_use_couponlist_pay_shuidian(couponids,payType,
                                     electricORwaterORhotwart):
    UCPS= Use_Couponlist_Pay_Shuidian()
    list_= UCPS.run_use_couponlist_pay_shuidian(
        url= UCPS.url_passpay+'use_couponlist_pay_shuidian',
        data= UCPS.run_data(
            UCPS.gcid,
            UCPS.token,
            couponids,
            '5d0854da0f4049f382e68b833a3d851c',
            payType,
            1,
            10,
            electricORwaterORhotwart,
            'bcc41cfdab7144bb821298111865132c')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)




if __name__ == '__main__':
    meter= raw_input("电表or水表or热水表?\n")
    if meter== '电表':
        test_use_couponlist_pay_shuidian(
            ['0aba5ca7bbf24ae3b06ced9836dd38d9'],
            1,
            Test_11_mineDianBiao.test_mineDianBiao()
        )
    elif meter== '水表':
        test_use_couponlist_pay_shuidian(
            ['0aba5ca7bbf24ae3b06ced9836dd38d9'],
            2,
            Test_12_mineShuiBiao.test_mineShuiBiao()[0]
        )
    elif meter== '热水表':
        test_use_couponlist_pay_shuidian(
            ['0aba5ca7bbf24ae3b06ced9836dd38d9'],
            4,
            Test_12_mineShuiBiao.test_mineShuiBiao()[1]
        )
    else:
        pass
