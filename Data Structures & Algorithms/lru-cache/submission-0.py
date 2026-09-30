class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None
class NodeList:
    def __init__(self,cap):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.length = 0
        self.cap = cap
    def putInList(self,node):
        tmp = self.head.nxt

        self.head.nxt = node
        node.prev = self.head

        node.nxt = tmp
        tmp.prev = node
    
        self.length+= 1
        if self.length > self.cap:
            return self.removeFromTail()

    def moveToFront(self,node):
        if self.length == 1 or self.head.nxt == node:
            return
        pre = node.prev
        nxt = node.nxt
        prefront = self.head.nxt

        self.head.nxt = node
        node.prev = self.head

        node.nxt = prefront
        prefront.prev = node

        pre.nxt = nxt
        nxt.prev = pre

    def removeFromTail(self):
        if not self.length:
            return
        toRemove = self.tail.prev
        pre = toRemove.prev

        pre.nxt = self.tail
        self.tail.prev = pre

        toRemove.prev = None
        toRemove.nxt = None

        self.length -= 1
        return toRemove

class LRUCache:

    def __init__(self, capacity: int):
        self.nodeList = NodeList(capacity)
        self.cap = capacity
        self.d = {}
    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.nodeList.moveToFront(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            newNode = Node(key,value)
            removed = self.nodeList.putInList(newNode)
            self.d[key] = newNode
            if removed:
                del self.d[removed.key]
        else:
            self.d[key].val = value
            self.nodeList.moveToFront(self.d[key])
            
        
