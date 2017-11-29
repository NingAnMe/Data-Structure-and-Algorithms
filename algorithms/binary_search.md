# Binary Search

二分法查找：给一个排好序的存有数字的列表，和一个值，判断这个值是否存在于列表中。

## 例子

给一个列表 number_list = [2, 3, 5, 9, 12, 15] 和一个数字 target = 12，返回True。

如果给target = 10，返回False。

## 算法
```Python
def binary_search(number_list, target):
    if len(number_list) < 0:
        return False

    left = 0
    right = len(number_list) - 1
    while left <= right:
        middle = (left + right) // 2
        guess = number_list[middle]

        if guess == target:
            return True
        elif guess < target:
            left = middle + 1
        else:
            right = middle - 1
```
