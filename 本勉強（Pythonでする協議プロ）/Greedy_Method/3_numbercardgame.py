"""
次のルールに従ってゲームを行わせる。

１．数字の書いてるカードがN*Mの形で乗せられている。Nは行の数で、Mは列の数である。
２．先に選ぼうとするカードの含まれている行を選択する。
３．その次に選ばれた行に含まれたカードの中、一番低いカードを引く。
４．つまり、最初に行を選ぶとき以降に該当行で一番低いカードをひくことを考慮して
    最終的に一番高いカードを引けるように戦略を立てなければならない。
"""

#自分の答案
n, m = map(int, input().split())

numbers = []

for i in range(n):
    row = list(map(int, input().split()))
    numbers.append(min(row))
    
print(max(numbers))

＃本の答案
n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(result, min_value)
  
print(result)


# min関数を使わない場合
n, m = map(int, input().split())

result = 0 

for i in range(n):
  data = list(map(int, input().split()))
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
    
  result = max(result, min_value)
  
print(result)
