#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


def quickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    return quickSort([x for x in array[1:] if x < pivot]) + [pivot] + quickSort([x for x in array[1:] if x >= pivot])

def quick_Sort(array, left, right):
    if left >= right:
        return array
    pivot = array[left]
    low = left
    high = right
    while left < right:
        while left < right and array[right] >= pivot:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= pivot:
            left += 1
        array[right] = array[left]
    array[right] = pivot
    quick_Sort(array, low, left-1)
    quick_Sort(array, left+1, high)



if __name__ == '__main__':
    array = [13, 7, 19, 8, 4, 10, 2, 20, 21, 11]
    #newarray = quickSort(array)
    quick_Sort(array,0,len(array)-1)
    print(array)