def get_card_num(text: str):
    return int(text[1])


def bubble_sort(arr: list[str], n: int):
    flag = True
    end_pos = 0
    while flag:
        flag = False
        for j in range(n - 1, end_pos, -1):
            if get_card_num(arr[j - 1]) > get_card_num(arr[j]):
                flag = True
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def selection_sort(arr: list[str], n: int):
    for i in range(n - 1):
        min_pos = i
        for j in range(i, n):
            if get_card_num(arr[j]) < get_card_num(arr[min_pos]):
                min_pos = j
        if min_pos != i:
            arr[min_pos], arr[i] = arr[i], arr[min_pos]
    return arr


def main():
    n = int(input())
    arr = input().split(" ")
    bubble_sort_res = bubble_sort([*arr], n)
    selection_sort_res = selection_sort([*arr], n)
    print(" ".join(bubble_sort_res))
    print("Stable")
    print(" ".join(selection_sort_res))
    # As we already know that bubble sort is stable, so just check if the result is correct
    print("Stable" if str(bubble_sort_res) == str(selection_sort_res) else "Not stable")
