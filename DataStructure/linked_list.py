#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 14:39
# @Author  : AnNing


class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_

    @staticmethod
    def append(node, data, index=None):
        if index is None:
            while True:
                if node.next is not None:
                    node = node.next
                else:
                    break
            node.next = Node(data=data)
        else:
            pre_node = node
            i = 0
            while i < index - 1:
                pre_node = pre_node.next
                i += 1
            node = pre_node.next
            new_node = Node(data=data, next_=node)
            pre_node.next = new_node

    def __str__(self):
        node = self
        s = "{} ".format(node.data)
        while True:
            if node.next is None:
                break
            node = node.next
            s += "{} ".format(node.data)
        return s


if __name__ == "__main__":
    linked_array = Node(1)
    print(linked_array)
    linked_array.append(linked_array, 2)
    print(linked_array)
    linked_array.append(linked_array, 3, 1)
    print(linked_array)
