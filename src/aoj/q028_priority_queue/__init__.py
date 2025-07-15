from math import floor


class PriorityQueue:
    heap: list[int]
    length: int

    def __init__(self) -> None:
        self.heap = [-1]
        self.length = 0

    def __heapify__(self, idx: int):
        heap = self.heap
        n = self.length
        left = idx * 2
        right = idx * 2 + 1
        max_idx = idx
        if left <= n and heap[left] > heap[max_idx]:
            max_idx = left
        if right <= n and heap[right] > heap[max_idx]:
            max_idx = right
        if max_idx != idx:
            heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
            self.__heapify__(max_idx)

    def insert(self, val: int):
        self.heap.append(val)
        self.length += 1
        if self.heap[self.length] > val:
            return
        pos = floor(self.length / 2)
        while pos >= 1:
            self.__heapify__(pos)
            pos = floor(pos / 2)

    def extract(self):
        # swap first and last element
        self.heap[1], self.heap[self.length] = self.heap[self.length], self.heap[1]
        res = self.heap.pop()
        self.length -= 1
        self.__heapify__(1)
        return res


def main():
    q = PriorityQueue()
    inst = ""
    while inst != "end":
        inst, *params = input().split(" ")
        if inst == "insert":
            q.insert(int(params[0]))
        if inst == "extract":
            print(q.extract())
