"""
一つの会議室があり、
これを使おうとするN個の会議についてスケジュール表を作る。
各々の会議のIに付いて開始時間と閉幕時間が与えられ、
会議が重ならないように会議室を使える会議の最大数を求める。
但し、会議は始まると途中中止は出来ず、一つの会議の終わりと同時に次の会議が始まることができる。
開始時間と閉幕時間が同じくなる場合がある。この場合、始まってからすぐ終わることに考えたらいい。
"""

n = int(input())

kaigi = []
start = []
end   = []


for _ in range(n):
    kaigi.append(list(map(int, input().split())))

kaigi = sorted(kaigi, key = lambda x : (x[1], x[0]))

for i in range(n):
    start.append(kaigi[i][0])
    end.append(kaigi[i][1])
    
dot = end[0]
cnt = 1

for i in range(1, n):
    if start[i] >= dot:
        cnt += 1
        dot = end[i]
        
print(cnt)



"""
最初はソート条件を会議が行われる時間として考えたがそうすると
配置にO＾２の時間がかかる。
その代わりに”終わる時間”を条件で整列すると
会議時間の話も入っていて、二重For文を使わずに済んだ。
早めにこの発想にたどり着かなかった。
会議時間にはまりすぎて別の方法を考えるのが鈍かった。
注意しなければならないと思う。
"""
