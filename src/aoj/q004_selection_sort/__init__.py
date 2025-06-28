#https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_2_B
def main():
    n = int(input())
    arr = list(map(int, input().split(' ')))
    count = 0
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_pos]:
                min_pos = j
        if min_pos != i:
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
            count += 1
    print(' '.join(map(str, arr)))
    print(count)