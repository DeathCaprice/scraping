# scraping
pythonでwebスクレイピングした実装コードです。

コードの実装について、完了しスクレイピングを実行してから日数が経過しており、現在webサイトの構造等が変化し、現在スクレイピングを実行しても情報収集できない可能性や以下のリンクをクリックしてもリンク切れしている場合がありますが、コード実装後のスクレイピング実施時には問題なく情報収集出来ております。
その証拠としては、収集した情報が反映されるエクセルファイルや別途作成してあるフォルダに格納されている画像ファイルです。


〇スクレイピング(1)/sbクリエイティブ/一覧ページ/sbitirannpage.py
sbクリエイティブの一覧ページ（トップページ）の「書名、著者名、発売日、カテゴリー名、画像url」と詳細ページのを抽出しました。
（https://www.sbcr.jp/books/investment/）

〇スクレイピング(1)/sbクリエイティブ/詳細ページ/sbsilyousaipage.py
sbクリエイティブの詳細ページの書名、著者名、サブタイトル、記事、定価、発売日、ISBN、サイズ、ページ数、画像を抽出しました。
尚、画像ファイルはファイルアップロード時に許容範囲を超えたため別のフォルダの「SBCR社の画像スプレイピング」にアップロードしております。
（https://www.sbcr.jp/books/investment/）

〇スクレイピング(2)/技術評論書籍/一覧ページ/gihiyousinnkanitiran.py
技術評論書籍サイトの一覧ページ（トップページ）の書名 著者名 定価 詳細ページURLを抽出しました。
（https://gihyo.jp/book/list?start=0）

〇スクレイピング(2)/技術評論書籍/詳細ページ/gihiyosiyousaipege.py
技術評論書籍サイトの詳細ページのurl、書名、発売日、著者名、型番/ページ数、定価、ISBNを抽出しました。
（https://gihyo.jp/book/list?start=0）

〇スクレイピング(2)/技術評論社(httpsgihyo.jp)/4.3.1.kijisiage.py
技術評論社の記事ページのURL、タイトル、発行日、記事を抽出しました。
（https://gihyo.jp"）

☆以下、翔泳社のスクレイピング
（https://www.seshop.com/）

〇スクレイピング(3)/翔泳社/一覧ページ
①silyoueisilyagazou.py・・・画像ファイルのスプレイピング
スプレイピングした画像はフォルダ「siyoueiimage」に抽出しております。
②silyoueisilyaitirannpage.py・・・一覧ページのスプレイピング。結果は「notebook_2023103122.csv」
③silyoueisilyaitirannpegepandas.py・・・一覧ページのスプレイピング。結果は「books.xlsx」

〇スクレイピング(3)/翔泳社/詳細ページ/
silyoueisilyasilyousaipage.py・・・書名　著者名 発売日 ISBN  判型 ページ数 画像urlを抽出しました。

〇スクレイピング(4)/技術評論書籍画像/itiranngazou.py
技術評論書籍サイトの画像を抽出しました。

(https://gihyo.jp/book/list?start=0)

画像ファイルはファイルアップロード時に許容範囲を超えたため別のフォルダの
/技術評論書籍画像①/gihiyou①/
/技術評論書籍画像②/gihiyou②/
にアップロードしております。
