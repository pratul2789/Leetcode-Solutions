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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dum = new ListNode(-1);
        dum.next = head;
        ListNode fast = head;
        ListNode slow = dum;
        
        while(n > 0 && fast != null){
            fast = fast.next;
            //dum = dum.next;
            n = n - 1;
        }
        
        while(fast != null){
            fast = fast.next;
            dum = dum.next;
        }
        
        dum.next = dum.next.next;
        
        return slow.next;
    }
}