from math import floor


def heapify(heap: list[int], n: int, idx: int):
    left = idx * 2
    right = idx * 2 + 1
    max_idx = idx
    if left <= n and heap[left] > heap[max_idx]:
        max_idx = left
    if right <= n and heap[right] > heap[max_idx]:
        max_idx = right
    if max_idx != idx:
        heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
        heapify(heap, n, max_idx)


def main():
    n = int(input())
    heap = [-1, *list(map(int, input().split(" ")))]
    for i in range(floor(n / 2), 0, -1):
        heapify(heap, n, i)
    print(f" {" ".join(map(str, heap[1:]))}")
