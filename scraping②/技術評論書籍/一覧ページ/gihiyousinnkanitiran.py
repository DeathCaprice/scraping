import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep

url="https://gihyo.jp/book/list?start=0"
item_list=[]


#書名 著者名 定価 詳細ページURL抽出

for i in range(9):
#while Ture:
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    for elem in soup.find_all("li",class_="clearfix"):
        
        item_name=elem.find("h3").text
        item_tsname=elem.find("p",class_="author").text
        item_price= elem.find("p",class_="price").text
        item_url=urljoin(url,elem.a["href"])
        item_list.append([item_name,item_tsname,item_price,item_url]) 
        
    if soup.select("#bookList > div:nth-child(3) > p.next > a"):
        url="https://gihyo.jp/"
        
        url=urljoin(url,soup.select("#bookList > div:nth-child(3) > p.next > a") [0]["href"])        
        sleep(1)
    else:
         break        

#csvデータファイル作成
csv_header=["書名","著者名","定価","詳細ページURL"]
csv_date=datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name="notebook_"+csv_date+".csv"
with open(csv_file_name,"w",errors="ignore") as file:
    writer=csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)


