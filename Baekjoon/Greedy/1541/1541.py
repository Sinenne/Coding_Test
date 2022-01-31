"""

0以上の数字と＋、－、そして括弧を使って式を作った。そして括弧をすべて消した。
そうしてから括弧を適切につけて、式の値を最小にしようとする。
そのプログラムを書け。

"""


formula = input()

def cal(formula):
    if "-" in formula:
        sep = formula.rsplit("-", 1)
        return cal(sep[0]) - cal(sep[1])
    elif "+" in formula:
        sep = formula.rsplit("+", 1)
        return cal(sep[0]) + cal(sep[1])
    else:
        return int(formula)
    
print(cal(formula))


"""
Greedyの条件をーの式を先に考えるようにした。
最初はRsplitの代わりにSplitを使ったものの
正式な計算順と逆になって誤答になった。

"""
