# [left, right]
def partition(arr: list[int], left: int, right: int):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    p = partition(arr, 0, n - 1)
    res = ""
    for idx, val in enumerate(arr):
        if idx == p:
            res += f" [{val}]"
        else:
            res += f" {val}"
    print(res.strip())
