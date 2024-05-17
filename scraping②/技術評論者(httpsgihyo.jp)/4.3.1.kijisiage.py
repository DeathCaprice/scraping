import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep

url="https://gihyo.jp"
#記事ページのURL、タイトル、発行日、記事の抽出
article_list=[]
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")

for elem in soup.select("#featured > ul > li > a"):
    url=urljoin(url,elem["href"])                  
    article_url=url.replace("?summary","") #記事ページのURL
    article_text=""
    for i in range(9):
        response= requests.get(article_url)
        soup=BeautifulSoup(response.text,"html.parser")
        #タイトル
        article_title=soup.select("div.article-title > h1")[0].text.replace("\u3000","").replace("\n","")
        #発行日
        publish_date=soup.select("p.date")[0].text
        #記事
        article_text = article_text+soup.select(".l-article-main")[0].text.replace("\u3000","").replace("\u2060","").replace("\n","").replace("\r","")
        sleep(1)

        if soup.select("a[rel='next']"):
            url=urljoin(url,soup.select("a[rel='next']")[0]["herf"])
        else:
            article_list.append([article_title,article_url,publish_date,article_text])
            break

抽出したタイトル、記事ページURL、発行日、記事をCSVに書き込み
csv_header=["タイトル","URL","発行日","本文"]
csv_date=datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name="gihyo_"+ csv_date + ".csv"
with open(csv_file_name,"w", errors="ignore") as file:
    writer=csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(article_list)

