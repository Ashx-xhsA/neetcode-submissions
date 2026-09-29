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
        ListNode cur = dummy;
        int overflow = 0;
        while(l1 != null && l2 != null){
            int total = l1.val + l2.val + overflow;
            int digit;
            if (total >= 10){
                digit = total - 10;
                overflow = 1;
            }
            else{
                digit = total;
                overflow = 0;
            }

            ListNode digitListNode =new ListNode(digit);
            cur.next = digitListNode;
            cur = digitListNode;

            l1 = l1.next;
            l2=l2.next;
        }
        ListNode remainLi = (l1 != null)? l1:l2;
        while (remainLi != null){
            int total = remainLi.val + overflow;
            int digit;
            if (total >= 10){
                digit = total - 10;
                overflow = 1;
            }
            else{
                digit = total;
                overflow = 0;
            }

            ListNode digitListNode =new ListNode(digit);
            cur.next = digitListNode;
            cur = digitListNode;

            remainLi = remainLi.next;
        }
        if (overflow != 0){
            cur.next = new ListNode(1);
        }
        return dummy.next;

        
    }
}
