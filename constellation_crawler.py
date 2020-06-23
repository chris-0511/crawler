import requests as rs
from bs4 import BeautifulSoup as bs
url='https://www.ptt.cc/bbs/Gossiping/index.html'
res=rs.get(url,cookies={'over18':'1'})
soup=bs(res.text,'lxml')
news=soup.find_all('div',class_='r-ent')
article=[]
for i in news:
    if i.find('a'):#確認文章內有東西
        title=i.find('a').text
        author=i.find('div',class_="author").text
        href=i.find('a')['href']
        num=i.find('div',class_="nrec").text
        article.append({
            'title':title,
            'author':author,
            'href':href,
            'num':num
        })
print(article)