"""算法
1. 计算整个列表的和作为 sum_right=sum(nums)，sum_left=0, mid=0
2. 从第一个数开始循环，sum_left+=mid, mid=sums[i], sum_right-=nums[i]
3. 如果 sum_left==sums_right，返回 i
时间复杂度O(n), 空间复杂度O(n)
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if i == 0:
                right_sum -= nums[i]
            else:
                left_sum += nums[i-1]
                right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1


if __name__ == '__main__':
    data_test1 = [1, 7, 3, 6, 5, 6]
    data_test2 = [1, 2, 3]
    data_test3 = [-1, -1, -1, 0, 1, 1]
    s = Solution()
    print(s.pivotIndex(data_test1))
    print(s.pivotIndex(data_test2))
