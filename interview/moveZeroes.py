#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/18 11:16
@Author  : AnNing
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = 0
        while i < length:
            if nums[i] == 0:
                self.move_number_to_last(i, nums)
                length -= 1
            else:
                i += 1

    def move_number_to_last(self, index, nums):
        index_last = len(nums) - 1
        while index < index_last:
            index_next = index + 1
            self.change_two_number(index, index_next, nums)
            index += 1

    def change_two_number(self, index1, index2, nums):
        nums[index1], nums[index2] = nums[index2], nums[index1]


if __name__ == '__main__':
    nums1_test = [1, 2, 2, 1]
    nums2_test = [2, 2]
    nums3_test = [1, 0, 1]
    nums4_test = []
    nums5_test = [0, 0, 1]
    s = Solution()
    print s.moveZeroes(nums2_test)
