### [2\. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

Difficulty: **Medium**



You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example:**

```
**Input:** (2 -> 4 -> 3) + (5 -> 6 -> 4)
**Output:** 7 -> 0 -> 8
**Explanation:** 342 + 465 = 807.
```



#### Solution

Language: **Python3**

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l1
        if not l1:
            return l2
        if not l2:
            return l1
        # 真正要做的就是模拟小学在草稿纸上的加法过程
        # 此处计算方法是，如果 l1 位数不够就给 l1 高位补上 0
        while l1 and l2:
            temp = l1.val + l2.val
            if not l1.next:
                # 保证 l1 和 l2 位数一样长，但是如果 l1 最后一位有进位的话需要讲进位保留下来，因此也需要补位
                if l2.next or temp >= 10:
                    l1.next = ListNode(0)
                    l1.val, l1.next.val = temp % 10, l1.next.val + temp // 10
                else:
                    l1.val = temp
            else:
                l1.val, l1.next.val = temp % 10, l1.next.val + temp // 10
            # 从低位向高位进位
            l1 = l1.next
            l2 = l2.next
        # 到此处只剩下进位后的项，然后逐位计算看有无进位
        while l1:
            if l1.val >= 10:
                if not l1.next:
                    l1.next = ListNode(0)
                l1.val, l1.next.val = l1.val % 10, l1.val // 10 + l1.next.val
            else:
                # 如果低位已经没有进位了，高位无需再计算
                break
            l1 = l1.next
        return result
```