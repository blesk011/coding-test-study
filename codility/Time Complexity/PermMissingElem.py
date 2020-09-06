# Time Complexity : O(n) or O(n * log(n))


def solution(A):

    if len(A) == 0:
        return 1

    compare_arr = [-1 for _ in range(len(A)+2)]
    for num in A:
        compare_arr[num] += 1

    idx = compare_arr[1:].index(-1) + 1
    return idx


def main():
    print(solution([]))
    print(solution([2, 3, 1, 5]))
    print(solution([2]))


if __name__ == "__main__":
    main()