#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 10:32
# @Author  : NingAnMe <ninganme@qq.com>
from math import sqrt


def mean(list_):
    """
    计算平均值
    :param list_:
    :return:
    """
    sum_ = 0
    for data in list_:
        sum_ += data
    return sum_


def deviation_from_mean(list_):
    """
    计算离均差
    :param list_:
    :return:
    """
    mean_ = mean(list_)
    dfa = []
    for data in list_:
        dfa.append(data - mean_)
    return dfa


def absolute_deviation(list_):
    """
    计算绝对偏差
    :param list_:
    :return:
    """
    dfa = deviation_from_mean(list_)
    ad = []
    for data in dfa:
        if data >= 0:
            ad.append(data)
        else:
            data.append(data * -1)
    return ad


def mean_of_absolute_deviation(list_):
    """
    计算平均绝对偏差
    :param list_:
    :return:
    """
    ad = absolute_deviation(list_)
    sum_ = 0
    for data in ad:
        sum_ += data
    return sum_ / len(ad)


def square_deviation(list_):
    """
    计算平方偏差
    :param list_:
    :return:
    """
    sd = []
    for data in deviation_from_mean(list_):
        sd.append(data ** 2)
    return sd


def variance(list_):
    """
    计算方差
    :param list_:
    :return:
    """
    sum_ = 0
    for data in square_deviation(list_):
        sum_ += data
        return sum_ / len(list_)


def standard_deviation(list_):
    """
    计算标准差
    :param list_:
    :return:
    """
    return sqrt(variance(list_))
