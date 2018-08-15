#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 15:55
@Author  : AnNing
"""
"""
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。

示例 1:

输入: nums = [3, 6, 1, 0]
输出: 1
解释: 6是最大的整数, 对于数组中的其他整数,
6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
 

示例 2:

输入: nums = [1, 2, 3, 4]
输出: -1
解释: 4没有超过3的两倍大, 所以我们返回 -1.
 

提示:

nums 的长度范围在[1, 50].
每个 nums[i] 的整数范围在 [0, 99].
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = -1
        second_max_value = -1
        for i in xrange(len(nums)):
            if i == 0:
                max_index = i
                continue
            value = nums[i]
            if value > nums[max_index]:
                value = nums[max_index]
                max_index = i
            if value > second_max_value:
                second_max_value = value
        if nums[max_index] >= (second_max_value * 2):
            return max_index
        else:
            return -1


if __name__ == '__main__':
    test_data1 = [3, 6, 1, 0]
    test_data2 = [1, 2, 3, 4]
    test_data3 = [2, 1]
    test_data4 = [1, 2]
    s = Solution()
    print s.dominantIndex(test_data1)
    print s.dominantIndex(test_data2)
    print s.dominantIndex(test_data3)
    print s.dominantIndex(test_data4)
