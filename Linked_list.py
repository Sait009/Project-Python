class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheFirst(self, data):
        if self.head != None:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
            self.tail = new_node

    def AtTheEnd(self, data):
        if self.head == None:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        if self.head != None:
            head = self.head.data
            tail = self.tail.data
            current = self.head
            print("ข้อมูลที่จัดเก็บในตำแหน่งที่พอยเตอร์ head และ tail ชี้ คือ")
            print("head = ", head)
            print("tail = ", tail)
            print("ข้อมูลใน Singly linked list คือ")
            while current:
                print(current.data, end=" \n")
                current = current.next


singly = LinkedList()

print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list")
print("1. เพื่อเพิ่มข้อมูลที่จุดเริ่มต้นของ Singly linked list")
print("2. เพื่อเพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list")
print(
    "3. เพื่อแสดงข้อมูลที่จัดเก็บในตำแหน่งที่พอยเตอร์ head และ tail ชี้และข้อมูลใน Singly linked list \n"
)
choice = int(input("ทางเลือกในการดำเนินการ = "))

while choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        data = int(
            input("ตัวเลขที่ต้องการเพิ่มที่จุดเริ่มต้นของ Singly linked list = ")
        )
        singly.AtTheFirst(data)
    elif choice == 2:
        data = int(
            input("ตัวเลขที่ต้องการเพิ่มแบบต่อจากโหนดสุดท้ายของ Singly linked list = ")
        )
        singly.AtTheEnd(data)
    elif choice == 3:
        singly.display()

    print("โปรดระบุทางเลือกในการดำเนินการกับ Singly linked list")
    print("1. เพื่อเพิ่มข้อมูลที่จุดเริ่มต้นของ Singly linked list")
    print("2. เพื่อเพิ่มข้อมูลแบบต่อจากโหนดสุดท้ายของ Singly linked list")
    print(
        "3. เพื่อแสดงข้อมูลที่จัดเก็บในตำแหน่งที่พอยเตอร์ head และ tail ชี้และข้อมูลใน Singly linked list \n"
    )
    choice = int(input("ทางเลือกในการดำเนินการ = "))
