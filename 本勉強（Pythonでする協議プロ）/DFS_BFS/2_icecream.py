"""
N*Mのサイズのアイスバックスがある。０は穴のある部分、１はパーティションのある部分を指す。
穴の部分が上下左右で隣接するなら結ばれてると想定する。
バックスの形が与えられると作られるアイスの数を数える。
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))
  
def DFS(x, y):
  # if out of range, then False
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  # if not yet visited
  if graph[x][y] = 0:
    graph[x][y] = 1
    DFS(x-1, y)
    DFS(x, y-1)
    DFS(x+1, y)
    DFS(x, y+1)
    return True
  return False


count = 0
for i in range(n):
  for j in range(m):
    if DFS(i, j) == True:
      result += 1
      
      
print(result)
