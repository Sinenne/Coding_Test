"""
N*Mのサイズの迷路から出る。
動ける部分は１で印す。
最初の一は１，１で出口はN,Mとする。
出るため動く最少のスペースの数を数える。
"""

from collections import deque

n, m = map(int, input().split())

maze = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  maze.append(list(map(int, input())))
 

def bfs(x, y):
  queue= deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny <0 or nx >= n or ny >= m:
        continue
      if maze[nx][ny] == 0:
        continue
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))
      
  return maze[n-1][m-1]


print(bfs(0, 0))
