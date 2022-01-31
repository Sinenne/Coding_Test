"""
10162
三つの時間調節用のボタンのABCの付いている電子レンジがある。
各々のボタンには一定な時間が指定されていてそれを押すと
その時間がどう割く時間に加えられる。
ABCに指定された時間は5分、1分、10秒である。

冷凍食品に調理時間のTが秒単位で票視されている。
ABCを適当に押してその総合が正確にT秒になるようにする。
この回数を最小にしろ。
"""

def main():
    t = int(input())
    
    button = [300, 60, 10]
    
    cnt = []
    
    for i in button:
        cnt.append(t//i)
        t %= i
        
    if t != 0:
        print(-1)
    else:
        print(cnt[0], cnt[1], cnt[2])
        
if __name__ == "__main__":
    main()
