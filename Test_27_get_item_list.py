#-*- coding: UTF-8 -*-
import Test_44_get_townList_by_cityId as GC
import requests
import json
import Read_ini



class Get_Item_List(Read_ini.Config):
    def __init__(self):
        super(Get_Item_List,self).read_ini()

    def run_data(self,gcid,token,preStayTime,quyuId,desc,cityId):
        self.get_item_list= {
            "gcid": gcid,
            "token": token,
            "preStayTime": preStayTime,
            "quyuId": quyuId,
            "sortFields": 'zujin_',
            "sortType": desc,
            "cityId": cityId}
        return self.get_item_list

    def run_get_item_list_data(self,url,data):
        self.get_item_list_data= json.dumps(data)
        self.get_item_list_data_result= requests.post(
            url= url,
            data= self.get_item_list_data)
        return self.get_item_list_data_result



def test_get_item_list(preStayTime,DorA):
    # 预期入住时间，门店在这个时间点上有没有可以签约的房源
    GIL= Get_Item_List()
    result_list= []
    item_list_= []
    # for i in GC.test_get_townList_by_cityId():
    #     item_list_.append(GIL.run_get_item_list_data(
    #         url= GIL.url+'get_item_list',
    #         data= GIL.run_data(
    #             GIL.gcid,
    #             GIL.token,
    #             preStayTime,
    #             i[3],
    #             DorA,
    #             i[1])).json()['result']['list'])
    # for j in item_list_:
    #     # 入住时间不在可租时间内，则不显示
    #     try:
    #         result_list.append((j[0]['itemName'],j[0]['id']))
    #     except:
    #         pass
    #     # 返回项目名称和项目ID
    # print json.dumps(result_list, encoding='UTF-8', ensure_ascii=False) + '\n'
    # print
    # print '*************************************************'
    # print
    # return result_list

    list_= GIL.run_get_item_list_data(
        url=GIL.url + 'get_item_list',
        data=GIL.run_data(
            GIL.gcid,
            GIL.token,
            preStayTime,
            '',
            DorA,
            'd94bba14-dec1-11e5-bcc3-00163e1c066c')).json()['result']['list']
    for i in list_:
        print json.dumps(i, encoding='UTF-8', ensure_ascii=False)+'\n'
    # 单独查询


if __name__ == '__main__':
    test_get_item_list('','desc')

