class TreeNode:
    def __init__(self, id: int, left=-1, right=-1, parent=-1) -> None:
        self.id = id
        self.left = left
        self.right = right
        self.parent = parent


def main():
    n = int(input())
    node_map: dict[int, TreeNode] = {}
    for _ in range(n):
        id, left, right = list(map(int, input().split(" ")))
        node_map[id] = TreeNode(id, left, right)

    for node in node_map.values():
        if node.left != -1:
            node_map[node.left].parent = node.id
        if node.right != -1:
            node_map[node.right].parent = node.id

    root = node_map[0]
    for node in node_map.values():
        if node.parent == -1:
            root = node

    def pre_order(root: TreeNode, res_arr: list[int]):
        res_arr.append(root.id)
        if root.left != -1:
            pre_order(node_map[root.left], res_arr)
        if root.right != -1:
            pre_order(node_map[root.right], res_arr)

    def in_order(root: TreeNode, res_arr: list[int]):
        if root.left != -1:
            in_order(node_map[root.left], res_arr)
        res_arr.append(root.id)
        if root.right != -1:
            in_order(node_map[root.right], res_arr)

    def post_order(root: TreeNode, res_arr: list[int]):
        if root.left != -1:
            post_order(node_map[root.left], res_arr)
        if root.right != -1:
            post_order(node_map[root.right], res_arr)
        res_arr.append(root.id)

    arr = []
    print("Preorder")
    pre_order(root, arr)
    print(" " + " ".join(map(str, arr)))
    arr.clear()

    print("Inorder")
    in_order(root, arr)
    print(" " + " ".join(map(str, arr)))
    arr.clear()

    print("Postorder")
    post_order(root, arr)
    print(" " + " ".join(map(str, arr)))
    arr.clear()
