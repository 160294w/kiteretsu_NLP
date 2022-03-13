# Janomeのロード
from janome.tokenizer import Tokenizer

# Tokenizerインスタンスの生成 
tokenizer = Tokenizer()

# 文章を入れると、単語のリストにする関数
# Janomeの wakati = True オプションを使う方法もあるが、
# これまで使ってきているのと同様の形式で実装
def make_wakati_list(input_str):
  result_list = []
  tokens = tokenizer.tokenize(input_str)
  for token in tokens:
    # 元の単語＋半角スペースを追加しているため、
    # 結果とした、単語の切れ目全てに半角スペースが入る
    result_list.append(token.surface)
  return result_list

print(make_wakati_list("この文章を単語の切れ目で区切ってみよう。"))
