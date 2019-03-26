#-*- coding: UTF-8 -*-
import ConfigParser as CP



class Config(object):
    def read_ini(self):
        self.cfg= CP.ConfigParser()
        self.cfg.read('config.ini')
        self.url= self.cfg.get('APP_url','url')
        self.gcid= self.cfg.get('APP_info','gcid')
        self.phone= self.cfg.get('APP_info','phone')
        self.token= self.cfg.get('Tokens','token')
        self.url_zi_dian= self.cfg.get('APP_url','url_zi_dian')
        self.url_ShuiDianBiao= self.cfg.get('APP_url','url_ShuiDianBiao')
        self.url_XiuGaiMenSuo= self.cfg.get('APP_url','url_XiuGaiMenSuo')
        self.lock_id= self.cfg.get('APP_info','lock_id')
        self.lock_verification_code= self.cfg.get('APP_info','lock_verification_code')
        self.userid= self.cfg.get('APP_info','userid')
        self.channelSourceId= self.cfg.get('APP_info','channelSourceId')
        self.chengjiaoTypeId = self.cfg.get('APP_info', 'chengjiaoTypeId')
        self.feiYongTypeId = self.cfg.get('APP_info', 'feiYongTypeId')
        self.MuDanYuan_HeTong = self.cfg.get('APP_info', 'MuDanYuan_HeTong')
        self.url_youhuiquan= self.cfg.get('APP_url','url_youhuiquan')
        self.url_passpay= self.cfg.get('APP_url','url_passpay')
        self.url_zhangdan= self.cfg.get('APP_url','url_zhangdan')




if __name__ == '__main__':
    pass