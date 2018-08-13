#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/11 14:00
@Author  : AnNing
"""


class Solution(object):

    def rotate(self, nums, k):
        """
        对前半段列表和后半段列表分别进行对调反转
        然后将整个列表进行对调反转
        得到的结果和旋转数组一样
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length  # 循环的次数k超过列表长度，那么对K进行取余

        index_before = (0, length - k - 1)  # 前半段列表
        index_later = (length - k, length - 1)  # 后半段列表

        index_first, index_last = index_before
        while index_first < index_last:
            nums[index_first], nums[index_last] = nums[index_last], nums[index_first]
            index_first += 1
            index_last -= 1
        index_first, index_last = index_later
        while index_first < index_last:
            nums[index_first], nums[index_last] = nums[index_last], nums[index_first]
            index_first += 1
            index_last -= 1
        index_first, index_last = (0, length - 1)
        while index_first < index_last:
            nums[index_first], nums[index_last] = nums[index_last], nums[index_first]
            index_first += 1
            index_last -= 1
        return nums


if __name__ == '__main__':
    nums = [1]
    k = 1
    solution = Solution()
    print solution.rotate(nums, k)
