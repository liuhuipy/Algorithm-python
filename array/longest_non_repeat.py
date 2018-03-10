# -*- coding:utf-8 -*-

# Given a string, find the length of the longest substring
# without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.


def longest_non_repeat(s):
    max_len, temp_str = 0, ''
    for i in s:
        if i in temp_str:
            ind = temp_str.index(i)
            temp_str = temp_str[ind+1:]
        temp_str += i
        max_len = max(max_len, len(temp_str))
    return max_len


if __name__ == '__main__':
    s1 = 'abcabcbb'
    s2 = 'bbbbb'
    s3 = 'pwwkew'
    print(longest_non_repeat(s1))
    print(longest_non_repeat(s2))
    print(longest_non_repeat(s3))

