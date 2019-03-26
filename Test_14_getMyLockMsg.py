#-*- coding: UTF-8 -*-
import ConfigParser as CP
import requests
import json
import Read_ini



class Get_MyLock_Msg(Read_ini.Config):
    def __init__(self):
        super(Get_MyLock_Msg,self).read_ini()

    def run_data(self,gcid,token,houseId):
        self.getMyLockMsg= {"gcid": gcid,
                            "token": token,
                            "houseId": houseId}
        return self.getMyLockMsg

    def run_getMyLockMsg_data(self,url,data):
        self.getMyLockMsg_data= json.dumps(data)
        self.getMyLockMsg_data_result= requests.post(
            url= url,
            data= self.getMyLockMsg_data)
        return self.getMyLockMsg_data_result



def test_getMyLockMsg():
    GMM= Get_MyLock_Msg()
    list_= GMM.run_getMyLockMsg_data(
        url= GMM.url+'getMyLockMsg',
        data= GMM.run_data(
            GMM.gcid,
            GMM.token,
            '2c9965ba41a846728ff8c698292f873c')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    # return list_



def write_into_ini(section,title,msg):
    # 将token值写入配置文件
    con= CP.ConfigParser()
    con.read('config.ini')
    con.set(section,title,msg)
    con.write(open('config.ini','r+'))



if __name__ == '__main__':
    # write_into_ini('APP_info',
    #                'lock_id',test_getMyLockMsg()[0]['lockid'])
    test_getMyLockMsg()