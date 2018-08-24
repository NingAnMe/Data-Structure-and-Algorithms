#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/18 11:16
@Author  : AnNing
"""
"""移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

"""算法
1. 记录与0值进行交换的位置的索引 index_last。从最后列表一个值开始判断，如果这个位置是0，index_last-1
2. 从第一个值开始循环，索引为 index_now，如果是 0，与 index_last 处的值进行交换，
   交换后重新寻找下一个 index_last
3. 如果 index_now >= index_last 循环结束
"""


class Solution(object):
    # TODO 根据现有算法重写程序
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
