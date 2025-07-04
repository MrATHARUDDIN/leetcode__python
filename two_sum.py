# Question :-Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example :

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].



def twoSum(nums, target):
    pair = {}
    for index, num in enumerate(nums):
        missing = target - num
        if missing in pair:
            print(f" Found: [{pair[missing]} , {index}] = {target}")
            return [pair[missing], index]
        pair[num] = index

        
nums = [3,2,4]
target = 6
twoSum(nums, target)
