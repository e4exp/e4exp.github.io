+++
title = 'sshトンネルを使って、githubからアクセストークンなしでリモートサーバにcloneする方法'
date = 2024-08-05T22:35:10+09:00
draft = false
summary = "ssh -A -L 2222:github.com:22 user@remote_machine"
+++


# sshトンネルを使って、githubからアクセストークンなしでリモートサーバにcloneする方法

## 前提

- 自身が管理者ではないgithubリポジトリで作業している。sshキーは登録してある
- リポジトリをリモートサーバ上でcloneしたい
- sshの秘密鍵をリモートサーバにアップロードしたくない
- 管理画面に入れないのでパーソナルアクセストークンは作れない


## 方法

sshトンネルを使って、リモートサーバ上でローカル端末のssh秘密鍵を参照し、githubからリポジトリをcloneする

```shell
# ローカル端末で、githubの秘密鍵をsshエージェントに登録
ssh-add /path/to/github_private_key

# ローカル端末で実行し、リモートサーバにsshログイン
ssh -A -L 2222:github.com:22 user@remote_machine

# リモートサーバでcloneを実行
git clone git@github.com:username/your_repo.git
```

## その他の方法


ChatGPTに聞いたら以下の4種類帰ってきた

1. git archive を使ってアーカイブを作成し、scp等でサーバに転送する
    - `git archive`コマンドを使うと、作業中のディレクトリからgit管理されているファイルだけを抽出して保存できるらしい
2. パーソナルアクセストークンを使ってHTTPS経由でリポジトリをクローン
3. githubからDownload ZIPでリソースをダウンロード
    - これで得られるのは1の`git archive`コマンドで抽出できるものと同じらしい
4. SSHトンネルを利用する(本記事で紹介した方法)


## 参考記事

- `Git リポジトリの内容を zip ファイルにする` 2019  
    - https://qiita.com/usamik26/items/9a2d14aea30cb01a60c6
        > git clone したフォルダを単純に zip すると、.git フォルダが含まれてしまったり、普段は .gitignore などで無視しているファイルが含まれてしまったりします。  
        > Git リポジトリの内容だけを取り出して zip ファイルにするには、git archive コマンドが便利