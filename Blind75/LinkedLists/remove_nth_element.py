#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse_list(self, head_val):
        previous = None 
        current = head_val 
        
        while(current):
            temp = current.next 
            current.next = previous 
            previous = current 
            current = temp 
        return previous
    
    def traverse(self, head_val):
        current = self.head = head_val
        while current:
            print(current.data)
            current = current.next
        print('-'*40)
        
    def remove_nth(self, nth_value):
        cnt = 0 
        current = self.head
        previous = None
        
        while(current):
            if cnt!=nth_value:
                cnt+=1
                previous = current 
                current = current.next
            else:
                previous.next = current.next 
                return 
            
#### rough work 
#1 -> 2 -> 3 -> 4 -> 5

node_obj = Node(1)
node_obj.next = Node(2)
node_obj.next.next = Node(3)
node_obj.next.next.next = Node(4)
node_obj.next.next.next.next = Node(5)

ll = LinkedList()
ll.traverse(node_obj)

new_head = ll.reverse_list(node_obj)

ll.traverse(new_head)
ll.remove_nth(2)
ll.traverse(new_head)