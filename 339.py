#https://leetcode.com/contest/weekly-contest-339/problems/find-the-longest-balanced-substring-of-a-binary-string/
s = "0100011100000001"

# def findTheLongestBalancedSubstring(s):
#     for i in range(len(s)):
#         if s[i] == '0' and s[i+1] == '1':
#             print('yo I found a cut')

def findTheLongestBalancedSubstring(s):
    zeros = 1
    ones = 1
    for i in range(0, len(s)):
        if s[i] == '0' and s[i+1] == '0':
            zeros += 1
        elif s[i] == '1' and s[i+1] == '1':
            ones += 1

findTheLongestBalancedSubstring(s)
