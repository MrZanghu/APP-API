#-*- coding: UTF-8 -*-
import Pics_Lists_for_all as PLFA
import requests
import Read_ini
import json



class Modify_Personal_Information(Read_ini.Config):
    def __init__(self):
        super(Modify_Personal_Information,self).read_ini()

    def run_data(self,gcid,token,userId,phone,email,sign,avatar,userName):
        self.modify_personal_information= {
            "gcid": gcid,
            "token": token,
            "userId": userId,
            "phone": phone,
            "email": email,
            "sign": sign,
            "avatar": avatar,
            "userName": userName}
        return self.modify_personal_information

    def run_modify_personal_information(self,url,data):
        self.modify_personal_information= json.dumps(data)
        self.modify_personal_information_result= requests.post(
            url= url,
            data= self.modify_personal_information)
        return self.modify_personal_information_result



def test_modify_personal_information():
    PL= PLFA.Pics_lits('Avatar')
    url_list= []
    for i in PL.get_P_list():
        url_list.append(PLFA.Insert_Pic(i).re_url()['url'])
    MPI= Modify_Personal_Information()
    list_= MPI.run_modify_personal_information(
        url= MPI.url+'modify_personal_information',
        data= MPI.run_data(
            MPI.gcid,
            MPI.token,
            MPI.userid,
            MPI.phone,
            'TestEmial@fvck.com',
            'TestSign_fvck1',
            url_list[0],
            '测试用户姓名')).json() # url_list[0]为地址字符串
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_modify_personal_information()