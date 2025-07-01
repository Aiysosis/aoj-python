from typing import Optional


class Node:
    def __init__(
        self,
        value: str,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


def delete_node(node: Node):
    prev = node.prev
    next = node.next
    if prev != None:
        prev.next = next
    if next != None:
        next.prev = prev
    del node


def insert_first(node: Node, root: Node):
    next = root.next
    node.next = next
    node.prev = root
    root.next = node
    if next != None:
        next.prev = node


# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_C
def main():
    root = Node("-1")
    tail = Node("-2")
    root.next = tail
    tail.prev = root

    n = int(input())
    for _ in range(n):
        inst = input().split(" ")
        cmd = inst[0]
        if cmd == "insert":
            opt = inst[1]
            new_node = Node(opt)
            insert_first(new_node, root)
        if cmd == "delete":
            opt = inst[1]
            cur_node = root.next
            while cur_node != None:
                if cur_node.value == opt:
                    delete_node(cur_node)
                    break
                else:
                    cur_node = cur_node.next
        if cmd == "deleteFirst":
            delete_node(root.next)
        if cmd == "deleteLast":
            delete_node(tail.prev)

    cur_node = root.next
    res = ""
    while cur_node != tail:
        if cur_node != None:
            res += f" {cur_node.value}"
            cur_node = cur_node.next
    print(res.strip())
