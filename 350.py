main_tank = 5
additional_tank = 10
#https://leetcode.com/contest/weekly-contest-350/problems/total-distance-traveled/

burned = 0
#refuel_needed = (main_tank // 5 liters) * 1 liter
refuel_needed = (main_tank // 5)
if main_tank >= 5 and refuel_needed <= additional_tank:
    burned = main_tank + refuel_needed + 1
elif main_tank >= 5 and refuel_needed > additional_tank:
    burned = main_tank + additional_tank
else: burned = main_tank
print(burned)

# main = 9
# additional = 2

# 9 - 5 + 1 = 5
# 5 - 5 + 1 = 1
# total: 6 l -> 60 km

# 9 - 5 = 4
# 4 + 1 = 5
# 5 - 5 = 0
# 0 + 1 = 1
# totl: 10 -> 100 km