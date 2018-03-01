# -*- coding:utf-8 -*-


def swap(alist, i, j):
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp

if __name__ == '__main__':
    alist = [1,3,5,7,9]
    swap(alist, 1, 3)
    print(alist)