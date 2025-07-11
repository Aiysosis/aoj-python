from typing import Union


class RootedTree:
    def __init__(
        self,
        val: int,
        children: Union[list["RootedTree"], None] = None,
        parent: Union["RootedTree", None] = None,
    ) -> None:
        self.val = val
        self.children = children if children is not None else []
        self.parent = parent

    def add_child(self, child: "RootedTree"):
        self.children.append(child)


def calc_depth(node: RootedTree) -> int:
    if node.parent == None:
        return 0
    return calc_depth(node.parent) + 1


def main():
    n = int(input())
    node_map: dict[int, RootedTree] = {}

    for i in range(n):
        node = RootedTree(i)
        node_map[i] = node

    for i in range(n):
        val, _, *children_ids = list(map(int, input().split(" ")))
        node = node_map[val]
        for id in children_ids:
            child_node = node_map[id]
            node.add_child(child_node)
            child_node.parent = node

    for node in node_map.values():
        is_root = node.parent == None
        is_leaf = len(node.children) == 0
        children_ids = list(map(lambda node: node.val, node.children))
        node_type = "root" if is_root else "leaf" if is_leaf else "internal node"
        print(
            f"node {node.val}: parent = {-1 if node.parent == None else node.parent.val}, depth = {calc_depth(node)}, {node_type}, {children_ids}"
        )
