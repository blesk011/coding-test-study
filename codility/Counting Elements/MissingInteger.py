# Time Complexity: O(N) or O(N * logN)


def solution(A):
    max_num = max(A)

    if max_num <= 0:
        return 1

    check = [0] * max_num
    cnt = 0

    for i, num in enumerate(A):
        if num <= 0:
            continue
        check[num-1] += 1

    if all(check):
        return max_num+1
    else:
        return check.index(0)+1


def main():
    print(solution([1, 3, 6, 4, 1, 2]))         # 5
    print(solution([1, 2, 3]))                  # 4
    print(solution([-1, -3]))                   # 1
    print(solution([-10000, 3, 3, 1, 10, 2, 5]))    # 4


if __name__ == "__main__":
    main()