# https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_3_A


def main():
    notation = input().split(" ")
    stack: list[int] = []
    for s in notation:
        if s.isdigit():
            stack.append(int(s))
        else:
            right = stack.pop()
            left = stack.pop()
            match s:
                case "+":
                    stack.append(left + right)
                case "-":
                    stack.append(left - right)
                case "*":
                    stack.append(left * right)
    print(stack[0])
