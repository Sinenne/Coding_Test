"""
色んな数でできている配列があるとき、与えられた数をM回足して一番大きい数を作る。
ただし、特定のIndexの数が連続でK回を超えて加えられることは出来ない。

お互い違うIndexに該当する数は数値上は同じでも別の数で扱う。

配列のサイズN、数が加えられる回数M、そしてKが与えらるとき結果を出力。
"""


#自分の回答
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

count = 0
sUm = 0

data.sort(reverse = True)

for i in range(m):
    if count == k:
        sUm += data[1]
        count = 0
    else:
        sUm += data[0]
        count += 1
        
print(sUm)


＃本の回答

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() 
first = data[n - 1] 
second = data[n - 2] 


count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first 
result += (m - count) * second 

print(result) 


＃時間を減らすため本が提案する第二の方法

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# Number of the biggest number added
count = int(m / (k + 1)) * k
count += m % (k + 1)
# Considering that m won't be dividable with k+1

result = 0
result += (count) * first
result += (m - count) * second

print(result)


