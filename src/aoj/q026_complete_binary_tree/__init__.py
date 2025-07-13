from math import floor


def main():
    n = int(input())
    arr = [-1, *list(map(int, input().split(" ")))]

    def is_valid_idx(idx: int):
        return idx > 0 and idx <= n

    for i in range(1, n + 1):
        line = f"node {i}: key = {arr[i]}, "
        left = 2 * i
        right = 2 * i + 1
        parent = floor(i / 2)
        if is_valid_idx(parent):
            line += f"parent key = {arr[parent]}, "
        if is_valid_idx(left):
            line += f"left key = {arr[left]}, "
        if is_valid_idx(right):
            line += f"right key = {arr[right]}, "
        print(line)
