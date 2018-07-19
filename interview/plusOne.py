#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/17 17:11
@Author  : AnNing
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
