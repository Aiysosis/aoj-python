def main():
    n = int(input())
    min_val = 1e10
    max_res = -1e10
    for _ in range(n):
        val = int(input())
        max_res = max(max_res, val - min_val)
        min_val = min(val, min_val)
    print(max_res)
