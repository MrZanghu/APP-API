#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Water_Meter_Payment_By_Coupon(Read_ini.Config):
    def __init__(self):
        super(Water_Meter_Payment_By_Coupon,self).read_ini()

    def run_data(self,gcid,token,couponids,houseId,num,
                 payType,totalFee,meterId,outTradeNo,openid,deptId
                 ,ipv4):
        self.water_Meter_Payment_By_Coupon= {
                 "gcid": gcid,
                 "token": token,
                 "couponids": couponids,
                 "houseId": houseId,
                 "num": num,
                 "payType": payType,
                 "totalFee": totalFee,
                 "meterId": meterId,
                 "outTradeNo": outTradeNo,
                 "openid":openid,
                 "deptId":deptId,
                 "ipv4":ipv4}
        return self.water_Meter_Payment_By_Coupon

    def run_water_Meter_Payment_By_Coupon_data(self,url,data):
        self.water_Meter_Payment_By_Coupon_data= json.dumps(data)
        self.water_Meter_Payment_By_Coupon_result= requests.post(
            url= url,
            data= self.water_Meter_Payment_By_Coupon_data)
        return self.water_Meter_Payment_By_Coupon_result



def test_water_Meter_Payment_By_Coupon(couponids,houseId,totalFee,meterId,deptId,ipv4):
    WMPBC= Water_Meter_Payment_By_Coupon()
    list_= WMPBC.run_water_Meter_Payment_By_Coupon_data(
        url= WMPBC.url+'water_Meter_Payment_By_Coupon',
        data= WMPBC.run_data(
            WMPBC.gcid,
            WMPBC.token,
            couponids,
            houseId,
            1,
            2,
            totalFee,
            meterId,
            'PASS',
            'PASS',
            deptId,
            ipv4)).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    # 支付宝充值电表



if __name__ == '__main__':
    test_water_Meter_Payment_By_Coupon(
        [''],
        '5d0854da0f4049f382e68b833a3d851c',
        10,
        '318020001936',
        'bcc41cfdab7144bb821298111865132c',
        '192.168.1.102')
