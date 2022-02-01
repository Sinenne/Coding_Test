"""
1789

お互い異なるN個の自然数の総合がSとする。
Sをすでに知っていると、Nの最大値は？
"""

s = int(input())

cnt = 0
sUm = 0
num = 1

while sUm < s:
    sUm += num
    num += 1
    cnt += 1
    
if sUm == s:
    print(cnt)
else:
    print(cnt - 1)
    
    
＃発想がしにくかった。１から足していってSを超えた瞬間に適当に調整したら済む問題だった。
