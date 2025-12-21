from LR7.structure import AdjacencyList, NestedSet, AdjacencyListToNestedSetConverter, NestedSetToAdjacencyListConverter

adj_list = AdjacencyList()
print("Adjacency List структура:")
adj_list.print_tree()
print()

nested_set = NestedSet()
print("Nested Set структура:")
nested_set.print_tree()
print()

converter1 = AdjacencyListToNestedSetConverter(adj_list)
converted_nested_set = converter1.convert()
print("После конвертации из Adjacency List в Nested Set:")
converted_nested_set.print_tree()
print()

converter2 = NestedSetToAdjacencyListConverter(nested_set)
converted_adj_list = converter2.convert()
print("После конвертации из Nested Set в Adjacency List:")
converted_adj_list.print_tree()