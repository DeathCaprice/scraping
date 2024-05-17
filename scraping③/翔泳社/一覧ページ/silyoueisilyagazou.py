from datetime import datetime
import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin
from time import sleep
import csv
import os
import shutil

url="https://www.seshop.com/product/616"
books=[]

for i in range(9):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    
    # CSSセレクターで <div class="list">の中の<div class="inner"> を取得
    divs = soup.select("div.list div.inner")
    for div in divs:
        
        img_url=urljoin(url,div.find("img")["src"])
        
        print(img_url)
        books.append([img_url])
        
    if soup.select("a[rel='next']"):
        url=urljoin(url,soup.select("a[rel='next']")[0]["href"])                                                                                                          
        sleep(1)
    else:
        break        

        

csv_header=['画像URL']
csv_date=datetime.today().strftime("%Y%m%d%H")
csv_file_name="notebook_"+csv_date+".csv"
with open(csv_file_name,"w",errors="ignore") as file:
    writer=csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(books)



path = r"C:\test_folder\siyoueiimage"
for i, book in enumerate(books):
    file_name = str(i) + "."+ book[0].split(".")[-1]
    image_path = os.path.join(path, file_name)
    response = requests.get(book[0], stream=True)   
    with open(image_path, "wb") as file:
        shutil.copyfileobj(response.raw, file)


