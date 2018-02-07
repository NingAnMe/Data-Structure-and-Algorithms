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
    寻找一个字符串的最长回文
    :param s:
    :return:
    """
    pass


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


if __name__ == '__main__':
    s = ''
    print(is_palindrome(s))
    s = 'a'
    print(is_palindrome(s))
    s = 'ab'
    print(is_palindrome(s))
    s = 'bb'
    print(is_palindrome(s))
    s = 'aba'
    print(is_palindrome(s))
