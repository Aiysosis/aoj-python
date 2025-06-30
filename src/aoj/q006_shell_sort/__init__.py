def insertion_sort(arr: list[int], n: int, g: int):
    cnt = 0
    for i in range(n):
        val = arr[i]
        j = i - g
        while j >= 0 and arr[j] > val:
            arr[j + g] = arr[j]
            j -= g
            cnt += 1
        arr[j + g] = val
    return cnt


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    g = 1
    # With g(i) = 3 * g(i - 1) + 1, Shell sort can achieve an average time complexity of O(n^{1.25}), and O(n^{1.5}) in the worst case
    g_arr = []
    while g <= n:
        g_arr.insert(0, g)
        g = g * 3 + 1

    cnt = 0
    for g in g_arr:
        cnt += insertion_sort(arr, n, g)
    print(len(g_arr))
    print(" ".join(map(str, g_arr)))
    print(cnt)
    for val in arr:
        print(val)
