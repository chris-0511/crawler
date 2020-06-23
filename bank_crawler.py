import requests as rs
from bs4 import BeautifulSoup as bs
title,school,date=[],[],[]
url='https://www.dcard.tw/f'
res=rs.get(url)
soup=bs(res.text,'lxml')
title1=soup.find_all('a',class_='sc-1v1d5rx-3 kPUUNB')
school1=soup.find_all('span',class_='sc-6oxm01-2 hiTIMq')
for i in title1:
    title.append(i.text)
cnt=1
for i in school1:
    if cnt%3==1:
        school.append(i.text)
    if cnt%3==0:
        date.append(i.text)
    cnt+=1
for i in range(len(date)):
    print(school[i])
    print(date[i])
    print(title[i])