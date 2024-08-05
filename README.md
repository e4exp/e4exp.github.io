
`Quick start`
https://gohugo.io/getting-started/quick-start/

## テーマ追加

一覧 https://themes.gohugo.io
```shell
git submodule add https://github.com/alex-shpak/hugo-book themes/hugo-book
echo "theme = 'hugo-book'" >> hugo.toml
hugo server
```

## 記事追加

```shell
hugo new content content/post/記事タイトル.md
```

## プレビュー


```shell
# -Dをつけるとdraft=falseの記事も表示される
hugo server -D
```
