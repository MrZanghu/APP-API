#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import base64



Choice_platform= raw_input('请确认使用Android还是iOS(1/0)' + '\n')
# 选择平台



class Tag_Api(Read_ini.Config):
    def __init__(self):
        super(Tag_Api,self).read_ini()

    @staticmethod
    def AndroidORiOS():
        return (Choice_platform== '1')

    def do_headers(self):
        if self.AndroidORiOS()== True:
            self.headers = {'Content-Type': 'application/json',
                            'Authorization': "Basic " + base64.b64encode(self.Android_token),
                            'Cache-Control': 'no-cache',
                            'Host': 'openapi.xg.qq.com'}
            self.platform= 'android'
        else:
            self.headers= {'Content-Type':'application/json',
                           'Authorization':"Basic "+base64.b64encode(self.iOS_token),
                           'Cache-Control':'no-cache',
                           'Host':'openapi.xg.qq.com'}
            self.platform= 'ios'
        return (self.platform,self.headers)

    def add_1Tag_1Tkone(self,tag_token_list):
        '''
        增加单个tag1，对单个token1
        :return:
        '''
        self.data= {
            "operator_type": 9,
            "platform": self.do_headers()[0],
            "tag_token_list": tag_token_list}
        self.rq= requests.post(self.url_tag,
                              headers= self.do_headers()[1],
                              data= json.dumps(self.data)).content
        print self.rq

    def del_1Tag_1Tkone(self,tag_list,token_list):
        '''
        删除单个tag1，对单个token1
        :return:
        '''
        self.data= {
            "operator_type": 2,
            "platform": self.do_headers()[0],
            "tag_list": tag_list,
            "token_list": token_list}
        self.rq= requests.post(self.url_tag,
                              headers= self.do_headers()[1],
                              data= json.dumps(self.data)).content
        print self.rq



if __name__ == '__main__':
    a= Tag_Api()
    a.add_1Tag_1Tkone(
        [["zhaiboyang_test",
          "add50ab98dde7554dd087dc5f80cd557b1b132001d611be5a6deac47c9c896b5"]]
    )