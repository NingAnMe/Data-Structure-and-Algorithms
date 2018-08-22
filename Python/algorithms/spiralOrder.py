#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/22 17:10
@Author  : AnNing
"""
"""螺旋矩阵
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

"""算法
分为四步，按顺序计算所有数值在矩阵中对应的坐标对（row，col）
1. row = row_min + i, col = [col for col in (col_min+i, col_max-i, 1)]
2. col = col_max - i, row = [row for row in (row_min+i, row_max-i, 1)]
3. row = row_max - i, col = [col for col in (col_max-i, col_min+i, -1)]
4. col = col_min + i, row = [row for row in (row_max-i, row_min+i+1, -1)]
按顺序输出所有(row, col)对应的数值
"""