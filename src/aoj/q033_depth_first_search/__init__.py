def recursive_solution():
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        _, deg, *edges = map(int, input().split(" "))
        for j in range(deg):
            graph[i][edges[j] - 1] = 1

    visit_t = [0 for _ in range(n)]
    finish_t = [0 for _ in range(n)]
    time = 1

    def dfs(v: int):
        nonlocal time
        if visit_t[v] > 0:
            return
        visit_t[v] = time
        time += 1
        for i in range(n):
            if graph[v][i] == 1:
                dfs(i)
        finish_t[v] = time
        time += 1

    flag = True
    while flag:
        flag = False
        for i in range(n):
            if visit_t[i] == 0:
                flag = True
                dfs(i)
    for i in range(n):
        print(f"{i + 1} {visit_t[i]} {finish_t[i]}")


def stack_solution():
    n = int(input())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        _, deg, *edges = map(int, input().split(" "))
        for j in range(deg):
            graph[i][edges[j] - 1] = 1

    visit_t = [0 for _ in range(n)]
    finish_t = [0 for _ in range(n)]
    time = 1

    def dfs(v: int):
        nonlocal time
        stack: list[int] = [v]

        while len(stack) > 0:
            cur_v = stack[-1]
            if visit_t[cur_v] == 0:
                # visit cur vertex
                visit_t[cur_v] = time
                time += 1
            # visit next vertex
            for i in range(n):
                if graph[cur_v][i] == 1 and visit_t[i] == 0:
                    stack.append(i)
                    break
            if stack[-1] == cur_v:
                stack.pop()
                finish_t[cur_v] = time
                time += 1

    flag = True
    while flag:
        flag = False
        for i in range(n):
            if visit_t[i] == 0:
                flag = True
                dfs(i)
    for i in range(n):
        print(f"{i + 1} {visit_t[i]} {finish_t[i]}")


def main():
    # recursive_solution()
    stack_solution()
