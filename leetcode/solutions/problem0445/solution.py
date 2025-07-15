'''
Leetcode 445. Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
Follow up: Could you solve it without reversing the input lists?
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_stack = []
        l2_stack = []
        ans_stack = []
        while l1:
            l1_stack.append(l1)
            l1 = l1.next
        while l2:
            l2_stack.append(l2)
            l2 = l2.next
        dummy = ListNode()
        node = dummy
        carry = 0
        while l1_stack or l2_stack:
            if l1_stack and l2_stack:
                total = l1_stack.pop().val + l2_stack.pop().val + carry
            elif l1_stack:
                total = l1_stack.pop().val + carry
            else:
                total = l2_stack.pop().val + carry
            ans_stack.append(ListNode(total%10))
            carry = total//10
        if carry != 0:
            ans_stack.append(ListNode(carry))

        while ans_stack:
            node.next = ans_stack.pop()
            node = node.next
        return dummy.next
        
