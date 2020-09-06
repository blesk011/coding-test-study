# Time Complexity: O(N) or O(N * log(N))
"""
# Distinct Value
주어진 배열에서 중복을 제거하고 구성하고 있는 요소들

"""


def solution(A):
    A.sort()
    cnt = 1

    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            cnt += 1

    return cnt


def main():
    print(solution([2, 2, 1, 3, 1, 2]))
    print(solution([1, 1]))
    print(solution([-1, 1, 1]))



if __name__ == "__main__":
    main()