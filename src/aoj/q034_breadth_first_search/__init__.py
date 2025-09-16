from collections import deque


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
    graph: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        _, deg, *edges = map(int, input().split(" "))
        for j in range(deg):
            graph[i].append(edges[j] - 1)

    depth_arr = [-1] * n
    visit_arr = [False] * n

    def bfs(v: int):
        queue = deque([v])
        depth_arr[v] = 0
        visit_arr[v] = True
        while len(queue) > 0:
            cur_v = queue.popleft()
            for next_v in graph[cur_v]:
                if not visit_arr[next_v]:
                    visit_arr[next_v] = True
                    depth_arr[next_v] = depth_arr[cur_v] + 1
                    queue.append(next_v)

    bfs(0)
    for i in range(n):
        print(f"{i + 1} {depth_arr[i]}")


def main():
    queue_solution()
