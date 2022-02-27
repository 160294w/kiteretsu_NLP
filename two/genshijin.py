from janome.tokenizer import Tokenizer

tokenizer = Tokenizer()
token = "肉を食べよう！"

# 形態素解析の実施
tokens = tokenizer.tokenize(token)

for token in tokens:
    #print(token)
    print("Original: ", token.surface)
    print("ヨミガナ:", token.reading) 
    print("原形:", token.base_form) 
    print("品詞情報:", token.part_of_speech)
    print(token.part_of_speech.split(','))
    print("可能性の高い品詞:", token.part_of_speech.split(',')[0])
    print("-----")
