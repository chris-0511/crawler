import requests as rs
from bs4 import BeautifulSoup as bs
import csv

import pandas as pd
ratelist,headlist,tablelist=[],[],[]

url='http://taiwanrate.com/'
res=rs.get(url)
res.encoding='utf-8'#避免亂碼,從網頁的從網頁的charset看出utf-8
soup=bs(res.text,'lxml')
ratetable=soup.find_all('table')

lefttop=ratetable[4].find('tr').find('tr').find('td')
headlist.append(lefttop.text)
ratehead=ratetable[4].find('tr').find_all('a',"bodytablehead")
for i in ratehead:
    headlist.append(i.text)
tablelist.append(headlist)

ratetd=ratetable[4].find('tr',"bodytabletr1")
for i in ratetd:
     ratelist.append(i.text)
tablelist.append(ratelist)
while ratetd.find_next_sibling('tr'):
    ratetd=ratetd.find_next_sibling('tr')
    ratelist = []#每次進入ratelist為空
    for i in ratetd:
        ratelist.append(i.text)
    tablelist.append(ratelist)
fn='bank_rate.csv'
with open(fn,'w',newline= '') as csvFile:
    csvWriter=csv.writer(csvFile)
    for i in tablelist:
        csvWriter.writerow(i)
rate=pd.DataFrame(tablelist)
rate