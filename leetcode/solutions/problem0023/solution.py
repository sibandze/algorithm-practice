# Leetcode 23: Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def _mergeKLists(start, end):
            if start == end:
                return lists[start]
            mid = (start+end+1)//2
            left = _mergeKLists(start, mid-1)
            right = _mergeKLists(mid, end)

            return self.mergeTwoLists(left, right)
        return _mergeKLists(0, len(lists)-1)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2
        return dummy.next
