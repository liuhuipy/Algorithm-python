# -*- coding:utf-8 -*-

"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.
function flatten(input){
}
Example:
Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

def list_flatten(alist, res=None):
    if res is None:
        res = []
    for lis in alist:
        if isinstance(lis, (list, tuple)):
            res = list_flatten(lis, res)
        else:
            res.append(lis)
    return res


if __name__ == '__main__':
    alist = [2, 1, [3, [4, 5], 6], 7, [8]]
    print(list_flatten(alist))