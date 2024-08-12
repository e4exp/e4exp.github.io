+++
title = 'Mysql_user_function'
date = 2024-08-13T01:43:46+09:00
draft = true
summary = ''
+++


# MySQLのユーザ定義関数を使うと、SELECT時に関数の戻り値を選択できるらしい




## 前提

- MySQLで、クエリ文字列に最も近い文字列をテーブル内のレコードから選択したい
- Levenshtein距離(1つの文字列を別の文字列に変換するために必要な操作（挿入、削除、置換）の最小回数を示す)を使って文字列間の類似度を測ることができるらしい

## 方法


### 定義

```shell
DELIMITER $$

CREATE FUNCTION LEVENSHTEIN(s1 VARCHAR(255), s2 VARCHAR(255))
RETURNS INT
DETERMINISTIC
BEGIN
  DECLARE s1len, s2len, i, j, c, ctemp, cost INT;
  DECLARE cv0, cv1 VARBINARY(256);

  SET s1len = CHAR_LENGTH(s1), s2len = CHAR_LENGTH(s2), cv1 = 0x00, j = 1, i = 1, c = 0;

  IF s1 = s2 THEN
    RETURN 0;
  ELSEIF s1len = 0 THEN
    RETURN s2len;
  ELSEIF s2len = 0 THEN
    RETURN s1len;
  ELSE
    WHILE j <= s2len DO
      SET cv1 = CONCAT(cv1, UNHEX(HEX(j))), j = j + 1;
    END WHILE;
    WHILE i <= s1len DO
      SET c = i, cv0 = UNHEX(HEX(i)), j = 1;
      WHILE j <= s2len DO
        SET cost = IF(SUBSTRING(s1, i, 1) = SUBSTRING(s2, j, 1), 0, 1);
        SET ctemp = CONV(HEX(SUBSTRING(cv1, j, 1)), 16, 10) + cost;
        SET c = LEAST(c + 1, CONV(HEX(SUBSTRING(cv1, j+1, 1)), 16, 10) + 1, ctemp);
        SET cv0 = CONCAT(cv0, UNHEX(HEX(c))), j = j + 1;
      END WHILE;
      SET cv1 = cv0, i = i + 1;
    END WHILE;
  END IF;
  RETURN c;
END$$

DELIMITER ;
```


### 使用方法

テーブル内の各文字列とクエリ文字列のLevenshtein距離を計算し、距離が最も小さいレコードを取得
```sql
SELECT *, LEVENSHTEIN(column_name, 'query_string') AS distance
FROM table_name
ORDER BY distance
LIMIT 1;
```

