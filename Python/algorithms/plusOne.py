#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/17 17:11
@Author  : AnNing
"""
"""加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""
"""算法
1. 将数组转为数字
2. 将数字加1
3. 将数字转为数组
时间复杂度O(n)，空间复杂度O(n)
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        integer = self.list2int(digits) + 1
        result = self.int2list(integer)
        return result

    @staticmethod
    def list2int(nums):
        length = len(nums)
        value = 0
        for i in xrange(length):
            k = i + 1
            value = value + 10 ** i * nums[-k]
        return value

    @staticmethod
    def int2list(number):
        result = list()
        while number > 0:
            n = number % 10
            number = number / 10
            result.append(n)
        result.reverse()
        return result


if __name__ == '__main__':
    nums1_test = [1, 2, 2, 1]
    nums2_test = [2, 2]
    nums2_test = [0]
    s = Solution()
    print s.plusOne(nums2_test)
