"""
Nを入力すると、０時０分０秒からN時５９分５９秒までの時刻の中
一つでも３が入っている時刻の数を数えよ。

"""

N = int(input())

count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count += 1
                
print(count)



#本の答案も同じである。なんか変な気がするが本は見ずにやった。
