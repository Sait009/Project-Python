def Is_full(stack):
    if len(stack) == size:
        True
    else:
        False


def Is_empty(stack):
    if len(stack) == 0:
        True
    else:
        False


def display_stack(stack):
    if Is_empty == False:
        print("ข้อมูล = ", stack)
    else:
        print("แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง")


def top_stack(stack):
    if Is_empty == False:
        print("ข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Stack คือ ", stack[-1])
    else:
        print("แสดงข้อมูลที่จัดเก็บในตำแหน่งสูงสุดของ Stack ไม่ได้เพราะ Satck ว่าง")


def push_stack(stack, data):
    if Is_full == True:
        print("จัดเก็บข้อมูลไม่ได้เพราะ Stack เต็ม")
    else:
        stack.append(data)


def pop_stack(stack):
    if Is_empty == False:
        stack.pop()
    else:
        print("ลบข้อมูลไม่ได้เพราะ Stack ว่าง ")


def max_min(stack):
    if Is_empty == False:
        print("ค่ามากที่สุดของข้อมูลใน Stack คือ ", max(stack))
        print("ค่าน้อยที่สุดของข้อมูลใน Stack คือ ", min(stack))
    else:
        print(
            "แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง"
        )


choise = 1
size = int(input("โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

while size < 5:
    size = int(input("โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

stack = [] * size

while choise >= 1 and choise <= 5:
    print("โปรดระบุทางเลือกในการดำเนินการกับ Stack")
    print("1. เพิ่มข้อมูลใน stack")
    print("2. ลบข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ stack")
    print("3. แสดงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Stack ทางจอภาพ")
    print("4. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Stack ทางจอภาพ")
    print("5. แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลที่จัดเก็บใน Satck ทางจอภาพ \n")
    choise = int(input("ทางเลือกในการดำเนินการ = "))
    if choise == 1:
        print("ทางเลือกในการดำเนินการ = 1")
        data = input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Stack = ")
        push_stack(stack, data)
    elif choise == 2:
        print("ทางเลือกในการดำเนินการ = 2")
        pop_stack(stack)
    elif choise == 3:
        print("ทางเลือกในการดำเนินการ = 3")
        top_stack(stack)
    elif choise == 4:
        print("ทางเลือกในการดำเนินการ = 4")
        display_stack(stack)
    elif choise == 5:
        print("ทางเลือกในการดำเนินการ = 5")
        max_min(stack)
