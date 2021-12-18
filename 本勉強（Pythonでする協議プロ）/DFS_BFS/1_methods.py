# DFS/BFS

# Adjacency Matrix
INF = 999999

graph = [
  [0, 7, 5],
  [7, 0 , INF],
  [5, INF, 0]
]


# Adjacency List
graph = [[] for _ in range(3)]

# Node Info for node No.0(node, dist)
graph[0].append((1,7))
graph[0].append((2,5))

# Node Info for node No.1
graph[1].append((0,7))

# Node Info for node No.2
graph[2].append((0,5))




# DFS Method (O(N))
# (Stack Oriented)

def dfs(graph, v, visited):
  # current node visited
  visited[v] = True
  print(v, end = ' ')
  
  # recursively visit connected nodes
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False * 9]

dfs(graph, 1, visited)


# BFS Method (O(N), generally better than DFS)
# Queue Oriented

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  
  # current node visited
  visited[start] = True

  # Until the queue is emptied
  while queue:
    v = queue.popleft()
    print(v, end = ' ')

    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

bfs(graph, 1, visited)
