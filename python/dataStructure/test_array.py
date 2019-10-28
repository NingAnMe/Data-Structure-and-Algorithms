#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 14:40
# @Author  : AnNing
from .array import Array


def test_append():
    array = Array(5)
    array.append(1)
    assert array.data == [1, 0, 0, 0, 0]
    assert len(array) == 1


def test_remove():
    array = Array(5)
    array.append(1)
    array.append(2)
    assert len(array) == 2
    array.remove(0)
    assert array.data == [2, 0, 0, 0, 0]
    assert len(array) == 1


def test_insert():
    array = Array(5)
    array.append(1)
    array.append(2)
    assert len(array) == 2
    array.insert(3, 1)
    assert array.data == [1, 3, 2, 0, 0]
    assert len(array) == 3
