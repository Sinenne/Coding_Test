

"""
Nこのロープがある。これを使い様々なものを運ぶことができる。
各々のロープはその太さや長さが異なるため、運べる重さが異なることがある。

しかし、いくつのロープを繋げれば各々のロープに掛かる重さを分けることができる。
ｋ個のロープを用いて重さのｗの物体を運ぶとき、各々のロープにはw/kくらいの重さがかかる。

各ロープの情報が与えられたとき、これたちを使って運べる物体の最大重量を求めよ。
但し、すべてのロープを使う必要はなく、任意でいくつか選び出して使ってもいい。
"""

n = int(input())
rope = []

for _ in range(n):
    rope.append(int(input()))

rope.sort(reverse = True)

ans = 0
kosu = 1

for i in range(n):
    weight = kosu * rope[i]
    
    if weight >= ans:
        ans = weight
    
    kosu += 1
    
print(ans)

"""
ロープをソートしていちいち確認しながら最大重量を更新するようにした。
なんか愚かな方法みたいだが、二重For文も使わないから問題はなさそう。
"""
