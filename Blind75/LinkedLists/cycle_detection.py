#https://leetcode.com/problems/linked-list-cycle/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def traverse(self):
        current = self.head 
        while current is not None:
            print(current.data)
            current=current.next
        return

    def detect_loop(self):
        slow_ptr = self.head 
        fast_ptr = self.head 
        
        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next 
            
            if slow_ptr.data == fast_ptr.data:
                return 'loop detected'
        return 'no loop'

node_1 = Node(1)
ll = LinkedList()
ll.head = node_1
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
ll.head.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
#node_5.next = node_1

print(ll.detect_loop())