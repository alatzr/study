# 栈：LIFO 后进先出
class Stack:
    def __init__(self):
        self.s = []

    def is_empty(self):
        return self.s == []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()
    
    def peek(self):
        return self.s[-1]

    def size(self):
        return s.__len__


