# Add Two numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
```

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = l1.val + l2.val
        if r <= 9:
            l1.val = r
            t = 0
        else:
            l1.val = r % 10
            t = r // 10

        if t == 0: # 判断是否进位
            if isinstance(l1.next, ListNode) and isinstance(l2.next, ListNode):
                l1.next = self.addTwoNumbers(l1.next, l2.next) # 递归
                return l1
            elif isinstance(l1.next, ListNode):
                return l1
            elif isinstance(l2.next, ListNode):
                l1.next = l2.next
                return l1
            else:
                return l1
        else:
            if isinstance(l1.next, ListNode) and isinstance(l2.next, ListNode):
                l1.next.val += t
                l1.next = self.addTwoNumbers(l1.next, l2.next)
                return l1
            elif isinstance(l1.next, ListNode):
                l1.next = self.addTwoNumbers(l1.next, ListNode(t))
                return l1
            elif isinstance(l2.next, ListNode):
                l1.next = l2.next
                l1.next = self.addTwoNumbers(l1.next, ListNode(t))
                return l1
            else:
                l1.next = ListNode(t)
                return l1
```
