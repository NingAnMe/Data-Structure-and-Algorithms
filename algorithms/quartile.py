#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 10:02
# @Author  : NingAnMe <ninganme@qq.com>


def quartile(list_, num):
    """
    计算四分位Q1、Q2、Q3
    :param list_:
    :param num:
    :return:
    """
    location = num * (len(list_) + 1) / 4
    if int(location) < location:
        location_int = int(location)
        quartile_ = list_[location_int-1] * (
                location_int + 1 - location) + list_[location_int+1] * (location - location_int)
        return quartile_


def iqr(list_):
    """
    计算IQR
    :param list_:
    :return:
    """
    return quartile(list_, 3) - quartile(list_, 1)


def median(list_):
    """
    计算中位数
    :param list_:
    :return:
    """
    return quartile(list_, 2)


def inner_outlier(list_):
    """
    计算内限
    :param list_:
    :return:
    """
    inner_outlier_low = quartile(list_, 1) - 1.5 * iqr(list_)
    inner_outlier_high = quartile(list_, 3) + 1.5 * iqr(list_)
    return inner_outlier_low, inner_outlier_high


def outer_outlier(list_):
    """
    计算外限
    :param list_:
    :return:
    """
    outer_outlier_low = quartile(list_, 1) - 3 * iqr(list_)
    outer_outlier_high = quartile(list_, 3) + 3 * iqr(list_)
    return outer_outlier_low, outer_outlier_high


def mild_outlier(list_):
    """
    查找温和异常值，返回索引
    :param list_:
    :return:
    """
    inner_outlier_low, inner_outlier_high = inner_outlier(list_)
    outer_outlier_low, outer_outlier_high = outer_outlier(list_)
    list_mild_outlier = []
    for i, data in enumerate(list_):
        if outer_outlier_low < data < inner_outlier_low or inner_outlier_high < data < outer_outlier_high:
            list_mild_outlier.append(i)
    return list_mild_outlier


def extreme_outlier(list_):
    """
    查找计算异常值，返回索引
    :param list_:
    :return:
    """
    outer_outlier_low, outer_outlier_high = outer_outlier(list_)
    list_extreme_outlier = []
    for i, data in enumerate(list_):
        if data < outer_outlier_low or outer_outlier_high < data:
            list_extreme_outlier.append(i)
    return list_extreme_outlier
