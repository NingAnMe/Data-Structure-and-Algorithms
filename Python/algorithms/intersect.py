#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/17 16:36
@Author  : AnNing
"""
"""两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
"""

"""算法1
1. 循环数值少的列表的数，判断在第二个列表是否存在 O(m*n)
2. 如果存在，记录，并且从第二个列表删除这个数；
时间复杂度O(m*n)，空间复杂度O(max(m, n))
"""
"""算法2
1. 对两个列表进行排序，m*log(m), n*log(n)
2. 循环数值少的列表的每个数，判断是否在第二个列表存在，O(m*log(n))
时间复杂度O(n*log(n))，空间复杂度O(max(m, n))
"""
"""算法3
1. 对两个列表进行排序，m*log(m), n*log(n)
2. 同时对两个列表进行循环，m_now, n_now
3. 如果m_now<n_now,继续循环m,反之继续循环n, O(m+n)
时间复杂度O(n*log(n))
"""


class Solution(object):
    # 不改变输入的数组，使用列表循环
    # 时间复杂度为 N1*N2
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1 永远为长度较短的数组
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        result_index = set()
        result = list()
        for i in xrange(len(nums1)):
            value1 = nums1[i]
            for k in xrange(len(nums2)):
                value2 = nums2[k]
                if value1 == value2:
                    if k not in result_index:
                        result_index.add(k)
                        break
                    else:
                        continue
        for i in result_index:
            result.append(nums2[i])
        return result

    # 时间复杂度为 N1+N2
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        value_count1 = dict()
        value_count2 = dict()
        result = list()

        for value in nums1:
            count = value_count1.get(value, 0)
            value_count1[value] = count + 1
        for value in nums2:
            count = value_count2.get(value, 0)
            value_count2[value] = count + 1

        for value, count1 in value_count1.iteritems():
            if value in value_count2:
                count2 = value_count2.get(value, 0)
                if count1 <= count2:
                    count = count1
                else:
                    count = count2
                for i in xrange(count):
                    result.append(value)
        return result


if __name__ == '__main__':
    nums1_test = [1, 2, 2, 1]
    nums2_test = [2, 2]
    s = Solution()
    print s.intersect(nums1_test, nums2_test)

