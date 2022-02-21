import random
import time
from decimal import Decimal

"""
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
示例：
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
"""

def a(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == nums[mid ^ 1]:
            low = mid + 1
        else:
            high = mid
    return nums[low]



"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

输入：nums = [3,2,4], target = 6
输出：[1,2]

输入：nums = [3,3], target = 6
输出：[0,1]
"""


def test(target, nums):
    res = []
    a = -1
    for i in nums:
        a += 1
        if target - i == i and nums.count(target - i) == 1:
            continue
        if target - i in nums:
            res.append(a)
    return res


"""
微信发红包！
"""


def random_pac(total_money, total_person):
    pac = []
    total = total_money
    add = 0
    for i in range(total_person-1):
        person = round(random.uniform(0.01, total-0.01*(total_person-i)), 2)
        add += person
        total -= person
        pac.append(person)
    pac.append(round(total_money-add, 2))
    return pac


lis = []
user = input(int(time.time()))
lis.append(user)



