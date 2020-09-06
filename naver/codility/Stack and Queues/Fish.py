# Time Complexity: O(N)


def solution(A, B):
    stack = []
    cnt = 0

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while len(stack):
                last = stack[-1]
                if last > A[i]:
                    break
                else:
                    stack.pop()

            if len(stack) is 0:
                cnt += 1

    cnt = cnt + len(stack)
    return cnt


def main():
    print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
    print(solution([4, 3], [1, 0]))


if __name__ == "__main__":
    main()