import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep
import os
import shutil



#詳細ページの書名、著者名、サブタイトル、記事、定価、発売日、ISBN、サイズ、ページ数、画像抽出

url="https://www.sbcr.jp/books/investment/"
item_list=[]

for i in range(9):
#while Ture:
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    for elem in soup.select("#home-box > ul > li> div.item-box > div > h3 > a"):#詳細ページURL抽出
        url=elem["href"]                  
        article_text=""
        response=requests.get(url)
        soup2=BeautifulSoup(response.text,"html.parser")
        #詳細ページURL抽出
        item_title=soup2.select("body > main > section.detail-box > div > div.detail-box-main > h2")[0].text     #書名
        item_Author_name=soup2.find("div",class_="detail-box-main__author").text #著者名
        item_subtitle=soup2.select_one("body > main > section.detail-box > div > div.detail-box-main > h3") #サブタイトル    
        if item_subtitle is None:
            print("要素がありません") 
            item_subtitle2="要素がありません"
        else:
            print(item_subtitle.text)
            item_subtitle2=item_subtitle.text 
       
        item_text=soup2.find("div",class_="detail-box-main__text").text #記事
        item_price=soup2.select(".price")[0].text.replace("定価：","") #定価
        item_date=soup2.select("div.detail-box-info > ul > li:nth-child(1)")[0].text.replace("発売日：","")#発売日
        item_isbn=soup2.select("div.detail-box-info > ul > li:nth-child(2)")[0].text.replace("ISBN：","")#ISBN
        item_size=soup2.select("div.detail-box-info > ul > li:nth-child(3)")[0].text.replace("サイズ：","")#サイズ
        item_page=soup2.select("div.detail-box-info > ul > li:nth-child(4)")[0].text.replace("ページ数：","")#ページ数
        img=soup2.select("body > main > section.detail-box > div > div.detail-box-left > div > img")[0]#画像url
        item_img_url=img["src"]
        print(item_img_url)
        #リスト作成
        item_list.append([item_title,item_Author_name,item_subtitle2,item_text,item_price,item_date,item_isbn,item_size,item_page,item_img_url])
     
    if soup.select("body > main > div > div > div.next-page.pjaxLink > a"):
        
        url=soup.select("body > main > div > div > div.next-page.pjaxLink > a") [0]["href"]
        print(url)
        sleep(1)
    else:
        break
#csvファイルに抽出項目を読み込む
csv_header=["書名","著者名","サブタイトル","記事","定価","発売日","ISBN","サイズ","ページ数","画像URL"]
csv_date=datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name="notebook_"+csv_date+".csv"
with open(csv_file_name,"w",errors="ignore") as file:
    writer=csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)                

path = r"C:\test_folder\sbcr"
for i, item in enumerate(item_list,1):
    file_name = str(i) + "."+ item[9].split(".")[-1]  #enumerate使用
    image_path = os.path.join(path, file_name)
    response = requests.get(item[9], stream=True)   #画像のダウンロード
    with open(image_path, "wb") as file:
        shutil.copyfileobj(response.raw, file)

     
