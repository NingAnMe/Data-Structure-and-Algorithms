# coding:utf-8
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

if not in −2,147,483,648 to 2,147,483,647, return 0
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1

        lyst = []

        x = abs(x)
        while x > 0:
            d = x % 10
            lyst.append(d)
            x //= 10

        res = 0
        for i in lyst:
            res *= 10
            res += i

        if res > 0x7FffFFff:
            return 0
        else:
            return res * sign

    def reverse_best(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        sign = 1
        num = []

        if x < 0:
            sign = -1
        if x == 0:
            return 0
        x = abs(x)

        while x:
            num.append(x % 10)
            x //= 10

        for i in num:
            res *= 10
            res += i

        if res > 0x7FffFFff:
            return 0
        else:
            return res * sign


if __name__ == '__main__':
    import time

    solution = Solution()

    start = time.clock()

    i = 0
    print(solution.reverse(i))

    i = 1
    print(solution.reverse(i))

    i = 9999999999999
    print(solution.reverse(i))

    i = 3743848
    print(solution.reverse(i))

    i = -3743848
    print(solution.reverse(i))

    end = time.clock()

    print(end - start)

    # best

    start = time.clock()

    i = 0
    print(solution.reverse_best(i))

    i = 1
    print(solution.reverse_best(i))

    i = 9999999999999
    print(solution.reverse_best(i))

    i = 3743848
    print(solution.reverse_best(i))

    i = -3743848
    print(solution.reverse_best(i))

    end = time.clock()

    print(end - start)
