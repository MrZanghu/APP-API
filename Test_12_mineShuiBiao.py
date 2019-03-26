#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Mine_Shui_Biao(Read_ini.Config):
    def __init__(self):
        super(Mine_Shui_Biao,self).read_ini()

    def run_data(self,gcid,token,houseId,loginType):
        self.mineShuiBiao= {"gcid": gcid,
                            "token": token,
                            "houseId": houseId,
                            "loginType":loginType}
        return self.mineShuiBiao

    def run_mineShuiBiao_data(self,url,data):
        self.mineShuiBiao_data= json.dumps(data)
        self.mineShuiBiao_data_result= requests.post(
            url= url,
            data= self.mineShuiBiao_data)
        return self.mineShuiBiao_data_result



def test_mineShuiBiao():
    MSB= Mine_Shui_Biao()
    list_= MSB.run_mineShuiBiao_data(
        url= MSB.url_ShuiDianBiao+'mineShuiBiao',
        data= MSB.run_data(
            MSB.gcid,
            MSB.token,
            "fc4a88b685e54148bb216847a93eca79",
            "APP")).json()['result']
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    waterlists= []
    for i in list_['list']:
        if i['type']== 10:
            waterlists.append(i['id'])
        elif i['type']== 20:
            waterlists.append(i['id'])
    return waterlists
    # 返回冷水、热水表id



if __name__ == '__main__':
    test_mineShuiBiao()