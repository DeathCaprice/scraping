import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep


#詳細ページスクレイピング

url = "https://gihyo.jp/book/list?start=0"
item_list = []



#詳細ページurl、書名、発売日、著者名、型番/ページ数、定価、ISBN抽出

for i in range(9):
# while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for elem in soup.find_all("li", class_="clearfix"):
        
        item_url = urljoin(url, elem.a["href"])
        print(item_url)
        response = requests.get(item_url)
           
        soup_detail = BeautifulSoup(response.text, "html.parser")

                        
        item_release = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(1)")[0].text

                

        if item_url=="https://gihyo.jp/magazine/SD/archive/2023/202310":

            item_name = soup_detail.select("#primary > h1")[0].text
            item_tsname=""
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text
            item_isbn=""
        elif item_url=="https://gihyo.jp/magazine/wdpress/archive/2023/vol136":
            item_name = soup_detail.select("#primary > h1")[0].text
            item_tsname=""
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text
            item_isbn=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(4) > span")[0].text

        elif item_url=="https://gihyo.jp/magazine/SD/archive/2023/202309":
            item_name = soup_detail.select("#primary > h1")[0].text
            item_tsname=""
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text
            item_isbn=""
        elif item_url=="https://gihyo.jp/magazine/SD/archive/2023/202308":
            item_name = soup_detail.select("#primary > h1")[0].text
            item_tsname=""
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text
            item_isbn=""
        elif item_url=="https://gihyo.jp/magazine/wdpress/archive/2023/vol135":
            
            item_name = soup_detail.select("#primary > h1")[0].text
            item_tsname=""
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text
            item_isbn=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(4) > span")[0].text

        elif item_url=="https://gihyo.jp/magazine/SD/archive/2023/202307":
            item_name = soup_detail.select("#primary > h1")[0].text
            item_tsname=""
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text
            item_isbn=""


        else:    
            item_name = soup_detail.select("#primary > div:nth-child(1) > h1")[0].text
            item_tsname=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(2)")[0].text
            item_size = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text.split("／")[0].strip()
            item_page = soup_detail.select("#publishedDetail > div.data > div > p:nth-child(3)")[0].text.split("／")[1].strip()
            item_price=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(4)")[0].text
            item_isbn=soup_detail.select("#publishedDetail > div.data > div > p:nth-child(5) > span")[0].text
        
        item_list.append([item_name ,item_release, item_tsname, item_size, item_page ,item_price, item_isbn, item_url])
        sleep(1)

    if soup.select("#bookList > div:nth-child(3) > p.next > a"):
        
        url="https://gihyo.jp/"
        
        url=urljoin(url,soup.select("#bookList > div:nth-child(3) > p.next > a") [0]["href"])
        print(url)
        sleep(1)
    else:
        break    


csv_header = ["書名","発売日","著者名","型番","ページ数","定価","ISBN","ページURL"]
csv_date = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "notebook_detail_" + csv_date + ".csv"
with open(csv_file_name,"w", errors = "ignore") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)

  

