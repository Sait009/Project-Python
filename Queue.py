# Class Queue
class queue :
    def __init__(self,n):
        self.n = n
        self.queue = []*n
        self.front = -1
        self.rear = -1

    def add(self,item):
        if self.rear == self.n - 1:
            print("Queue is full")
        else :
            if self.front == -1:
                self.queue[self.rear+1] = item
                self.rear = self.rear + 1
                self.front = self.front +1
            else:
                self.queue[self.rear+1] = item
                self.rear = self.rear+1

    def remove (self):
        if (self.rear-self.front)+1 == 0:
            print("Queue is empty")
        else:
            if self.front == self.rear:
                self.queue[self.rear] = None
                self.rear = -1
                self.front = -1
                print("Queue is empty")
            else:
                self.queue[self.front] = None
                self.front = self.front+1

    def len(self):
        return len(self.queue)

    def display(self):
        if (self.front == -1):
            print("Queue is empty")
        else:
            for i in self.queue:
                print(i)

# Class Circulur Queue
class circulurQueue:
    def __init__(self , n ):
        self.n = n
        self.queue = []*n
        self.front = -1
        self.rear = -1

    def addci(self,data):
        if ((self.rear+1) % self.n == self.front):
            print("Circular queue is full")
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue.append(data)
        else:
            self.rear = (self.rear + 1) % self.n
            self.queue.append(data)

    def removeci(self):
        if (self.front == -1):
            print("Circular queue is empty")
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else :
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.n
            return temp

    def displayci(self):
        if (self.front == -1):
            print("Circular queue is empty")
        elif self.rear >= self.front :
            for i in range(self.front, self.rear +1):
                print(self.queue[i])
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])
            for i in range(0, self.rear + 1):
                print(self.queue[i])

# END def

choice = 1
n = int(input("โปรดระบุขนาดของ Queue ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

while n < 5:
    n = int(input("โปรดระบุขนาดของ Queue ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

while (choice==1 or choice==2 or choice==3 or choice==4 or choice==5):
    print("โปรดระบุทางเลือกในการดำเนินการกับ Queue")
    print("1. เพิ่มข้อมูลใน Queue")
    print("2. ลบข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Queue")
    print("3. แสดงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Queue ทางจอภาพ")
    print("4. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Queue ทางจอภาพ")
    print("5. แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลที่จัดเก็บใน Queue ทางจอภาพ \n")
    choice = int(input("ทางเลือกในการดำเนินการ = "))

    if choice == 1:

