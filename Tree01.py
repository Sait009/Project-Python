class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        self.data = data
        left_input = int(
            input(
                "โปรดป้อนหมายเลขของโหนด Left child ของ %d (ถ้าไม่มีให้ป้อน -1234) :\n"
                % self.data
            )
        )
        if left_input != -1234:
            self.leftChild = Node()
            self.leftChild.insert(left_input)

        right_input = int(
            input(
                "โปรดป้อนหมายเลขของโหนด Right child ของ %d (ถ้าไม่มีให้ป้อน -1234) :\n"
                % self.data
            )
        )
        if right_input != -1234:
            self.rightChild = Node()
            self.rightChild.insert(right_input)

    def PreOrder(self):
        if self:
            if self.data % 3 == 0:
                print(self.data, end=" ")
            if self.leftChild:
                self.leftChild.PreOrder()
            if self.rightChild:
                self.rightChild.PreOrder()

    def InOrder(self):
        if self:
            if self.leftChild:
                self.leftChild.InOrder()
            if self.data > 20:
                print(self.data, end=" ")
            if self.rightChild:
                self.rightChild.InOrder()

    def PostOrder(self):
        if self:
            if self.leftChild:
                self.leftChild.PostOrder()
            if self.rightChild:
                self.rightChild.PostOrder()
            if self.data % 2 != 0:
                print(self.data, end=" ")


root = Node()
root.insert(int(input("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ Root node : ")))

txtchoice = "ทางเลือกในการดำเนินการ\n1. ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 3 ลงตัวทางจอภาพ\n2. ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าเกิน 20 ทางจอภาพ\n3. ท่องไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคี่ทางจอภาพ\nโปรดระบุทางเลือกในการดำเนินการ = "
choice = int(input(txtchoice))

while choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        print("PreOrder = ", end=" ")
        root.PreOrder()
        print()
    elif choice == 2:
        print("InOrder = ", end=" ")
        root.InOrder()
        print()
    elif choice == 3:
        print("PostOrder = ", end=" ")
        root.PostOrder()
        print()

    choice = int(input(txtchoice))
