#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/17 16:36
@Author  : AnNing
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

