"""
とある数のNが１になるまで次の過程の中一つを繰り返しに選んで遂行しようとする。
ただし、二つ目はNがKの倍数であるだけ可能である。

１．Nから１を引く。
２．NをKで分ける。

Nが１になるまで第一や第二を選ぶ最少回数を求めよ。

NとKは、２から10万の間の範囲で決まる。
"""


# 自分の回答

n, k = map(int, input().split())

count = 0

while n != 1:
    if n%k != 0:
        n -= 1
        count += 1
    else:
        n = n/k
        count += 1
        
print(count)


# 本の回答

n, k = map(int, input().split())
result = 0

while m >= k:
  while n % k != 0:
    n -= 1
    result += 1
  n //= k
  result += 1
  
  
while n > 1:
  n -= 1
  result += 1
  
print(result)



# Nが100億以上の数である場合

n, k = map(int, input().split())
result = 0

while True:
  target = (n//k) * k
  result += (n - target)
  n = target
  
  if n < k:
    break
    
  result += 1
  n //= k 
  
  
result += (n-1)
print(result)


