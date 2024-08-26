+++
title = 'docker compose downでdockerイメージを削除する'
date = 2024-08-27T02:26:24+09:00
draft = false
summary = 'docker compose down --rmi local --remove-orphans'
+++


## 前提

- compose.ymlを書いて`docker compose up`でコンテナを立ち上げている
- 開発中のリポジトリを別の環境でpullしたときに、compose.ymlやDockerfileに変更があって再ビルドしたいときがある
- そのときにdockerイメージを削除する方法が知りたかったので、`docker compose down`についてchatGPTに聞いた


## 方法

```shell
docker compose down --rmi local --remove-orphans
```

`docker compose down`の効果
- docker compose upで作成・起動したコンテナが停止され、その後削除される
- 自動的に作成されたデフォルトのネットワークも削除される

`--rmi`オプション
- `--rmi local`はDockerfileからビルドしたイメージを削除、
- `--rmi all`にすると全てのイメージを削除

`--remove-orphans`
- (compose.ymlに)定義されていないが存在するコンテナを削除
