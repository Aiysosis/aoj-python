from math import floor


def binary_search(arr: list[int], n: int, target: int):
    if int(target) < int(arr[0]):
        return False
    if int(target) > int(arr[n - 1]):
        return False
    left = 0
    right = n
    while left <= right:
        mid = floor((left + right) / 2)
        if arr[mid] == target:
            return True
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    n = int(input())
    seq = list(map(int, input().split(" ")))
    input()
    targets = list(map(int, input().split(" ")))
    cnt = 0
    for val in targets:
        if binary_search(seq, n, val):
            cnt += 1
    print(cnt)
