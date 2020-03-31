#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'liuhui'


class SeqList:

    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.num = 0
        self.data = [None] * self.maxsize

    # 判断表是否为空
    def is_empty(self):
        return self.num is 0

    # 判断表是否已满
    def is_full(self):
        return self.num is self.maxsize

    # 获取表元素个数
    def count(self):
        return self.num

    # 清除表
    def clear(self):
        self.__init__()

    # 获取某个位置的元素
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError
        if 0 <= key < self.num:
            return self.data[key]
        else:
            # 超出索引范围引发索引错误
            raise IndexError

    # 在表尾添加一个元素
    def append(self, value):
        if self.is_full():
            print('list is full')
            return
        else:
            self.data[self.num] = value
            self.num += 1

    # 在表中任意位置插入元素
    def insert(self, key, value):
        if not isinstance(key, int):
            raise TypeError
        if self.is_full():
            print('list is full')
            return
        if key < 0 or key >= self.maxsize:
            raise IndexError
        else:
            for i in range(self.num, key, -1):
                self.data[i] = self.data[i-1]
            self.data[key] = value
            self.num += 1

    # 查找表中元素的索引位置
    def index(self, value):
        for i in range(self.num):
            if self.data[i] == value:
                return i
        raise ValueError('{} is not find in the list'.format(value))

    # 将表反转
    def reverse(self):
        i,j = 0, self.num-1
        while i < j:
            self.data[i], self.data[j] = self.data[j], self.data[i]
            i,j = i+1, j-1


if __name__ == "__main__":
    # 初始化长度为10的表
    seql = SeqList(10)
    # 开始表为空
    print(seql.data)
    print(seql.is_empty())
    # 向表中添加7个元素
    seql.append(1)
    seql.append(4)
    seql.append(3)
    seql.append(7)
    seql.append(8)
    seql.append(5)
    seql.append(2)
    print(seql.data)
    print(seql.num)
    # 获取元素为3的位置
    print(seql.__getitem__(3))
    # 在表中索引3的位置插入元素6
    seql.insert(3,6)
    print(seql.data)
    print(seql.index(8))
    # 将表反转，再输出表
    seql.reverse()
    print(seql.data)






