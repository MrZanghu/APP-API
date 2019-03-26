#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_12_mineShuiBiao



class Water_Meter_Recharge_Record(Read_ini.Config):
    def __init__(self):
        super(Water_Meter_Recharge_Record,self).read_ini()

    def run_data(self,gcid,token,id):
        self.water_meter_recharge_record= {
            "gcid": gcid,
            "token":token,
            "ids":id}
        return self.water_meter_recharge_record

    def run_water_meter_recharge_record_data(self,url,data):
        self.water_meter_recharge_record_data= json.dumps(data)
        self.water_meter_recharge_record_data_result= requests.post(
            url= url,
            data= self.water_meter_recharge_record_data)
        return self.water_meter_recharge_record_data_result



def test_water_meter_recharge_record(ids):
    WMRR= Water_Meter_Recharge_Record()
    list_= WMRR.run_water_meter_recharge_record_data(
        url= WMRR.url+'water_meter_recharge_record',
        data= WMRR.run_data(
            WMRR.gcid,
            WMRR.token,
            ids)).json()

    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_water_meter_recharge_record(
        Test_12_mineShuiBiao.test_mineShuiBiao()
    )
