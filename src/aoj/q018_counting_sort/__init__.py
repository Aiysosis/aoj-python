MAX_LEN = int(1e4) + 1


def counting_sort(arr: list[int], n: int):
    buckets = [0 for _ in range(MAX_LEN)]
    res = [*arr]
    for val in arr:
        buckets[val] += 1
    for i in range(1, MAX_LEN):
        buckets[i] += buckets[i - 1]
    for i in range(n - 1, -1, -1):
        cnt = buckets[arr[i]]
        buckets[arr[i]] -= 1
        res[cnt - 1] = arr[i]
    return res


def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    res = counting_sort(arr, n)
    print(" ".join(map(str, res)))
