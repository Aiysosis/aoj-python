def main():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    input()
    targets = list(map(int, input().split(" ")))

    def solve(idx: int, target: int):
        if idx >= n:
            return False
        if target == arr[idx]:
            return True
        return solve(idx + 1, target) or solve(idx + 1, target - arr[idx])

    for t in targets:
        if solve(0, t):
            print("yes")
        else:
            print("no")
