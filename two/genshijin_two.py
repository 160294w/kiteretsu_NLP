# 原始人のコトバに変える
from janome.tokenizer import Tokenizer

# 1. 全てカタカナに
# 2. 助詞は削除
def token2genshigo(token):
    if token.part_of_speech.split(',')[0] == "助詞":
        return " "
    else:
        return token.reading


if __name__ == '__main__':
    tokenizer = Tokenizer()
    # input_str = "肉を食べよう！"
    input_str = "これでみんなで原始人。肉を食べよう！"
    # 形態素解析の実施
    tokens = tokenizer.tokenize(input_str)
    result_str = ""
    for token in tokens:
        result_str += token2genshigo(token) + ""
    print(result_str)
    
