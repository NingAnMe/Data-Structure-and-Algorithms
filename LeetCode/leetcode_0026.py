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
        for i in range(len(nums)):
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
    print("-" * 100)
    print(s.removeDuplicates(lyst1))
    print("-" * 100)
    print(s.removeDuplicates(lyst2))
    print("-" * 100)
    print(s.removeDuplicates(lyst3))
    print("-" * 100)
    print(s.removeDuplicates(lyst4))
