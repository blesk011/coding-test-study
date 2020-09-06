# Time Complexity : O(N) or O(N * log(N))


def solution(A):
    # 배열 A의 길이가 1인 경우
    if len(A) == 1:
        return A[0]

    A = sorted(A)

    for i in range(0, len(A), 2):
        # 마지막 숫자가 1개인 경우
        if i+1 == len(A):
            return A[i]
        # 다음 인덱스의 숫자가 다른 경우 -> 그 숫자는 하나임
        if A[i] != A[i+1]:
            return A[i]


def main():
    print(solution([9, 3, 9, 3, 9, 7, 9]))


if __name__ == "__main__":
    main()
