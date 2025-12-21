class AdjacencyList:
    def __init__(self):
        self.tree = {
            'Вб категории': ['Игрушки', 'Все для сада', 'Компьютерная фурнитура', 'Одежда'],
            'Игрушки': ['Поп иты', 'Лабубы', 'Спинеры'],
            'Поп иты': [],
            'Лабубы': [],
            'Спинеры': [],
            'Все для сада': ['Семена', 'Инвентарь', 'Обустройство'],
            'Семена': ['Семена томата', 'Семена дыньки', 'Семена огурца', 'Семена перца'],
            'Семена томата': [],
            'Семена дыньки': [],
            'Семена огурца': [],
            'Семена перца': [],
            'Инвентарь': ['Лейки', 'Лопаты', 'Перчатки', 'Ведра'],
            'Лейки': [],
            'Лопаты': [],
            'Перчатки': [],
            'Ведра': [],
            'Обустройство': ['Лавочки', 'Кашпо'],
            'Лавочки': ['Деревянные', 'Раскладные'],
            'Деревянные': [],
            'Раскладные': [],
            'Кашпо': [],
            'Компьютерная фурнитура': ['Мышь', 'Клавиатура', 'Наушники'],
            'Мышь': [],
            'Клавиатура': [],
            'Наушники': [],
            'Одежда': ['Мужская', 'Женская'],
            'Мужская': ['Брюки', 'Рубашки', 'Тапки'],
            'Брюки': [],
            'Рубашки': [],
            'Тапки': [],
            'Женская': ['Шапочки', 'Юбочки', 'Каблучки'],
            'Шапочки': [],
            'Юбочки': [],
            'Каблучки': []
        }

    def print_tree(self, node=None, level=0):
        if node is None:
            node = 'Вб категории'

        print("  " * level + node)
        for child in self.tree.get(node, []):
            self.print_tree(child, level + 1)


class NestedSet:
    def __init__(self):
        self.tree = [
            ('Вб категории', 1, 50),
            ('Игрушки', 2, 7),
            ('Поп иты', 3, 4),
            ('Лабубы', 5, 6),
            ('Спинеры', 8, 9),
            ('Все для сада', 10, 31),
            ('Семена', 11, 20),
            ('Семена томата', 12, 13),
            ('Семена дыньки', 14, 15),
            ('Семена огурца', 16, 17),
            ('Семена перца', 18, 19),
            ('Инвентарь', 21, 28),
            ('Лейки', 22, 23),
            ('Лопаты', 24, 25),
            ('Перчатки', 26, 27),
            ('Ведра', 29, 30),
            ('Обустройство', 32, 39),
            ('Лавочки', 33, 36),
            ('Деревянные', 34, 35),
            ('Раскладные', 37, 38),
            ('Кашпо', 40, 41),
            ('Компьютерная фурнитура', 42, 47),
            ('Мышь', 43, 44),
            ('Клавиатура', 45, 46),
            ('Наушники', 48, 49),
            ('Одежда', 51, 62),
            ('Мужская', 52, 57),
            ('Брюки', 53, 54),
            ('Рубашки', 55, 56),
            ('Тапки', 58, 59),
            ('Женская', 60, 65),
            ('Шапочки', 61, 62),
            ('Юбочки', 63, 64),
            ('Каблучки', 66, 67)
        ]

    def print_tree(self):
        sorted_tree = sorted(self.tree, key=lambda x: x[1])
        stack = []

        for node_id, left, right in sorted_tree:
            while stack and left > stack[-1][2]:
                stack.pop()

            level = len(stack)
            print("  " * level + node_id)
            stack.append((node_id, left, right))


class AdjacencyListToNestedSetConverter:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        self.nested_set = NestedSet()
        self.counter = 1
        self.result = []

    def convert(self):
        self._traverse('Вб категории')
        self.nested_set.tree = self.result
        return self.nested_set

    def _traverse(self, node_id):
        left = self.counter
        self.counter += 1

        for child in self.adjacency_list.tree.get(node_id, []):
            self._traverse(child)

        right = self.counter
        self.counter += 1
        self.result.append((node_id, left, right))


class NestedSetToAdjacencyListConverter:
    def __init__(self, nested_set):
        self.nested_set = nested_set
        self.adjacency_list = AdjacencyList()

    def convert(self):
        self.adjacency_list.tree = {}
        sorted_nodes = sorted(self.nested_set.tree, key=lambda x: x[1])
        stack = []

        for node_id, left, right in sorted_nodes:
            while stack and left > stack[-1][2]:
                stack.pop()

            if not stack:
                self.adjacency_list.tree[node_id] = []
            else:
                parent_id = stack[-1][0]
                if parent_id not in self.adjacency_list.tree:
                    self.adjacency_list.tree[parent_id] = []
                self.adjacency_list.tree[parent_id].append(node_id)
                self.adjacency_list.tree[node_id] = []

            stack.append((node_id, left, right))

        return self.adjacency_list


