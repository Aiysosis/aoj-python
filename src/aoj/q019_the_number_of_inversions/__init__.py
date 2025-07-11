from math import floor

INF = int(1e10)
cnt = 0


def merge(arr: list[int], left: int, mid: int, right: int):
    global cnt
    seq_l = arr[left:mid]
    seq_l_len = mid - left
    seq_l.append(INF)
    seq_r = arr[mid:right]
    seq_r.append(INF)
    i = 0
    j = 0
    for k in range(left, right):
        if seq_l[i] <= seq_r[j]:
            arr[k] = seq_l[i]
            i += 1
        else:
            if i < seq_l_len:
                cnt += seq_l_len - i
            arr[k] = seq_r[j]
            j += 1


def get_inversion_num(arr: list[int], left: int, right: int):
    if left + 1 < right:
        mid = floor((left + right) / 2)
        get_inversion_num(arr, left, mid)
        get_inversion_num(arr, mid, right)
        merge(arr, left, mid, right)


def main():
    global cnt
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split(" ")))
    get_inversion_num(arr, 0, n)
    print(cnt)
