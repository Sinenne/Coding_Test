"""
10610

0以上の数のNが与えられると
そのNに含まれた数字を混ぜて30の倍数になる一番大きい数を探せ。
そういうのがなければー１を返す。
"""

n = input()


each_n = list(map(int, list(n)))


exist = True
ans = ''

while True:
    if 0 not in each_n:
        exist = False
        break
    else:
        each_n.remove(0)
        
        if sum(each_n) % 3 != 0:
            exist = False
            break
        else:
            each_n.sort(reverse = True)
            each_n = list(map(str, each_n))
            ans = ''.join(each_n) + "0"
            break
        
        
        
if exist == False:
    print(-1)
else:
    print(int(ans))
