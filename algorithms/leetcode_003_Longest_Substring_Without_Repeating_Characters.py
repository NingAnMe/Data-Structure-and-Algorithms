# coding:utf-8

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def length_of_longest_substring(s):
    """
    更快速的办法是使用字典记录键值对
    :type s: str
    :rtype: int
    """
    lyst = []
    longest_length = 0
    length = 0

    for i in s:
        if i in lyst:
            lyst.append(i)
            idx = lyst.index(i) + 1
            lyst = lyst[idx:]
            length = len(lyst)
        else:
            lyst.append(i)
            length += 1
            if length > longest_length:
                longest_length = length
            else:
                continue
    return longest_length


if __name__ == '__main__':
    s = 'abcabcbb'
    print length_of_longest_substring(s)

    s = 'bbbbb'
    print length_of_longest_substring(s)

    s = 'pwwkew'
    print length_of_longest_substring(s)

    s = 'p'
    print length_of_longest_substring(s)

    s = ''
    print length_of_longest_substring(s)

    s = "bpfbhmipx"
    print length_of_longest_substring(s)