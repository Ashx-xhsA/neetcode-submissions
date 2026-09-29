/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if (head == null){
            return null;
        }
        Node p = head;
        Map<Node,Node> map = new HashMap<>();

        while (p != null){
            Node copy = new Node(p.val);
            map.put(p,copy);
            p=p.next;
        }
        p = head;
        while (p!=null){
            Node copy = map.get(p);
            copy.next = map.get(p.next);
            copy.random = map.get(p.random);
            p = p.next;
        }
        return map.get(head);
    }
}
