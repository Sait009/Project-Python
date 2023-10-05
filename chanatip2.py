class circulurQueue:
    def __init__(self, n):
        self.n = n
        self.circulurqueue = [None] * n
        self.front = -1
        self.rear = -1

    def addci(self, data):
        if (self.rear + 1) % self.n == self.front:
            print("เพิ่มข้อมูลไม่ได้เพราะคิววงกลมเต็ม")
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.n
            self.circulurqueue[self.rear] = data

    def removeci(self):
        if self.front == -1:
            print("ลบข้อมูลไม่ได้เพราะคิววงกลมว่าง")
        else:
            temp = self.circulurqueue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.n
            return temp

    def displayci(self):
        if self.front == -1:
            print(
                "แสดงข้อมูลตัวเลขจำนวนเต็มที่เป็นเลขคู่ที่จัดเก็บในคิววงกลมไม่ได้เพราะคิววงกลมว่าง"
            )
        else:
            if self.rear >= self.front:
                for i in range(self.front, self.rear + 1):
                    if self.circulurqueue[i] % 2 == 0:
                        print(self.circulurqueue[i])
            else:
                for i in range(self.front, self.n):
                    if self.circulurqueue[i] % 2 == 0:
                        print(self.circulurqueue[i])
                for i in range(0, self.rear + 1):
                    if self.circulurqueue[i] % 2 == 0:
                        print(self.circulurqueue[i])


n = int(input("โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 4 ช่อง: "))

while n < 4:
    n = int(input("โปรดระบุขนาดของคิววงกลมที่มีขนาดตั้งแต่ 4 ช่อง: "))

q = circulurQueue(n)

print("โปรดระบุทางเลือกในการดำเนินการกับคิววงกลม")
print("กด 1 เพื่อรับข้อมูลตัวเลขที่ต้องการจัดเก็บในคิววงกลม")
print("กด 2 เพื่อลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว")
print("กด 3 เพื่อแสดงตัวเลขจำนวนเต็มที่เป็นเลขคู่ที่จัดเก็บในคิววงกลมทางจอภาพ")
choice = int(input("ทางเลือกในการดำเนินการ = "))

while choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        data = int(input("ตัวเลขจำนวนเต็มที่ต้องการจัดเก็บในคิววงกลม = "))
        q.addci(data)
    elif choice == 2:
        q.removeci()
    elif choice == 3:
        q.displayci()

    choice = int(
        input(
            "โปรดระบุทางเลือกในการดำเนินการกับคิววงกลม\nกด 1 เพื่อรับข้อมูลตัวเลขที่ต้องการจัดเก็บในคิววงกลม\nกด 2 เพื่อลบข้อมูลที่จัดเก็บในคิววงกลม 1 ตัว\nกด 3 เพื่อแสดงตัวเลขจำนวนเต็มที่เป็นเลขคู่ที่จัดเก็บในคิววงกลมทางจอภาพ\nทางเลือกในการดำเนินการ = "
        )
    )
