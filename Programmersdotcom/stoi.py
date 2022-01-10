def solution(s):
    code = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

    answer = ""
    word = ""

    for i in s:
        if i.isdecimal():
            answer += i
        else:
            word += i
            if word in code.keys():
                answer += str(code[word])
                word = ''
            else:
                continue


    return int(answer)
  
  
  
  
  ##
  
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
