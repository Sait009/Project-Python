# Class Queue
class queue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1

    def add(self, item):
        if self.rear == self.n - 1:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear = self.rear + 1
            self.queue[self.rear] = item

    def remove(self):
        if (self.rear - self.front) + 1 == 0:
            print("Queue is empty")
        else:
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
                print("Queue is empty")
            else:
                self.front = self.front + 1

    def length(self):
        if self.front == -1:
            return 0
        return self.rear - self.front + 1

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


# Class Circulur Queue
class circulurQueue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * n
        self.front = -1
        self.rear = -1

    def addci(self, data):
        if (self.rear + 1) % self.n == self.front:
            print("Circular queue is full")
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.n
            self.queue[self.rear] = data

    def removeci(self):
        if self.front == -1:
            print("Circular queue is empty")
        else:
            temp = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.n
            return temp

    def displayci(self):
        if self.front == -1:
            print("Circular queue is empty")
        else:
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    print(self.queue[i])
            else:
                for i in range(self.front, self.n):
                    print(self.queue[i])
                for i in range(0, self.rear + 1):
                    print(self.queue[i])


# END def

choice = 1


n = int(input("โปรดระบุขนาดของ Queue ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

while n < 5:
    n = int(input("โปรดระบุขนาดของ Queue ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

# while (
#     choice == 1
#     or choice == 2
#     or choice == 3
#     or choice == 4
#     or choice == 5
#     or choice == 6
#     or choice == 7
#     or choice == 8
#     or choice == 9
#     or choice == 10
# ):
#     print("โปรดระบุทางเลือกในการดำเนินการกับ Queue หรือ Circulur Queue")
#     print("1. เพิ่มข้อมูลใน Queue")
#     print("2. เพิ่มข้อมูลใน Circulur Queue")
#     print("3. ลบข้อมูลที่จัดเก็บใน Queue")
#     print("4. ลบข้อมูลที่จัดเก็บใน Circulur Queue")
#     print("5. แสดงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Queue ทางจอภาพ")
#     print("6. แสดงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Circulur Queue ทางจอภาพ")
#     print("7. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Queue ทางจอภาพ")
#     print("8. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Circulur Queue ทางจอภาพ")
#     print("9. แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลที่จัดเก็บใน Queue ทางจอภาพ")
#     print(
#         "10. แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลที่จัดเก็บใน Circulur Queue ทางจอภาพ \n"
#     )
#     choice = int(input("ทางเลือกในการดำเนินการ = "))

#     if choice == 1:
#         q = queue(n)
#         item = input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Queue = ")
#         q.add(item)
#     elif choice == 2:
#         q = circulurQueue(n)
#         data = input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Circulur Queue = ")
#         q.addci(data)
#     elif choice == 3:
#         q = queue(n)
#         q.remove()
#     elif choice == 4:
#         q = circulurQueue(n)
#         q.removeci()
#     elif choice == 5:
#         q = queue(n)

#     elif choice == 6:
#     elif choice == 7:
#     elif choice == 8:
#     elif choice == 9:
#     elif choice == 10:
