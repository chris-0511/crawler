# from pymongo import MongoClienthttp://localhost:8889/notebooks/%E5%A9%9A%E5%AE%B4.ipynb#
import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import time
import csv
content,pic=[],[]
headers = ['新聞標題', '網址', '內文', '照片', '真假']
with open('fake_news.csv', 'a') as f:
    writeCsv = csv.writer(f)
    writeCsv.writerow(headers)

for i in range(1,53):
    nextlink = "https://tfc-taiwan.org.tw/articles/report?page="+str(i)
    nl_response = rq.get(nextlink) # 用 requests 的 get 方法把網頁抓下來
    soup = BeautifulSoup(nl_response.text, "lxml") # 指定 lxml 作為解析器
    for url1 in soup.findAll('a', {'class': 'read-more'}):
      try:
          url=('https://tfc-taiwan.org.tw/'+url1.get('href'))
          response = rq.get('https://tfc-taiwan.org.tw/'+url1.get('href'))
          soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
          t=soup.select('h3')[0].text
          title=t
          c=soup.find_all('p')
          for i ,v in enumerate(c):
              if (i==0) or (i==len(c)-1) or (i==len(c)-2):
                  pass
              else:
                # print(v.text)
                  content.append(v.text)
          content1=' '.join(content)
          # content2.append(content1)
          content.clear()    
          p=soup.find_all('img',{'alt':''})
          for i in p:
              pic.append('https://tfc-taiwan.org.tw/'+i['src'])
          pic1='#'.join(pic)
          # img.append(pic1)
          pic.clear()
          for i in range(len(url)):
              true_false='False'
      except:
              print(f'第{i}頁的這個{url1}沒資料')
              csvFile = open('fake_news.csv', 'a')
              try:
                  writer = csv.writer(csvFile)
                  writer.writerow([title,url,content1,pic1,true_false])
              finally:
                  csvFile.close()
              continue
      else:

            with open('fake_news.csv', 'a') as f:
                writeCsv = csv.writer(f)
                # writeCsv.writerow(headers)
            
                # print(type(title),type(url),type(content1),type(pic1),type(true_false))
               
                writeCsv.writerow([title,url,content1,pic1,true_false])




        
            
    
              
# df = pd.DataFrame({'新聞標題':title, '網址':url, '內文':content2,'照片':img,'真假':true_false})
# df.to_csv('fakenews.csv')
# # df