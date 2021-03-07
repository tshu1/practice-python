## 改行コード

print("""これは、改行が行われるものです。
どういうことかというと。
こういう形で、改行すると、それがそのまま表示されます。
      段落を合わせるとこういった形になります。""")


## for

for i in range(10):
    print("Hello, World!")

## データ型

print(2.2 + 2.2 )


## 定数と変数

print(2 + 2)
print(2 - 2)
print(4 / 2)
print(2 * 2)

## インクリメント、デクリメント

x = 10
print(x)
x = x + 1
print(x)

x = x -1
print(x)
x = x -1
print(x)

x = 10
print(x)
x += 1
print(x)
x -= 1
print(x)

## 変数のルール
"""
1. 変数名にはスペースを含めることはできない(区切りたい場合はアンダースコア"_"を使用すると良い)
1. 変数名には文字、数値、アンダースコア記号の３種類の文字だけを含めることができる
1. 変数名の１文字目に数値は使えない
1. 変数目の１文字目にアンダースコアを使用することはできるが、アンダースコアではじまる変数名は特別な意味を持つ
1. pythonのキーワードは変数名には使えない
    https://docs.python.org/ja/3/reference/lexical_analysis.html#keywords

## 構文
ある言語において、単語の順序で文章の構造を支配する、一連の規則、原則、処理のこと
例えば、Pythonでは、文字列は必ずクォートで囲まれている
"""

print("これが文字列")

## エラーと例外

"""
my_string = "Hello World.
"""

"""
  File "/Users/tshu1/ghq/github.com/tshu1/practice-python/section3.py", line 63
    my_string = "Hello World.
                            ^
SyntaxError: EOL while scanning string literal
"""

"""
pythonには２種類のエラーがある

1. 構文エラー(SyntaxError)
1. 例外(Exception)

構文エラーでないエラーはすべて例外です
後部エラーと違って、例外は致命的ではありません
例外が起きることを想定してプログラムを書いていれば、例外がおきてもプログラムを実行し続けられます
"""

"""
print(10/0)
"""

"""
Traceback (most recent call last):
  File "/Users/tshu1/ghq/github.com/tshu1/practice-python/section3.py", line 85, in <module>
    print(10/0)
ZeroDivisionError: division by zero
"""

## 算術演算子

"""
|演算子|意味|例|評価結果|
|:--|:--|:--|:--|
|**|累乗|2 ** 3|8|
|%|割り算のあまり(剰余)| 14 % 4|2|
|//|整数の割り算、切り捨て|13 // 8 |1|
|/|割り算(除算)|13 / 8 | 1.625 |
|*|掛け算(積算)|8 * 2|16|
|-|引き算(減算)|7 - 1|6|
|+|足し算（加算)|2 + 2|4|
"""

print("13//5の結果は :", 13//5)
print("13%5の結果は :", 13%5)
print("12%2の結果は :", 12%2)

"""
2を剰余計算に使うと、あまりがなければ偶数、余りがあれば奇数となる
"""


"""
- 演算子の前後に書く値(ここでは数値)は被演算子(あるいはオペランド)といいます。
- ２つの被演算子と１つの演算子があれば、それを式(expression)と言います。
"""

## 演算子の優先順位

"""
Please Excuse My Dear Aunt Sally ?
の頭文字で暗記すると良く、以下の優先順位となる

- Parentheses(カッコ)
- Exponents(累乗)
- Multiplication(掛け算)
- Division(割り算)
- Addition(足し算)
- Subtraction(引き算)
"""


## 比較演算子

"""
算術演算子と同様に、2つの被演算子と1つの演算子で1つの式を表す
Pythonでは、比較演算子は算術演算子とは別のカテゴリです
比較演算子を使った式は、True or Falseのどちらかしか返さないという点が異なります
"""

"""
|演算子|意味|例|評価結果|
|:--|:--|:--|:--|
|>|より大きい|100 > 10|True|
|<|より小さい|100 < 10|False|
|>=|以上|2 >= 2|True|
|<=|以下|1 <= 4 |True|
|==|等価|6 == 9|False|
|!=|非等価|3 != 2|True|
"""

## 論理演算子

"""
論理演算子は比較演算子と同様にTrue or Falseのどちらかを返します
"""

"""
|演算子|意味|例|評価結果|
|:--|:--|:--|:--|
|and|かつ| True and True|True|
|or|または|True or False|True|
|not|否定| not True|False|
"""

"""
and はPythonのキーワードで、andの左右に与えられた式がTrueと評価される場合にTrueを返します
どちらかがFalseと評価された場合は、Falseを返します
"""

print("1 == 1 and 2 ==2", 1 == 1 and 2 == 2)
print("1 == 2 and 2 ==2", 1 == 2 and 2 == 2)
print("1 == 2 and 2 ==1", 1 == 2 and 2 == 1)
print("1 == 1 and 10 != 2 and 2 < 10",1 == 1 and 10 != 2 and 2 < 10)

"""
orキーワードは、orの左右に与えられた式どちらかがTrueと評価されればTrueを返します
"""


print("1 == 1 or 1 ==2", 1 == 1 or 1 == 2)
print("1 == 1 or 2 ==2", 1 == 1 or 2 == 2)
print("1 == 2 or 2 ==1", 1 == 2 or 2 == 1)
print("1 == 1 or 1 ==2 or 1 == 3", 1 == 1 or 1 == 2 or 1 == 3)

"""
notキーワードは式の前に書いて、その式の評価結果を逆転します
"""

print("not 1 == 1", not 1 == 1)
print("not 1 == 2", not 1 == 2)


## 条件文

home = "america"
if home == "america":
    print("Hello, America!")
else:
    print("Hello World!")


home = "japan"
if home == "america":
    print("Hello, America!")
else:
    print("Hello, World!")


home = "japan"
if home == "japan":
    print("Hello, Japan")

x = 2
if x == 2:
    print("数値は2です。")
if x % 2 == 0:
    print("数値は偶数です。")
if x % 2 != 0:
    print("数値は奇数です。")

x = 10
y = 11

if x == 10:
    if y == 11:
        print("x + y = ", x + y)

home = "タイ"
if home == "日本":
    print("Hello, Japan!")
elif home == "タイ":
    print("Hello, Thailand!")
elif home == "インド":
    print("Hello, India!")
elif home == "中国":
    print("Hello, Chaina!")
else:
    print("Hello, World!")


## 文

"""
- 単純文
    - 1行のコードで表現される
- 複合文
    - 通常複数の行で表現される
    - 1つ以上の節で構成される
    - 1つの節は2行以上のコードで、1行のヘッダー部分と、それに続くスイート部分で構成されている
    - ヘッダーは、キーワードが含まれる1行のコードです
    - 行の最後にコロン(:) があり、インデントされた1行以上のコード(スイート)が次に続きます
    - 1つのスイートは1行のコードだけで構成されます
"""

for i in range(10):
    print("Hello, World!")

## チャレンジ
### 1 3つの異なる文字列を出力しよう

print("文字列")
print("1 + 1 = ", 1 + 1)
s = "変数にいれた文字列"
print(s)

### 変数が10未満だったらメッセージを出力しよう。10より大きく25以下だったら、別のメッセージを出力しよう。25よりおおきかったらさらに別のメッセージを出力しよう

n = 9
m1 = "10より小さい数字です"
m2 = "10より大きく25以下の数字です"
m3 = "25より大きい数字です"

if n < 10:
    print(m1)
elif 10 < n <= 25:
    print(m2)
elif n > 25:
    print(m3)
    

### 2つの値で割り算して、その余りを出力しよう
print("8 / 5 の余りは？", 8 % 5)

### 2つの値で割り算して、その商を出力しよう
print("8 / 5 の商は？", 8 // 5)

age = 19

if age < 13:
    print("あなたは小学生です")
elif 12 < age < 16:
    print("あなたは中学生です")
elif 15 < age < 19:
    print("あなたは、高校生の可能性が高いです")
else:
    print("あなたは、学生ではありません")