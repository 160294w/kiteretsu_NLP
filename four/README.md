# Overview
江戸川乱歩とコナンドイルのデータからマルコフ連鎖で文章を生成する。

## Preparation

データ作成

```
$ download_data_from_zip_url.py
```

## Usage


文章生成

```
$ python3 markov.py
```

## Other

青空文庫のデータを取得する
```
wget http://x0213.org/codetable/jisx0213-2004-std.txt
```