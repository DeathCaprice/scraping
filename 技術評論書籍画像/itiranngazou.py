import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os
import shutil
from urllib.parse import urljoin
from time import sleep

url="https://gihyo.jp/book/list?start=0"
item_list=[]

for i in range(9):
#while Ture:
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    for elem in soup.find_all("li",class_="clearfix"):
    #書名 著者名 定価 詳細ページURL抽出    
        item_name=elem.find("h3").text
        item_tsname=elem.find("p",class_="author").text
        item_price= elem.find("p",class_="price").text
        item_url=urljoin(url,elem.a["href"])
        item_image_url = urljoin(url, elem.find("img")["src"])
    #画像抽出
        path = r"C:\test_folder\gihiyou"
        file_name = item_image_url.split("/")[-1]
        image_path = os.path.join(path, file_name)
        response = requests.get(item_image_url, stream=True)  
        with open(image_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)

        item_list.append([item_name,item_tsname,item_price,item_url,item_image_url])                        
        
    if soup.select("#bookList > div:nth-child(3) > p.next > a"):
        url="https://gihyo.jp/"
        
        url=urljoin(url,soup.select("#bookList > div:nth-child(3) > p.next > a") [0]["href"])
        print(url)
        sleep(1)
    else:
         break        
#書名 著者名 定価 詳細ページURL 画像URLをエクセルに書き込む
csv_header=["書名","著者名","定価","詳細ページURL","画像URL"]
csv_date=datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name="notebook_"+csv_date+".csv"
with open(csv_file_name,"w",errors="ignore") as file:
    writer=csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)

