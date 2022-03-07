import csv
np_dic = {}
fp = open("pn.csv", "rt", encoding="utf-8")
reader = csv.reader(fp, delimiter='\t')
for i, row in enumerate(reader):
    name = row[0]
    result = row[1]
    np_dic[name] = result
print("OK")

# Janomeのロード
from janome.tokenizer import Tokenizer

# Tokenizerインスタンスの生成 
tokenizer = Tokenizer()

# 入力した文字列に対して、
# ポジティブ単語数、ネガティブ単語数、全単語数、の3つを返す
def np_rate(input_str):
  pos_count  = 0
  neg_count  = 0
  word_count = 0
  
  tokens = tokenizer.tokenize(input_str)
  for token in tokens:
    base_form = token.base_form # 原形/基本形
    # ネガポジ辞書に存在するか確認して対応する方を1増やす
    if base_form in np_dic:
      # 単語を辞書のキーとして、そのバリューが p か n か確認する
      if np_dic[base_form] == "p" :
        pos_count += 1
        # どんな言葉がポジ判定されてるか確認用（あとでコメントアウト）
        print("POS:" + base_form) 
      if np_dic[base_form] == "n" :
        neg_count += 1
        # どんな言葉がネガ判定されてるか確認用（あとでコメントアウト）
        print("NEG:" + base_form) 
    # 存在しようがしまいが、単語数を1増やす
    word_count += 1
  return pos_count, neg_count, word_count

print(np_rate("メロスは激怒した。必ず、かの邪智暴虐の王を除かなければならぬと決意した。"))
