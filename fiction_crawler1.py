import requests as rs
import bs4
from bs4 import BeautifulSoup as bs
url="https://www.biqukan.com/1_1496/450365.html"
res=rs.get(url)
res.encoding='gbk'
soup=bs(res.text,'lxml')
contents=soup.find('div',id='content')
for content in contents: 
    if type(content) == bs4.element.NavigableString:    # 確定資料格式
        txt = content.strip()  
        if type(txt) == str and txt != '':
            txt = content.strip()
            print(txt)                                  # 列印每段內文
            print()

