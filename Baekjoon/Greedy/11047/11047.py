

"""
N種類をコインを持って、各々を多量で持つとする。
コインを適切に使い、その値の総合をKにしようとする。この時必要なコインの個数の最小値を求めよ。
"""

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse = True)
numco = 0

for i in coins:
    if i > k:
        continue
    
    numco += k//i
    k %= i
    
print(numco)
