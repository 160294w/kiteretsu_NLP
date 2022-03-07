# 原始人のコトバに変える
from janome.tokenizer import Tokenizer

def hiragana_to_katakana(input_str):
    return "".join([chr(ord(ch) + 96) if ("あ" <= ch <="ん") else ch for ch in input_str])

# 1. 全てカタカナに
# 2. 助詞は削除
def token2genshigo(token):
    if token.part_of_speech.split(',')[0] == "助詞":
        return " "
    else:
        return token.reading

def start(input_str):
    tokenizer = Tokenizer()
    # input_str = "肉を食べよう！"
    # 形態素解析の実施
    tokens = tokenizer.tokenize(input_str)
    result_str = ""
    for token in tokens:
        result_str += token2genshigo(token) + ""
    return(result_str)


if __name__ == '__main__':
    str_ = "これでみんなで原始人。肉を食べよう！"
    #print(start("これでみんなで原始人。肉を食べよう！"))
    print(hiragana_to_katakana(str_))
