#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Mine_Dian_Biao(Read_ini.Config):
    def __init__(self):
        super(Mine_Dian_Biao,self).read_ini()

    def run_data(self,gcid,token,houseId,loginType):
        self.mineDianBiao= {"gcid": gcid,
                            "token": token,
                            "houseId": houseId,
                            "loginType": loginType}
        return self.mineDianBiao

    def run_mineDianBiao_data(self,url,data):
        self.mineDianBiao_data= json.dumps(data)
        self.mineDianBiao_data_result= requests.post(
            url= url,
            data= self.mineDianBiao_data)
        return self.mineDianBiao_data_result



def test_mineDianBiao():
    MDB= Mine_Dian_Biao()
    list_= MDB.run_mineDianBiao_data(
        url= MDB.url_ShuiDianBiao+'mineDianBiao',
        data= MDB.run_data(
            MDB.gcid,
            MDB.token,
            "5d0854da0f4049f382e68b833a3d851c",
            "APP")).json()['result']
    # 牡丹园北里-6号楼1号楼1单元301室
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    return list_['id']



if __name__ == '__main__':
    test_mineDianBiao()