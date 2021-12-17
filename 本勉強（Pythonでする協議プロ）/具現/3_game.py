"""
ゲームのキャラクターが地図の中で動くシステムを開発する。
キャラのある場所は１＊１のサイズの正方形でできたN*Mのサイズの四角形で、
各々のスペースは陸地、または海である。キャラは東西南北のいずれかを見ている。
マップのスペースは（A,B）の座標で表せて、Aは北から離れた距離、Bは二死からの距離である。
キャラは上下左右で動けて、海には行けない。
キャラの動きのマニュアルは次のようになる。

１．現在から現在方向を基準にして左の方向（反時計回りに９０度）から行き場を決める。
２．すぐ左側に未だ行ってない場所があるなら左に回ってから左に一歩進む。左にそういうスペースがないなら回転だけして１段階に戻る。
３．四つの方向が全部言ってみたスペースだったり海のスペースである場合は、眺める方向を維持したまま後進して一段階に戻る。
    但し、後ろの方向が海であれば動けなくなり、止まる。
    
こういう過程の後訪れたスペースの数を数える。

"""


# n for nums of row, m for nums of cols
n, m = map(int, input().split())

# position (a, b) and direction
a, b, d = map(int, input().split())

# position of the places visited
vis = [[0] * m for _ in range(n)]
vis[a][b] = 1  # already visited(starting point)



chizu = []
for i in range(n):
  chizu.append(list(map(int, input().split())))

# definition of directions NESW
dx = [-1, 0, 1, 0]
dy = [0, 1, -1, 0]

# left rotation
def left_rotation():
  global d
  d -= 1
  if d == -1:
    d = 3

# simulation
count = 1
rotation_time = 0

while True:
  left_rotation()
  nx = a + dx[d]
  ny = b + dy[d]

  if vis[nx][ny] == 0 and chizu[nx][ny] == 0:
    vis[nx][ny] = 1
    a = nx
    b = ny
    count += 1
    rotation_time += 1
    continue

  else:
    rotation_time += 1

  if rotation_time == 4:
    nx = a - dx[d]
    ny = b - dy[d]

    if chizu[nx][ny] == 0:
      a = nx
      b = ny
    else:
      break
    
    rotation_time = 0



print(count)
