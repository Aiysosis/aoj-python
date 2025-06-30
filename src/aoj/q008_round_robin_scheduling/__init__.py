# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_B
def main():
    n, time_slot = map(int, input().split(" "))
    queue = []
    for _ in range(n):
        task_name, cost_time = input().split(" ")
        queue.append((task_name, int(cost_time)))
    cur_time = 0
    while len(queue) > 0:
        task_name, cost_time = queue.pop(0)
        if cost_time <= time_slot:
            cur_time += cost_time
            print(f"{task_name} {cur_time}")
        else:
            cur_time += time_slot
            queue.append((task_name, cost_time - time_slot))
