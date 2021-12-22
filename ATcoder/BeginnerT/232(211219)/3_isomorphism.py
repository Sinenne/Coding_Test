"""
Time Limit: 2 sec / Memory Limit: 1024 MB
Score : 300 points
Problem Statement
Takahashi and Aoki each have a toy made by attaching M cords to N balls.
In Takahashi's toy, the balls are numbered 1,…,N, and the i-th cord ties Ball Ai and Bi.
Similarly, in Aoki's toy, the balls are numbered 1,…,N, and the i-th cord ties Ball Ci and Di.
In each toy, no cord ties a ball to itself, and no two balls are tied by two or more different cords.
Snuke is wondering whether the two toys have the same shape.
Here, they are said to have the same shape when there is a sequence P that satisfies the conditions below.
•	P is a permutation of (1,…,N).
•	For every pair of integers i,j between 1 and N (inclusive), the following holds.
o	Balls i and j in Takahashi's toy are tied by a cord if and only if Balls Pi and Pj in Aoki's toy are tied by a cord.
If the two toys have the same shape, print Yes; otherwise, print No.


"""


from itertools import permutations

iso = False

taka_list = []
aoki_list = []

def make_matrx(dare):
  global taka_list, aoki_list
  global m, n
  mtrx = [[0] * n for i in range(n)]

  if m == 0:
    return False
  
  for i in range(m):
    a, b = map(int, input().split())
    mtrx[a-1][b-1] = 1
    mtrx[b-1][a-1] = 1
    if dare == 1:
      taka_list.append([a, b])
    elif dare == 2:
      aoki_list.append([a, b])

  return mtrx

def switch_matrx(kazu):
  global aoki_list
  global n
  key = dict()
  for i in range(1, n + 1):
    key[i] = kazu[i-1] + 1

  new_aoki_list = [[key[i[0]], key[i[1]]] for i in aoki_list]

  new_aoki_matrix = [[0] * n for i in range(n)]

  for i in new_aoki_list:
    new_aoki_matrix[i[0]-1][i[1]-1] = 1
    new_aoki_matrix[i[1]-1][i[0]-1] = 1

  return new_aoki_matrix

n, m = map(int, input().split())

Taka = make_matrx(1)
Aoki = make_matrx(2)

if Taka == False:
  iso = True
  print("Yes")
else:
  perms = list(permutations(list(range(n)) ,n))

  for i in perms:
    newone = switch_matrx(list(i))
    if newone == Taka:
      print("Yes")
      iso = True
      break


  if iso == False:
    print("No")
