# Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

给一个存有整数的列表，返回两个数字的索引，这两个数字相加等于一个特殊的目标值。

You may assume that each input would have exactly one solution, and you may not use the same element twice.

假设每一个输入都有一个确定的结果，并且每个数字都不能使用两次。

## Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

## 第一种

第一步，使用Hash结构，将所有整数和整数在列表中的位置映射到字典中，这一步的时间复杂度是O(n)。

第二步，循环整个列表，得到第一个加数，然后在字典中寻找是否存在另一个加数，如果存在，返回另一个加数的位置。这一步的时间复杂度是O(n)。

整个算法的时间复杂度是O(n)。

```python
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return None

        nums_dict = {}
        for p, i in enumerate(nums):
            nums_dict[i] = p

        for p1, i1 in enumerate(nums):
            x = target - i1
            p2 = nums_dict.get(x)
            if (p2 != None) and (p1 != p2):
                return [p1, p2]

        return None
```

## 第二种

循环整个列表，得到整数和整数的位置。然后判断字典中是否存在目标值和整数的差值。如果存在，返回差值的位置和整数的位置。如果不存在，将差值和整数的位置的映射添加到字典中。

整个算法的时间复杂度是O(n)。

```python
def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return None

        nums_dict = {}
        for i, num in enumerate(nums):
            if target-num in nums_dict:
                return nums_dict[target-num], i
            nums_dict[num] = i

        return None
```
