from datetime import datetime
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import pandas as pd
import re

url="https://www.seshop.com/product/616"
books=[]

for i in range(9):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    
    # CSSセレクターで <div class="list">の中の<div class="inner"> を取得
    divs = soup.select("div.list div.inner")
    for div in divs:
        img_url=urljoin(url,div.find("img")["src"])
    #日付の文字列を取得
        day=div.find("span",class_="date").text.strip().replace("発売","") 
        published = str(datetime.strptime(day, "%Y.%m.%d")).replace("00:00:00","") 

        div_txt=div.find("div",class_="txt")
        # aタグを取得
        a_tag = div_txt.find("a")
        # 書籍タイトルを取得
        title = a_tag.text.strip()  
        # 書籍URLを取得
        url=urljoin(url,a_tag["href"])
        # 販売価格を取得
        pattern = re.compile("円") 
        price_s=div_txt.find(string=pattern).text 
        price_s = price_s.strip()
        price_s = price_s.replace("円（税込）", "")
        price_s = price_s.replace(",", "")
        price = int(price_s)
        print(url)
        print(img_url)
        books.append([title,img_url,url,price,published])    
    
    if soup.select("a[rel='next']"):
        url=urljoin(url,soup.select("a[rel='next']")[0]["href"])                                                                                                          
        sleep(1)
    else:
        break        


#リストをデータフレームに入れる
df = pd.DataFrame(books, columns=['書籍名','画像URL','ページURL','価格','発売日'])

#Excelにデータを出力する（※ファイルパスは変更してください）
df.to_excel('books.xlsx', sheet_name='books',index=False)

   




