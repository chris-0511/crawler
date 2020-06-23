import requests as rs
from bs4 import BeautifulSoup as bs
con,bir,fort,script,chapter=[],[],[],[],[]
url="https://www.biqukan.com/1_1496/"
res=rs.get(url)
res.encoding='gbk'
soup=bs(res.text,'lxml')
name=soup.find('div',class_='cover')
all=soup.find('div',class_='small')
author=all.find('span')
catalog=author.next_sibling
status=catalog.next_sibling
wordcount=status.next_sibling
time=wordcount.next_sibling
chapter1=soup.find('div',class_='listmain')
name1=chapter1.find_all('dt')[1]
chapter=chapter1.find_all('dd')[12:]

print(name.text)
print(author.text)
print(catalog.text)
print(status.text)
print(wordcount.text)
print(time.text)
print(name1.text)
for i in chapter:
    chapter.append(i.text)
    print(i.text)