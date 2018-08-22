#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/13 11:56
@Author  : AnNing
"""

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in xrange(len(nums)):
            x = nums[i]
            if x in d:
                return [d[x], i]
            else:
                y = target - x
                d[y] = i


if __name__ == '__main__':
    nums1_test = [1, 2, 2, 1]
    nums2_test = [2, 2]
    s = Solution()
    print s.twoSum(nums2_test, 3)
