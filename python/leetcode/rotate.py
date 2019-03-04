#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/11 14:00
@Author  : AnNing
"""
"""旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的原地算法。
"""

"""算法
1. 将k位置左边的数字进行反顺序操作
2. 将k位置和k位置右边的数字进行反顺序操作
3. 将整个数组进行反顺序操作
空间复杂度为O(1), 时间复杂度为O(n)
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
