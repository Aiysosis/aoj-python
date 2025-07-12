class TreeNode:
    def __init__(self, id: int, left=-1, right=-1) -> None:
        self.id = id
        self.left = left
        self.right = right


def main():
    n = int(input())
    pre_order_seq = list(map(int, input().split(" ")))
    in_order_seq = list(map(int, input().split(" ")))

    node_map: dict[int, TreeNode] = {}
    for id in pre_order_seq:
        node_map[id] = TreeNode(id)

    def rebuild_tree(pre_l: int, pre_r: int, in_l: int, in_r: int) -> int:
        if pre_l >= pre_r or in_l >= in_r:
            return -1
        id = pre_order_seq[pre_l]
        root = node_map[id]
        pos = in_l
        while pos < in_r:
            if in_order_seq[pos] == id:
                break
            pos += 1
        root.left = rebuild_tree(pre_l + 1, pre_l + 1 + pos - in_l, in_l, pos)
        root.right = rebuild_tree(pre_l + 1 + pos - in_l, pre_r, pos + 1, in_r)
        return id

    root_id = rebuild_tree(0, n, 0, n)
    res: list[int] = []

    def post_order(root_id: int):
        if root_id == -1:
            return
        node = node_map[root_id]
        post_order(node.left)
        post_order(node.right)
        res.append(root_id)

    post_order(root_id)

    print(" ".join(map(str, res)))
