#https://leetcode.com/problems/merge-two-sorted-lists/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def merge_lists(self, list_1, list_2):
        temp = dummy = Node(0)
        
        while(list_1 and list_2):
            if list_1.data < list_2.data:
                temp.next = list_1
                list_1=list_1.next
            else:
                temp.next = list_2 
                list_2 = list_2.next
            temp=temp.next
        if(list_1):
            temp.next = list_1
        if(list_2):
            temp.next = list_2
        return dummy.next
    
    def traverse(self, head_val):
        current = head_val 
        
        while current:
            print(current.data)
            current = current.next
        print('-'*40)

ll = LinkedList()
node_list = Node(1)
node_list.next = Node(3)
node_list.next.next = Node(5)
node_list.next.next.next = Node(7)
node_list.next.next.next.next = Node(9)

node2_list = Node(1)
node2_list.next = Node(4)
node2_list.next.next = Node(6)
node2_list.next.next.next = Node(8)
node2_list.next.next.next.next = Node(10)

res = ll.merge_lists(node_list, node2_list)
ll.traverse(res)
