#LAB7 ##HASH TABLE ##1
n = int(input("โปรดป้อนขนาดตารางแฮช : "))
tb_coll  = 0
Hash_Table = [None]*n
while True:
    key = int(input("โปรดป้อนค่าคีย์ (Key) ที่เป็นจำนวนตั้งแต่ 1 ขึ้นไป : "))
    data = (input("โปรดป้อนข้อมูล (data) ที่เป็นข้อความเพื่อจัดเก็บข้อมูลในตารางแฮช : "))
    if key<1 :
        break
    else:
        address = key%n
        if Hash_Table[address] == None:
            Hash_Table[address] = data
        else:
            print("จัดเก็บข้อมูลในตารางแฮชไม่ได้เพราะ Collision")
            tb_coll  = tb_coll + 1

print("ข้อมูลที่จัดเก็บในตารางแฮช")
for x in Hash_Table:
    if x != None:
        print("index = ",Hash_Table.index(x),"ข้อมูลที่จัดเก็บคือ",x)

print("จำนวนครั้งที่เกิด Collission = ",tb_coll )