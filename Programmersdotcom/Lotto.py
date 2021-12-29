def solution(lottos, win_nums):
    maxrank = 7
    minrank = 7
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            maxrank-=1
            minrank-=1
        elif lottos[i] == 0:
            maxrank-=1
    answer = []
    if maxrank == 7:
        maxrank-=1
    if minrank == 7:
        minrank-=1
    answer.append(maxrank)
    answer.append(minrank)
    return answer
  
  #Others
  def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
  
  
  def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
