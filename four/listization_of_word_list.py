from wakatigaki import *
# 元ネタとなる小説のテキストデータと、
# マルコフ連鎖の単語数（チェインナンバー）を入れると、
# マルコフ連鎖用の辞書を作成する関数
def make_markov_dict(input_text_file_path, chain_number):
  # マルコフ連鎖用の辞書
  markov_dict = {}

  # readlinesで、テキストを読み込んで１行ごとにリスト化
  with open(input_text_file_path) as f:
    text_lines = f.readlines()
    # print(text_lines)

  # １行ごとに処理してマルコフ連鎖用の辞書に追記していく
  for one_line in text_lines:
    # １行ごとに、改行コードやタブなどを消す（綺麗化前処理）
    one_line = ''.join(one_line.splitlines())
    # 形態素解析して、１行を、単語リストにする
    word_list = make_wakati_list(one_line)

    # 単語リストの最初と最後に、文頭/文末を示すフラグを追加する
    word_list = ["__BOS__"] +  word_list + ["__EOS__"]

    # 最低でもchain_number+1個の単語が残っている必要があり、
    # word_listの単語数が十分な間は処理を繰り返す
    while len(word_list) > chain_number:
      # 最初の chain_number 個の単語を、辞書に登録する際のキーとする。
      # （辞書のキーとして扱うため、tupleという形式に変換しておく）
      # key = ("__BOF__", "この", "文章") value = "を" のような形で格納される。
      # ループの２回目では、最初の"__BOF__"が削除されて繰り返されるため、
      # key = ("この", "文章", "を") value = "単語" のような形になる。以下同様  
      key = tuple( word_list[0 : chain_number] )
      # 次に続く単語は、そのキーの次の単語
      value = word_list[chain_number]
      #      print(markov_dict)

      # 初回登録の場合、そのkeyに対する空のリストを作る処理
      # 既にそのkeyに対するデータがある場合は何もしない
      markov_dict.setdefault(key, [] )

      # そのkeyに登録されているリストに、今回のvalueを追加する
      markov_dict[key].append(value)

      # リストの最初の単語を削除する
      # ※ここでだんだん単語数が減っていくため、いつかはループ処理を抜ける
      word_list.pop(0)
  
  # 全ての行を処理し終わったら、完成した辞書データをリターン
  return markov_dict

# コナン・ドイルの全作品からマルコフ連鎖用の辞書データを作成する
konan_markov_dict = make_markov_dict("konan_all_text.txt", 3)

print(list(konan_markov_dict.items())[0:3])
