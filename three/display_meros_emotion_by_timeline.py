from main import *
from download_from_aozora import *
import matplotlib.pyplot as plt
plt.ion()

# ダウンロードしたいURLを入力する
ZIP_URL = 'https://www.aozora.gr.jp/cards/000035/files/1567_ruby_4948.zip'

# ダウンロード＆テキスト取得
aozora_dl_text = get_flat_text_from_aozora(ZIP_URL)

# タグや外字などのデータを加工
flat_text = flatten_aozora(aozora_dl_text) 

# フラットなテキストを「改行コード」で区切ってリスト形式にする
mero_list = flat_text.split('\n')
#print(mero_list);
# グラフ作成用のx軸,　y軸
# X座標（物語の進行の時間軸として、それまでの単語総数を入れる）
x =  []
# Y座標は２種類＝positive_levelにポジティブ度合い、negative_levelにネガティブ度合いとする
positive_level = []
negative_level = []

total_word_count = 0
# 作ったリストの各要素に対して処理を行う
for mero_str in mero_list:
  # リストの中身＝文字列に対してネガポジ分析を行う。
  pos_count, neg_count, word_count = np_rate(mero_str)
  # 単語数が０となる行があった場合、その行を飛ばす（０除算防止）
  if word_count <1 :
    continue
  # 全単語数に対するポジティブの比率を、リストに追加する
  positive_level.append(pos_count/word_count)
  # 全単語数に対するポジティブの比率を、リストに追加する
  negative_level.append(neg_count/word_count)
  # これまでに出てきた単語数の合計をX軸とする
  total_word_count += word_count
  x.append(total_word_count)

# グラフのフォーマットを指定してプロット
plt.plot(x, positive_level, marker="o", color = "red", linestyle = "--")
plt.plot(x, negative_level, marker="x", color = "blue",  linestyle = ":")

plt.show()
plt.savefig('meros_negaposi.png')
