"""
Time Limit: 2 sec / Memory Limit: 1024 MB
Score : 100 points

You are given a 3-character string S, 
which is a concatenation of integers a and b between 1 and 9 (inclusive) and the character x in this order: axb.
Find the product of a and b.
Constraints
•	The length of S is 3.
•	The 1-st and 3-rd characters are digits between 1 and 9 (inclusive).
•	The 2-nd character is x.
"""

S = input()
print(int(S[0]) * int(S[2]))
