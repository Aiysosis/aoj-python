def main():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    flag = True
    count = 0
    while flag:
        flag = False
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                flag = True
                count += 1
    print(' '.join(map(str, arr)))
    print(count)