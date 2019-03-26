#-*- coding: UTF-8 -*-
import Pics_Lists_for_all as PA
import Test_45_anticipated_bill_clientApp as ABC
import requests
import json
import Read_ini



class Sign_Contract(Read_ini.Config):
    def __init__(self):
        super(Sign_Contract,self).read_ini()

    def run_data(self,gcid,token,nickname,phone,certificateType,cardType,
                 cardNo,cardTypeZhihang,emergencyPeo,emergencyPeoPhone,
                 cotenantList,startTime,endTime,zhifuTypeId,zukeSfzZheng,
                 zukeSfzFan,handheldIdentityCard,sfzNo,gender,buchongRemark,
                 channelSourceId,chengjiaoTypeId,contractZuKeMaxNum,contractZuKeNowNum,
                 electronicTemplateId,houseId,id,isElectron,jiage,yaJin,time,tiqianType,
                 tiqianDays,shoudingId,phoneBeiyong,no,homeAddress,fuZeRenList,chengjiaorenBumenId,
                 cardName,shouZhiList,urgentEmail):
        self.sign_contract={
            "gcid": gcid,
            "token": token,
            "buchongRemark": buchongRemark,
            "cardName": cardName,
            "cardNo": cardNo,
            "cardType": cardType,
            "cardTypeZhihang": cardTypeZhihang,
            "certificateType": certificateType,
            "channelSourceId": channelSourceId,
            "chengjiaoTypeId": chengjiaoTypeId,
            "chengjiaorenBumenId": chengjiaorenBumenId,
            "contractZuKeMaxNum": contractZuKeMaxNum,
            "contractZuKeNowNum": contractZuKeNowNum,
            "cotenantList": cotenantList,
            "electronicTemplateId": electronicTemplateId,
            "emergencyPeo": emergencyPeo,
            "emergencyPeoPhone": emergencyPeoPhone,
            "endTime": endTime,
            "fuZeRenList": fuZeRenList,
            "gender": gender,
            "homeAddress": homeAddress,
            "houseId": houseId,
            "id": id,
            "isElectron": isElectron,
            "jiage": jiage,
            "nickname": nickname,
            "no": no,
            "phone": phone,
            "phoneBeiyong": phoneBeiyong,
            "sfzNo": sfzNo,
            "shouZhiList": shouZhiList,
            "shoudingId": shoudingId,
            "startTime": startTime,
            "time": time,
            "tiqianDays": tiqianDays,
            "tiqianType": tiqianType,
            "yaJin": yaJin,
            "zhifuTypeId": zhifuTypeId,
            "handheldIdentityCard": handheldIdentityCard,
            "zukeSfzZheng": zukeSfzZheng,
            "zukeSfzFan": zukeSfzFan,
            "urgentEmail": urgentEmail}
        return self.sign_contract

    def run_sign_contract_data(self,url,data):
        self.sign_contract_data= json.dumps(data)
        self.sign_contract_data_result= requests.post(
            url= url,
            data= self.sign_contract_data)
        return self.sign_contract_data_result



def test_sign_contract(shoudingId):
    Pay_mark_list= {}
    PA_list= []

    with open('ID_marks.txt','r') as ID:
        for i in (ID.read().split(',')):
            try:
                if i.split(':')[0]== '季付':
                    Pay_mark_list[i.split(':')[0]]= i.split(':')[1]
            except:
                pass #忽略分割后会出现空值

    for j in PA.Pics_lits('Picture').get_P_list():
        PA_list.append(PA.Insert_Pic(j).re_url()['url'])
        # 生成身份证照list

    tongzhuren_list= [{'gender': 1,'phone': '15311111111','sfzNo': '110223199110094274','nickname': '1asdasdada'}]
    SC= Sign_Contract()
    list_= SC.run_sign_contract_data(
        url=SC.url + 'sign_contract',
        data=SC.run_data(
            SC.gcid,
            SC.token,
            '啊啊啊啊啊啊啊啊啊啊啊·1',
            SC.phone,
            1,
            '所属银行',
            666666,
            '所属银行支行',
            '紧急联系人',
            '紧急联系人电话',
            tongzhuren_list,
            '2018-11-22',
            '2020-11-21',
            Pay_mark_list['季付'],
            PA_list[0],
            PA_list[1],
            PA_list[2],
            110223200010105641,
            0,
            '补充说明',
            SC.channelSourceId,
            SC.chengjiaoTypeId,
            '',
            len(tongzhuren_list)+1,
            SC.MuDanYuan_HeTong,
            'fc4a88b685e54148bb216847a93eca79',
            '',
            1,
            '6940',
            '6940',
            '2018-11-21',
            1,
            1,
            shoudingId,
            '',
            '',
            '',
            '',
            '',
            '银行卡名称',
            ABC.test_anticipated_bill_clientApp()
        ,'emailTest@qq.com'
        )).json()
    print json.dumps(list_, encoding='UTF-8', ensure_ascii=False)



if __name__ == '__main__':
    test_sign_contract('')