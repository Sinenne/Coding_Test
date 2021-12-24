"""
Time Limit: 2 sec / Memory Limit: 1024 MB
Score : 400 points
Problem Statement
There is a H×W-square grid with H horizontal rows and W vertical columns. Let (i,j) denote the square at the i-th row from the top and j-th column from the left.
Each square is described by a character Ci,j, where Ci,j= . means (i,j) is an empty square, and Ci,j= # means (i,j) is a wall.
Takahashi is about to start walking in this grid. When he is on (i,j), he can go to (i,j+1) or (i+1,j). However, he cannot exit the grid or enter a wall square. He will stop when there is no more square to go to.
When starting on (1,1), at most how many squares can Takahashi visit before he stops?


"""

from collections import deque

h, w = map(int, input().split())

maze = []

for i in range(h):
  row = list(input())
  maze.append(row)

maze[0][0] = 1

dx = [0, 1]
dy = [1, 0]

def bfs(x, y):
  global maze
  biggest = 1
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= h or ny < 0 or ny >= w:
        continue
      if maze[nx][ny] == "#":
        continue
      queue.append((nx, ny))
      maze[nx][ny] = maze[x][y] + 1
      if maze[nx][ny] > biggest:
        biggest = maze[nx][ny]


  print(biggest)

bfs(0,0)

