#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/24 9:05
@Author  : AnNing
"""
"""存在重复
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""

"""算法
1. 循环每个值，如果这个值没有被记录，记录下来
2. 如果这个值已经被记录，返回 TRUE
3. 如果这个列表被循环到最后一个，没有出现被记录，返回 FALSE
使用集合set()实现，时间复杂度为O(n)，空间复杂度为O(n)
"""


class Solution(object):
    # TODO 实现算法
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pass
