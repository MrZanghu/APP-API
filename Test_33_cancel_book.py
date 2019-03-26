#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import Test_19_get_preordain_list



class Cancel_Book(Read_ini.Config):
    def __init__(self):
        super(Cancel_Book,self).read_ini()

    def run_data(self,gcid,token,shoudingStatus,id,phone,remark,balanceSheetId,indentType,money,predictTime,note):
        self.cancel_book= {
            "gcid": gcid,
            "token": token,
            "shoudingStatus": shoudingStatus,
            "id": id,
            "phone": phone,
            "remark": remark,
            "balanceSheetId": balanceSheetId,
            "indentType": indentType,
            "money": money,
            "predictTime": predictTime,
            "note": note}
        print json.dumps(self.cancel_book, encoding='UTF-8', ensure_ascii=False)
        # 打印请求参数
        return self.cancel_book

    def run_cancel_book_data(self,url,data):
        self.cancel_book_data= json.dumps(data)
        self.cancel_book_data_result= requests.post(
            url= url,
            data= self.cancel_book_data)
        return self.cancel_book_data_result



def test_cancel_book():
    CB= Cancel_Book()
    for i in Test_19_get_preordain_list.test_get_preordain_list():
        list_= CB.run_cancel_book_data(
            url= CB.url+'cancel_book',
            data= CB.run_data(
                CB.gcid,
                CB.token,
                0,
                i[0],
                CB.phone,
                '测试备注',
                i[1],
                1,
                1000,
                '2018-08-07',
                '测试收支备注')).json()
        print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_cancel_book()