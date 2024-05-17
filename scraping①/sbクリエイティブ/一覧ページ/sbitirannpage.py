import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep

url="https://www.sbcr.jp/books/investment/"
item_list=[]
for i in range(9):
#while Ture:
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")   
    #書名、著者名、発売日、カテゴリー名、画像url抽出
    for elem in soup.find_all("div",class_="item-box"):
        #書名
        item_title=elem.find("h3").text
        #著者名
        item_Author_name=elem.find("div",class_="item-box__author").text
        #発売日
        item_date=elem.find("div",class_="item-box__date").text.strip().replace("発売日："," ")
        #カテゴリー名
        item_category=elem.find("div",class_="item-box__category").text
        #画像url
        item_img_url=elem.find("img")["src"]
        #リスト作成
        item_list.append([item_title,item_Author_name,item_date,item_category,item_img_url])
             
    if soup.select("body > main > div > div > div.next-page.pjaxLink > a"):              
        url=soup.select("body > main > div > div > div.next-page.pjaxLink > a") [0]["href"]        
        sleep(1)
    else:
        break    

csv_header=["書名","著者名","発売日","カテゴリー名","画像URL"]
csv_date=datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name="notebook_"+csv_date+".csv"
with open(csv_file_name,"w",errors="ignore") as file:
    writer=csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)

 
                                
        


