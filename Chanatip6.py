class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_set(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find_set(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        x = self.find_set(parent, x)
        y = self.find_set(parent, y)
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] = rank[x] + 1

    def kruskal(self):
        A = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for vertex in range(self.V):
            parent.append(vertex)
            rank.append(0)
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find_set(parent, u)
            y = self.find_set(parent, v)
            if x != y:
                e = e + 1
                A.append([u, v, w])
                self.union(parent, rank, x, y)
                print("เส้นเชื่อมระหว่างจุด %d กับจุด %d น้ำหนัก = %d" % (u, v, w))
        sum = 0
        for u, v, weight in A:
            sum = sum + weight
        print("ค่าน้ำหนักรวมของ Minimum spanning tree = %d" % (sum))


vertices = int(
    input("โปรดระบุจำนวนจุดในกราฟแบบไม่มีทิศทง (undirected graph) ที่มีค่ามากกว่า 2: ")
)
while vertices <= 2:
    vertices = int(
        input(
            "โปรดระบุจำนวนจุดในกราฟแบบไม่มีทิศทง (undirected graph) ที่มีค่ามากกว่า 2: "
        )
    )

g = Graph(vertices)

edge = int(input("โปรดระบุจำนวนเส้นเชื่อม (Edge) : "))

print(
    "โปรดระบุชื่อจุดที่เป็น Source ชื่อจุดที่เป็น Destination และค่าน้ำหนัก (Weight) ของเส้นเชื่อม : "
)
while edge > 0:
    source = int(input("Source = "))
    destination = int(input("Destination = "))
    weight = int(input("น้ำหนัก = "))
    g.addEdge(source, destination, weight)
    edge -= 1

print("Minimum spanning tree คือ ")
g.kruskal()
