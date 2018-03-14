# -*- coding:utf-8 -*-

def binarysearch(target, sortedlist):
    left = 0
    right = len(sortedlist) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == sortedlist[mid]:
            return mid
        elif target < sortedlist[mid]:
            right = mid - 1
        else:
            left = mid + 1

if __name__ == '__main__':
    sortedlist = [1,2,3,4,5,6,7,8,9,10,11]
    index = binarysearch(3, sortedlist)
    print(index, sortedlist[index])