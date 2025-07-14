/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode node1 = l1, node2 = l2, node = dummy;
        int carry = 0, total = 0;
        while(node1 != null || node2 != null){
            if(node1 == null){
                total = node2.val + carry;
                node2 = node2.next;
            }
            else if(node2 == null){
                total = node1.val + carry;
                node1 = node1.next;
            }
            else{
                total = node1.val + node2.val + carry;
                node1 = node1.next;
                node2 = node2.next;
            }
            node.next = new ListNode(total%10);
            node = node.next;
            carry = total/10;
        }
        if(carry != 0){
            node.next = new ListNode(carry);
        }
        return dummy.next;
    }
}
