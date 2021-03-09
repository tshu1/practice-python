## 関数
"""
スコープ：
変数を定義すると、その変数を読み書きできる範囲が決まる
その範囲のことをスコープと呼ぶ
変数を読むとは、その変数をスコープ内で探すということ
変数のスコープは、変数がプログラム内のどこで定義されているかによって決まる
関数またはクラスの外に変数を定義すると変数はグローバルスコープに定義され、プログラムのどこからでも読み書きできる
グローバルスコープの変数は、グローバル変数と呼ぶ
関数またはクラスの内部に変数を定義すると、その変数はローカルスコープに置かれる
プログラムは、その変数が定義された関数またはクラス内でしか変数を読み書きできない
ローカルスコープの変数は、ローカル変数と呼ぶ
"""

x = 1
y = 2
z = 3

def f():
    print(x)
    print(y)
    print(z)

f()

"""
関数内で定義した変数は、その関数の内部からのみ読み書きできる
Pythonでは、定義された関数の外から関数内の変数にアクセスすると、例外が発生する
"""


def f1():
    x = 1
    y = 2
    z = 3

print(x)
print(y)
print(z)


"""
関数内で指定すると問題ない
"""


def f2():
    x = 1
    y = 2
    z = 3

    print(x)
    print(y)
    print(z)


f2()

"""
どこからでもグローバル変数に書き込めるが、ローカルスコープの中からグローバル変数に書き込むには、
追加の手順としてglobalキーワードを使って明示的に変数を指定する
"""

x = 100

def f3():
    global x
    x += 1
    print(x)

f3()
print(x)

"""
globalを指定しないとグローバル変数に影響を与えない
"""

x = 100

def f4():
    x = 10
    x += 1
    print(x)

f4()
print(x)

## 例外処理

a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)

print(a / b)

"""
コードで例外が発生する可能性があると思った場合、キーワードtryとexceptを含む複合文を使用して例外を捕まえる
try節には、発生する可能性のあるエラーが含まれている
except節には、try節の例外が発生した場合にのみ実行されるコードが含まれている
"""


a = input("type a number:")
b = input("type another:")
a = int(a)
b = int(b)

try:
    print(a / b)
except ZeroDivisionError:
    print("b cannnot be zero.")

"""
次に整数に変換できない文字列をユーザが入力した場合も、プログラムはエラーで中断する

>>> a = input("type a number:")
type a number:test
>>> b = input("type another:")
type another:10
>>> a = int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'test'

ValueErrorが想定されるので、以下のように修正する
"""

try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")
    


"""
except節内で、try節で定義されたヘンスを使用しないこと
try節でヘンスが定義される前に例外が発生する可能性がり、変数定義前に例外が発生するとexcept節で別の例外が発生するため

try:
    10 / 0
    c = "I will never get defined."
except ZeroDivisionError:
    print(c)

>> NameError: name 'c' is node defined
"""

### ドキュメンテーション文字列

"""
関数宣言の次の行にdocstring(ドキュメンテーション文字列)と呼ばれるコメントを書いて、引数のデータ型について説明する
docstringには、関数の目的と、必要な引数の種類について説明を書く
"""

def add(x, y):
    """
    Returns x + y.
    : param x: int.
    : param y: int.
    : return: int sum of x and y.
    """
    return x + y

print(add(1, 2))


## チャレンジ
### 1.

def f5(x):
    return x ** 2

print(f5(8))

### 2,

def s(x):
    return str(x)

print(s("test"))

### 3.

def f6(x, y, z, a=10, b=5):
    return x + y + z + a + b

print(f6(1,2,3,4,5))

### 4.

def f7(x):
    return int(x) / 2

def f8():
    global result
    return int(result) * 4


result = f7(10)
print(f8())

### 5.

def f9(x):
    try:
        string = str(x)
        return float(string)
    except ValueError:
        print("cannot convert string to float")

f9("test")