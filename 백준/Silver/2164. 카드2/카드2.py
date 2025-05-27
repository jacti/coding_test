import sys

N = int(input())
class Queue:
    def __init__(self, size):
        self.q = [x for x in range(1,size+1)]
        self.head = 0
        self.tail = 0
        self.size = size
        self.max_size = size
    
    def enqueue(self,n):
        self.q[self.tail] = n
        self.tail +=1
        self.tail%=self.max_size
        self.size+=1

    def dequeue(self):
        tmp = self.q[self.head]
        self.head +=1
        self.head %=self.max_size
        self.size -=1
        return tmp
    
    def front(self):
        return self.q[self.head]
    
q = Queue(N)
for _ in range(N-1):
    q.dequeue()
    q.enqueue(q.dequeue())
print(q.front())