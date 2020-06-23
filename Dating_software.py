# ch23_3.py
import requests
import csv
def get_data(page):
    url = 'http://www.lovewzly.com/api/user/pc/list/search?'    
    form_data = {'gender':'2', 'mary':'1', 'page':'1'} 
    # 傳遞參數
    form_data['page']=page
    datahtml = requests.get(url, params=form_data)
    datas = datahtml.json()
    nickname,bir,education,height,city,picurl=[],[],[],[],[],[]
    data = datas['data']['list']
    for d in data:
        nickname.append(d['username'])
        print('暱稱:',d['username'])
        bir.append(d['birthdayyear'])
        print('出生年:',d['birthdayyear'])
        height.append(d['height'])
        print('身高:',d['height'])
        city.append(d['city'])
        print('城市:',d['city'])
    print('上面為第 %s 頁-----------------------------------------------------'%(page))
    

for i in range(1,11):
    get_data(i)
        