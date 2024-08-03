class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    # 공백 상태와 포화 상태 표시
    def isEmpty(self):
        return self.front == self.rear
    

    def isFull(self):
        return self.rear == (self.rear + 1) % self.capacity
    

    # 원형 큐 : 삽입 연산
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+ 1) % self.capacity
            self.array[self.rear] = item

        else:
            pass

    
    # 원형 큐 : 링 버퍼 삽입 연산
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity


    # 원형 큐 : 삭제 연산
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        
        else:
            pass


    def peak(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        
        else: 
            pass


    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    

    def display(self, msg):
        print(msg, end='= [')
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i%self.capacity])

        print("]")



#test code

q = ArrayQueue(8)

q.display("초기상태")
for i in range(6):
    q.enqueue2(i)
q.display('삽입 0 ~ 5')

q.enqueue2(6) ; q.enqueue2(7)
q.display('삽입 6,7')

q.enqueue2(8) ; q.enqueue2(9)
q.display("삽입 8,9")

q.dequeue() ; q.dequeue()