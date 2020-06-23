import requests
from time import sleep
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver

browser = webdriver.Chrome(executable_path=r'C:\menting\爬蟲\chromedriver_win32\chromedriver') #填入chromedriver的路徑
browser.get('https://www.facebook.com/pg/nba.taiwan/posts/')

browser.find_element_by_css_selector('[name="email"]').send_keys('m7234809@yahoo.com.tw')
browser.find_element_by_css_selector('#pass').send_keys('mt2252047')
browser.find_element_by_css_selector('[type="submit"]').click()


# 在滑鼠不移動情況下，selenium打開的視窗裡，可以顯示幾篇動態牆文章？
soup = bs(browser.page_source, 'lxml')
len(soup.select('.userContentWrapper'))

userContentWrapper = soup.select('._1dwg._1w_m._q7o')
name, userContent, timestamp = [] ,[], []
for i in userContentWrapper:
    
    if i.select_one('.fwb.fcg'):
        name.append(i.select_one('.fwb.fcg').text)
    else:
        name.append('找不到Name')
    
    if i.select_one('.userContent'):
        userContent.append(i.select_one('.userContent').text)
    else:
        userContent.append('找不到userContent')
    
    if i.select_one('.timestampContent'):
        timestamp.append(i.select_one('.timestampContent').text)
    else:
        timestamp.append('找不到timestampContent')
        
for i in range(3):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)

df = pd.DataFrame({'name':name, 'content':userContent, 'time':timestamp})
df = df.drop_duplicates()
browser.quit()
df