key = 0
coll = 0
size = int(input("โปรดป้อนขนาดตารางแฮช: "))

Hash_table = [None] * size  # 7

while key >= 0:
    key = int(input("โปรดป้อนค่าคีย์ (Key) ที่เป็นจำนวนตั้งแต่ 0 ขึ้นไป: "))
    data = input("โปรดป้อนข้อมูล (data) ที่เป็นข้อความเพื่อจัดเก็บข้อมูลในตารางแฮช: ")
    if key < 0:
        break
    else:
        address = key % size
        if Hash_table[address] == None:
            Hash_table[address] = data
        else:
            print("ตําแหน่งดังกล่าวในตารางแฮชจัดเก็บข้อมูล %s" % Hash_table[address])
            coll += 1

print("ตารางแฮช")
for i in range(len(Hash_table)):
    if i != None:
        if Hash_table[i] != None:
            print("index %d" % i, "ข้อมูลที่จัดเก็บคือ %s" % Hash_table[i])
            i += 1
        else:
            print("index %s" % i, "ว่าง")
            i += 1

print("จำนวนครั้งที่เกิด Collission = %d" % coll)
