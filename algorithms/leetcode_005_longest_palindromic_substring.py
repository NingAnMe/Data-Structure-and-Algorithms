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


def longest_palindrome(s):
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
    elif is_palindrome(s):
        return s
    else:
        longest = 0
        longest_sub = None
        for i in xrange(0, n):
            sub_s = s[:-i]
            if not is_palindrome(sub_s):
                continue
            else:
                length = len(sub_s)
                if length > longest:
                    longest = length
                    longest_sub = sub_s
                break
        for i in xrange(0, n):
            sub_s = s[i:]
            if not is_palindrome(sub_s):
                continue
            else:
                length = len(sub_s)
                if length > longest:
                    longest = length
                    longest_sub = sub_s
                break
        if longest >= (n - 2):
            return longest_sub
        else:
            sub = s[1: -1]
            longest_s = longest_palindrome(sub)
            if longest_s is not None and len(longest_s) > longest:
                return longest_s
            else:
                return longest_sub


def is_palindrome(s):
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
    print(is_palindrome(s))
    s = 'a'
    print(is_palindrome(s))
    s = 'ab'
    print(is_palindrome(s))
    s = 'bb'
    print(is_palindrome(s))
    s = 'aba'
    print(is_palindrome(s))

    s = ''
    print(longest_palindrome(s))
    s = 'a'
    print(longest_palindrome(s))
    s = 'ab'
    print(longest_palindrome(s))
    s = 'bb'
    print(longest_palindrome(s))
    s = 'aba'
    print(longest_palindrome(s))
