def Is_full(stack, size):
    return len(stack) == size


def Is_empty(stack):
    return len(stack) == 0


def display_stack(stack):
    if not Is_empty(stack):
        print("ข้อมูล = ", stack)
    else:
        print("แสดงข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง")


def top_stack(stack):
    if not Is_empty(stack):
        print("ข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Stack คือ ", stack[-1])
    else:
        print("แสดงข้อมูลที่จัดเก็บในตำแหน่งสูงสุดของ Stack ไม่ได้เพราะ Stack ว่าง")


def push_stack(stack, data, size):
    if not Is_full(stack, size):
        stack.append(data)
    else:
        print("จัดเก็บข้อมูลไม่ได้เพราะ Stack เต็ม")


def pop_stack(stack):
    if not Is_empty(stack):
        stack.pop()
    else:
        print("ลบข้อมูลไม่ได้เพราะ Stack ว่าง ")


def max_min(stack):
    if not Is_empty(stack):
        print("ค่ามากที่สุดของข้อมูลใน Stack คือ ", max(stack))
        print("ค่าน้อยที่สุดของข้อมูลใน Stack คือ ", min(stack))
    else:
        print(
            "แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลใน Stack ไม่ได้เพราะ Stack ว่าง"
        )


choice = 1
size = int(input("โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

while size < 5:
    size = int(input("โปรดระบุขนาดของ Stack ที่มีขนาดตั้งแต่ 5 ช่องขึ้นไป : "))

stack = [] * size

while choice >= 1 and choice <= 5:
    print("โปรดระบุทางเลือกในการดำเนินการกับ Stack")
    print("1. เพิ่มข้อมูลใน stack")
    print("2. ลบข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ stack")
    print("3. แสดงข้อมูลที่จัดเก็บในตำแหน่งบนสุดของ Stack ทางจอภาพ")
    print("4. แสดงข้อมูลทั้งหมดที่จัดเก็บใน Stack ทางจอภาพ")
    print("5. แสดงค่ามากที่สุดและค่าน้อยที่สุดของข้อมูลที่จัดเก็บใน Satck ทางจอภาพ \n")
    choice = int(input("ทางเลือกในการดำเนินการ = "))
    if choice == 1:
        data = input("ข้อมูลที่ต้องการจัดเก็บข้อมูลใน Stack = ")
        push_stack(stack, data, size)
    elif choice == 2:
        pop_stack(stack)
    elif choice == 3:
        top_stack(stack)
    elif choice == 4:
        display_stack(stack)
    elif choice == 5:
        max_min(stack)
