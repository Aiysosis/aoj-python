# unsolved
def main():
    n = int(input())
    if n < 2:
        print(0)
        return
    arr: list[int] = []
    min_idx = 0
    for i in range(n):
        if i == 0:
            arr.extend(map(int, input().split(" ")))
            min_idx = 0 if arr[0] < arr[1] else 1
            continue
        arr.append(int(input().split(" ")[1]))
        if arr[-1] < arr[min_idx]:
            min_idx = len(arr) - 1
    res = 0
    flag = False
    for i in range(min_idx + 1, n):
        if min_idx == 0 and i + 1 == n:
            flag = True
        res += arr[min_idx] * arr[i] * arr[i + 1]
    for i in range(1, min_idx):
        if min_idx == n and i - 1 == 0:
            flag = True
        res += arr[min_idx] * arr[i] * arr[i - 1]
    if not flag:
        res += arr[0] * arr[min_idx] * arr[-1]
    print(res)
