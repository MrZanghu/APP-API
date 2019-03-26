#-*- coding: UTF-8 -*-
import ConfigParser as CP



class Config(object):
    def read_ini(self):
        self.cfg= CP.ConfigParser()
        self.cfg.read('config.ini')

        self.url_push= self.cfg.get('Accept_url','url_push')
        self.url_tag= self.cfg.get('Accept_url','url_tag')

        self.iOS_token= self.cfg.get('iOS_token','token')
        self.iOS_accesssID= self.cfg.get('iOS_token','accesssID')
        self.iOS_secretKey= self.cfg.get('iOS_token','secretKey')

        self.Android_token= self.cfg.get('Android_token','token')
        self.Android_accesssID= self.cfg.get('Android_token','accesssID')
        self.Android_secretKey= self.cfg.get('Android_token','secretKey')



if __name__ == '__main__':
    pass