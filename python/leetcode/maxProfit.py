#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/6/15 9:36
@Author  : AnNing
"""
"""买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
"""算法
1. 计算相邻两个值的大小，如果后一个值大于前一个值，计算其差值
2. 对所有差值进行相加
3. 输出结果
"""


class Solution(object):
    # TODO 使用新的算法实现
    def maxProfit(self, prices):
        """
        设置两个值，lastValue, currentValue
        当currentValue小于等于上个值，使用当前值替换上一个值
        当currentValue大于上个值，计算利润,使用当前值替换上一个值
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        lenPrice = len(prices)
        allProfit = 0
        profits = []
        lastValue = prices[0]
        currentValue = prices[0]

        for i in range(lenPrice):
            currentValue = prices[i]
            if currentValue > lastValue:
                profits.append(currentValue - lastValue)
            lastValue = currentValue

        allProfit = sum(profits)
        return allProfit


if __name__ == "__main__":
    lyst1 = [7,1,5,3,6,4]
    lyst2 = [1,2,3,4,5]
    lyst3 = [7,6,4,3,1]
    s = Solution()
    print(s.maxProfit(lyst1))
    print(s.maxProfit(lyst2))
    print(s.maxProfit(lyst3))
