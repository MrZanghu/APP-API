#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini



class Book_House(Read_ini.Config):
    def __init__(self):
        super(Book_House,self).read_ini()

    def run_data(self,gcid,token,zukePhone,
                 houseId,zukeName,endtime,
                 remark,isJizhong,zukeSfz,signTime):
        # 定金默认1000
        self.book_house= {
            "gcid": gcid,
            "token": token,
            "zukePhone": zukePhone,
            "houseId": houseId,
            "zukeName": zukeName,
            "endtime": endtime,
            "remark": remark,
            "isJizhong": isJizhong,
            "money": "1000",
            "zukeSfz": zukeSfz,
            "signTime": signTime}
        return self.book_house

    def run_book_house_data(self,url,data):
        self.book_house_data= json.dumps(data)
        self.book_house_data_result= requests.post(
            url= url,
            data= self.book_house_data)
        return self.book_house_data_result



def test_book_house():
    BH= Book_House()
    list_= BH.run_book_house_data(
        url= BH.url+'book_house',
        data= BH.run_data(
            BH.gcid,
            BH.token,
            BH.phone,
            '2c9965ba41a846728ff8c698292f873c',
            '翟伯洋',
            '2018-09-30',
            '测试备注',
            '1',
            '110223199110094274',
            '2018-09-21')).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_book_house()