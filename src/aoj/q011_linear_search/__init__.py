def main():
    input()
    seq = set(input().split(" "))
    input()
    targets = list(input().split(" "))
    cnt = 0
    for val in targets:
        if val in seq:
            cnt += 1
    print(cnt)
