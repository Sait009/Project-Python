import math
import random


class Vertex:
    def __init__(self, data):
        self.id = data
        self.distance = math.inf
        self.color = "white"
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def set_color(self, color):
        self.color = color

    def set_distance(self, distance):
        self.distance = distance

    def set_pred(self, predecessor):
        self.pred = predecessor

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_pred(self):
        return self.pred

    def get_distance(self):
        return self.distance

    def get_color(self):
        return self.color


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)

        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)

        self.vertices[from_vertex].add_neighbor(self.vertices[to_vertex])

    def breadth_first_search(self, start_vertex):
        start = self.vertices[start_vertex]
        start.set_distance(0)
        start.set_pred(None)
        queue = []
        queue.append(start)
        while queue:
            current_vertex = queue.pop(0)
            for neighbor in current_vertex.get_connections():
                if neighbor.get_color() == "white":
                    neighbor.set_color("gray")
                    neighbor.set_distance(current_vertex.get_distance() + 1)
                    neighbor.set_pred(current_vertex)
                    queue.append(neighbor)
            current_vertex.set_color("black")


# Main part of the code
graph = Graph()
num_vertices = int(input("ป้อนจำนวนของจุดในกราฟแบบมีทิศทาง: "))

while num_vertices <= 2:
    num_vertices = int(input("โปรดป้อนจำนวนที่มากกว่า 2: "))

for _ in range(num_vertices):
    vertex_name = input("ป้อนชื่อของจุด: ")
    graph.add_vertex(vertex_name)

while True:
    print("ป้อนจุดต้นทางและปลายทางสำหรับเส้นเชื่อม (หรือปล่อยว่างทั้งสองเพื่อสิ้นสุด)")
    source = input("จุดต้นทาง: ")
    destination = input("จุดปลายทาง: ")
    if not source and not destination:
        break
    else:
        graph.add_edge(source, destination)

# print("โปรดป้อนจุดเริ่มต้นสำหรับการค้นหาแบบค้นความลึกก่อนเส้นเชื่อม:")
# start_vertex = input("จุดเริ่มต้น: ")
# graph.breadth_first_search(start_vertex)

# for vertex_name in graph.vertices:
#     if vertex_name != start_vertex:
#         target_vertex = graph.vertices[vertex_name]
#         shortest_distance = target_vertex.distance
#         print(
#             f"ระยะทางสั้นที่สุดจาก {start_vertex} ไปยัง {vertex_name} = {shortest_distance}"
#         )

print("โปรดป้อนจุดเริ่มต้นสำหรับการค้นหาแบบค้นความลึกก่อนเส้นเชื่ม:")
start_vertex = input("จุดเริ่มต้น: ")

# เพิ่มส่วนสุ่มจุดปลายทาง
if start_vertex in graph.vertices:
    random_destination = random.choice(
        list(graph.vertices.keys())
    )  # เลือกจุดปลายทางแบบสุ่ม
    print(f"จุดปลายทางสุ่ม: {random_destination}")

    graph.breadth_first_search(start_vertex)

    # คำนวณระยะทางจากจุดเริ่มต้นไปยังจุดปลายทางแบบสุ่ม
    target_vertex = graph.vertices[random_destination]
    shortest_distance = target_vertex.distance
    print(
        f"ระยะทางสั้นที่สุดจาก {start_vertex} ไปยัง {random_destination} = {shortest_distance}"
    )
else:
    print("จุดเริ่มต้นไม่ถูกต้อง")
