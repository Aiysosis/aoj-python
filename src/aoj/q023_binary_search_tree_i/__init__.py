from typing import Optional

TreeNode = Optional["Node"]


class Node:
    def __init__(
        self,
        key: int,
        left: TreeNode = None,
        right: TreeNode = None,
        parent: TreeNode = None,
    ) -> None:
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent


def pre_order(root: TreeNode) -> str:
    if root == None:
        return ""
    return f" {root.key}" + pre_order(root.left) + pre_order(root.right)


def in_order(root: TreeNode) -> str:
    if root == None:
        return ""
    return in_order(root.left) + f" {root.key}" + in_order(root.right)


def main():
    n = int(input())
    root: TreeNode = None

    def insert(root: TreeNode, key: int):
        pre: TreeNode = None
        cur = root
        while cur != None:
            pre = cur
            if key < cur.key:
                cur = cur.left
            else:
                cur = cur.right
        if pre == None:
            return Node(key)
        if key < pre.key:
            pre.left = Node(key)
        else:
            pre.right = Node(key)
        return root

    def walk_tree(root: TreeNode):
        print(in_order(root))
        print(pre_order(root))

    for _ in range(n):
        inst, *params = input().split(" ")
        if inst == "insert":
            root = insert(root, int(params[0]))
        if inst == "print":
            walk_tree(root)
