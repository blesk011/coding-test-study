# Time Complexity: O(N * log(N))


def solution(A):
    A.sort()

    for i in range(len(A)-2):
        if (A[i] + A[i+1]) > A[i+2]:
            return 1

    return 0


def main():
    print(solution([2147483647, 2147483646, 1000000]))


if __name__ == "__main__":
    main()