from math import floor


Cards = list[tuple[str, int]]


# [left, right]
def partition(arr: Cards, left: int, right: int):
    pivot = arr[right][1]
    i = left
    for j in range(left, right):
        if arr[j][1] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quick_sort(arr: Cards, left: int, right: int):
    if left < right:
        pivot_pos = partition(arr, left, right)
        quick_sort(arr, left, pivot_pos - 1)
        quick_sort(arr, pivot_pos + 1, right)


# [left, right)
def merge(arr: Cards, left, mid, right):
    INF = 1e10
    left_arr = [*arr[left:mid], ("", INF)]
    right_arr = [*arr[mid:right], ("", INF)]
    i = 0
    j = 0
    for k in range(left, right):
        if left_arr[i][1] <= right_arr[j][1]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1


def merge_sort(arr: Cards, left, right):
    if left + 1 < right:
        mid = floor((left + right) / 2)
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def main():
    n = int(input())
    arr: list[tuple[str, int]] = []
    for _ in range(n):
        char, val = input().split(" ")
        arr.append((char, int(val)))
    arr_copy = [*arr]
    quick_sort(arr, 0, n - 1)
    merge_sort(arr_copy, 0, n)
    # check stability, just compare the result of a stable sort algorithm
    is_stable = True
    for idx, val in enumerate(arr):
        if str(val) != str(arr_copy[idx]):
            is_stable = False
            break
    if is_stable:
        print("Stable")
    else:
        print("Not stable")
    for val in arr:
        print(f"{val[0]} {val[1]}")
