#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Water_or_Electric_Recharge_Coupon(Read_ini.Config):
    def __init__(self):
        super(Water_or_Electric_Recharge_Coupon,self).read_ini()

    def run_data(self,gcid,token,couponids,houseId,num,
                 payType,totalFee,meterId,outTradeNo):
        self.water_or_electric_recharge_coupon= {
                 "gcid": gcid,
                 "token": token,
                 "couponids": couponids,
                 "houseId": houseId,
                 "num": num,
                 "payType": payType,
                 "totalFee": totalFee,
                 "meterId": meterId,
                 "outTradeNo": outTradeNo}
        return self.water_or_electric_recharge_coupon

    def run_water_or_electric_recharge_coupon_data(self,url,data):
        self.water_or_electric_recharge_coupon_data= json.dumps(data)
        self.water_or_electric_recharge_coupon_data_result= requests.post(
            url= url,
            data= self.water_or_electric_recharge_coupon_data)
        return self.water_or_electric_recharge_coupon_data_result



def test_water_or_electric_recharge_coupon(couponids,houseId,totalFee,meterId):
    WERC= Water_or_Electric_Recharge_Coupon()
    list_= WERC.run_water_or_electric_recharge_coupon_data(
        url= WERC.url+'water_or_electric_recharge_coupon',
        data= WERC.run_data(
            WERC.gcid,
            WERC.token,
            couponids,
            houseId,
            1,
            2,
            totalFee,
            meterId,
            'PASS')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    # 支付宝充值电表



if __name__ == '__main__':
    test_water_or_electric_recharge_coupon(
        [''],
        '5d0854da0f4049f382e68b833a3d851c',
        10,
        '318020001936')
