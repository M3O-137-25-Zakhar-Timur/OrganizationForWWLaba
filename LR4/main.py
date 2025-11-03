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
# ----------------------- Реализация методов ----------------
#Реализация BFS обхода - нахождения пути. (Обход в ширину)
def shortest_path(graph,start,end):
    queue = deque([(start,[start])])
    visited = set()
    while queue:
        (node, path) = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        for child in graph.nodes[node]:
            if child == end:
                return path + [end]
            else:
                queue.append((child, path + [child]))
    return None
# Реализация DFS обхода - нахождения пути. (Обход в глубину)
def dfs_find_path(graph,node,end,path):
    if graph.nodes[node] is None:
        return False
    path.append(node)
    if graph.nodes[node] == graph.nodes[end]:
        return True
    for child in graph.nodes[node]:
        if dfs_find_path(graph,child,end,path):
            return True
    path.pop()
# ------------------------------------------------------------------
def find_path(graph,start,end):
    path = []
    if dfs_find_path(graph,start,end,path):
        return path
#--------------Вывод результатов------------------------------------
print(find_path(graph,"A","I"))
print(shortest_path(graph,"A","I"))
