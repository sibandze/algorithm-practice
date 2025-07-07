# Leetcode 19 Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        while fast and n>=0:
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
