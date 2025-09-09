def main():
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        _, deg, *edges = map(int, input().split(" "))
        for j in range(deg):
            graph[i][edges[j] - 1] = 1
    for row in graph:
        print(" ".join(map(str, row)))
