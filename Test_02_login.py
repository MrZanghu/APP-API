#-*- coding: UTF-8 -*-
import ConfigParser as CP
import Test_01_get_code
import requests
import json
import Read_ini



class Login(Read_ini.Config):
    def __init__(self):
        super(Login,self).read_ini()

    def run_data(self,gcid,phone,collectRoomIds,checkCode,token):
        self.Login_data= {
            'gicd':gcid,
            'phone':phone,
            'collectRoomIds':collectRoomIds,
            'checkCode':checkCode,
            'token':token}
        return self.Login_data

    def run_login(self,url,data):
        self.Login_data_post= json.dumps(data)
        self.Login_result= requests.post(
            url= url,
            data= self.Login_data_post)
        return self.Login_result



def test_login(code):
    LG= Login()
    list_= LG.run_login(
        url= LG.url+'login',
        data= LG.run_data(
            LG.gcid,
            LG.phone,
            [''],
            code,
            '')).json()
    # 牡丹园北里-6号楼的精致开间户型，传入list
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)
    return (list_['result']['token'],list_['result']['userId'])



def write_into_ini(section,title,msg):
    # 将token值写入配置文件
    con= CP.ConfigParser()
    con.read('config.ini')
    con.set(section,title,msg)
    con.write(open('config.ini','r+'))



if __name__ == '__main__':
    write_into_ini('Tokens',
                   'token',
                   test_login(Test_01_get_code.test_get_code())[0])
    #写入token
    write_into_ini('APP_info',
                   'userid',
                   test_login(Test_01_get_code.test_get_code())[1])
    #写入用户ID