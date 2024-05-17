import requests
from bs4 import BeautifulSoup
import datetime
import csv
from urllib.parse import urljoin
from time import sleep


#詳細ページからスクレイピング
url = "https://www.seshop.com/product/616"
item_list = []

for i in range(9):
# while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    divs = soup.select("div.list div.inner")
    for div in divs:
        #ページURL取得
        div_txt=div.find("div",class_="txt")
        a_tag = div_txt.find("a") 
        item_url=urljoin(url,a_tag["href"])
        response = requests.get(item_url)
        soup_detail = BeautifulSoup(response.text, "html.parser")

        # 　書名　著者名 発売日 ISBN  判型 ページ数 画像url
        item_name = soup_detail.find("h1").text.strip().replace("発売予定","")
        div_txt=soup_detail.find("div",class_="col-md-5")
        # aタグを取得
        a_tag = div_txt.find("a")
        # 著者名を取得
        item_author = a_tag.text.strip()
       
        item_releasedate = soup_detail.select("dl > dd:nth-child(8)")[0].text.strip()
        item_isbn=soup_detail.select("dl > dd:nth-child(12)")[0].text
     
        item_format=soup_detail.select("dl > dd:nth-child(14)")[0].text.strip()
        item_page=float(soup_detail.select("dl > dd:nth-child(16)")[0].text.strip())
        

        
        item_list.append([item_name, item_author, item_releasedate,item_isbn, item_format, item_page])
        sleep(1)

    if soup.select("a:-soup-contains('Next')"):
        url = urljoin(url, soup.select("a:-soup-contains('Next')")[0]["href"])
    else:
        break


csv_header = ["書名","著者名","発売日","ISBN","判型","ページ数"]
csv_date = datetime.datetime.today().strftime("%Y%m%d%H")
csv_file_name = "notebook_detail_" + csv_date + ".csv"
with open(csv_file_name,"w", errors = "ignore") as file:
    writer = csv.writer(file,lineterminator="\n")
    writer.writerow(csv_header)
    writer.writerows(item_list)



   
