#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_11_mineDianBiao



class Electric_Meter_Recharge_Record(Read_ini.Config):
    def __init__(self):
        super(Electric_Meter_Recharge_Record,self).read_ini()

    def run_data(self,gcid,token,id):
        self.electric_meter_recharge_record= {
            "gcid": gcid,
            "token": token,
            "id": id,
            "app_version": "1.0.3"
        }
        return self.electric_meter_recharge_record
        # 传入电表ID

    def run_electric_meter_recharge_record_data(self,url,data):
        self.electric_meter_recharge_record_data= json.dumps(data)
        self.electric_meter_recharge_record_data_result= requests.post(
            url= url,
            data= self.electric_meter_recharge_record_data)
        return self.electric_meter_recharge_record_data_result


def test_electric_meter_recharge_record(ids):
    EMRR= Electric_Meter_Recharge_Record()
    list_= EMRR.run_electric_meter_recharge_record_data(
        url= EMRR.url+'electric_meter_recharge_record',
        data= EMRR.run_data(
            EMRR.gcid,
            EMRR.token,
            ids)).json()['result']['list']
    print
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False)
        print '*'*10




if __name__ == '__main__':
    test_electric_meter_recharge_record(
        Test_11_mineDianBiao.test_mineDianBiao()
    )