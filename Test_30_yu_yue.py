#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Yu_Yue(Read_ini.Config):
    def __init__(self):
        super(Yu_Yue,self).read_ini()

    def run_data(self,gcid,token,name,age,phone,seeTime,houseId,loginCellPhone,needRemark,roomTypeId):
        self.yu_yue= {
            "gcid": gcid,
            "token": token,
            "name": name,
            "age": age,
            "phone": phone,
            "seeTime": seeTime,
            "houseId": houseId,
            "loginCellPhone": loginCellPhone,
            "needRemark": needRemark,
            "roomTypeId": roomTypeId}
        return self.yu_yue

    def run_yu_yue_data(self,url,data):
        self.yu_yue_data= json.dumps(data)
        self.yu_yue_data_result= requests.post(
            url= url,
            data= self.yu_yue_data)
        return self.yu_yue_data_result



def test_yu_yue():
    YY= Yu_Yue()
    list_= YY.run_yu_yue_data(
        url= YY.url+'yu_yue',
        data= YY.run_data(
            YY.gcid,
            YY.token,
            '用户名啦啦',
            '',
            YY.phone,
            '2018-09-09',
            '',
            YY.phone,
            '',
            '38E3A01AF817034F5579A9BB28731DFB94B1')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_yu_yue()