import requests as rs
from bs4 import BeautifulSoup as bs
import os
urlptt='https://www.ptt.cc'
beauty='/bbs/Beauty/index.html'
res=rs.get(urlptt+beauty,cookies={'over18':'1'})
soup=bs(res.text,'lxml')
nexturl=soup.find_all('div',class_="r-ent")[2]
geturl=nexturl.find('a')['href']

#------------------------------找到要蒐集照片的文章
photos=[]
res1=rs.get(urlptt+geturl,cookies={'over18':'1'})
soup1=bs(res1.text,'lxml')
allpic=soup1.find('div',id="main-container")
realurl=allpic.find_all('a')#找到所有圖片
for i in realurl:
    pic=i['href']
    if pic.startswith('https://i.imgur'):
        photos.append(pic)
destdir='pic'        
if os.path.exists(destdir)==False:
    os.mkdir(destdir)
for photo in photos:
    picture=rs.get(photo)
    pictfile=open(os.path.join(destdir,os.path.basename(photo)),'wb')
    for i in picture.iter_content(10240):
        pictfile.write(i)
    pictfile.close()