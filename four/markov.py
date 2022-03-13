import random
from listization_of_word_list import * 

# マルコフ連鎖用の辞書と最初のキー候補リストを入れると文章を作る関数
def make_markov_sentence(markov_dict):
  # 出力用の文字列
  output_sentence = ""

  # 最大１万回ランダムに繰り返して冒頭を取得する
  key_list = list(markov_dict.keys())
  for a in range(10000):
    # 最初のキーをランダムに取得する
    key = random.choice(key_list)
    # 文頭のフラグが出るまで繰り返し
    if key[0] == "__BOS__":
      break
  
  # key(tuple型)を結合して文字列にして追記
  output_sentence += "".join(map(str, key))
  
  # 最大１万回繰り返し（通常は途中でbreakして終了）
  for a in range(10000):
    # keyに対応するvalue（次の単語候補のリスト）を取得
    value = markov_dict.get(key)
    # 例外処理：もしkeyが辞書に見つからない場合処理終了
    if value == None:
      break

    # 単語のリストから次の単語をランダムに選ぶ
    next_word = random.choice(value)
    # 文章に追記する
    output_sentence += next_word
    # 文末のフラグが出ていたら終了
    if next_word == "__EOS__":
      break
    
    # 既存キーの最初を除外して、next_wordをくっつけて新しいkeyに更新する
    # ※tupleの結合処理
    key = key[1:] + (next_word, )
  
  # 生成された文章を返す
  return output_sentence

# 何回か文章を生成してみる
for a in range(20):
  print(make_markov_sentence(konan_markov_dict))

