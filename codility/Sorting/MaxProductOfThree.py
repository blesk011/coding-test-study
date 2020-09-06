# Time Complexity: O(N * log(N))


def solution(A):
    A.sort()

    """
    1. 맨 뒤 3자리 수
    vs
    2. 2개 이상 음수이고 최대값이 양수인 경우 3자리 수
    """
    res = A[-1] * A[-2] * A[-3]

    if (A[0] <= 0) and (A[1] <= 0) and (A[-1] >= 0):
        compare = A[0] * A[1] * A[-1]

        if res < compare:
            res = compare

    return res


def main():
    print(solution([-3, 1, 2, -2, 5, 6]))
    print(solution([-9, -8, 1, 2, 4]))
    print(solution([-7, -9, -8, 1, 2, 10]))         # -9, -8, -7, 1, 2, 10
    print(solution([-3, -4, 0, 1, 2]))              # -4, -3, 0, 1, 2 / 0, 1, 2, 3, 4
    print(solution([-9, -5, -3, -2]))


if __name__ == "__main__":
    main()