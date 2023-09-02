#https://leetcode.com/contest/weekly-contest-360/problems/furthest-point-from-origin/

moves = "L_RL__R"
pos = 0
_ = 0

for m in moves:
    if m == 'L': pos -= 1
    elif m == 'R': pos += 1
    else: _ += 1

a = abs(pos + _)
b = abs(pos - _)

print (max(a,b))