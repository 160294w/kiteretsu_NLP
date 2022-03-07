ojou_word_dict = {
    "こんにちは":"ごきげんよう",
    "すみません":"恐れ入ります",
    "ああそう":"左様でございますか",
    "おなら":"天使のため息",
    "ぶっとばすぞ":"快適な空の旅をお楽しみください",
    }

def word2ojou(input_str):
    result_str = input_str
    for key, value in ojou_word_dict.items():
        result_str = result_str.replace(key, value)
    return result_str

print(word2ojou('こんにちは、調子はどう？'))
print(word2ojou('すみません、おならが出そうです。'))
print(word2ojou('ああそう、ぶっとばすぞ。'))
    
