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
        /**
        T: O(max(n1, n2)); n1 and n2 are lengths of l1 and l2.
        and S: O(1) ignore space required for storing results.
        */
        l1 = reverse(l1);
        l2 = reverse(l2);
        ListNode l = add(l1, l2);
        l = reverse(l);
        return l;
    }
    
    public static ListNode reverse(ListNode head) {
        ListNode prev = null;
        ListNode tail = head;
        while (tail != null) {
            ListNode temp = tail.next;
            tail.next = prev;
            prev = tail;
            tail = temp;
        }
        return prev;
    }
    
    public static ListNode add(ListNode l1, ListNode l2) {
        ListNode l = new ListNode(0);
        ListNode t1 = l1;
        ListNode t2 = l2;
        ListNode t = l;
        int carry = 0;
        int v1, v2, sum;
        while (t1 != null || t2 != null || carry != 0) {
            if (t1 != null) {
                v1 = t1.val;
                t1 = t1.next;
            }
            else {
                v1 = 0;
                t1 = null;
            }
            if (t2 != null) {
                v2 = t2.val;
                t2 = t2.next;
            }
            else {
                v2 = 0;
                t2 = null;
            }
            
            sum = v1 + v2 + carry;
            carry = sum / 10;
            sum = sum % 10;
            
            t.next = new ListNode(sum);
            t = t.next;
        }
        return l.next;
        
    }
}
