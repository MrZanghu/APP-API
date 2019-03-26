#-*- coding: UTF-8 -*-
import requests
import json
import Read_ini
import base64



class IOS_PUSH(Read_ini.Config):
    def __init__(self):
        super(IOS_PUSH,self).read_ini()
        self.headers= {
            'Host': 'openapi.xg.qq.com',
            'Content-Type': 'application/json',
            'Authorization': 'Basic '+ base64.b64encode(self.iOS_token),
            'Cache-Control': 'no-cache'}

    def run(self):
        self.data = {
            "audience_type": "tag",
            "tag_list": {"tags": ["zhaiboyang_test"],"op": "AND"},
            "platform": "ios",
            "environment": "dev",
            'message_type':'notify',
            'message':{
                'title':'猪爪',
                'content':'这是三只猪爪',
                'ios':{
                    'aps':{
                        'alert':{
                            'subtitle':'subtitlessssss'
                        }
                    }
                }
            }
        }
        self.a= requests.post(self.url_push,headers= self.headers,
                              data= json.dumps(self.data)).content
        print self.a



if __name__ == '__main__':
    a= IOS_PUSH()
    a.run()
