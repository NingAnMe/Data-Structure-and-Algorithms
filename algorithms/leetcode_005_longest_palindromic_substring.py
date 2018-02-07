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


Example:

Input: "cb"

Output: "c"
"""


def longestPalindrome(s):
    """
    寻找一个字符串的最长回文
    :param s:
    :return:
    """
    n = len(s)
    if n == 0:
        return None
    if n == 1:
        return s
    elif isPalindrome(s):
        return s
    else:
        longest = 0
        longest_sub = None
        for i in xrange(0, n):
            sub_s = s[:-i]
            if isPalindrome(sub_s):
                length = len(sub_s)
                if length > longest:
                    longest = length
                    longest_sub = sub_s
                break
            else:
                sub_s = s[i:]
                if isPalindrome(sub_s):
                    length = len(sub_s)
                    if length > longest:
                        longest = length
                        longest_sub = sub_s
                    break

    if longest >= (n - 2):
        return longest_sub
    else:
        sub = s[1: -1]
        longest_s = longestPalindrome(sub)
        if longest_s is not None and len(longest_s) > longest:
            return longest_s
        else:
            return longest_sub


def isPalindrome(s):
    """
    判断是否是回文
    :param s:
    :return:
    """
    length = len(s)
    if length == 0:
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
    print(isPalindrome(s))
    s = 'a'
    print(isPalindrome(s))
    s = 'ab'
    print(isPalindrome(s))
    s = 'bb'
    print(isPalindrome(s))
    s = 'aba'
    print(isPalindrome(s))

    s = ''
    print(longestPalindrome(s))
    s = 'a'
    print(longestPalindrome(s))
    s = 'ab'
    print(longestPalindrome(s))
    s = 'bb'
    print(longestPalindrome(s))
    s = 'aba'
    print(longestPalindrome(s))
