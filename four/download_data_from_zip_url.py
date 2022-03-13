from get_zip_url_of_edogawa_book import *
from download_from_aozora import * 

edogawa_zip_list = sakusyaurl2zipurllist("https://www.aozora.gr.jp/index_pages/person1779.html")

# 江戸川乱歩の全データの取得＆加工
edogawa_all_text = get_all_flat_text_from_zip_list(edogawa_zip_list)
# 得た結果をファイルに書き込む
with open('edogawa_all_text.txt', 'w') as f:
  print(edogawa_all_text, file=f)
  print("★江戸川ALLファイル出力完了")

konan_zip_list = sakusyaurl2zipurllist("https://www.aozora.gr.jp/index_pages/person9.html")

# コナン・ドイルの全データの取得＆加工
# ※超例外的に１件だけ別作家の小説をリンク/紹介しているため、除外
konan_zip_list.remove("https://www.aozora.gr.jp/cards/000082/files/1293_ruby_5382.zip")
konan_all_text = get_all_flat_text_from_zip_list(konan_zip_list)
# 得た結果をファイルに書き込む
with open('konan_all_text.txt', 'w') as f:
  print(konan_all_text, file=f)
  print("★コナンALLファイル出力完了")

# 江戸川＆コナンの両方の全テキストをつなげたファイルも作っておく
edogawa_konan_all_text = edogawa_all_text + konan_all_text
with open('edogawa_konan_all_text.txt', 'w') as f:
  print(edogawa_konan_all_text, file=f)
  print("★江戸川＆コナンALLファイル出力完了")

