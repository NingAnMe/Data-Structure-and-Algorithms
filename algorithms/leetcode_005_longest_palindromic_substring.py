# coding:utf-8
"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.


Example:

Input: "cbbd"

Output: "bb"
"""

def longest_palindrome(s):
    """

    :param s:
    :return:
    """


def is_palindrome(s):
    """
    判断是否是回文
    :param s:
    :return:
    """
    length = len(s)
    if length <= 1:
        return False
    n = length / 2
    for i in xrange(0, n):
        start = i
        end = (i + 1) * (-1)
        if s[start] == s[end]:
            continue
        else:
            return False
    return True
