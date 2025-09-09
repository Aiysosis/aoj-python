def recursive_solution():
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        _, deg, *edges = map(int, input().split(" "))
        for j in range(deg):
            graph[i][edges[j] - 1] = 1

    depth_arr = [-1 for _ in range(n)]

    def bfs(v: int, cur_depth: int):
        if depth_arr[v] == -1 or cur_depth < depth_arr[v]:
            depth_arr[v] = cur_depth
        else:
            return
        for i in range(n):
            if graph[v][i] == 1:
                bfs(i, cur_depth + 1)

    bfs(0, 0)
    for i in range(n):
        print(f"{i + 1} {depth_arr[i]}")


def queue_solution():
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        _, deg, *edges = map(int, input().split(" "))
        for j in range(deg):
            graph[i][edges[j] - 1] = 1


def main():
    recursive_solution()
