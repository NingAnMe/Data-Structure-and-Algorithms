#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/12 16:15
@Author  : AnNing
"""
"""只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""
"""算法1
1. 循环整个列表，如果数字没有在集合中，放入集合
2. 如果已经出现过，从集合中删除
3. 循环完整个列表以后，集合中留下来的值，只出现过一次
时间复杂度 O(n),空间复杂度O(n)
"""
"""算法2
1. 两个相同的值做异或运算，值为0
2. 多个值做异或运算，如果两两相同，值为0，与运算顺序无关
3. 对整个列表的每个值进行异或运算，最后的值为只出现过一次的数字的值
时间复杂度O(n)，空间复杂度O(1)
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
    print(s.singleNumber(nums_test))
