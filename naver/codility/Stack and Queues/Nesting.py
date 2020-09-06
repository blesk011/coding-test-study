# Time Complexity: O(N)


def solution(S):
    stack = []

    if len(S) == 0:
        return 1

    for string in S:
        # print("string: {}".format(string))
        if string == "(":
            stack.append(string)
        else:
            if len(stack) != 0:
                last = stack[-1]
                # print("last: {}".format(last))
                if last == '(':
                    stack.pop()
                # print("stack: {}".format(stack))
            else:
                return 0

    # print(stack)

    if len(stack) == 0:
        return 1
    else:
        return 0


def main():

    print(solution('(()(())())'))
    print(solution('())'))
    print(solution('((()))))'))
    print(solution('((()))'))
    print(solution('()()'))
    print(solution('(()())'))
    print(solution(')('))
    print(solution(''))


if __name__ == "__main__":
    main()