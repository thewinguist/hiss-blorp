#https://leetcode.com/contest/weekly-contest-356/problems/number-of-employees-who-met-the-target/
hours = [0,1,2,3,4]
target = 2
# hours = [5,1,4,2,2]
# target = 6

met_target = len([e for e in hours if e >= target])
print(met_target)