#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/14 16:21
@Author  : AnNing
"""
"""删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

"""算法
1. 记录需要被修改的位置的索引 index_modify，初始值为 0
2. 记录当前移动到的位置的索引 index_now，初始值为 0
3. 记录当前的最大值 num_max，初始值为 -1（nums 的取值范围 > 0)
4. 从第一个数字开始循环处理，
   当 num_now 大于 num_max 的时候，修改 index_modify 处的数字为 num_now, index_modify + 1
5. 新数组的长度等于循环结束时 index_modify 的值

"""

class Solution(object):
    # TODO 根据现在的算法进行重写
    def removeDuplicates(self, nums):
        """
        一个变量，记录非重复数字的数量，即最后的字符集长度
        一个变量，记录当前最大的数字
        如果遇到新的数字，字符集长度加 1
        最大的数字变更为新的数字
        :type nums: List[int]
        :rtype: int
        """
        numsLen = 0
        numsTem = None
        for i in xrange(len(nums)):
            if i == 0:
                numsTem = nums[i]
                numsLen += 1
            elif nums[i] == numsTem:
                continue
            else:
                nums[numsLen] = nums[i]
                numsTem = nums[i]
                numsLen += 1
        return numsLen


if __name__ == "__main__":
    lyst1 = []
    lyst2 = [1]
    lyst3 = [1,1,2]
    lyst4 = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    print "-" * 100
    print s.removeDuplicates(lyst1)
    print "-" * 100
    print s.removeDuplicates(lyst2)
    print "-" * 100
    print s.removeDuplicates(lyst3)
    print "-" * 100
    print s.removeDuplicates(lyst4)
