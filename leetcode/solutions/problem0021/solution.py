# Leetcode 21: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while list1 != None and list2 != None:                
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
                current = current.next
            else:
                current.next = list1
                list1 = list1.next
                current = current.next
        current.next = list2 or list1
        return head.next


        
