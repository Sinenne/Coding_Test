
def separate(s, num):
    return [s[i:i+num] for i in range(0, len(s), num)]

def shrink(s_list):
    res = []
    i = 0
    while i < len(s_list):
        cnt = 1
        moji = s_list[i]

        while i < len(s_list)-1 and s_list[i] == s_list[i+1]:
            cnt += 1
            i += 1

        if cnt != 1:
            res.append(str(cnt) + moji)
        else:
            res.append(moji)

        i += 1

    return ''.join(res)


def solution(s):
    answer = 0
    candi = [len(shrink(separate(s, i))) for i in range(1, len(s)+1)]

    answer = min(candi)    

    return answer
  
  
  #other
  
  def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
