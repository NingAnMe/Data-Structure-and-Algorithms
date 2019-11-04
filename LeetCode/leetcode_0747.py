class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_index = -1
        second_max_value = -1
        for i in range(len(nums)):
            if i == 0:
                max_index = i
                continue
            value = nums[i]
            if value > nums[max_index]:
                value = nums[max_index]
                max_index = i
            if value > second_max_value:
                second_max_value = value
        if nums[max_index] >= (second_max_value * 2):
            return max_index
        else:
            return -1


if __name__ == '__main__':
    test_data1 = [3, 6, 1, 0]
    test_data2 = [1, 2, 3, 4]
    test_data3 = [2, 1]
    test_data4 = [1, 2]
    s = Solution()
    print(s.dominantIndex(test_data1))
    print(s.dominantIndex(test_data2))
    print(s.dominantIndex(test_data3))
    print(s.dominantIndex(test_data4))
