# Time Complexity: O(N)
# 너무 어렵다. 이해가 안된다.
# 나중에 다시 풀어보자


def solution(H):
    stack = []
    cnt = 0

    for h in H:
        if len(stack) == 0:
            stack.append(h)
        else:
            last = stack[-1]
            if last != h:
                stack.append(h)
                cnt += 1

    if cnt == 0:
        cnt = 1

    return cnt


def main():
    print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
    print(solution([1, 2, 3, 4, 5, 6]))


if __name__ == "__main__":
    main()