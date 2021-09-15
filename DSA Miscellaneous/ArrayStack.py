# ArrayStack - list implementation of Stack

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def size(self):
        return len(self._data)

    def isEmpty(self):
        if self.size() == 0:
            raise Empty('Stack is empty')
        else:
            print('Stack is not empty')
    
    def top(self):
        return self._data[-1]

    def push(self,element):
        self._data.append(element)

    def pop(self):
        if self.size() == 0:
            raise Empty('Stack is empty')
        else:
            return self._data.pop()

    def display(self):
        if self.size()!=0:
            return [self._data[i] for i in range(len(self._data)-1, -1,-1)]
        else:
            return "Stack is empty! Add elements."
        

stack = ArrayStack()
stack.push(5)
stack.push(10)


print('top',stack.top())
stack.pop()

print(stack.display())

stack.pop()

print(stack.display())

stack.pop()


