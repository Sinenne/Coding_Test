"""
旅行者のAはN*Nのサイズの正方四角形のうえに立っている。
この空間は１＊１のサイズの正方方でできていて、
左上の隅が（１，１）、右下の隅が（N,N）である。
この旅行者には計画書があって、空白を基準にL,R,U,Dのいずれかが反復的に書かれている。
この時AがN＊Nの四角形から離れようとする動きは無視される。
計画書が与えられたときAが最終的に到着する地点の座標を求めよ。
"""

#本人の答案
N = int(input())
plan = input().split()

x= 1
y = 1

for i in plan:
    if i == "R":
        x_move = 0
        y_move = 1
    elif i == "L":
        x_move = 0
        y_move = -1
    elif i == "D":
        x_move = 1
        y_move = 0
    elif i == "U":
        x_move = -1
        y_move = 0
    if x + x_move > N or x + x_move < 1 or y + y_move > N or y + y_move < 1:
        continue
        
    x += x_move
    y += y_move

print(x, y)

#本からの答案

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, -1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


for plan in plans:
  for i in ragne(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      
    if nx < 1 or ny < 1 or nx > n or ny > n:
      continue
    x , y = nx, ny
    
print(x, y)


