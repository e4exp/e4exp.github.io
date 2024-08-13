+++
title = 'テキストファイルの行について、重複がないように抽出するコマンド'
date = 2024-08-14T01:00:27+09:00
draft = false
summary = 'sort -u input.txt > output.txt'
+++



## 前提

- テキストファイル内の1行ごとにプログラムの実行ログが書いてあり、同じ内容の行は飛ばして、内容の異なるすべての行を別のファイルに抽出したい


## 方法

以下のように`sort`コマンドでできる
```shell
sort -u input.txt > output.txt
```

以下のように`uniq`コマンドでもできるらしい
```shell
sort input.txt | uniq > output.txt
```

> テキストファイル input.txt をソートします。uniqコマンドは連続する重複行しか処理しないため、事前にソートが必要です。

とのこと。