#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/22 10:07
@Author  : AnNing
"""


class Array:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [0 for _ in range(self.capacity)]
        self.count = 0

    def append(self, value):
        if self.count == self.capacity:
            raise MemoryError
        self.data[self.count] = value
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise IOError
        self.count -= 1
        temp = self.data[self.count]
        self.data[self.count] = 0
        return temp

    def insert(self, value, index):
        if index >= self.capacity or index < 0:
            raise IndexError
        if self.count == self.capacity:
            raise MemoryError
        i = self.count - 1
        while i >= index:
            self.data[i + 1] = self.data[i]
            i -= 1
        self.data[index] = value
        self.count += 1

    def remove(self, index):
        if index >= self.capacity or index < 0:
            raise IndexError
        if self.count == 0:
            raise MemoryError
        i = index
        while i < self.count:
            self.data[i] = self.data[i + 1]
            i += 1
        self.count -= 1

    def __len__(self):
        return self.count

    def __str__(self):
        return '[' + ', '.join(map(str, self.data[:self.count])) + ']'


if __name__ == '__main__':
    array = Array()
    array.append(1)
    print(array)
    print(len(array))
    array.insert(2, 0)
    print(array)
    print(len(array))
    array.pop()
    print(array)
    print(len(array))
    array.append(5)
    print(array)
    print(len(array))
    array.remove(0)
    print(array)
    print(len(array))
