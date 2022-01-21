

"""
長さNの整数配列のAとBがある。次のように関数Sを定義する。
S = A[0] × B[0] + ... + A[N-1] × B[N-1]
Sの値を一番小さくするためAの数を再配列する。但し、Bの数は再配列しない。
Sの最小値を出力しろ。
"""


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

ans = [a[i] * b[i] for i in range(n)]
print(sum(ans))
