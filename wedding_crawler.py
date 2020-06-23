from pymongo import MongoClient
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
name,services,address,tel=[],[],[],[]
for i in range(1,33):
    nextlink = "https://tfc-taiwan.org.tw/articles/report?page="+str(i)
    nl_response = rq.get(nextlink) # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(nl_response.text, "lxml") # 指定 lxml 作為解析器
    for url in soup.findAll('a', {'class': 'shop_name'}):
        response = rq.get(url.get('href')) # 用 requests 的 get 方法把網頁抓下來
        html_doc = response.text # text 屬性就是 html 檔案
        soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
        com=soup.select('h1')[0].find('a').text
        name.append(com)
        ser=",".join([p.text.strip()  for p in soup.findAll('li', {'class': 'icon-check'})])
        services.append(ser)
        test=soup.findAll('span', {'rel': 'calls'})
        if(len(test)==1):
            test=test[0].text.strip('\r\n')
        tel.append(test)
        test1=soup.find('span', {'class': 'contacts_info'})
        try:
            address.append(test1.text)
        except:
            address.append("抓不到")
        
    

df = pd.DataFrame({'name':name, 'address':address, 'tel':tel,'services':services})
client = MongoClient()
database = client["NodeJSDB"]  # SQL: Database Name
collection = database["wedding"]   # SQL: Table Name


records = df.to_dict('records') # 參數 record 代表把列轉成個別物件
collection.insert(records)