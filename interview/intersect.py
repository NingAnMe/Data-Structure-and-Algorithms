#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/7/17 16:36
@Author  : AnNing
"""


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1 永远为长度较短的数组
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        print nums1, nums2
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


if __name__ == '__main__':
    nums1_test = [1, 1]
    nums2_test = [1]
    s = Solution()
    print s.intersect(nums1_test, nums2_test)

