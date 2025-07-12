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
            pre.left = Node(key, None, None, pre)
        else:
            pre.right = Node(key, None, None, pre)
        return root

    def walk_tree(root: TreeNode):
        print(in_order(root))
        print(pre_order(root))

    def find(root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        if root.key == key:
            return root
        return find(root.left, key) if key < root.key else find(root.right, key)

    def delete(n: Node):
        if n.left != None and n.right != None:
            s = n.right
            while s.left != None:
                s = s.left
            delete(s)
            s.left = n.left
            s.right = n.right
            s.parent = n.parent
            if n.parent != None:
                if n.parent.left == n:
                    n.parent.left = s
                else:
                    n.parent.right = s
        elif n.left != None:
            s = n.left
            s.parent = n.parent
            if n.parent != None:
                if n.parent.left == n:
                    n.parent.left = s
                else:
                    n.parent.right = s
        elif n.right != None:
            s = n.right
            s.parent = n.parent
            if n.parent != None:
                if n.parent.left == n:
                    n.parent.left = s
                else:
                    n.parent.right = s
        else:
            if n.parent != None:
                if n.parent.left == n:
                    n.parent.left = None
                else:
                    n.parent.right = None

    def delete_node(root: TreeNode, key: int):
        if root == None:
            return root
        if key == root.key and root.left == None and root.right == None:
            return None
        n = find(root, key)
        if n:
            delete(n)
        return root

    for _ in range(n):
        inst, *params = input().split(" ")
        if inst == "insert":
            root = insert(root, int(params[0]))
        if inst == "print":
            walk_tree(root)
        if inst == "find":
            res = find(root, int(params[0]))
            print("yes" if res != None else "no")
        if inst == "delete":
            root = delete_node(root, int(params[0]))
