# Time Complexity: O(N)
# from collections import deque
from queue import Queue

def solution(S):
    stack = list()
    string_dict = {')': '(', '}': '{', ']': '['}

    if len(S) == 0:
        return 1

    for string in S:
        if string == '{' or string == '(' or string == '[':
            stack.append(string)
        else:
            if len(stack) == 0:
                return 0
            pop_string = stack.pop()
            if pop_string != string_dict[string]:
                return 0

            """
            pop_string = stack[-1]
            if pop_string == string_dict[string]:
                stack.pop()
                continue

            """

    if len(stack) == 0:
        return 1
    else:
        return 0


def main():
    print(solution("{[()()]}"))
    print(solution("([)()]"))
    print(solution(""))
    print(solution("[[[[[[[[[(((((()))}}}]]]]]"))

if __name__ == "__main__":
    main()