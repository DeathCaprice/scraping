# scraping
pythonでwebスクレイピングしたコードです。

〇スクレイピング(1)/sbクリエイティブ/一覧ページ/sbitirannpage.py
sbクリエイティブ（https://www.sbcr.jp/books/investment/）の一覧ページ（トップページ）の「書名、著者名、発売日、カテゴリー名、画像url」と詳細ページのを抽出しました。


〇スクレイピング(1)/sbクリエイティブ/詳細ページ/sbsilyousaipage.py
sbクリエイティブ（https://www.sbcr.jp/books/investment/）の詳細ページの書名、著者名、サブタイトル、記事、定価、発売日、ISBN、サイズ、ページ数、画像を抽出しております。
尚、画像ファイルはファイルアップロード時の許容範囲を超えたため別のフォルダの「SBCR社の画像スプレイピング」にアップロードしております。

〇スクレイピング(2)/技術評論書籍/一覧ページ/gihiyousinnkanitiran.py
技術評論書籍サイト（https://gihyo.jp/book/list?start=0）の一覧ページ（トップページ）の書名 著者名 定価 詳細ページURLを抽出しております。

〇スクレイピング(2)/技術評論書籍/詳細ページ/gihiyosiyousaipege.py
技術評論書籍サイト（https://gihyo.jp/book/list?start=0）の詳細ページのurl、書名、発売日、著者名、型番/ページ数、定価、ISBNを抽出しております。

