#-*- coding: UTF-8 -*-
import requests
import Read_ini
import os
import re



class Pics_lits(object):
    # 遍历出PNG文件，返回地址+图片+格式的list
    def __init__(self,Finder):
        self.P_file_path= \
            '/Users/violet/Desktop/kevin/康桥地产/Project/APP/APP-API/'+Finder

    def get_P_list(self):
        self.P_lists= []
        for dirpath, dirnames, filenames in os.walk(self.P_file_path):
            for filepath in filenames:
                if re.search('png', os.path.join(dirpath, filepath)) == None:
                    pass
                else:
                     self.P_lists.append(os.path.join(dirpath, filepath))
        return self.P_lists



class Insert_Pic(Read_ini.Config):
    # 上传图片，返回图片网址
    def __init__(self,Pic_s):
        super(Insert_Pic,self).read_ini()
        self.url_one= 'http://pms.hntpsjwy.com/UploadAllObjectServlet?server=upload&'
        self.file_one= {'file': open(Pic_s, 'rb')}
        self.headers_one= {
            'Content-Type': 'text/javascript;charset=UTF-8',
            'User-Agent':'Mozilla / 5.0(Macintosh;IntelMac OS X 10_13_3) AppleWebKit/537.36(KHTML, likeGecko) Chrome/67.0.3396.99Safari/537.36'}

    def re_url(self):
        return requests.post(url= self.url_one,
                             files= self.file_one,
                             data= self.headers_one).json()



if __name__ == '__main__':
    P= Pics_lits('Picture')
    for i in P.get_P_list():
        print Insert_Pic(i).re_url()