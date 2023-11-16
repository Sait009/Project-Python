key = 0
coll = 0
size = int(input("โปรดป้อนขนาดตารางแฮช: "))

Hash_table = [None] * size

while key >= 0:
    key = int(input("โปรดป้อนค่าคีย์ (Key) ที่มีค่าตั้งแต่ 0 ขึ้นไป: "))
    data = input("โปรดป้อนข้อมูลชื่อพนักงานเพื่อจัดเก็บข้อมูลในตารางแฮช: ")
    if key < 0:
        break
    else:
        address = key % size
        if Hash_table[address] == None:
            Hash_table[address] = data
        else:
            while Hash_table[address] != None:
                coll += 1
                address = (key + coll) % size
            else:
                coll = 0
            Hash_table[address] = data
    print("Address : ", address)

print("ข้อมูลในตารางแฮช")
for i in range(len(Hash_table)):
    if i != None:
        if Hash_table[i] != None:
            print("Address : %d" % i, "ข้อมูลที่จัดเก็บคือ %s" % Hash_table[i])
            i += 1
        else:
            print("Address : %s" % i, "ไม่มีข้อมูลจัดเก็บ")
            i += 1
