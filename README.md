# scraping
pythonでwebスクレイピングしたコードです。

〇スクレイピング(1)/sbクリエイティブ/一覧ページ/sbitirannpage.py
sbクリエイティブ（https://www.sbcr.jp/books/investment/）の一覧ページ（トップページ）の「書名、著者名、発売日、カテゴリー名、画像url」と詳細ページのを抽出しました。

〇スクレイピング(1)/sbクリエイティブ/詳細ページ/sbsilyousaipage.py
sbクリエイティブ（https://www.sbcr.jp/books/investment/）の詳細ページの書名、著者名、サブタイトル、記事、定価、発売日、ISBN、サイズ、ページ数、画像を抽出しました。
尚、画像ファイルはファイルアップロード時の許容範囲を超えたため別のフォルダの「SBCR社の画像スプレイピング」にアップロードしております。

〇スクレイピング(2)/技術評論書籍/一覧ページ/gihiyousinnkanitiran.py
技術評論書籍サイト（https://gihyo.jp/book/list?start=0）の一覧ページ（トップページ）の書名 著者名 定価 詳細ページURLを抽出しました。

〇スクレイピング(2)/技術評論書籍/詳細ページ/gihiyosiyousaipege.py
技術評論書籍サイト（https://gihyo.jp/book/list?start=0）の詳細ページのurl、書名、発売日、著者名、型番/ページ数、定価、ISBNを抽出しました。

〇スクレイピング(2)/技術評論社(httpsgihyo.jp)/4.3.1.kijisiage.py
技術評論社（https://gihyo.jp"）の記事ページのURL、タイトル、発行日、記事を抽出しました。


☆以下、翔泳社（https://www.seshop.com/）のスクレイピング
〇スクレイピング(3)/翔泳社/一覧ページ
①silyoueisilyagazou.py・・・画像ファイルのスプレイピング
スプレイピングした画像はフォルダ「siyoueiimage」に抽出しております。
②silyoueisilyaitirannpage.py・・・一覧ページのスプレイピング。結果は「notebook_2023103122.csv」
③silyoueisilyaitirannpegepandas.py・・・一覧ページのスプレイピング。結果は「books.xlsx」
〇スクレイピング(3)/翔泳社/詳細ページ/
silyoueisilyasilyousaipage.py・・・書名　著者名 発売日 ISBN  判型 ページ数 画像urlを抽出しました。





