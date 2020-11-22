'''
implementing basic queue using array - with enqueue and dequeue operations
'''

class Queue:
    def __init__(self):
        self.data = list()
        self.size = 0
        self.front = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, value):
        self.data.append(value)
        self.size+=1

    def print_queue(self):
        return self.data
    
    def dequeue(self):
        val = self.data[self.front]
        self.data[self.front] = None
        self.size-=1
        self.front+=1


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(10)
    q.enqueue(3)
    print(q.print_queue())
    print('performing dequeue')
    q.dequeue()
    print('queue after dequeue--', q.print_queue())

    


