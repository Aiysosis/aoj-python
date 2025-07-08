from math import floor

cnt = 0


# [left, right), [left, mid), [mid, right)
def merge(arr: list[int], left: int, mid: int, right: int):
    global cnt
    INF = 1e10
    left_arr = [*arr[left:mid], INF]
    right_arr = [*arr[mid:right], INF]
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1


def merge_sort(arr: list[int], left: int, right: int):
    if left + 1 < right:
        mid = floor((left + right) / 2)
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def main():
    global cnt
    n = int(input())
    arr = list(map(int, input().split(" ")))
    merge_sort(arr, 0, n)
    print(" ".join(map(str, arr)))
    print(cnt)
