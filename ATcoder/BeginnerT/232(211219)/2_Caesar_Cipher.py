"""
Time Limit: 2 sec / Memory Limit: 1024 MB
Score : 200 points
Problem Statement
Takahashi has a string S consisting of lowercase English letters.
On this string, he will do the operation below just once.
•	First, choose a non-negative integer K.
•	Then, shift each character of S to the right by K (see below).
Here,
•	a shifted to the right by 1 is b;
•	b shifted to the right by 1 is c;
•	c shifted to the right by 1 is d;
•	y shifted to the right by 1 is z;
•	z shifted to the right by 1 is a.
For example, b shifted to the right by 4 is f, and y shifted to the right by 3 is b.
You are given a string T. Determine whether Takahashi can make S equal T by the operation above.
Constraints
•	Each of S and T is a string of length between 1 and 10^5 (inclusive) consisting of lowercase English letters.
•	The lengths of S and T are equal.
"""


def getk(S, T):  # Getting the value of K
  for i in range(len(S)):
    if ord(T[i]) > ord(S[i]):
      return ord(T[i]) - ord(S[i])
    else:
      return (122-ord(S[i])) + (ord(T[i]) - 96)


def transformer(S, k):   #Changing S according to the rule
  result = ''
  for i in range(len(S)):
    newone = ord(S[i]) + k
    if newone > 122:
      newone -= 26
    
    result += chr(newone)


  return result  


S = input()
T = input()

k = getk(S, T)
newstring = transformer(S, k)

if newstring == T:
  print("Yes")
else:
  print("No")
