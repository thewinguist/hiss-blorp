import random
nums = [3,2,1,4]
# no_extremes = [i for i in nums if i not in (min(nums),max(nums))]
# if bool(no_extremes) == False : answer = -1
# else : answer = random.choice(no_extremes)
# print(answer)

#lol, better:
if len(nums) < 3:
    print -1
nums.remove(min(nums))
nums.remove(max(nums))
print(random.choice(nums))