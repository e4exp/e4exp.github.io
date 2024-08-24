+++
title = 'pandas.Dataframeで、引数に与える辞書のkeyは列名、valueは列方向の値'
date = 2024-08-25T04:11:56+09:00
draft = false
summary = ""
+++


## 前提


- google Colaboratory
- pandas==2.1.4
- pandasのDataframeで以下のようなデータを作成した際に、各列と各行はどれか、またA,Bは何か知りたかったのでChatGPTに聞いた。聞いた結果をgoogle Colabで実行して確認した

```python
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})
```


## 説明

```python
import pandas as pd

# keyのA,Bは列名、valueのlistは各列の値
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})
```


```python
df
```
以下のような`DataFrame`が作成されている
|    | A | B  |
|----|---|----|
| 0  | 1 | 10 |
| 1  | 2 | 20 |
| 2  | 3 | 30 |
| 3  | 4 | 40 |


```python
df["A"]
```
列Aにアクセスしている
|	|A|
|---|---|
|0	|1|
|1	|2|
|2	|3|
|3	|4|


```python
df.iloc[0]
```
行0にアクセスしている
|	|0|
|---|---|
|A	|1|
|B	|10|

