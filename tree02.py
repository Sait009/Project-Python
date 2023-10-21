class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        self.data = data
        data = int(
            input(
                "โปรดป้อนหมายเลขของโหนด Left child ของ %d (ถ้าไม่มีให้ป้อน -1234) :\n"
                % self.data
            )
        )
        if data != -1234:
            self.leftChild = Node()
            self.leftChild.insert(data)

        data = int(
            input(
                "โปรดป้อนหมายเลขของโหนด Right child ของ %d (ถ้าไม่มีให้ป้อน -1234) :\n"
                % self.data
            )
        )
        if data != -1234:
            self.rightChild = Node()
            self.rightChild.insert(data)

    def PreOrder(self, tree):
        if tree is not None:
            if tree.data % 3 == 0:
                print(tree.data, end=" ")
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)

    def InOrder(self, tree):
        if tree is not None:
            self.InOrder(tree.leftChild)
            if tree.data > 20:
                print(tree.data, end=" ")
            self.InOrder(tree.rightChild)

    def PostOrder(self, tree):
        if tree is not None:
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            if tree.data % 2 != 0:
                print(tree.data, end=" ")


root = Node()
root.insert(int(input("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ Root node : ")))

txtch = "ทางเลือกในการดำเนินการ\n1. ท่องไปในต้นไม้ทวิภาคแบบ Pre-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่หารด้วย 3 ลงตัวทางจอภาพ\n2. ท่องไปในต้นไม้ทวิภาคแบบ In-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่าเกิน 20 ทางจอภาพ\n3. ท่องไปในต้นไม้ทวิภาคแบบ Post-order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคี่ทางจอภาพ\nโปรดระบุทางเลือกในการดำเนินการ = "
choice = int(input(txtch))

while choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        print("PreOrder = ", end=" ")
        root.PreOrder(root)
        print()
    elif choice == 2:
        print("InOrder = ", end=" ")
        root.InOrder(root)
        print()
    elif choice == 3:
        print("PostOrder = ", end=" ")
        root.PostOrder(root)
        print()

    choice = int(input(txtch))
