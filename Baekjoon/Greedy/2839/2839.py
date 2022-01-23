"""
整数ｎが与えられると、それを５と３の線形数で表すとき
係数の総合の最小値を求めよ。出来ない場合は－１を出力。
"""

n = int(input())

ans = 0

if n < 5:
    if n%3 != 0:
        ans = -1
    else:
        ans = n//3
else:
    five = n//5   
    left = n% 5   
    
    while left%3 != 0:
        five -= 1   
        left += 5   
        if five == 0:
            break
    
    if left%3 != 0:
        ans = -1
    else:
        ans = five + left//3
    
print(ans)
