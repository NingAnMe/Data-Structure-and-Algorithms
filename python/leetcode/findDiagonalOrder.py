#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/15 17:19
@Author  : AnNing
"""
"""对角线遍历
给定一个含有 M x N 个元素的矩阵（M行，N列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出:  [1,2,4,7,5,3,6,8,9]
"""
"""算法
1.共循环 row.length + col.length - 1 次
2.循环次数i从0开始计
3.当循环次数是偶数时，使用row的坐标求col的坐标，从 min(row.max, i) 到 0
4.当循环次数是奇数是，使用col的坐标求row的坐标，从 min(col.max, i) 到 0
5.根据坐标，输出对应位置的值
"""


class Solution(object):
    # TODO 根据现在的算法重写程序
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_amount = len(matrix)
        if row_amount < 1:
            return []
        if row_amount == 1:
            return matrix[0]
        col_amount = len(matrix[0])
        if col_amount == 1:
            result = list()
            for row in matrix:
                result.append(row[0])
            return result

        localtions = list()
        now = (0, 0)
        localtions.append(now)
        for i in range(len(matrix[0]) + len(matrix)):
            if i < col_amount:
                if self.is_even(i):  # i 为偶数
                    # 先向右移动一格
                    next = self.add_vector_2(now, (0, 1))
                    if self.is_valid(next, row_amount, col_amount):
                        now = next
                        localtions.append(now)
                        # 如果向右成功，循环向左下移动
                        while self.is_valid(now, row_amount, col_amount):
                            next = self.add_vector_2(now, (1, -1))
                            if self.is_valid(next, row_amount, col_amount):
                                now = next
                                localtions.append(now)
                            else:
                                break
                else:  # i 为奇数
                    # 先向下移动一格
                    next = self.add_vector_2(now, (1, 0))
                    if self.is_valid(next, row_amount, col_amount):
                        now = next
                        localtions.append(now)
                        # 如果向下移动成功，循环向右上移动
                        while self.is_valid(now, row_amount, col_amount):
                            next = self.add_vector_2(now, (-1, 1))
                            if self.is_valid(next, row_amount, col_amount):
                                now = next
                                localtions.append(now)
                            else:
                                break
            else:  # 沿边界移动次数超过 col_amount
                # i 为偶数
                if self.is_even(i):
                    # 先向下移动一格
                    next = self.add_vector_2(now, (1, 0))
                    if self.is_valid(next, row_amount, col_amount):
                        now = next
                        localtions.append(now)
                        # 如果向右成功，循环向左下移动
                        while self.is_valid(now, row_amount, col_amount):
                            next = self.add_vector_2(now, (1, -1))
                            if self.is_valid(next, row_amount, col_amount):
                                now = next
                                localtions.append(now)
                            else:
                                break
                else:  # i 为奇数
                    # 先向右移动一格
                    next = self.add_vector_2(now, (0, 1))
                    if self.is_valid(next, row_amount, col_amount):
                        now = next
                        localtions.append(now)
                        # 如果向下移动成功，循环向右上移动
                        while self.is_valid(now, row_amount, col_amount):
                            next = self.add_vector_2(now, (-1, 1))
                            if self.is_valid(next, row_amount, col_amount):
                                now = next
                                localtions.append(now)
                            else:
                                break
        result = list()
        for local in localtions:
            result.append(matrix[local[0]][local[1]])
        return result

    def add_vector_2(self, vector1, vector2):
        return vector1[0] + vector2[0], vector1[1] + vector2[1]

    def is_valid(self, vector, m, n):
        """
        :param vector:
        :param m: 行
        :param n: 列
        :return:
        """
        if (0 <= vector[0] < m) and (0 <= vector[1] < n):
            return True
        else:
            return False

    def is_even(self, i):
        if i % 2 == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    test_data1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    test_data2 = [[7], [9], [6]]
    test_data3 = [[1, 2, 3, 4]]
    test_data4 = []
    s = Solution()
    print(s.findDiagonalOrder(test_data1))
    print(s.findDiagonalOrder(test_data2))
    print(s.findDiagonalOrder(test_data3))
    print(s.findDiagonalOrder(test_data4))
