
"""
店にはおつりで５００，１００，５０，１０，５，１円玉が十分にあり、
いつもおつりを最小個数で上げる。
物を買い1000円を払うとお釣りの個数を求める。
"""

nedan = int(input())
change = 1000 - nedan

coin = [500, 100, 50, 10, 5, 1]

cnt = 0

for i in coin:
    cnt += change//i
    change %= i
    
    if change == 0:
        break
    
print(cnt)


"""
この問題、本で最小で見たやつ
"""
