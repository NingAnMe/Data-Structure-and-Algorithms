#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/12 16:15
@Author  : AnNing
"""


class Solution(object):
    """
    数字第一次出现，放入集合
    数字第二次出现，从集合中删除
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set()
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                temp.remove(i)
        return temp.pop()


class Solution1(object):
    def singleNumber(self, nums):
        """
        同一个数字异或会变为0
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    nums_test = [4, 1, 2, 1, 2]
    s = Solution1()
    print s.singleNumber(nums_test)
