def main():
    diagram = input()
    # (char, area_up, area_down)
    stack: list[tuple[str, int, int]] = []
    left_cnt = 0
    for char in diagram:
        if char == "\\":
            stack.append((char, 0, 0))
            left_cnt += 1
        if char == "_":
            stack.append((char, 1, 0))
        if char == "/":
            area = 0
            cnt = 1
            while len(stack) > 0 and left_cnt > 0:
                pre_char, area_up, area_down = stack.pop()
                if pre_char == "_":
                    area += area_up + area_down
                    cnt += area_up
                if pre_char == "\\":
                    # area of the triangle \/
                    area += 1
                    cnt += 1
                    stack.append(("_", cnt, area))
                    left_cnt -= 1
                    break
    sum = 0
    area_list = []
    for _, _, val in stack:
        if val > 0:
            sum += val
            area_list.append(val)
    print(sum)
    if sum == 0:
        print(0)
    else:
        print(f'{len(area_list)} {" ".join(map(str, area_list))}')
