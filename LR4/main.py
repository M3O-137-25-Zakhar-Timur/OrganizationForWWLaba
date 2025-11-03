from collections import deque
# Класс графа
class Graph():
    def __init__(self):
        self.nodes = {}
    def add_node(self,node):
        if node not in self.nodes:
            self.nodes[node] = []
    def add_edge(self,start,end):
        if start in self.nodes and end in self.nodes:
            self.nodes[start].append(end)
# Создание узлов и граней графа
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_node("G")
graph.add_node("H")
graph.add_node("J")
graph.add_node("I")
graph.add_edge("A","B")
graph.add_edge("A","C")
graph.add_edge("B","D")
graph.add_edge("D","E")
graph.add_edge("E","F")
graph.add_edge("F","G")
graph.add_edge("G","I")
graph.add_edge("F","H")
graph.add_edge("H","J")
graph.add_edge("J","I")
graph.add_edge("C","E")
# ----------------------- Реализация классов ----------------
#Реализация BFS обхода - нахождения пути. (Обход в ширину)
class BFSFindPath():
    def __init__(self):
        self.graph = 0
        self.start = 0
        self.end = 0
    def set_data(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
    def get_path(self):
        queue = deque([(self.start,[self.start])])
        visited = set()
        while queue:
            (node, path) = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            for child in self.graph.nodes[node]:
                if child == self.end:
                    return path + [self.end]
                else:
                    queue.append((child, path + [child]))
        return None
# Реализация DFS обхода - нахождения пути. (Обход в глубину)
class DFSFindPath():
    def __init__(self):
        self.graph = 0
        self.start = 0
        self.end = 0
    def set_data(self, graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
    def get_path(self):
        path = []
        if self.dfs_find_path(self.graph, self.start, self.end, path):
            return path
    def dfs_find_path(self,graph,node,end,path):
        if graph.nodes[node] is None:
            return False
        path.append(node)
        if graph.nodes[node] == graph.nodes[end]:
            return True
        for child in graph.nodes[node]:
            if self.dfs_find_path(graph,child,end,path):
                return True
        path.pop()
#--------------Вывод результатов------------------------------------
DFS = DFSFindPath()
BFS = BFSFindPath()

DFS.set_data(graph,"A","I")
BFS.set_data(graph,"A","I")

print(F"DFS: {DFS.get_path()}")
print(F"BFS: {BFS.get_path()}")
