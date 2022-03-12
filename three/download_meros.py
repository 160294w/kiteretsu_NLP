from download_from_aozora import *
# ダウンロードしたいURLを入力する
ZIP_URL = 'https://www.aozora.gr.jp/cards/000035/files/1567_ruby_4948.zip'

# 青空文庫からダウンロードする関数を実行
aozora_dl_text = get_flat_text_from_aozora(ZIP_URL)

# 途中経過を見たい場合以下のコメントを解除
# 冒頭1000文字を出力
print(aozora_dl_text[0:1000])

# 青空文庫のテキストを加工する関数を実行
flat_text = flatten_aozora(aozora_dl_text)

# 冒頭1000文字を出力
print(flat_text[0:1000])
