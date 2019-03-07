#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Sort:
    """
    排序模板
    """

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

    @classmethod
    def main(cls, a: list):
        cls.sort(a)
        assert cls.is_sorted(a)
        cls.show(a)


class Selection(Sort):
    """
    选择排序
    """

    @classmethod
    def sort(cls, a: list):
        length = len(a)
        for i in range(0, length-1):
            i_min = i
            for j in range(i+1, length):
                if cls.less(a[j], a[i_min]):
                    i_min = j
            cls.exch(a, i, i_min)


class Insertion(Sort):
    @classmethod
    def sort(cls, a: list):
        length = len(a)
        for i in range(1, length):
            print('i', i, a)
            j_min = i - 1
            for j in range(i, 0, -1):
                print('j', j, a[j], a[j_min])
                if cls.less(a[j], a[j_min]):

                    cls.exch(a, j, j_min)
                    j_min = j - 2
                else:
                    break
                print('j', j, a)


class Bubble(Sort):
    @classmethod
    def sort(cls, a: list):
        pass


if __name__ == '__main__':
    values = [1, 4, 2, 7, 5, 3, 5, 6]
    values1 = []
    S = Insertion
    S.main(values)
    S.main(values1)
