#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/14 17:04
@Author  : AnNing
"""
"""寻找数组的中心索引
给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。

我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

示例 1:

输入: 
nums = [1, 7, 3, 6, 5, 6]
输出: 3
解释: 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
示例 2:

输入: 
nums = [1, 2, 3]
输出: -1
解释: 
数组中不存在满足此条件的中心索引。
说明:

输入: 
nums = [-1, -1, -1, 0, 1, 1]
输出: 0


nums 的长度范围为 [0, 10000]。
任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。
"""
"""算法
1. 计算整个列表的和作为 sum_right=sum(nums)，sum_left=0, mid=0
2. 从第一个数开始循环，sum_left+=mid, mid=sums[i], sum_right-=nums[i]
3. 如果 sum_left==sums_right，返回 i
时间复杂度O(n), 空间复杂度O(n)
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if i == 0:
                right_sum -= nums[i]
            else:
                left_sum += nums[i-1]
                right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1


if __name__ == '__main__':
    data_test1 = [1, 7, 3, 6, 5, 6]
    data_test2 = [1, 2, 3]
    data_test3 = [-1, -1, -1, 0, 1, 1]
    s = Solution()
    print(s.pivotIndex(data_test1))
    print(s.pivotIndex(data_test2))
