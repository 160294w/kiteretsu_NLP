import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

# <a href>タグのリンク先URL（絶対URL）を全て取得する関数
def get_a_href_list_from_url(load_url):
  html = requests.get(load_url)
  soup = BeautifulSoup(html.content, "html.parser")
  result_url_list = []
  for a_element in soup.find_all("a"):
    # 空だった場合は次のエレメントへ継続
    if a_element == None:
      continue
    # 各href属性を取得する
    link_str = a_element.get("href")
    # 空だった場合は次のエレメントへ継続
    if link_str == None:
      continue

    # "../cards/000009/card50713.html" などは
    # 元のURL（load_url）からのリンクとして相対的参照になっているため、
    # 元のURL+相対URLを入れると絶対URLを返してくれるライブラリを使用して加工する
    # urllib.parse.urljoin("http://www.example.com/foo/bar.html", "../hoge/fuga.html")
    # ⇒ http://www.example.com/hoge/fuga.html
    abs_url = urllib.parse.urljoin(load_url, link_str)

    # 取得した絶対URLを結果リストへ追加
    result_url_list.append(abs_url)
  return result_url_list

# 作者ページのURLを入力すると、ページを全探索して
# その作者の作品のzipファイルのURL一覧を返す関数
# 作者ページのURL = "https://www.aozora.gr.jp/index_pages/person9.html" など
def sakusyaurl2zipurllist(sakusya_url):
  # 作者ページから出ている全てのリンク先URLを取得
  url_list_from_sakusya = get_a_href_list_from_url(sakusya_url)

  # 図書カード＝作品ごとのページ、のURLを探す
  # 末尾が、 /cards/000009/card50713.html　のような形式になっている
  tosyo_card_url_list = []
  for tosyo_card_url in url_list_from_sakusya:
    # 条件に一致する場合（cardのURLの場合）のみリストに追加
    if re.match(r'.*cards.*card.*\.html', tosyo_card_url):
      tosyo_card_url_list.append(tosyo_card_url)

  # 図書カード＝作品ごとのページ に再度スクレイピングでアクセスして、
  # そのリンク先を全て取得
  # https://www.aozora.gr.jp/cards/000082/files/1293_ruby_5382.zip
  # のように、青空文庫内のZIPファイルへのアクセスになっている箇所を取得する
  zip_url_list = []
  for tosyo_card_url in tosyo_card_url_list:
    # 図書カードから出ている全てのリンク先URLを取得
    for zip_url in get_a_href_list_from_url(tosyo_card_url):
      # 条件に一致する場合（zipのURLの場合）のみリストに追加
      if re.match(r'.*aozora.*ruby.*\.zip', zip_url):
        zip_url_list.append( zip_url )

  # 取得したzipファイルの絶対URL一覧を返す
  return zip_url_list

# 江戸川乱歩の全作品のzipファイルのURLリスト
edogawa_zip_list = sakusyaurl2zipurllist("https://www.aozora.gr.jp/index_pages/person1779.html")
# 実際に取得できたリストを書き出す
print(edogawa_zip_list)
# 取得したリストの個数を書き出す
print(len(edogawa_zip_list))

# コナン・ドイルの全作品のzipファイルのURLリスト
konan_zip_list = sakusyaurl2zipurllist("https://www.aozora.gr.jp/index_pages/person9.html")
# 実際に取得できたリストを書き出す
print(konan_zip_list)
# 取得したリストの個数を書き出す
print(len(konan_zip_list))

