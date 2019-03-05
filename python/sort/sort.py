#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Sort:
    @classmethod
    def sort(cls, a: list):
        pass

    @classmethod
    def less(cls, v: object, w: object):
        return v < w

    @classmethod
    def exch(cls, a: list, i: int, j: int):
        a[i], a[j] = a[j], a[i]

    @classmethod
    def show(cls, a: list):
        print(a)

    @classmethod
    def is_sorted(cls, a: list):
        length = len(a)
        for i in range(1, length):
            if cls.less(a[i], a[i-1]):
                return False
        return True

